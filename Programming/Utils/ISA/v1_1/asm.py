import os, sys
path: str = os.path.dirname(__file__)
while(not path.endswith("ISA")):
    path = os.path.dirname(path)
sys.path.append(os.path.dirname(path))

import enum, re
from writer import Write
from ISA.v1_1.ucode.ashelp import *
from ISA.v1_1.ucode.macros import *

def __DecOrHexSearch(str) -> int:
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


def __ParseAssemblerDirectives(FilteredSplitLines: list[OLineSplit]) -> tuple[list[OLineGroup], list[str]]:
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


def __PopulateMemoryMap(MemoryMap: OSymbolicMemoryMap, LineGroup: OLineGroup) -> None:
        # Parse the label and its (potential) associated data 

    # Syntax of labels:
    #   Code label  -> do not increment offset (no code space dedicated to code labels)
    #       ["label_name:"]
    #   > r"^([A-Za-z_][A-Za-z0-9_]*):$"
    #
    #   BLKW        -> increment offset by hex/dec value
    #       ["label_name:", ".BLKW", "hex/dec value"]
    #   > r"^.BLKW"
    #
    #   STRINGZ     -> increment offset by length of <character_string> plus 1 for null terminator
    #       ["label_name:", ".STRINGZ", "<character_string>"]
    #   > r"^.STRINGZ$"
    #   > r"^\"(.*)\"$"
  
    MemoryIndex: int
    CurCodeLabel: str
    CurBlockLabel: str
    WordListLen: int
    RegexLabelTemp: re.Match
    RegexStringTemp: re.Match
    BlockwordTemp: int


    MemoryIndex = LineGroup.Orig

    for LineSplit in LineGroup.Lines:
        if(LineSplit.IsAnInstruction):
            MemoryIndex = MemoryMap.PlaceInstruction(
                MemoryIndex=MemoryIndex,
                WordList=LineSplit.WordList,
                LineNumber=LineSplit.LineNumber,
                Label=CurCodeLabel
            )
            CurCodeLabel = None     # Clear the current label so it's only paired with one code line

        else:
            # Determine what kind of label it is
            WordListLen = len(LineSplit.WordList)
            RegexLabelTemp = re.search(r"^([A-Za-z_][A-Za-z0-9_]*):$", LineSplit.WordList[0])

            if(RegexLabelTemp is None):
                raise Exception(f"Label on line {LineSplit.LineNumber} is not of the expected format")

            if(WordListLen == 1):
                # Code label
                CurCodeLabel = RegexLabelTemp.groups()[0]
            elif(WordListLen == 3):
                CurBlockLabel = RegexLabelTemp.groups()[0]


                if(re.search(r"^.BLKW", LineSplit.WordList[1]) is not None):
                    BlockwordTemp = __DecOrHexSearch(LineSplit.WordList[2])
                    if(BlockwordTemp is int):
                        MemoryIndex = MemoryMap.GenerateBlock(
                            MemoryIndex=MemoryIndex,
                            BlockSize=BlockwordTemp,
                            LineNumber=LineSplit.LineNumber,
                            Label=CurBlockLabel
                        )
                    else:
                        raise Exception(f"Blockword length for label {CurBlockLabel} on line {LineSplit.LineNumber} cannot be determined")
                elif(re.search(r"^.STRINGZ$", LineSplit.WordList[1]) is not None):
                    RegexStringTemp = re.search(r"^\"(.*)\"$", LineSplit.WordList[2])
                    if(RegexStringTemp is not None):
                        MemoryIndex = MemoryMap.GenerateString(
                            MemoryIndex=MemoryIndex,
                            String=RegexStringTemp.groups()[0],
                            LineNumber=LineSplit.LineNumber,
                            Label=CurBlockLabel
                        )

    return


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
    LineGroups, IncludeFiles = __ParseAssemblerDirectives(FilteredSplitLines)
    del FilteredSplitLines

    # Assemble a dictionary of macros from IncludeFiles
    IncludedMacros: dict[str, str]
    IncludedMacros = __ParseHeaders(IncludeFiles, SourceDir)
    del IncludeFiles

    MemoryMap: OSymbolicMemoryMap = OSymbolicMemoryMap(2**NUM_CODE_ADDRESS_PINS)

    for LineGroup in LineGroups:
        __PopulateMemoryMap(MemoryMap, LineGroup)
        
    # MemoryMap.ToFile("Test.txt")

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