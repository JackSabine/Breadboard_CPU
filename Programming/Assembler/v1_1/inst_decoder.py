import os, sys
path: str = os.path.dirname(__file__)
while(not path.endswith("Assembler")):
    path = os.path.dirname(path)
sys.path.append(os.path.dirname(path))

from Assembler.v1_1.ucode.macros import *
import Assembler.v1_1.InstructionDefinition as InstDef
import re, enum


def __ExtractRegister(Word: int, RegPos: int) -> str:
    Reg: int

    Reg = (Word >> RegPos) & 0x07

    return (f"r{Reg}")


def __ExtractSignedImmediate(Word: int, ImmPos: int, ImmWidth: int) -> str:
    SignedImmediate: int
    HexValue: int
    Mask: int

    Mask = (1 << ImmWidth) - 1
    HexValue = (Word >> ImmPos) & Mask

    if(HexValue >> (ImmWidth-1) == 1):
        SignedImmediate = HexValue - (1 << ImmWidth)
    else:
        SignedImmediate = HexValue

    return ("#{} / 0x{:0{}X}".format(SignedImmediate, HexValue, 2))


def __ExtractBitfield(Word: int, EndIndex: int, StartIndex: int) -> int:
    Mask: int

    Mask = ( 1 << (abs(EndIndex - StartIndex) + 1) ) - 1

    return ((Word >> StartIndex) & Mask)


def __ParseDataAsASCII(Word: int) -> str:
    if(Word in range(0, 256)):
        return f"'{chr(Word)}'"
    else:
        return "' '"



def __ParseInstruction(Word: int) -> str:
    Operation: str
    OpMask: int
    Arguments: list[str] = []

    OpMask = (1 << NUM_OPC_BITS) - 1
    Operation = InstDef.OPERATION_DICT.get((Word >> INSTRUCTION_POS) & OpMask)

    if(Operation is not None):
        if(Operation in InstDef.TWOREG):
            Arguments.append(__ExtractRegister(Word, REGA_POS))
            Arguments.append(__ExtractRegister(Word, REGB_POS))
        elif(Operation in InstDef.REGIMM):
            Arguments.append(__ExtractRegister(Word, REGA_POS))
            Arguments.append(__ExtractSignedImmediate(Word, IMM_POS, NUM_IMM_BITS))
        elif(Operation in InstDef.SINGR):
            Arguments.append(__ExtractRegister(Word, REGA_POS))
        elif(Operation in InstDef.PCOFF):
            Arguments.append(__ExtractSignedImmediate(Word, IMM_POS, NUM_JUMP_BITS))
        elif(Operation in InstDef.NOARG):
            pass
        elif(Operation in InstDef.BASER):
            Arguments.append(__ExtractRegister(Word, REGA_POS))
            Arguments.append(__ExtractRegister(Word, REGB_POS))
            Arguments.append(__ExtractSignedImmediate(Word, IMM_POS, NUM_BASER_OFFSET_BITS))
        elif(Operation in InstDef.OTHER):
            if(Operation == "TRAP"):
                Arguments.append(hex(__ExtractBitfield(Word, 16-NUM_OPC_BITS, 0)))
            elif(Operation == "LEA"):
                Arguments.append(__ExtractRegister(Word, REGA_POS))
                Arguments.append(__ExtractSignedImmediate(Word, IMM_POS, NUM_LEA_BITS))
                pass
            else:
                raise Exception(f"Operation {Operation} appears in set OTHER ({InstDef.OTHER}) but is not implemented")
        elif(Operation in InstDef.PORTIMM):
            Arguments.append(hex(__ExtractBitfield(Word, 10, 8)))
            Arguments.append(__ExtractSignedImmediate(Word, IMM_POS, NUM_IMM_BITS))
        elif(Operation in InstDef.PORTREG):
            Arguments.append(hex(__ExtractBitfield(Word, 10, NUM_IMM_BITS)))
            Arguments.append(__ExtractRegister(Word, REGB_POS))
        else:
            raise Exception(f"While re-parsing, Operation {Operation} recognized in OPCODE_DICT but does not appear in any instruction collections")
        return ("{:<6} {}".format(Operation, ", ".join(Arguments)))

    else:
        return ("None")



def DecodeBinary(BinarySource: str, OutputFile: str):
    MemoryBytes: bytes
    MemoryWord: int
    MemoryIndex: int = 0x0000
    CurLinStr: str

    # Re-parse binary
    with open(BinarySource, "rb") as Reparse:
        
        with open(OutputFile, "w") as Output:
            CurLinStr = "{} | {} | {}\n".format(
                str.ljust("Addrs", 4 + 2),
                str.ljust("Instruction Disassembly", 30),
                str.ljust("ASCII Character", 20)
            )
            Output.write(CurLinStr)

            CurLineStr = "-"*(4+2+1+30+20+5) + "\n"
            Output.write(CurLineStr)

            while(MemoryBytes := Reparse.read(2)):

                MemoryWord = int.from_bytes(MemoryBytes, "little")

                CurLinStr = "0x{:0{}X} | {} | {}\n".format(
                    MemoryIndex,
                    4,
                    str.ljust(__ParseInstruction(MemoryWord), 30),
                    __ParseDataAsASCII(MemoryWord)
                )

                Output.write(CurLinStr)
                MemoryIndex += 1

    return

class __FlagState(enum.Enum):
    BIN_FILE    = 0
    OUT_FILE    = 1

if __name__ == "__main__":
    cwd: str = os.getcwd()

    InFile  = None
    OutFile = None
    StateV  = None

    # InFile = "./Programs/HelloWorld_1_1.asm"
    # OutFile = "./Assembler/v1_1/Testing.bin"

    if(len(sys.argv) < 2):
        raise Exception("Not enough input arguments")

    for arg in sys.argv[1:]:
        if(re.search(r"-b", arg, re.IGNORECASE)):
            StateV = __FlagState.BIN_FILE
        elif(re.search(r"-o", arg, re.IGNORECASE)):
            StateV = __FlagState.OUT_FILE
        else:
            if(StateV == __FlagState.BIN_FILE):
                InFile = arg
            elif(StateV == __FlagState.OUT_FILE):
                OutFile = arg   

    if(OutFile is None):
        OutFile = rf"{cwd}/a.bin"

    if(InFile is None):
        raise Exception("Specify an input file with -c <file>")

    DecodeBinary(InFile, OutFile)