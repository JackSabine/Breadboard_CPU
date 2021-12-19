import os, sys
path: str = os.path.dirname(__file__)
while(not path.endswith("Assembler")):
    path = os.path.dirname(path)
sys.path.append(os.path.dirname(path))

from Assembler.v1_1.ucode.macros import *

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


def CreateBitArgs(Operation: str, Args: list[str], SymbolTable: dict[str, int], Instruction_MemoryIndex: int, LineNumber: int) -> int:

    BitArgs: int

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
        raise Exception(f"Operation {Operation} on line {LineNumber} recognized in OPCODE_MAP but does not appear in any instruction collections")
    
    return (BitArgs)



def TwoReg(Args: list[str], LineNumber: int) -> int:
    if(len(Args) != 2):
        raise Exception(f"Incorrect number of arguments on line {LineNumber}")

    ArgA: int
    ArgB: int
    MatchA: re.Match
    MatchB: re.Match
    
    MatchA = re.search(r"r([0-7])",Args[0],re.IGNORECASE)   
    MatchB = re.search(r"r([0-7])",Args[1],re.IGNORECASE)

    if(MatchA is None or MatchB is None):
        raise Exception(f"Incorrect arguments on line {LineNumber}")

    ArgA = int(MatchA.groups()[0]) << REGA_POS
    ArgB = int(MatchB.groups()[0]) << REGB_POS

    return (ArgA | ArgB)



def RegImm(Args: list[str], LineNumber: int) -> int:
    if(len(Args) != 2):
        raise Exception(f"Incorrect number of arguments on line {LineNumber}")

    ArgA: int
    ArgC: int
    MatchA: re.Match
    ValueC: int

    MatchA = re.search(r"r([0-7])", Args[0], re.IGNORECASE)
    ValueC = __DecOrHexSearch(Args[1])

    if(MatchA is None or ValueC is None):
        raise Exception(f"Incorrect arguments on line {LineNumber}")

    MaxPos =  (2**NUM_IMM_BITS) - 1 
    MaxNeg = -(2**NUM_IMM_BITS)

    if(ValueC not in range(MaxNeg, MaxPos+1, 1)):
        raise Exception(f"LD immediate value on line {LineNumber} exceeds max range [{MaxNeg},{MaxPos}]")

    ArgA = int(MatchA.groups()[0]) << REGA_POS
    ArgC = (ValueC & 0xFF) << IMM_POS

    return (ArgA | ArgC)



def SingR(Args: list[str], LineNumber: int):
    if(len(Args) != 1):
        raise Exception(f"Incorrect number of arguments on line {LineNumber}")

    ArgA: int
    MatchA: re.Match

    MatchA = re.search(r"r([0-7])",Args[0],re.IGNORECASE)

    if(MatchA is None):
        raise Exception(f"Incorrect arguments on line {Args}")

    ArgA = int(MatchA.groups()[0]) << REGA_POS
    
    return (ArgA)



def PCOff(Args: list[str], LineNumber: int, SymbolTable: dict[str, int], Instruction_MemoryIndex: int):
    if(len(Args) != 1):
        raise Exception(f"Incorrect number of arguments on line {LineNumber}")
    if(SymbolTable.get(Args[0]) is None):
        raise Exception(f"Label {Args[0]} has no defined destination on line {LineNumber}")

    PCOffset: int
    MaxPos: int
    MaxNeg: int

    PCOffset = SymbolTable.get(Args[0]) - (Instruction_MemoryIndex + 1)
    MaxPos = (2**(NUM_JUMP_BITS-1))             # Example 1024 and -1023 (not typical -1024 to 1023 because of PC+1)
    MaxNeg = (-1*2**(NUM_JUMP_BITS-1) + 1)

    if(PCOffset not in range(MaxNeg, MaxPos+1, 1)):
        raise Exception(f"Jump/Call on line {LineNumber} to label {Args[0]} exceeds max range [{MaxNeg},{MaxPos}]")
    
    return (PCOffset & 0x07FF)        # Return lower 11 bits
    


def NoArg():
    return (0x0000)



def BaseR(Args: list[str], LineNumber: int):
    if(len(Args) != 3):
        raise Exception(f"Incorrect number of arguments on line {LineNumber}")

    ArgA: int
    ArgB: int
    ArgC: int
    MatchA: re.Match
    MatchB: re.Match
    ValueC: int

    MatchA = re.search(r"r([0-7])",Args[0],re.IGNORECASE)
    MatchB = re.search(r"r([0-7])",Args[1],re.IGNORECASE)
    ValueC = __DecOrHexSearch(Args[2])

    if(MatchA is None or MatchB is None or ValueC is None):
        raise Exception(f"Incorrect arguments on line {LineNumber}")

    ArgA = int(MatchA.groups()[0]) << REGA_POS
    ArgB = int(MatchB.groups()[0]) << REGB_POS
    ArgC = (ValueC & 0x1F) << IMM_POS

    MaxPos = (2**NUM_BASER_OFFSET_BITS)-1
    MaxNeg = -(2**NUM_BASER_OFFSET_BITS)

    if(ArgC not in range(MaxNeg, MaxPos+1, 1)):
        raise Exception(f"LDR/STR offset on line {LineNumber} exceeds max range [{MaxNeg},{MaxPos}]")

    return (ArgA | ArgB | ArgC)



# Operation must be in set: OTHER
def Other(Operation: str, Args: list[str], LineNumber: int):    

    ArgC: int
    ValueC: int

    if(Operation == "TRAP"):
        if(len(Args) != 1):
            raise Exception(f"Incorrect number of arguments on line {LineNumber}")

        ValueC = __DecOrHexSearch(Args[0])

        if(ValueC is None):
            raise Exception(f"Incorrect arguments on line {LineNumber}")

        ArgC = ValueC

        MaxPos = (2**NUM_TRAPV_BITS)-1
        MaxNeg = -(2**NUM_TRAPV_BITS)

        if(ArgC not in range(MaxNeg, MaxPos+1, 1)):
            raise Exception(f"TRAP vector exceeds on line {LineNumber} exceeds max range [{hex(MaxNeg)},{hex(MaxPos)}]")

        return (ArgC)

    else:
        raise Exception(f"Operation {Operation} in set OTHER {OTHER}, but does not match any instructions")



# Syntax: STP #/0x{PortNum}, r[0-7]
def PortReg(Args: list[str], LineNumber: int) -> int:
    if(len(Args) != 2):
        raise Exception(f"Incorrect number of arguments on line {LineNumber}")

    ArgA: int
    ArgB: int
    PortNumber: int
    MatchA: re.Match
    
    PortNumber = __DecOrHexSearch(Args[0])
    MatchA = re.search(r"r([0-7])",Args[1],re.IGNORECASE)

    if(PortNumber is None or MatchA is None):
        raise Exception(f"Incorrect arguments on line {LineNumber}")

    ArgA = PortNumber << REGA_POS
    ArgB = int(MatchA.groups()[0]) << REGB_POS
    
    return (ArgA | ArgB)



# Syntax: STPI #/0x{PortNum}, #/0x{Val}
def PortImm(Args: list[str], LineNumber: int) -> int:
    if(len(Args) != 2):
        raise Exception(f"Incorrect number of arguments on line {LineNumber}")

    ArgA: int
    ArgC: int
    PortNumber: int
    ValueC: int

    PortNumber = __DecOrHexSearch(Args[0])
    ValueC = __DecOrHexSearch(Args[1])

    if(PortNumber is None or ValueC is None):
        raise Exception(f"Incorrect arguments on line {LineNumber}")
    
    ArgA = PortNumber << REGA_POS
    ArgC = ValueC << IMM_POS

    return (ArgA | ArgC)
