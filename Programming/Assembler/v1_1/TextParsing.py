import os, sys
path: str = os.path.dirname(__file__)
while(not path.endswith("Assembler")):
    path = os.path.dirname(path)
sys.path.append(os.path.dirname(path))

import re
from Assembler.v1_1.classes import OLine, OLineSplit, OLineGroup, OSymbolicMemoryMap
import Assembler.v1_1.Utils as Utils

def CreateOLineList(LineText: list[str]) -> list[OLine]:
    OLineList: list[OLine] = []

    for i, LineText in enumerate(LineText):
        OLineList.append(OLine(Text=LineText, LineNumber=i+1))

    return (OLineList)

def FilterLinesAndSplitOnSpaces(UneditedLines: list[OLine]):
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


def ParseAssemblerDirectives(FilteredSplitLines: list[OLineSplit]) -> tuple[list[OLineGroup], list[str]]:
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

                CurrentORIG = Utils.DecOrHexSearch(FSLine.WordList[1])

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

def ParseHeaders(IncludeFiles: list[str], SourceDir: str) -> dict[str, str]:
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