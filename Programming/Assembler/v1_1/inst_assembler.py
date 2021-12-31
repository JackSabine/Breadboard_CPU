import os, sys
path: str = os.path.dirname(__file__)
while(not path.endswith("Assembler")):
    path = os.path.dirname(path)
sys.path.append(os.path.dirname(path))

from Assembler.v1_1.ucode.macros import *
import Assembler.v1_1.Utils as Utils
import Assembler.v1_1.InstructionDefinition as InstDef
from Assembler.v1_1.classes import *
from Assembler.v1_1.InstructionDefinition import OPCODE_DICT

import re

def InterpretInstructions(MemoryMap: OSymbolicMemoryMap, ProgramMemory: bytearray) -> None:
    # Iterate over each instruction in MemoryMap
    Operation: str
    Arguments: list[str]

    for i, _ in enumerate(MemoryMap.MemoryBlock):
        if(MemoryMap.MemoryBlock[i].IsCellAnInstruction()):
            
            Operation = MemoryMap.MemoryBlock[i].GetWordList()[0].upper()
            Arguments = MemoryMap.MemoryBlock[i].GetWordList()[1:]

            if(Operation.upper() not in OPCODE_DICT):
                raise Exception(f"Instruction {Operation} on line {MemoryMap.MemoryBlock[i].GetAssociatedLineNumber()} is an invalid instruction")

            InstructionOp = OPCODE_DICT.get(Operation.upper()) << INSTRUCTION_POS

            InstructionArgs = CreateBitArgs(
                Operation               =   Operation, 
                Args                    =   Arguments,
                SymbolTable             =   MemoryMap.SymbolTable,
                Instruction_MemoryIndex =   i,
                LineNumber              =   MemoryMap.MemoryBlock[i].GetAssociatedLineNumber()
            )

            Instruction = InstructionOp | InstructionArgs

            ProgramMemory[2*i + 0] = (Instruction >> 0) & 0xFF
            ProgramMemory[2*i + 1] = (Instruction >> 8) & 0xFF
        else:
            # No instruction to assemble, just copy raw data
            ProgramMemory[2*i + 0] = MemoryMap.MemoryBlock[i].GetCellValue() & 0xFF
            ProgramMemory[2*i + 1] = 0x00

    return

def CreateBitArgs(Operation: str, Args: list[str], SymbolTable: dict[str, int], Instruction_MemoryIndex: int, LineNumber: int) -> int:

    BitArgs: int

    if(Operation in InstDef.TWOREG):
        BitArgs = TwoReg(Args, LineNumber)
    elif(Operation in InstDef.REGIMM):
        BitArgs = RegImm(Args, LineNumber)
    elif(Operation in InstDef.SINGR):
        BitArgs = SingR(Args, LineNumber)
    elif(Operation in InstDef.PCOFF):
        BitArgs = PCOff(Args, LineNumber, SymbolTable, Instruction_MemoryIndex)
    elif(Operation in InstDef.NOARG):
        BitArgs = NoArg()
    elif(Operation in InstDef.BASER):
        BitArgs = BaseR(Args, LineNumber)
    elif(Operation in InstDef.OTHER):
        BitArgs = Other(Operation, Args, LineNumber)
    elif(Operation in InstDef.PORTIMM):
        BitArgs = PortImm(Args, LineNumber)
    elif(Operation in InstDef.PORTREG):
        BitArgs = PortReg(Args, LineNumber)
    else:
        raise Exception(f"Operation {Operation} on line {LineNumber} recognized in OPCODE_MAP but does not appear in any instruction collections")
    
    return (BitArgs)



def ParseReg(Arg: str, LineNumberForExceptions: int) -> int:
    Match: re.Match = re.search(r"r([0-7])", Arg, re.IGNORECASE)

    if(Match is not None):
        return int(Match.groups()[0])
    else:
        raise Exception(f"Incorrect arguments on line {LineNumberForExceptions}")



def ParseImmediate(Arg: str, BitWidth: int, LineNumberForExceptions: int) -> int:
    Value = Utils.DecOrHexSearch(Arg)
    BitMask: int = (1 << BitWidth) - 1

    if(Value is not None):
        MaxPos =  (2**BitWidth) - 1 
        MaxNeg = -(2**BitWidth)

        if(Value not in range(MaxNeg, MaxPos+1, 1)):
            raise Exception(f"Immediate value on line {LineNumberForExceptions} exceeds max range [{MaxNeg},{MaxPos}]")

        return (Value & BitMask)

    else:
        raise Exception(f"Incorrect arguments on line {LineNumberForExceptions}")



def TwoReg(Args: list[str], LineNumber: int) -> int:
    if(len(Args) != 2):
        raise Exception(f"Incorrect number of arguments on line {LineNumber}")

    ArgA: int = ParseReg(Args[0], LineNumber) << REGA_POS
    ArgB: int = ParseReg(Args[1], LineNumber) << REGB_POS

    return (ArgA | ArgB)



def RegImm(Args: list[str], LineNumber: int) -> int:
    if(len(Args) != 2):
        raise Exception(f"Incorrect number of arguments on line {LineNumber}")

    ArgA: int = ParseReg(Args[0], LineNumber) << REGA_POS
    ImmVal: int = ParseImmediate(Args[1], NUM_IMM_BITS, LineNumber) << IMM_POS

    return (ArgA | ImmVal)



def SingR(Args: list[str], LineNumber: int):
    if(len(Args) != 1):
        raise Exception(f"Incorrect number of arguments on line {LineNumber}")

    ArgA: int = ParseReg(Args[0], LineNumber) << REGA_POS
    
    return (ArgA)



def PCOff(Args: list[str], LineNumber: int, SymbolTable: dict[str, int], Instruction_MemoryIndex: int):
    if(len(Args) != 1):
        raise Exception(f"Incorrect number of arguments on line {LineNumber}")
    if(SymbolTable.get(Args[0]) is None):
        raise Exception(f"Label {Args[0]} has no defined destination on line {LineNumber}")

    PCOffset: int
    MaxPos: int
    MaxNeg: int
    BitMask: int = (1 << NUM_JUMP_BITS) - 1

    PCOffset = SymbolTable.get(Args[0]) - (Instruction_MemoryIndex + 1)
    MaxPos = (2**(NUM_JUMP_BITS-1))             # Example 1024 and -1023 (not typical -1024 to 1023 because of PC+1)
    MaxNeg = (-1*2**(NUM_JUMP_BITS-1) + 1)

    if(PCOffset not in range(MaxNeg, MaxPos+1, 1)):
        raise Exception(f"Jump/Call on line {LineNumber} to label {Args[0]} exceeds max range [{MaxNeg},{MaxPos}]")
    
    return (PCOffset & BitMask)
    


NoArg = lambda: 0x0000


def BaseR(Args: list[str], LineNumber: int):
    if(len(Args) != 3):
        raise Exception(f"Incorrect number of arguments on line {LineNumber}")

    ArgA: int = ParseReg(Args[0], LineNumber) << REGA_POS
    ArgB: int = ParseReg(Args[1], LineNumber) << REGB_POS
    ValueC: int = ParseImmediate(Args[2], NUM_BASER_OFFSET_BITS, LineNumber) << IMM_POS

    return (ArgA | ArgB | ValueC)



# Operation must be in set: OTHER
def Other(Operation: str, Args: list[str], LineNumber: int):    

    ValueC: int

    if(Operation == "TRAP"):
        if(len(Args) != 1):
            raise Exception(f"Incorrect number of arguments on line {LineNumber}")

        ValueC = ParseImmediate(Args[0], NUM_TRAPV_BITS, LineNumber)

        return (ValueC)

    else:
        raise Exception(f"Operation {Operation} in set OTHER {InstDef.OTHER}, but does not match any instructions")



# Syntax: STP #/0x{PortNum}, r[0-7]
def PortReg(Args: list[str], LineNumber: int) -> int:
    if(len(Args) != 2):
        raise Exception(f"Incorrect number of arguments on line {LineNumber}")

    ArgA: int = ParseImmediate(Args[0], NUM_PORT_BITS, LineNumber) << PORT_POS
    ArgB: int = ParseReg(Args[1], LineNumber)
    
    return (ArgA | ArgB)
    


# Syntax: STPI #/0x{PortNum}, #/0x{Val}
def PortImm(Args: list[str], LineNumber: int) -> int:
    if(len(Args) != 2):
        raise Exception(f"Incorrect number of arguments on line {LineNumber}")

    ArgA: int = ParseImmediate(Args[0], NUM_PORT_BITS, LineNumber) << PORT_POS
    ArgC: int = ParseImmediate(Args[1], NUM_IMM_BITS) << IMM_POS

    return (ArgA | ArgC)
