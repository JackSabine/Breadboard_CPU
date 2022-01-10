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
            
            Operation, *Arguments = MemoryMap.MemoryBlock[i].GetWordList()
            Operation = Operation.upper()

            if(Operation not in OPCODE_DICT):
                raise Exception(f"Instruction {Operation} on line {MemoryMap.MemoryBlock[i].GetAssociatedLineNumber()} is an invalid instruction")

            InstructionOp = OPCODE_DICT.get(Operation) << INSTRUCTION_POS

            InstructionArgs = __CreateBitArgs(
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
            ProgramMemory[2*i + 0] = MemoryMap.MemoryBlock[i].GetCellValue() & IMM_MASK
            ProgramMemory[2*i + 1] = 0x00

    return

def __CreateBitArgs(Operation: str, Args: list[str], SymbolTable: dict[str, int], Instruction_MemoryIndex: int, LineNumber: int) -> int:

    BitArgs: int

    if(Operation in InstDef.TWOREG):
        BitArgs = TwoReg(Args, LineNumber)
    elif(Operation in InstDef.REGIMM):
        BitArgs = RegImm(Args, LineNumber)
    elif(Operation in InstDef.SINGR):
        BitArgs = SingR(Args, LineNumber)
    elif(Operation in InstDef.PCOFF):
        BitArgs = JumpInstruction(Args, LineNumber, SymbolTable, Instruction_MemoryIndex)
    elif(Operation in InstDef.NOARG):
        BitArgs = NoArg()
    elif(Operation in InstDef.BASER):
        BitArgs = BaseR(Args, LineNumber)
    elif(Operation in InstDef.OTHER):
        BitArgs = Other(Operation, Args, LineNumber, SymbolTable, Instruction_MemoryIndex)
    elif(Operation in InstDef.PORTIMM):
        BitArgs = PortImm(Args, LineNumber)
    elif(Operation in InstDef.PORTREG):
        BitArgs = PortReg(Args, LineNumber)
    else:
        raise Exception(f"Operation {Operation} on line {LineNumber} recognized in OPCODE_MAP but does not appear in any instruction collections")
    
    return (BitArgs)



def CheckNumArgs(Args: list[str], ExpectedNum: int, LineNumberForExceptions: int) -> None:
    if(len(Args) != ExpectedNum):
        raise Exception(f"Incorrect number of arguments on line {LineNumberForExceptions}")
    
    return
    


def ParseReg(Arg: str, LineNumberForExceptions: int) -> int:
    Match: re.Match = re.search(r"r([0-7])", Arg, re.IGNORECASE)

    if(Match is not None):
        return int(Match.groups()[0])
    else:
        raise Exception(f"Incorrect arguments on line {LineNumberForExceptions}")



def ParseSignedImmediate(Arg: str, BitWidth: int, LineNumberForExceptions: int) -> int:
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



def CalcPCOffset(TargetLabel: str, SymbolTable: dict[str, int], LineNumberForExceptions: int, Instruction_MemoryAddress: int, PCOffsetBitWidth: int) -> int:
    if(SymbolTable.get(TargetLabel) is None):
        raise Exception(f"Label {TargetLabel} has no defined destination on line {LineNumberForExceptions}")

    BitMask: int = (1 << PCOffsetBitWidth) - 1
    PCOffset: int = SymbolTable.get(TargetLabel) - (Instruction_MemoryAddress + 1)
    MaxPos: int = 2**(PCOffsetBitWidth-1)             # Example 1024 and -1023 (not typical -1024 to 1023 because of PC+1)
    MaxNeg: int = -(2**(PCOffsetBitWidth-1)) + 1

    if(PCOffset not in range(MaxNeg, MaxPos+1, 1)):
        raise Exception(f"PC Offset on line {LineNumberForExceptions} to label {TargetLabel} exceeds max range [{MaxNeg},{MaxPos}]")

    return (PCOffset & BitMask)



def TwoReg(Args: list[str], LineNumber: int) -> int:
    CheckNumArgs(Args, 2, LineNumber)

    ArgA: int = ParseReg(Args[0], LineNumber) << REGA_POS
    ArgB: int = ParseReg(Args[1], LineNumber) << REGB_POS

    return (ArgA | ArgB)



def RegImm(Args: list[str], LineNumber: int) -> int:
    CheckNumArgs(Args, 2, LineNumber)

    ArgA: int = ParseReg(Args[0], LineNumber) << REGA_POS
    ImmVal: int = ParseSignedImmediate(Args[1], NUM_IMM_BITS, LineNumber) << IMM_POS

    return (ArgA | ImmVal)



def SingR(Args: list[str], LineNumber: int):
    CheckNumArgs(Args, 1, LineNumber)

    ArgA: int = ParseReg(Args[0], LineNumber) << REGA_POS
    
    return (ArgA)



def JumpInstruction(Args: list[str], LineNumber: int, SymbolTable: dict[str, int], Instruction_MemoryIndex: int):
    CheckNumArgs(Args, 1, LineNumber)

    return CalcPCOffset(Args[0], SymbolTable, LineNumber, Instruction_MemoryIndex, NUM_JUMP_BITS) << JUMP_POS 


NoArg = lambda: 0x0000



def BaseR(Args: list[str], LineNumber: int):
    CheckNumArgs(Args, 3, LineNumber)

    ArgA: int = ParseReg(Args[0], LineNumber) << REGA_POS
    ArgB: int = ParseReg(Args[1], LineNumber) << REGB_POS
    ValueC: int = ParseSignedImmediate(Args[2], NUM_BASER_OFFSET_BITS, LineNumber) << IMM_POS

    return (ArgA | ArgB | ValueC)



# Operation must be in set: OTHER
def Other(Operation: str, Args: list[str], LineNumber: int, SymbolTable: dict[str, int], Instruction_MemoryAddress: int):    

    if(Operation == "TRAP"):
        CheckNumArgs(Args, 1, LineNumber)

        TRAP_TABLE_START_POS: int = 0x0100

        ValueC: int = ParseSignedImmediate(Args[0], NUM_TRAPV_BITS, LineNumber)

        return (ValueC + TRAP_TABLE_START_POS)

    elif(Operation == "LEA"):
        CheckNumArgs(Args, 2, LineNumber)

        ArgA: int = ParseReg(Args[0], LineNumber)
        ValueC: int = CalcPCOffset(Args[1], SymbolTable, LineNumber, Instruction_MemoryAddress, NUM_LEA_BITS) << JUMP_POS

        return (ArgA | ValueC)


    else:
        raise Exception(f"Operation {Operation} in set OTHER {InstDef.OTHER}, but does not match any instructions")



# Syntax: STP #/0x{PortNum}, r[0-7]
def PortReg(Args: list[str], LineNumber: int) -> int:
    CheckNumArgs(Args, 2, LineNumber)

    ArgA: int = ParseSignedImmediate(Args[0], NUM_PORT_BITS, LineNumber) << PORT_POS
    ArgB: int = ParseReg(Args[1], LineNumber) << REGB_POS
    
    return (ArgA | ArgB)
    


# Syntax: STPI #/0x{PortNum}, #/0x{Val}
def PortImm(Args: list[str], LineNumber: int) -> int:
    CheckNumArgs(Args, 2, LineNumber)

    ArgA: int = ParseSignedImmediate(Args[0], NUM_PORT_BITS, LineNumber) << PORT_POS
    ArgC: int = ParseSignedImmediate(Args[1], NUM_IMM_BITS, LineNumber) << IMM_POS

    return (ArgA | ArgC)
