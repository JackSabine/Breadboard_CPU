import sys, os, enum, re
from writer import Write
from ISA.v1_1.ashelp import *

def Assemble(FileToCompile, FileToWrite):

    Binary = bytearray(2 ** 15)

    # Read in data 
    with open(FileToCompile, 'r') as F:
        Raw = F.readlines()
    
    # UneditedLines is an ordered list of all lines in FileToCompile
    UneditedLines: list[OLine] = []
    for i in range(len(Raw)):
        UneditedLines.append(OLine(Text=Raw[i], LineNumber=i+1))

    # Need to iterate through each line and filter out excess whitespace, comments, blank lines
    FilteredSplitLines: list[OLineSplit] = []
    CurText: str
    CurNum: int
    for ULine in UneditedLines:
        CurText = ULine.Text
        CurNum = ULine.LineNumber

        if(CurText.find(";") != -1):
            CurText = CurText[ : CurText.find(";") ]
        
        CurText = CurText.strip()

        # Delete newlines and replace commas with spaces
        CurText = CurText.replace("\n", "").replace(",", " ")

        # Remove blank lines
        if CurText != "":

            # Split each line by spaces (commas replaced with spaces)
            FilteredSplitLines.append(OLineSplit(Text=CurText.split(), LineNumber=CurNum))

    # Identify assembler directives and do not translate those to binary
    # Current directives:
    # .ORIG (active until next ORIG found)
    # .INCLUDE (file-wide include)


class __FlagState(enum.Enum):
    SRC_FILE     = 0
    OUT_FILE     = 1

if __name__ == "__main__":
    cwd = os.getcwd()

    InFile  = None
    OutFile = None
    StateV  = None

    InFile = "./Programs/OSR_1_1.asm"
    OutFile = "./Utils/Testing.bin"

    # if(len(sys.argv) < 2):
    #     raise Exception("Not enough input arguments")

    # for arg in sys.argv[1:]:
    #     if(re.search(r"-c", arg, re.IGNORECASE)):
    #         StateV = __FlagState.SRC_FILE
    #     elif(re.search(r"-o", arg, re.IGNORECASE)):
    #         StateV = __FlagState.OUT_FILE
    #     else:
    #         if(StateV == __FlagState.SRC_FILE):
    #             InFile = arg
    #         elif(StateV == __FlagState.OUT_FILE):
    #             OutFile = arg   

    # if(OutFile is None):
    #     OutFile = rf"{cwd}/a.bin"

    # if(InFile is None):
    #     raise Exception("Specify an input file with -c <file>")

    Assemble(FileToCompile=InFile, FileToWrite=OutFile)