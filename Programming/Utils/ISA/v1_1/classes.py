import math, copy

class OLine:
    def __init__(self, Text: str, LineNumber: int):
        self.Text: str = Text
        self.LineNumber: int = LineNumber

        return

class OLineSplit:
    def __init__(self, WordList: list[str], LineNumber: int, IsAnInstruction: bool):
        self.WordList: list[str] = WordList
        self.LineNumber: int = LineNumber
        self.IsAnInstruction: bool = IsAnInstruction
        
        return

class OLineGroup:
    def __init__(self, Origin: int, Lines: list[OLineSplit]):
        self.Orig: int = Origin
        self.Lines: list[OLineSplit] = Lines

        return

class OSymbolicMemoryCell:
    def __init__(self):
        self.__IsAnInstruction: bool = False
        self.__WordList: list[str] = []
        self.__ImmediateData: int = 0x0000
        return
    
    def CreateInstruction(self, WordList: list[str]) -> None:
        self.__WordList = WordList
        self.__IsAnInstruction = True
        return
    
    def CreateImmediate(self, ImmediateData: int) -> None:
        self.__ImmediateData = ImmediateData
        self.__IsAnInstruction = False
        return

    def GetWordList(self) -> list[str]:
        return copy.deepcopy(self.__WordList)

    def IsCellAnInstruction(self) -> bool:
        return self.__IsAnInstruction

    def GetCellValue(self) -> int:
        return self.__ImmediateData

    def GetFormattedCellChar(self) -> str:
        if(self.__ImmediateData == 0):
            return "NULL"
        else:
            return f"'{chr(self.__ImmediateData)}'"

class OSymbolicMemoryMap:

    def __init__(self, MemorySize):
        self.MemoryBlock: list[OSymbolicMemoryCell] = [OSymbolicMemoryCell() for i in range(MemorySize)]
        # Can't use ```[OSymbolicMemoryCell()] * MemorySize``` or will be all the same object

        self.__MemorySize = MemorySize
        self.SymbolTable: dict[str, int] = {}
        self.__SymbolLookup: dict[int, str] = {}
        return

    def ToFile(self, FileName) -> None:
        f = open(FileName, "w")
        
        # Determine the longest label
        Label_MaxLen: int = 0
        Label_CurLen: int
        for Label in self.SymbolTable.keys():
            Label_CurLen = len(Label)
            if(Label_CurLen > Label_MaxLen):
                Label_MaxLen = Label_CurLen

        

        # Determine number of hex digits
        NumHexDigits: int = 1 + math.floor(math.log(self.__MemorySize) / math.log(16))

        CurLineStr: str

        for i in range(self.__MemorySize):
            CurLineStr = "{}\t: 0x{:0{}X} : {}\n".format(
                str.ljust(self.__SymbolLookup[i], Label_MaxLen) if self.__SymbolLookup.get(i) is not None else str.ljust("", Label_MaxLen),
                i,
                NumHexDigits,
                "\t".join(self.MemoryBlock[i].GetWordList()) if self.MemoryBlock[i].IsCellAnInstruction() is True else self.MemoryBlock[i].GetFormattedCellChar()
            )

            f.write(CurLineStr)

        f.close()

        return

    def __PlaceLabel(self, MemoryIndex: int, Label: str, LineNumber: int) -> None:
        if(self.SymbolTable.get(Label) is not None): 
            raise Exception(f"Redefinition of label {Label} on line {LineNumber}")

        self.SymbolTable[Label] = MemoryIndex
        self.__SymbolLookup[MemoryIndex] = Label

        return None

    def PlaceInstruction(self, MemoryIndex: int, WordList: list[str], LineNumber: int, Label: str = None) -> int:
        if(Label is not None):
            self.__PlaceLabel(MemoryIndex, Label, LineNumber)

        self.MemoryBlock[MemoryIndex].CreateInstruction(WordList)

        return (MemoryIndex + 1)

    def GenerateBlock(self, MemoryIndex: int, BlockSize: int, LineNumber: int, Label: str) -> int:
        IndexOffset: int

        self.__PlaceLabel(MemoryIndex, Label, LineNumber)

        for IndexOffset in range(BlockSize):
            self.MemoryBlock[MemoryIndex + IndexOffset].CreateImmediate(0)

        return (MemoryIndex + IndexOffset)

    def GenerateString(self, MemoryIndex: int, String: str, LineNumber: int, Label: str) -> int:
        IndexOffset: int = 0

        self.__PlaceLabel(MemoryIndex, Label, LineNumber)

        for Char in String:
            self.MemoryBlock[MemoryIndex + IndexOffset].CreateImmediate(ord(Char))
            IndexOffset += 1
        
        self.MemoryBlock[MemoryIndex + IndexOffset].CreateImmediate(0)
        IndexOffset += 1

        return (MemoryIndex + IndexOffset)