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

INSTRUCTION_POS = 11
NUM_JUMP_BITS = INSTRUCTION_POS
NUM_BASER_OFFSET_BITS = 5
NUM_IMM_BITS = 8

REGA_POS = 8
REGB_POS = 5
IMM_POS = 0

NUM_CODE_ADDRESS_PINS = 15


OPCODE_DICT: dict[str, int] = {
    "ADD":    0b00000,
    "ADDI":   0b00001,
    "LEA":    0b00010,
    "NOT":    0b00011,
    "AND":    0b00100,
    "ANDI":   0b00101,
    "STP":    0b00110,
    "CMP":    0b00111,
    "LD":     0b01000,
    "LDR":    0b01001,
    "STR":    0b01010,
    "PAUSE":  0b01011,
    "CALL":   0b01100,
    "RET":    0b01101,
    "TRAP":   0b01110,
    "STPI":   0b01111,
    "START":  0b10000,
    "SETSP":  0b10001,
    "PUSH":   0b10010,
    "POP":    0b10011,
    "OR":     0b10100,
    "ORI":    0b10101,
    "CPYSP":  0b10110,
    "JMP":    0b10111,
    "JO":     0b11000,
    "JNO":    0b11001,
    "JZ":     0b11010,
    "JNZ":    0b11011,
    "JS":     0b11100,
    "JNS":    0b11101,
    "JC":     0b11110,
    "JNC":    0b11111
}

OPERATION_DICT: dict[int, str] = {
    0b00000: "ADD",
    0b00001: "ADDI",
    0b00010: "LEA",
    0b00011: "NOT",
    0b00100: "AND",
    0b00101: "ANDI",
    0b00110: "STP",
    0b00111: "CMP",
    0b01000: "LD",
    0b01001: "LDR",
    0b01010: "STR",
    0b01011: "PAUSE",
    0b01100: "CALL",
    0b01101: "RET",
    0b01110: "TRAP",
    0b01111: "STPI",
    0b10000: "START",
    0b10001: "SETSP",
    0b10010: "PUSH",
    0b10011: "POP",
    0b10100: "OR",
    0b10101: "ORI",
    0b10110: "CPYSP",
    0b10111: "JMP",
    0b11000: "JO",
    0b11001: "JNO",
    0b11010: "JZ",
    0b11011: "JNZ",
    0b11100: "JS",
    0b11101: "JNS",
    0b11110: "JC",
    0b11111: "JNC"    
}

TWOREG:     set[str] = {"ADD", "AND", "OR"}
REGIMM:     set[str] = {"ADDI", "ANDI", "ORI"}
SINGR:      set[str] = {"NOT", "START", "SETSP", "PUSH", "POP", "CPYSP"}
PCOFF:      set[str] = {"JMP", "JO", "JNO", "JZ", "JNZ", "JS", "JNS", "JC", "JNC", "CALL", "LEA"}
NOARG:      set[str] = {"PAUSE", "RET"}
BASER:      set[str] = {"LDR", "STR"}
PORTIMM:    set[str] = {"STPI"}
PORTREG:    set[str] = {"STP"}

OTHER:      set[str] = {"CMP", "LD", "TRAP"}
