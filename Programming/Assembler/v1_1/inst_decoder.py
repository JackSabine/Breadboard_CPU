import os, sys
path: str = os.path.dirname(__file__)
while(not path.endswith("Assembler")):
    path = os.path.dirname(path)
sys.path.append(os.path.dirname(path))

from Assembler.v1_1.ucode.macros import *



def __ExtractRegister(Word: int, RegPos: int) -> str:
    Reg: int

    Reg = (Word >> RegPos) & 0x07

    return (f"r{Reg}")



def __ExtractSignedImmediate(Word: int, ImmPos: int, ImmWidth: int) -> str:
    SignedImmediate: int
    Mask: int

    Mask = (1 << ImmWidth) - 1
    SignedImmediate = (Word >> ImmPos) & Mask

    return (f"#{SignedImmediate}")

def __ParseDataAsASCII(Word: int) -> str:
    if(Word in range(0, 256)):
        return f"'{chr(Word)}'"
    else:
        return "' '"


def DecodeBinary(BinarySource: str, OutputFile: str):
    MemoryBytes: bytes
    MemoryWord: int
    # Re-parse binary
    with open(BinarySource, "rb") as Reparse:
        
        MemoryBytes = Reparse.read(2)
        while(MemoryBytes):
            MemoryWord = int.from_bytes(MemoryBytes, "little")







            MemoryBytes = Reparse.read(2)
        
        print("exit")


    return