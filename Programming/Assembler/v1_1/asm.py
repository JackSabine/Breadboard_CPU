import os, sys
path: str = os.path.dirname(__file__)
while(not path.endswith("Assembler")):
    path = os.path.dirname(path)
sys.path.append(os.path.dirname(path))

import enum, re
from Assembler.v1_1.inst_assembler import InterpretInstructions
from Assembler.v1_1.classes import OLine, OLineSplit, OLineGroup, OSymbolicMemoryMap
from Assembler.v1_1.ucode.macros import NUM_CODE_ADDRESS_PINS, INSTRUCTION_POS
from Assembler.v1_1.inst_decoder import DecodeBinary
import Assembler.v1_1.TextParsing as Parsing
import Assembler.v1_1.Utils as Utils

def __MacroSubstitution(LineGroups: list[OLineGroup], MacroDict: dict[str, str]) -> None:
    for LineGroup in LineGroups:
        for LineSplit in LineGroup.Lines:
            for i, Argument in enumerate(LineSplit.WordList):
                if(Argument in MacroDict):
                    LineSplit.WordList[i] = Argument.replace(Argument, MacroDict[Argument])

def __PopulateMemoryMap(MemoryMap: OSymbolicMemoryMap, LineGroups: list[OLineGroup]) -> None:
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

    for LineGroup in LineGroups:
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
                        BlockwordTemp = Utils.DecOrHexSearch(LineSplit.WordList[2])
                        if(type(BlockwordTemp) is int):
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



def Assemble(FileToCompile, FileToWrite, Debug=False):
    
    SourceDir: str
    Raw: list[str]
    UneditedLines: list[OLine]
    FilteredSplitLines: list[OLineSplit]
    IncludeFiles: list[str]
    IncludedMacros: dict[str, str]
    LineGroups: list[OLineGroup]
    MemoryMap: OSymbolicMemoryMap
    ProgramMemory: bytearray
    
    SourceDir = os.path.dirname(os.path.abspath(FileToCompile))

    # Read in data 
    
    with open(FileToCompile, "r") as FileToCompile_Handle:
        Raw = FileToCompile_Handle.readlines()
    
    # UneditedLines is an list of all lines in FileToCompile
    UneditedLines = Parsing.CreateOLineList(Raw)

    # Convert our raw text into a list of lines split into their arguments and with an associated line number
    FilteredSplitLines = Parsing.FilterLinesAndSplitOnSpaces(UneditedLines)

    # Separate the Filtered lines
    LineGroups, IncludeFiles = Parsing.ParseAssemblerDirectives(FilteredSplitLines)

    # Assemble a dictionary of macros from IncludeFiles
    IncludedMacros = Parsing.ParseHeaders(IncludeFiles, SourceDir)

    if(Debug):
        MemoryMap_BeforeMacros: OSymbolicMemoryMap = OSymbolicMemoryMap(2**(NUM_CODE_ADDRESS_PINS-1))
        __PopulateMemoryMap(MemoryMap_BeforeMacros, LineGroups)   # Pass MemoryMap by reference
        MemoryMap_BeforeMacros.ToFile(f"./Assembler/v1_1/Testing__PreMacro.txt")

    # Perform macro substitution
    __MacroSubstitution(LineGroups, IncludedMacros)

    MemoryMap = OSymbolicMemoryMap(2**(NUM_CODE_ADDRESS_PINS-1))    # One instruction is two memory locations
    __PopulateMemoryMap(MemoryMap, LineGroups)   # Pass MemoryMap by reference
    if(Debug):
        MemoryMap.ToFile(f"./Assembler/v1_1/Testing__PostMacro.txt")

    ProgramMemory = bytearray(2**NUM_CODE_ADDRESS_PINS)

    InterpretInstructions(MemoryMap, ProgramMemory)
        
    Utils.Write(ProgramMemory, FileToWrite)

    DecodeBinary("./Assembler/v1_1/Testing.bin", "./Assembler/v1_1/Decoded.txt")

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
    OutFile = "./Assembler/v1_1/Testing.bin"

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

    Assemble(FileToCompile=InFile, FileToWrite=OutFile, Debug=True)