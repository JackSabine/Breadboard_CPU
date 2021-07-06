from writer import Write
import re

class OLine:
    def __init__(self, Text, LineNumber):
        self.Text = Text
        self.LineNumber = LineNumber

class OLineSplit:
    def __init__(self, WordList, LineNumber):
        self.WordList = WordList
        self.LineNumber = LineNumber

def main():
    """
    if(len(sys.argv) < 2):
        raise Exception("Provide an input file to compile")
    
    FileToCompile = sys.argv[1]
    FileToWrite = sys.argv[2] if len(sys.argv) >= 3 else "a.bin"
    """
    FileToCompile = "OSR.asm"
    FileToWrite = "a.bin"

    Binary = bytearray(2 ** 15)

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

        for i in range(len(CleanedSplitLines)):
            for Line in CleanedSplitLines[i].WordList:
                if(Line.endswith(":")):
                    LabelMap[Line[:Line.find(":")]] = i - len(list(LabelMap.keys()))

        InstructionLineLists = list(filter(lambda Line: Line.WordList[0].endswith(":") is not True, CleanedSplitLines))
        # print(LabelMap)
        # print(InstructionLineLists)

    for ORIG_Offset in range(len(InstructionLineLists)):
        WordList = InstructionLineLists[ORIG_Offset].WordList
        WordLen = len(WordList)
        Operation = WordList[0]
        if(re.match(r"ADD",Operation,re.IGNORECASE)):
            if(WordLen < 3):
                raise Exception(f"Insufficient arguments provided for {Operation} on line {InstructionLineLists[ORIG_Offset].LineNumber}")
            else:
                pass
        elif(re.match(r"NOT",Operation,re.IGNORECASE)):
            if(WordLen < 2):
                raise Exception(f"Insufficient arguments provided for {Operation} on line {InstructionLineLists[ORIG_Offset].LineNumber}")
            else:
                pass
        elif(re.match(r"AND",Operation,re.IGNORECASE)):
            if(WordLen < 3):
                raise Exception(f"Insufficient arguments provided for {Operation} on line {InstructionLineLists[ORIG_Offset].LineNumber}")
            else:
                pass
        elif(re.match(r"NEG",Operation,re.IGNORECASE)):
            if(WordLen < 2):
                raise Exception(f"Insufficient arguments provided for {Operation} on line {InstructionLineLists[ORIG_Offset].LineNumber}")
            else:
                pass
        elif(re.match(r"CMP",Operation,re.IGNORECASE)):
            if(WordLen < 3):
                raise Exception(f"Insufficient arguments provided for {Operation} on line {InstructionLineLists[ORIG_Offset].LineNumber}")
            else:
                pass
        elif(re.match(r"LD",Operation,re.IGNORECASE)):
            if(WordLen < 3):
                raise Exception(f"Insufficient arguments provided for {Operation} on line {InstructionLineLists[ORIG_Offset].LineNumber}")
            else:
                pass
        elif(re.match(r"LDR",Operation,re.IGNORECASE)):
            if(WordLen < 4):
                raise Exception(f"Insufficient arguments provided for {Operation} on line {InstructionLineLists[ORIG_Offset].LineNumber}")
            else:
                pass
        elif(re.match(r"STR",Operation,re.IGNORECASE)):
            if(WordLen < 4):
                raise Exception(f"Insufficient arguments provided for {Operation} on line {InstructionLineLists[ORIG_Offset].LineNumber}")
            else:
                pass
        elif(re.match(r"HLT",Operation,re.IGNORECASE)):
            pass
        elif(re.match(r"CALL",Operation,re.IGNORECASE)):
            if(WordLen < 2):
                raise Exception(f"Insufficient arguments provided for {Operation} on line {InstructionLineLists[ORIG_Offset].LineNumber}")
            else:
                pass
        elif(re.match(r"RET",Operation,re.IGNORECASE)):
            pass
        elif(re.match(r"TRAP",Operation,re.IGNORECASE)):
            if(WordLen < 2):
                raise Exception(f"Insufficient arguments provided for {Operation} on line {InstructionLineLists[ORIG_Offset].LineNumber}")
            else:
                pass
        elif(re.match(r"SETBK",Operation,re.IGNORECASE)):
            if(WordLen < 2):
                raise Exception(f"Insufficient arguments provided for {Operation} on line {InstructionLineLists[ORIG_Offset].LineNumber}")
            else:
                pass
        elif(re.match(r"START",Operation,re.IGNORECASE)):
            if(WordLen < 2):
                raise Exception(f"Insufficient arguments provided for {Operation} on line {InstructionLineLists[ORIG_Offset].LineNumber}")
            else:
                pass
        elif(re.match(r"SETSP",Operation,re.IGNORECASE)):
            if(WordLen < 2):
                raise Exception(f"Insufficient arguments provided for {Operation} on line {InstructionLineLists[ORIG_Offset].LineNumber}")
            else:
                pass
        elif(re.match(r"PUSH",Operation,re.IGNORECASE)):
            if(WordLen < 2):
                raise Exception(f"Insufficient arguments provided for {Operation} on line {InstructionLineLists[ORIG_Offset].LineNumber}")
            else:
                pass
        elif(re.match(r"POP",Operation,re.IGNORECASE)):
            if(WordLen < 2):
                raise Exception(f"Insufficient arguments provided for {Operation} on line {InstructionLineLists[ORIG_Offset].LineNumber}")
            else:
                pass
        elif(re.match(r"OR",Operation,re.IGNORECASE)):
            if(WordLen < 3):
                raise Exception(f"Insufficient arguments provided for {Operation} on line {InstructionLineLists[ORIG_Offset].LineNumber}")
            else:
                pass
        elif(re.match(r"CPYSP",Operation,re.IGNORECASE)):
            if(WordLen < 2):
                raise Exception(f"Insufficient arguments provided for {Operation} on line {InstructionLineLists[ORIG_Offset].LineNumber}")
            else:
                pass
        elif(re.match(r"JMP",Operation,re.IGNORECASE)):
            if(WordLen < 2):
                raise Exception(f"Insufficient arguments provided for {Operation} on line {InstructionLineLists[ORIG_Offset].LineNumber}")
            else:
                pass
        elif(re.match(r"JO",Operation,re.IGNORECASE)):
            if(WordLen < 2):
                raise Exception(f"Insufficient arguments provided for {Operation} on line {InstructionLineLists[ORIG_Offset].LineNumber}")
            else:
                pass
        elif(re.match(r"JNO",Operation,re.IGNORECASE)):
            if(WordLen < 2):
                raise Exception(f"Insufficient arguments provided for {Operation} on line {InstructionLineLists[ORIG_Offset].LineNumber}")
            else:
                pass
        elif(re.match(r"JZ",Operation,re.IGNORECASE)):
            if(WordLen < 2):
                raise Exception(f"Insufficient arguments provided for {Operation} on line {InstructionLineLists[ORIG_Offset].LineNumber}")
            else:
                pass
        elif(re.match(r"JNZ",Operation,re.IGNORECASE)):
            if(WordLen < 2):
                raise Exception(f"Insufficient arguments provided for {Operation} on line {InstructionLineLists[ORIG_Offset].LineNumber}")
            else:
                pass
        elif(re.match(r"JS",Operation,re.IGNORECASE)):
            if(WordLen < 2):
                raise Exception(f"Insufficient arguments provided for {Operation} on line {InstructionLineLists[ORIG_Offset].LineNumber}")
            else:
                pass
        elif(re.match(r"JNS",Operation,re.IGNORECASE)):
            if(WordLen < 2):
                raise Exception(f"Insufficient arguments provided for {Operation} on line {InstructionLineLists[ORIG_Offset].LineNumber}")
            else:
                pass
        elif(re.match(r"JC",Operation,re.IGNORECASE)):
            if(WordLen < 2):
                raise Exception(f"Insufficient arguments provided for {Operation} on line {InstructionLineLists[ORIG_Offset].LineNumber}")
            else:
                pass
        elif(re.match(r"JNC",Operation,re.IGNORECASE)):
            if(WordLen < 2):
                raise Exception(f"Insufficient arguments provided for {Operation} on line {InstructionLineLists[ORIG_Offset].LineNumber}")
            else:
                pass
        else:
            print(f"Unrecognized operation {Operation} on line {InstructionLineLists[ORIG_Offset].LineNumber}")

    Write(Binary, FileToWrite)

    return

if __name__ == "__main__":
    main()