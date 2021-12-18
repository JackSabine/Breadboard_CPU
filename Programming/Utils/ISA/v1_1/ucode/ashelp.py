import os, sys
path: str = os.path.dirname(__file__)
while(not path.endswith("ISA")):
    path = os.path.dirname(path)
sys.path.append(os.path.dirname(path))

from ISA.v1_1.ucode.macros import *
from ISA.v1_1.classes import *

import re

def __DecOrHexSearch(str):
    MatchDec = re.search(r"#(-?[0-9]+)",str,re.IGNORECASE)
    MatchHex = re.search(r"0?x([0-9A-F]+)",str,re.IGNORECASE)
    RetVal = None

    if MatchDec is not None:
        RetVal = int(MatchDec.groups()[0])
    elif MatchHex is not None:
        RetVal = int(MatchHex.groups()[0],base=16)

    return RetVal



OPCODE_MAP = {
    "ADD":    0b00000,
    "ADDI":   0b00001,
    "LEA":    0b00010,
    "NOT":    0b00011,
    "AND":    0b00100,
    "ANDI":   0b00101,
    "STP":    0b00110,
    "CMP":    0b00111,
    "LD":     0b01000,
    "LDR":    0b01001,
    "STR":    0b01010,
    "PAUSE":  0b01011,
    "CALL":   0b01100,
    "RET":    0b01101,
    "TRAP":   0b01110,
    "STPI":   0b01111,
    "START":  0b10000,
    "SETSP":  0b10001,
    "PUSH":   0b10010,
    "POP":    0b10011,
    "OR":     0b10100,
    "ORI":    0b10101,
    "CPYSP":  0b10110,
    "JMP":    0b10111,
    "JO":     0b11000,
    "JNO":    0b11001,
    "JZ":     0b11010,
    "JNZ":    0b11011,
    "JS":     0b11100,
    "JNS":    0b11101,
    "JC":     0b11110,
    "JNC":    0b11111
}

TWOREG = ["ADD", "AND", "OR"]
REGIMM = ["ADDI", "ANDI", "ORI"]
SINGR = ["NOT", "START", "SETSP", "PUSH", "POP", "CPYSP"]
PCOFF = ["JMP", "JO", "JNO", "JZ", "JNZ", "JS", "JNS", "JC", "JNC", "CALL", "LEA"]
NOARG = ["PAUSE", "RET"]
BASER = ["LDR", "STR"]
PORTIMM = ["STPI"]
PORTREG = ["STP"]

OTHER = ["CMP", "LD", "TRAP"]



def CreateBitArgs(Operation: str, Args: list[str], SymbolTable: dict[str, int], Instruction_MemoryIndex: int, LineNumber: int) -> int:
    BitArgs = 0x0000

    if(Operation in TWOREG):
        BitArgs = TwoReg(Args, LineNumber)
    elif(Operation in REGIMM):
        BitArgs = RegImm(Args, LineNumber)
    elif(Operation in SINGR):
        BitArgs = SingR(Args, LineNumber)
    elif(Operation in PCOFF):
        BitArgs = PCOff(Args, LineNumber, SymbolTable, Instruction_MemoryIndex)
    elif(Operation in NOARG):
        BitArgs = NoArg()
    elif(Operation in BASER):
        BitArgs = BaseR(Args, LineNumber)
    elif(Operation in OTHER):
        BitArgs = Other(Operation, Args, LineNumber)
    elif(Operation in PORTIMM):
        BitArgs = PortImm(Args, LineNumber)
    elif(Operation in PORTREG):
        BitArgs = PortReg(Args, LineNumber)
    else:
        raise Exception(f"Operation {Operation} recognized in opmap but does not appear in any instruction collections")
    
    return BitArgs



def TwoReg(Args: list[str], LineNumber: int) -> int:
    if(len(Args) != 2):
        raise Exception(f"Incorrect number of arguments on line {LineNumber}")
    MatchA = re.search(r"r([0-7])",Args[0],re.IGNORECASE)
    MatchB = re.search(r"r([0-7])",Args[1],re.IGNORECASE)
    ArgA: int = 0x00
    ArgB: int = 0x00

    if MatchA is None or MatchB is None:
        raise Exception(f"Incorrect arguments on line {LineNumber}")

    ArgA = int(MatchA.groups()[0]) << REGA_POS
    ArgB = int(MatchB.groups()[0]) << REGB_POS

    return ArgA | ArgB



def RegImm(Args: list[str], LineNumber: int) -> int:

    if(len(Args) != 2):
        raise Exception(f"Incorrect number of arguments on line {LineNumber}")

    MatchA = re.search(r"r([0-7])",Args[0],re.IGNORECASE)
    ValueC = __DecOrHexSearch(Args[1])

    ArgA: int = 0x00
    ArgB: int = 0x00

    if MatchA is None or ValueC is None:
        raise Exception(f"Incorrect arguments on line {LineNumber}")

    ArgA = int(MatchA.groups()[0]) << REGA_POS
    ArgB = (ValueC & 0xFF) << IMM_POS

    return ArgA | ArgB



def SingR(Args: list[str], LineNumber: int):
    if(len(Args) != 1):
        raise Exception(f"Incorrect number of arguments on line {LineNumber}")
    MatchA = re.search(r"r([0-7])",Args[0],re.IGNORECASE)
    if MatchA is None:
        raise Exception(f"Incorrect arguments on line {Args}")
    ArgA = int(MatchA.groups()[0]) << REGA_POS
    
    return ArgA



def PCOff(Args: list[str], LineNumber: int, SymbolTable: dict[str, int], Instruction_MemoryIndex: int):
    if(len(Args) != 1):
        raise Exception(f"Incorrect number of arguments on line {LineNumber}")
    if(SymbolTable.get(Args[0]) is None):
        raise Exception(f"Label {Args[0]} has no defined destination on line {Args}")

    PCOffset = SymbolTable.get(Args[0]) - (Instruction_MemoryIndex + 1)
    MaxPos = (2**(NUM_JUMP_BITS-1))             # Example 1024 and -1023 (not typical -1024 to 1023 because of PC+1)
    MaxNeg = (-1*2**(NUM_JUMP_BITS-1) + 1)
    if(PCOffset not in range(MaxNeg, MaxPos+1, 1)):
        raise Exception(f"Jump/Call on line {Args} to label {Args[0]} exceeds max range [{MaxNeg},{MaxPos}]")
    
    return PCOffset & 0x07FF        # Return lower 11 bits
    


def NoArg():
    return 0x0000



def BaseR(Args: list[str], LineNumber: int):
    if(len(Args) != 3):
        raise Exception(f"Incorrect number of arguments on line {LineNumber}")
    MatchA = re.search(r"r([0-7])",Args[0],re.IGNORECASE)
    MatchB = re.search(r"r([0-7])",Args[1],re.IGNORECASE)
    ValueC = __DecOrHexSearch(Args[2])
    if MatchA is None or MatchB is None or ValueC is None:
        raise Exception(f"Incorrect arguments on line {LineNumber}")

    ArgA = int(MatchA.groups()[0]) << REGA_POS
    ArgB = int(MatchB.groups()[0]) << REGB_POS
    ArgC = (ValueC & 0x1F) << IMM_POS

    MaxPos = (2**NUM_BASER_OFFSET_BITS)-1
    MaxNeg = -(2**NUM_BASER_OFFSET_BITS)
    if(ArgC not in range(MaxNeg, MaxPos+1, 1)):
        raise Exception(f"LDR/STR offset on line {LineNumber} exceeds max range [{MaxNeg},{MaxPos}]")

    return ArgA | ArgB | ArgC



def Other(Operation: str, Args: list[str], LineNumber: int):
    # Operation must be in list: ["CMP", "LD", "TRAP"]

    ArgA: int = 0x00
    ArgB: int = 0x00

    if(re.search(r"^CMP$", Operation, re.IGNORECASE) is not None):
        if(len(Args) != 2):
            raise Exception(f"Incorrect number of arguments on line {LineNumber}")

        MatchA = re.search(r"r([0-7])",Args[0],re.IGNORECASE)
        MatchB = re.search(r"r([0-7])",Args[1],re.IGNORECASE)

        if MatchA is None or MatchB is None:
            raise Exception(f"Incorrect arguments on line {LineNumber}")

        ArgA = int(MatchA.groups()[0]) << REGA_POS
        ArgB = int(MatchB.groups()[0]) << REGB_POS


    elif(re.search(r"^LD$", Operation, re.IGNORECASE) is not None):
        if(len(Args) != 2):
            raise Exception(f"Incorrect number of arguments on line {LineNumber}")

        MatchA = re.search(r"r([0-7])", Args[0], re.IGNORECASE)
        ValueB = __DecOrHexSearch(Args[1])

        if MatchA is None or ValueB is None:
            raise Exception(f"Incorrect arguments on line {LineNumber}")

        Immediate = ValueB
        MaxPos =  (2**NUM_IMM_BITS) - 1 
        MaxNeg = -(2**NUM_IMM_BITS)
        if(Immediate not in range(MaxNeg, MaxPos+1, 1)):
            raise Exception(f"LD immediate value on line {LineNumber} exceeds max range [{MaxNeg},{MaxPos}]")
        
        ArgA = int(MatchA.groups()[0]) << REGA_POS
        ArgB = (Immediate & 0xFF) << IMM_POS


    elif(re.search(r"^TRAP$", Operation, re.IGNORECASE) is not None):
        if(len(Args) != 1):
            raise Exception(f"Incorrect number of arguments on line {LineNumber}")

        ValueB = __DecOrHexSearch(Args[0])

        if(type(ValueB) is int):
            ArgB = ValueB
        else:
            raise Exception(f"Incorrect arguments on line {LineNumber}")

    else:
        raise Exception(f"Operation {Operation} recognized as type \"Other\", but does not match any instructions")


    return ArgA | ArgB



def PortReg(Args: list[str], LineNumber: int) -> int:
    # Syntax: STP #/0x{PortNum}, r[0-7]
    
    if(len(Args) != 2):
        raise Exception(f"Incorrect number of arguments on line {LineNumber}")

    ArgA: int = 0x00
    ArgB: int = 0x00
    
    PortNumber: int = __DecOrHexSearch(Args[0])
    MatchReg: re.Match = re.search(r"r([0-7])",Args[1],re.IGNORECASE)
    if PortNumber is not None or MatchReg is not None:
        raise Exception(f"Incorrect arguments on line {LineNumber}")

    ArgA = PortNumber << REGA_POS
    ArgB = int(MatchReg.groups()[0]) << REGB_POS
    
    return ArgA | ArgB



def PortImm(Args: list[str], LineNumber: int) -> int:
    # Syntax: STPI #/0x{PortNum}, #/0x{Val}

    if(len(Args) != 2):
        raise Exception(f"Incorrect number of arguments on line {LineNumber}")

    ArgA: int = 0x00
    ArgB: int = 0x00

    PortNumber: int = __DecOrHexSearch(Args[0])
    ValueC: int  = __DecOrHexSearch(Args[1])

    if PortNumber is None or ValueC is None:
        raise Exception(f"Incorrect arguments on line {LineNumber}")
    
    ArgA = PortNumber << REGA_POS
    ArgB = ValueC << REGB_POS

    return ArgA | ArgB
