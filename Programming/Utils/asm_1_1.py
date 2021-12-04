import sys, os, enum, re
from writer import Write
from ISA.v1_1.ashelp import *

def __DecOrHexSearch(str):
    MatchDec = re.search(r"#(-?[0-9]+)",str,re.IGNORECASE)
    MatchHex = re.search(r"0?x([0-9A-F]+)",str,re.IGNORECASE)
    RetVal = None

    if MatchDec is not None:
        RetVal = int(MatchDec.groups()[0])
    elif MatchHex is not None:
        RetVal = int(MatchHex.groups()[0],base=16)

    return RetVal

def __FilterLinesAndSplitOnSpaces(UneditedLines: list[OLine]):
    # Need to iterate through each line and filter out excess whitespace, comments, blank lines
    FilteredSplitLines: list[OLineSplit] = []
    CurText: str
    CurNum: int
    IsCurAnInstruction: bool

    for ULine in UneditedLines:
        CurText = ULine.Text
        CurNum = ULine.LineNumber
        

        if(CurText.find(";") != -1):
            CurText = CurText[ : CurText.find(";") ]
        
        # If we find a single character, continue parsing
        if(re.search(r"[\S]+", CurText)):
            IsCurAnInstruction = CurText.startswith(("\t", " "))
            CurText = CurText.strip()
            # Delete newlines and replace commas with spaces
            CurText = CurText.replace("\n", "").replace(",", " ")
            # print("{:<40} is {:<3} an instruction".format(CurText, "" if IsCurAnInstruction else "not"))

            # Remove blank lines
            if CurText != "":
                # Split each line by spaces (commas replaced with spaces)
                FilteredSplitLines.append(OLineSplit(WordList=CurText.split(), LineNumber=CurNum, IsAnInstruction=IsCurAnInstruction))
        
    return FilteredSplitLines

def __CreateLineGroups(FilteredSplitLines: list[OLineSplit]) -> tuple[list[OLineGroup], list[str]]:
    # Identify assembler directives and do not translate those to binary
    # Current directives:
    # .ORIG (active until next ORIG found)
    # .INCLUDE (for macro defintions)

    LineGroups: list[OLineGroup] = []
    LineGroupIdx: int = -1
    CurrentORIG: int = 0x0000
    IncludeFiles: list[str] = []
    IncludeFile: re.Match

    for FSLine in FilteredSplitLines:
        # Check if the current line is an assembler directive
        if(FSLine.WordList[0].startswith(".")):
            # Process an assembler directive
            if  (re.search(r"^.ORIG$",      FSLine.WordList[0], re.IGNORECASE) is not None):
                if(len(FSLine.WordList) < 2):
                    raise Exception(f"Insufficient number of arguments for .ORIG directive on line {FSLine.LineNumber}")

                CurrentORIG = __DecOrHexSearch(FSLine.WordList[1])

                if(CurrentORIG is not None):
                    LineGroupIdx += 1
                    LineGroups.append(OLineGroup(Origin=CurrentORIG, Lines=[]))
                else:
                    raise Exception(f"Incorrect arguments on line {FSLine.LineNumber}")

            elif(re.search(r"^.INCLUDE$",   FSLine.WordList[0], re.IGNORECASE) is not None):
                if(len(FSLine.WordList) < 2):
                    raise Exception(f"Insufficient number of arguments for .INCLUDE directive on line {FSLine.LineNumber}")
                IncludeFile = re.search(r"([A-Za-z0-9_]+.h)", FSLine.WordList[1])
                if(IncludeFile is not None):
                    IncludeFiles.append(IncludeFile.groups()[0])
                else:
                    raise Exception(f"Incorrect arguments on line {FSLine.LineNumber}")
        else:
            if(LineGroupIdx >= 0):
                LineGroups[LineGroupIdx].Lines.append(FSLine)
            else:
                raise Exception(f"Line {FSLine.LineNumber} does not fall under any .ORIG directive")

    return (LineGroups, IncludeFiles)

def __ParseHeaders(IncludeFiles: list[str], SourceDir: str) -> dict[str, str]:
    IncludedMacros: dict[str, str] = {}
    CurrentMacro: str
    MacroMatch: re.Match
    for IncF in IncludeFiles:
        # Search in the directory above the assembler
        if(not os.path.exists(f"{SourceDir}\\{IncF}")):
            raise Exception(f"{IncF} does not exist in {SourceDir}")
        else:
            with open(f"{SourceDir}\\{IncF}") as IncludedFile:
                IncludedFileLines = IncludedFile.readlines()
                for CurrentMacro in IncludedFileLines:
                    # Ensure that the macro begins with a letter (no numbers or symbols)
                    MacroMatch = re.search(r"#define ([A-Za-z][A-Za-z0-9_]+)[\s\t]+([0-9x#]+)", CurrentMacro)
                    if(MacroMatch is not None):
                        IncludedMacros[MacroMatch.groups()[0]] = MacroMatch.groups()[1]
    return IncludedMacros

def __IdentifyLabels(LineGroup: OLineGroup) -> dict[str, int]:

    LabelMap: dict[str, int] = {}

    CurrentMemLoc: int = LineGroup.Orig
    CurrentLabel: str
    LabelTmp: re.Match
    RgxTmp: re.Match

    for SplitLine in LineGroup.Lines:
        if(SplitLine.IsAnInstruction):
            CurrentMemLoc += 1
        else:
            # Identify a label
            pass



    return LabelMap

def Assemble(FileToCompile, FileToWrite):
    
    SourceDir: str = os.path.dirname(os.path.abspath(FileToCompile))

    # Read in data 
    with open(FileToCompile, "r") as F:
        Raw = F.readlines()
    
    # UneditedLines is an ordered list of all lines in FileToCompile
    UneditedLines: list[OLine] = []
    for i in range(len(Raw)):
        UneditedLines.append(OLine(Text=Raw[i], LineNumber=i+1))

    del i, F, Raw

    # Convert our raw text into a list of lines split into their arguments and with an associated line number
    FilteredSplitLines: list[OLineSplit]
    FilteredSplitLines = __FilterLinesAndSplitOnSpaces(UneditedLines)
    del UneditedLines

    # Separate the Filtered lines
    LineGroups: list[OLineGroup]
    IncludeFiles: list[str]
    LineGroups, IncludeFiles = __CreateLineGroups(FilteredSplitLines)
    del FilteredSplitLines

    # Assemble a dictionary of macros from IncludeFiles
    IncludedMacros: dict[str, str]
    IncludedMacros = __ParseHeaders(IncludeFiles, SourceDir)

    # Convert the list of instructions into a populated memory map (expands multi-cell label arrays (strings, blockwords) while keeping inst's single cell)

    MemoryMap: list[OSymbolicMemoryCell] = [OSymbolicMemoryCell()] * (2**NUM_CODE_ADDRESS_PINS)
    Offset: int

    for LineGroup in LineGroups:
        Offset = 0

        for SplitLine in LineGroup.Lines:
            MemoryMap[LineGroup.Orig + Offset].IsAnInstruction = SplitLine.IsAnInstruction
            MemoryMap[LineGroup.Orig + Offset].CodeLineNumber = SplitLine.LineNumber
            if(SplitLine.IsAnInstruction):
                MemoryMap[LineGroup.Orig + Offset].OLineSplit = SplitLine.WordList
                Offset += 1
            else:
                # Determine the label and whether it is a string, blkw, or code label
                # Need to idenfity code labels and ROM labels (eg. STRINGZ, BLKW)
                # Syntax of labels:
                #   Regular label
                #       ["label_name:"]
                #   BLKW
                #       ["label_name", ".BLKW", "hex/dec value"]
                #   STRINGZ
                #       ["label_name", ".STRINGZ", "<character_string>"]
                

                if(len(SplitLine.WordList) == 1):
                    # Code label
                    LabelTmp = re.match(r"^([A-Za-z_][A-Za-z0-9_]*):$", SplitLine.WordList[0])
                    if(LabelTmp is not None):
                        MemoryMap[LineGroup.Orig + Offset].CodeLabel = LabelTmp.groups()[0]
                        
                        Offset += 0
                    else:
                        raise Exception(f"Code label on line {SplitLine.LineNumber} does not match standard format")
                elif(len(SplitLine.WordList) == 3):
                    pass                
                    # Label with arguments
                    if(re.match(r"^.STRINGZ$", SplitLine.WordList[1], re.IGNORECASE) is not None):
                        RgxTmp = re.match(r"^\"(.*)\"$", SplitLine.WordList[2])
                        
                    elif(re.match(r"^.BLKW", SplitLine.WordList[1], re.IGNORECASE) is not None):
                        pass
                    else:
                        raise Exception(f"Label type {SplitLine.WordList[1]} does not match any defined types")
                else:
                    raise Exception(f"Incorrect number of arguments for label on line {SplitLine.LineNumber}")
                Offset += 1000


            
        

        pass
        


    return


class __FlagState(enum.Enum):
    SRC_FILE    = 0
    OUT_FILE    = 1

if __name__ == "__main__":
    cwd: str = os.getcwd()

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