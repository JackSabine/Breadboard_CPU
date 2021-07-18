import sys
from writer import Write
from OpMaker import *
from AssemblerClasses import *
import re

def Assemble(FileToCompile, FileToWrite):

    Binary = bytearray(2 ** 15)
    ORIG = 0x0000

    ### CONVERT TEXT .ASM FILE INTO A LIST OF COMMAND ARG LIST AND LINE NUMBER PAIRS ###
    with open(FileToCompile, 'r') as F:
        Raw = F.readlines()
        Indexed = []
        for Ind in range(len(Raw)):
            Indexed.append(OLine(Raw[Ind], Ind+1))
        # print(Raw)
        Lines = []
        for Line in Indexed:
            # Remove any lines that start with a comment or have no contents (newline only)
            if(Line.Text != '\n' and not Line.Text.startswith(';')):
                Tmp = Line.Text.replace('\n', '').replace(',', ' ')
                if Tmp.find(";") != -1:
                    Lines.append(OLine(Tmp[:Tmp.find(';')], Line.LineNumber))
                else:
                    Lines.append(OLine(Tmp, Line.LineNumber))

        # print(Lines)
        SplitLines = []
        for Line in Lines:
            SplitLines.append(OLineSplit(Line.Text.split(), Line.LineNumber))

        CleanedSplitLines = [OStrList for OStrList in SplitLines if OStrList.WordList != []]
        LabelMap = {}

        
        # print(CleanedSplitLines)

        for i in range((len(CleanedSplitLines))):
            if(CleanedSplitLines[i].WordList[0].startswith(".")):
                # Assembler directive
                CmdMatch = re.search(r".([A-Za-z]+)", CleanedSplitLines[i].WordList[0])
                if(CmdMatch is not None):
                    Directive = CmdMatch.groups()[0]
                    if(re.search(r"^ORIG$", Directive, re.IGNORECASE) is not None):
                        if(len(CleanedSplitLines[i].WordList) != 2):
                            raise Exception(f"Incorrect number of arguments on line {CleanedSplitLines[i].LineNumber}")
                        MatchA = re.search(r"^(?:0x)?(?:x)?([0-9A-F]{4})$", CleanedSplitLines[i].WordList[1])
                        if(MatchA is not None):
                            ORIG = int(MatchA.groups()[0], base=16)
                        else:
                            raise Exception(f"Expected hex address on line {CleanedSplitLines[i].LineNumber} in formax 0xhhhh, xhhhh, or hhhh")

                    else:
                        raise Exception(f"Unrecognized assembler directive on line {CleanedSplitLines[i].LineNumber}")
                else:
                    raise Exception(f"Unterminated assembler directive on line {CleanedSplitLines[i].LineNumber}")

        for i in range(len(CleanedSplitLines)):
            for Line in CleanedSplitLines[i].WordList:
                if(Line.endswith(":")):
                    LabelMap[Line[:Line.find(":")]] = i - len(list(LabelMap.keys())) - 1

        InstructionLineLists = list(filter(lambda Line: ( Line.WordList[0].endswith(":") or Line.WordList[0].startswith(".") )is not True, CleanedSplitLines))
        # print(LabelMap)


    ### GENERATE ARRAY OF HALF-WORD OPERATIONS ###
    for ORIG_Offset in range(len(InstructionLineLists)):
        Operation = InstructionLineLists[ORIG_Offset].WordList[0]
        Instruction = 0x0000

        if(OPCODE_MAP.get(Operation.upper()) is not None):
            Instruction |= OPCODE_MAP.get(Operation.upper()) << INSTRUCTION_POS
        else:
            raise Exception(f"Unrecognized instruction {Operation} on line {InstructionLineLists[ORIG_Offset].LineNumber}")

        Op = Operation.upper()

        if(Op in AMBIG):
            Instruction |= Ambig(OLineSplit(WordList=InstructionLineLists[ORIG_Offset].WordList[1:], LineNumber=InstructionLineLists[ORIG_Offset].LineNumber))
            # print(hex(Instruction))
        elif(Op in SINGR):
            Instruction |= SingR(OLineSplit(WordList=InstructionLineLists[ORIG_Offset].WordList[1:], LineNumber=InstructionLineLists[ORIG_Offset].LineNumber))
            # print(hex(Instruction))
            # print(InstructionLineLists[ORIG_Offset].LineNumber)
        elif(Op in JUMPS):
            Instruction |= Jumps(OLineSplit(WordList=InstructionLineLists[ORIG_Offset].WordList[1:], LineNumber=InstructionLineLists[ORIG_Offset].LineNumber), LabelMap, ORIG_Offset)
            # print(hex(Instruction))
            # print(InstructionLineLists[ORIG_Offset].LineNumber)
        elif(Op in NOARG):
            Instruction |= NoArg()
            # print(hex(Instruction))
            # print(InstructionLineLists[ORIG_Offset].LineNumber)
        elif(Op in BASER):
            Instruction |= BaseR(OLineSplit(WordList=InstructionLineLists[ORIG_Offset].WordList[1:], LineNumber=InstructionLineLists[ORIG_Offset].LineNumber))
            # print(hex(Instruction))
            # print(InstructionLineLists[ORIG_Offset].LineNumber)
        elif(Op in OTHER):
            Instruction |= Other(OLineSplit(WordList=InstructionLineLists[ORIG_Offset].WordList[:], LineNumber=InstructionLineLists[ORIG_Offset].LineNumber))
            # print(hex(Instruction))
            # print(InstructionLineLists[ORIG_Offset].LineNumber)
        else:
            raise Exception(f"Operation {Operation} recognized in opmap but does not appear in any instruction collections")

        # Little endian
        Binary[2*ORIG+2*ORIG_Offset + 0] = Instruction & 0x00FF
        Binary[2*ORIG+2*ORIG_Offset + 1] = (Instruction & 0xFF00) >> 8

    Write(Binary, FileToWrite)

    return

if __name__ == "__main__":
    # if(len(sys.argv) < 2):
    #     raise Exception("Not enough input arguments")

    InFile = "./Fibonacci.asm"
    OutFile = "./Fib.bin"

    

    # if(len(sys.argv) == 2):
    #     FilePrefix = re.search(r"^([A-z0-9]+)(?:.asm)$", sys.argv[1])
    #     if FilePrefix is not None:
    #         InFile = f"{sys.argv[1]}"
    #         OutFile = f"{FilePrefix}.bin"
    #     else:
    #         InFile = sys.argv[1]
    #         OutFile = "a.bin"
    # else:
    #     InFile = sys.argv[1]
    #     OutFile = sys.argv[2]

    Assemble(FileToCompile=InFile, FileToWrite=OutFile)