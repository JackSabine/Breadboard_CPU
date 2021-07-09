import re
from AssemblerClasses import *

OPCODE_MAP = {
"ADD":    0b00000,
"ADDI":   0b00001,
"BLANK":  0b00010,
"NOT":    0b00011,
"AND":    0b00100,
"ANDI":   0b00101,
"NEG":    0b00110,
"CMP":    0b00111,
"LD":     0b01000,
"LDR":    0b01001,
"STR":    0b01010,
"HLT":    0b01011,
"CALL":   0b01100,
"RET":    0b01101,
"TRAP":   0b01110,
"SETBK":  0b01111,
"START":  0b10000,
"SETSP":  0b10001,
"PUSH":   0b10010,
"POP":    0b10011,
"OR":     0b10100,
"ORI":    0b10101,
"CPYSP":  0b10110,
"J":      0b10111,
"JO":     0b11000,
"JNO":    0b11001,
"JZ":     0b11010,
"JNZ":    0b11011,
"JS":     0b11100,
"JNS":    0b11101,
"JC":     0b11110,
"JNC":    0b11111
}

INSTRUCTION_POS = 11
NUM_JUMP_BITS = INSTRUCTION_POS
NUM_BASER_OFFSET_BITS = 5
NUM_IMM_BITS = 8

REGA_POS = 8
REGB_POS = 5
IMM_POS = 0

AMBIG = ["ADD", "AND", "OR"]
SINGR = ["NOT", "NEG", "SETBK", "START", "SETSP", "PUSH", "POP", "CPYSP"]
JUMPS = ["J", "JO", "JNO", "JZ", "JNZ", "JS", "JNS", "JC", "JNC", "CALL"]
NOARG = ["HLT", "RET"]
BASER = ["LDR", "STR"]
OTHER = ["CMP", "LD", "TRAP"]

def __DecOrHexSearch(str):
    MatchDec = re.search(r"#(-?[0-9]+)",str,re.IGNORECASE)
    MatchHex = re.search(r"0?x([0-9A-F]+)",str,re.IGNORECASE)
    if MatchDec is not None:
        return int(MatchDec.groups()[0])
    elif MatchHex is not None:
        return int(MatchHex.groups()[0],base=16)
    else:
        return None

def Ambig(Args):
    if(len(Args.WordList) != 2):
        raise Exception(f"Incorrect number of arguments on line {Args.LineNumber}")
    MatchA = re.search(r"r([0-7])",Args.WordList[0],re.IGNORECASE)
    MatchB = re.search(r"r([0-7])",Args.WordList[1],re.IGNORECASE)
    ValueC = __DecOrHexSearch(Args.WordList[1])
    ArgA = 0x00
    ArgB = 0x00
    if MatchA is None or (MatchB is None and ValueC is None):
        raise Exception(f"Incorrect arguments on line {Args.LineNumber}")
    ArgA = int(MatchA.groups()[0]) << REGA_POS
    if(MatchB is None):
        ArgB = (ValueC & 0xFF) << IMM_POS
    else:
        ArgB = int(MatchB.groups()[0]) << REGB_POS

    return ArgA | ArgB

def SingR(Args):
    if(len(Args.WordList) != 1):
        raise Exception(f"Incorrect number of arguments on line {Args.LineNumber}")
    MatchA = re.search(r"r([0-7])",Args.WordList[0],re.IGNORECASE)
    if MatchA is None:
        raise Exception(f"Incorrect arguments on line {Args.LineNumber}")
    ArgA = int(MatchA.groups()[0]) << REGA_POS
    
    return ArgA

def Jumps(Args, SymbolTable, ORIG_Offset):
    if(len(Args.WordList) != 1):
        raise Exception(f"Incorrect number of arguments on line {Args.LineNumber}")
    if(SymbolTable.get(Args.WordList[0]) is None):
        raise Exception(f"Label {Args.WordList[0]} has no defined destination on line {Args.LineNumber}")

    PCOffset = SymbolTable.get(Args.WordList[0]) - (ORIG_Offset + 1)
    MaxPos = (2**(NUM_JUMP_BITS-1))             # Example 1024 and -1023 (not typical -1024 to 1023 because of PC+1)
    MaxNeg = (-1*2**(NUM_JUMP_BITS-1) + 1)
    if(     PCOffset > MaxPos or PCOffset < MaxNeg    ):
        raise Exception(f"Jump/Call on line {Args.LineNumber} to label {Args.WordList[0]} exceeds max range [{MaxNeg},{MaxPos}]")
    
    return PCOffset & 0x07FF        # Return lower 11 bits
    
def NoArg():
    return 0x0000

def BaseR(Args):
    if(len(Args.WordList) != 3):
        raise Exception(f"Incorrect number of arguments on line {Args.LineNumber}")
    MatchA = re.search(r"r([0-7])",Args.WordList[0],re.IGNORECASE)
    MatchB = re.search(r"r([0-7])",Args.WordList[1],re.IGNORECASE)
    ValueC = __DecOrHexSearch(Args.WordList[2])
    if MatchA is None or MatchB is None or ValueC is None:
        raise Exception(f"Incorrect arguments on line {Args.LineNumber}")

    ArgA = int(MatchA.groups()[0]) << REGA_POS
    ArgB = int(MatchB.groups()[0]) << REGB_POS
    ArgC = (ValueC & 0x1F) << IMM_POS

    MaxPos = (2**NUM_BASER_OFFSET_BITS)-1
    MaxNeg = -(2**NUM_BASER_OFFSET_BITS)
    if(ArgC > MaxPos or ArgC < MaxNeg):
        raise Exception(f"LDR/STR offset on line {Args.LineNumber} exceeds max range [{MaxNeg},{MaxPos}]")

    return ArgA | ArgB | ArgC

def Other(Args):
    # Args includes the opcode as Arg.WordList[0]
    # ["CMP", "LD", "TRAP"]
    ArgA = 0x00
    ArgB = 0x00
    if(re.search(r"^CMP$", Args.WordList[0], re.IGNORECASE)):
        if(len(Args.WordList) != 2 + 1):
            raise Exception(f"Incorrect number of arguments on line {Args.LineNumber}")
        MatchA = re.search(r"r([0-7])",Args.WordList[1],re.IGNORECASE)
        MatchB = re.search(r"r([0-7])",Args.WordList[2],re.IGNORECASE)
        if MatchA is None or MatchB is None:
            raise Exception(f"Incorrect arguments on line {Args.LineNumber}")

        ArgA = int(MatchA.groups()[0]) << REGA_POS
        ArgB = int(MatchB.groups()[0]) << REGB_POS

    elif(re.search(r"^LD$", Args.WordList[0], re.IGNORECASE)):
        if(len(Args.WordList) != 2 + 1):
            raise Exception(f"Incorrect number of arguments on line {Args.LineNumber}")

        MatchA = re.search(r"r([0-7])", Args.WordList[1], re.IGNORECASE)

        ValueB = __DecOrHexSearch(Args.WordList[2])
        if MatchA is None or ValueB is None:
            raise Exception(f"Incorrect arguments on line {Args.LineNumber}")

        ArgA = int(MatchA.groups()[0]) << REGA_POS

        Immediate = ValueB
        MaxPos =  (2**NUM_IMM_BITS) - 1 
        MaxNeg = -(2**NUM_IMM_BITS)
        if(     Immediate > MaxPos or Immediate < MaxNeg    ):
            raise Exception(f"LD immediate value on line {Args.LineNumber} exceeds max range [{MaxNeg},{MaxPos}]")
        ArgB = (Immediate & 0xFF) << IMM_POS

    elif(re.search(r"^TRAP$", Args.WordList[0], re.IGNORECASE)):
        if(len(Args.WordList) != 1 + 1):
            raise Exception(f"Incorrect number of arguments on line {Args.LineNumber}")

        raise Exception(f"Not implemented")
    else:
        raise Exception(f"Operation {Args.WordList[0]} recognized as type \"Other\", but does not match any instructions")
    return ArgA | ArgB