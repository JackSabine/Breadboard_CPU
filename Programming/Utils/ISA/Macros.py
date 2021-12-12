ROM_WIDTH = 8
ROM_GRP1  = ROM_WIDTH*1
ROM_GRP2  = ROM_WIDTH*2
ROM_GRP3  = ROM_WIDTH*3
ROM_GRP4  = ROM_WIDTH*4
ROM_GRP5  = ROM_WIDTH*5

ROM_POS0  = 0
ROM_POS1  = 1
ROM_POS2  = 2
ROM_POS3  = 3
ROM_POS4  = 4
ROM_POS5  = 5
ROM_POS6  = 6
ROM_POS7  = 7

AAC	    =   1   <<      (ROM_GRP2 + ROM_POS4)
ACO	    =   1   <<      (ROM_GRP4 + ROM_POS0)
ACU	    =   1   <<      (ROM_GRP2 + ROM_POS7)
AIB	    =   1   <<      (ROM_GRP4 + ROM_POS2)
ARI	    =   1   <<      (ROM_GRP4 + ROM_POS1)
ARO	    =   1   <<      (ROM_GRP4 + ROM_POS7)
ASI	    =   1   <<      (ROM_GRP2 + ROM_POS5)
ASO	    =   1   <<      (ROM_GRP4 + ROM_POS4)
ASX	    =   1   <<      (ROM_GRP4 + ROM_POS3)
AUA	    =   1   <<      (ROM_GRP4 + ROM_POS6)
AUN	    =   1   <<      (ROM_GRP4 + ROM_POS5)
CCU	    =   1   <<      (ROM_GRP2 + ROM_POS6)
CSU     =   1   <<      (ROM_GRP1 + ROM_POS0)
GAO	    =   1   <<      (ROM_GRP3 + ROM_POS1)
GBO	    =   1   <<      (ROM_GRP3 + ROM_POS0)
HT	    =   1   <<      (ROM_GRP5 + ROM_POS5)
IHI	    =   1   <<      (ROM_GRP1 + ROM_POS2)
ILI	    =   1   <<      (ROM_GRP1 + ROM_POS1)
MAHI	=   1   <<      (ROM_GRP1 + ROM_POS4)
MALI	=   1   <<      (ROM_GRP1 + ROM_POS3)
MI	    =   1   <<      (ROM_GRP1 + ROM_POS5)
MO	    =   1   <<      (ROM_GRP1 + ROM_POS7)
MRH	    =   1   <<      (ROM_GRP1 + ROM_POS6)
NI	    =   1   <<      (ROM_GRP2 + ROM_POS0)
PHI	    =   1   <<      (ROM_GRP3 + ROM_POS4)
PHO	    =   1   <<      (ROM_GRP3 + ROM_POS7)
PI	    =   1   <<      (ROM_GRP3 + ROM_POS5)
PLI	    =   1   <<      (ROM_GRP3 + ROM_POS3)
PLO	    =   1   <<      (ROM_GRP3 + ROM_POS6)
RAS	    =   1   <<      (ROM_GRP5 + ROM_POS2)
RBS	    =   1   <<      (ROM_GRP5 + ROM_POS1)
RI	    =   1   <<      (ROM_GRP2 + ROM_POS3)
RO	    =   1   <<      (ROM_GRP5 + ROM_POS7)
RSH	    =   1   <<      (ROM_GRP5 + ROM_POS6)
SD	    =   1   <<      (ROM_GRP3 + ROM_POS2)
SHI	    =   1   <<      (ROM_GRP2 + ROM_POS2)
SHO	    =   1   <<      (ROM_GRP5 + ROM_POS4)
SI	    =   1   <<      (ROM_GRP5 + ROM_POS0)
SLI	    =   1   <<      (ROM_GRP2 + ROM_POS1)
SLO	    =   1   <<      (ROM_GRP5 + ROM_POS3)

NOINST  =   0

NUM_UINST_BITS          =   4
NUM_CONDFL_BITS         =   1
NUM_OPC_BITS            =   5
NUM_CS_BITS             =   3
NUM_UCODE_ADDRESS_PINS  =   NUM_UINST_BITS+NUM_CONDFL_BITS+NUM_OPC_BITS+NUM_CS_BITS
POS_CS                  =   0+NUM_UINST_BITS+NUM_CONDFL_BITS+NUM_OPC_BITS
POS_OPC                 =   0+NUM_UINST_BITS+NUM_CONDFL_BITS
POS_CONDFL              =   0+NUM_UINST_BITS
POS_UINST               =   0
INVERTING_MASK          =   GAO|GBO|MO|NI|PHI|PHO|PLI|PLO|RAS|RBS|RI|RO|SHO|SLO

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

class OSymbolicMemoryMap:

    def __init__(self, MemorySize):
        self.MemoryBlock: list[OSymbolicMemoryCell] = [OSymbolicMemoryCell()] * MemorySize
        self.__MemorySize = MemorySize
        self.SymbolTable: dict[str, int] = {}
        return

    def __PlaceLabel(self, MemoryIndex: int, Label: str, LineNumber: int) -> None:
        if(self.SymbolTable.get(Label) is not None): 
            raise Exception(f"Redefinition of label {Label} on line {LineNumber}")

        self.SymbolTable[Label] = MemoryIndex

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

INSTRUCTION_POS = 11
NUM_JUMP_BITS = INSTRUCTION_POS
NUM_BASER_OFFSET_BITS = 5
NUM_IMM_BITS = 8

REGA_POS = 8
REGB_POS = 5
IMM_POS = 0

NUM_CODE_ADDRESS_PINS = 15

if __name__ == "__main__":
    x = OSymbolicMemoryMap(2048)

    print("Hello")