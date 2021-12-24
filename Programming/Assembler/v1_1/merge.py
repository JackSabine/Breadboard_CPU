import os, sys
path: str = os.path.dirname(__file__)
while(not path.endswith("Assembler")):
    path = os.path.dirname(path)
sys.path.append(os.path.dirname(path))

import re, enum
from Assembler.v1_1.ucode.macros import NUM_CODE_ADDRESS_PINS
import Assembler.v1_1.Utils as Utils

class __FlagState(enum.Enum):
    MERGE_FILES     = 0
    WRITE_FILE      = 1

def Merge(InFiles, OutFile):

    if(InFiles == []):
        raise Exception("No input files provided")

    Merged = bytearray(2**NUM_CODE_ADDRESS_PINS)

    for File in InFiles:
        with open(File, "rb") as Inp:
            Bytes = Inp.read()
            for Idx, _ in enumerate(Bytes):
                Merged[Idx] |= Bytes[Idx]

    Utils.Write(Merged, OutFile)

if __name__ == "__main__":
    FlagState = None
    InFiles = []
    OutFile = r"a.bin"
    for arg in sys.argv[1:]:
        if(re.search(r"^-m$", arg, re.IGNORECASE)):
            FlagState = __FlagState.MERGE_FILES
        elif(re.search(r"^-o$", arg, re.IGNORECASE)):
            FlagState = __FlagState.WRITE_FILE
        else:
            if(FlagState == __FlagState.MERGE_FILES):
                InFiles.append(arg)
            elif(FlagState == __FlagState.WRITE_FILE):
                OutFile = arg
            else:
                raise Exception("Missing flag before arguments")
    Merge(InFiles, OutFile)