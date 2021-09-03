import sys, os, enum, re
from writer import Write
from ISA.v1_1.ashelp import *

def Assemble(FileToCompile, FileToWrite):

    Binary = bytearray(2 ** 15)

    ### CONVERT TEXT .ASM FILE INTO A LIST OF COMMAND ARG LIST AND LINE NUMBER PAIRS ###
    with open(FileToCompile, 'r') as F:
        Raw = F.readlines()
        Indexed: list[OLine] = []

        # Create a list that contains every line in the passed file and its line number (hold onto line number in case we need to throw errors about a particular line)
        for Ind in range(len(Raw)):
            Indexed.append(OLine(Raw[Ind], Ind+1))

        # Remove any lines that start with a comment or have no contents (newline only)
        # We can't outright delete them from Indexed because we are iterating through indexed (could use filter but the lambda would become large)
        Lines: list[OLine] = []
        for Line in Indexed:
            if(Line.Text != '\n' and not Line.Text.startswith(';')):
                Tmp = Line.Text.replace('\n', '').replace(',', ' ')
                if Tmp.find(";") != -1:
                    Lines.append(OLine(Tmp[:Tmp.find(';')], Line.LineNumber))
                else:
                    Lines.append(OLine(Tmp, Line.LineNumber))

        # Split each line across whitespace into a list of operations/operands
        SplitLines: list[OLineSplit] = []
        for Line in Lines:
            SplitLines.append(OLineSplit(Line.Text.split(), Line.LineNumber))

        # Filter out any empty lines
        CleanedSplitLines = [OStrList for OStrList in SplitLines if OStrList.WordList != []]

        # Prepare to generate a label map based on the lines INDEX (not the line number!)
        LabelMap: dict[str, int] = {}

        # Need to iterate through all cleaned split lines and generate different groups of lines to assemble and a label directory/map

        # Desired output:
        #
        # List of OLineGroup
        # Label map

        LineGroups: list[OLineGroup] = []
        CurrentLineGroup: OLineGroup = None
        CurrentLineGroupIdx: int = 0
        
        for CSL_Index in range(len(CleanedSplitLines)):
            # Check for assembler directives
            DirectiveMatch      = re.search(r"\.([A-Za-z]+)",    CleanedSplitLines[CSL_Index].WordList[0])
            LabelMatch          = re.search(r"([A-Za-z_0-9]+):",   CleanedSplitLines[CSL_Index].WordList[0])
            InstructionMatch    = re.search(r"([A-Za-z]+)",     CleanedSplitLines[CSL_Index].WordList[0])

            if(DirectiveMatch is not None):
                # Is an assembler directive
                if(re.search(r"^ORIG$", DirectiveMatch.groups()[0], re.IGNORECASE) is not None):
                    if(len(CleanedSplitLines[CSL_Index].WordList) != 2):
                        raise Exception(f"Incorrect number of arguments on line {CleanedSplitLines[CSL_Index].LineNumber}")
                    HexMatch = re.search(r"^(?:0x)?(?:x)?([0-9A-F]{4})$", CleanedSplitLines[CSL_Index].WordList[1], re.IGNORECASE)
                    if HexMatch is not None:
                        if(CurrentLineGroup is not None):
                            LineGroups.append(CurrentLineGroup)
                            CurrentLineGroupIdx = 0
                        CurrentLineGroup = OLineGroup(int(HexMatch.groups()[0], base=16), [])
                    else:
                        raise Exception(f"Expected hex address on line {CleanedSplitLines[CSL_Index].LineNumber} in formax 0xhhhh, xhhhh, or hhhh")
                else:                 
                    raise Exception(f"Unterminated assembler directive on line {CleanedSplitLines[CSL_Index].LineNumber}")
            
            elif(LabelMatch is not None):           # Not a directive; could it be a label?
                if(CurrentLineGroup is not None):
                    LabelMap[LabelMatch.groups()[0]] = CurrentLineGroup.Orig + CurrentLineGroupIdx
                else:
                    raise Exception(f"Line {CleanedSplitLines[CSL_Index].LineNumber} must be under a .ORIG statement")

            elif(InstructionMatch is not None):     # Not a directive nor a label; could it be an instruction?
                if(CurrentLineGroup is not None):
                    CurrentLineGroup.Lines.append(CleanedSplitLines[CSL_Index])
                    CurrentLineGroupIdx += 1
                else:
                    raise Exception(f"Line {CleanedSplitLines[CSL_Index].LineNumber} must be under a .ORIG statement")
            else:
                raise Exception("What do it be then???")

        # Append the last line group
        if(CurrentLineGroup is not None):
            LineGroups.append(CurrentLineGroup)        
        
        
        # print(LabelMap)


    ### GENERATE ARRAY OF 16b INSTRUCTIONS ###
    for LineGroup in LineGroups:
        CurOrig: int = LineGroup.Orig
        InstructionLineLists: list[OLineSplit] = LineGroup.Lines

        for OrigOffset in range(len(InstructionLineLists)):
            Operation: str = InstructionLineLists[OrigOffset].WordList[0]
            WordList: list[str] = InstructionLineLists[OrigOffset].WordList[1:]
            LineNumber: int = InstructionLineLists[OrigOffset].LineNumber

            Arguments: OLineSplit = OLineSplit(WordList, LineNumber)

            Instruction = 0x0000
            InstructionOp = 0x0000
            InstructionArgs = 0x0000

            if(OPCODE_MAP.get(Operation.upper()) is not None):
                InstructionOp |= OPCODE_MAP.get(Operation.upper()) << INSTRUCTION_POS
            else:
                raise Exception(f"Unrecognized instruction {Operation} on line {LineNumber}")

            Op = Operation.upper()

            InstructionArgs = CreateBitArgs(Operation, Arguments, LabelMap)

            Instruction = InstructionOp | InstructionArgs
            

            # Little endian arrangement in code EEPROM
            Binary[2*CurOrig+2*OrigOffset + 0] = Instruction & 0x00FF
            Binary[2*CurOrig+2*OrigOffset + 1] = (Instruction & 0xFF00) >> 8

    Write(Binary, FileToWrite)

    return

class __FlagState(enum.Enum):
    SRC_FILE     = 0
    OUT_FILE     = 1

if __name__ == "__main__":
    cwd = os.getcwd()

    InFile  = None
    OutFile = None
    StateV  = None

    # InFile = "./Programs/OSR.asm"
    # OutFile = "./Utils/Testing.bin"

    if(len(sys.argv) < 2):
        raise Exception("Not enough input arguments")

    for arg in sys.argv[1:]:
        if(re.search(r"-c", arg, re.IGNORECASE)):
            StateV = __FlagState.SRC_FILE
        elif(re.search(r"-o", arg, re.IGNORECASE)):
            StateV = __FlagState.OUT_FILE
        else:
            if(StateV == __FlagState.SRC_FILE):
                InFile = arg
            elif(StateV == __FlagState.OUT_FILE):
                OutFile = arg   

    if(OutFile is None):
        OutFile = rf"{cwd}/a.bin"

    if(InFile is None):
        raise Exception("Specify an input file with -c <file>")

    Assemble(FileToCompile=InFile, FileToWrite=OutFile)