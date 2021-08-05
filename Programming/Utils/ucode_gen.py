import sys,re,enum
from writer import Write
from aliases import *

# print("cd \"", os.path.dirname(os.path.abspath(__file__)), "\"", sep="")
# print("format-hex a.bin | more")

# uInstructions per the excel (not automatically copied)

ADD     =   [ PLO|MALI, PHO|MAHI, PI|MO|ILI, MO|MRH|IHI,      RAS|RO|ARI,	                RBS|RO|AUA|ASI|ARO|CSU,	        ASO|CCU|RAS|RI,	        NI  ]
ADDI    =   [ PLO|MALI, PHO|MAHI, PI|MO|ILI, MO|MRH|IHI,      RAS|RO|ARI,     	            GBO|AUA|ASI|ARO|CSU,            ASO|CCU|RAS|RI,         NI  ]
NOT     =   [ PLO|MALI, PHO|MAHI, PI|MO|ILI, MO|MRH|IHI,      RAS|RO|AUA|ASI|AIB,           ASO|CCU|RAS|RI,	                NI  ]
AND     =   [ PLO|MALI, PHO|MAHI, PI|MO|ILI, MO|MRH|IHI,      RAS|RO|ARI,	                RBS|RO|AUN|ASI|ARO,             ASO|CCU|RAS|RI,	        NI  ]
ANDI    =   [ PLO|MALI, PHO|MAHI, PI|MO|ILI, MO|MRH|IHI,      RAS|RO|ARI,	                GBO|AUN|ASI|ARO,                ASO|CCU|RAS|RI,	        NI  ]
NEG     =   [ PLO|MALI, PHO|MAHI, PI|MO|ILI, MO|MRH|IHI,      RAS|RO|AUA|ASI|AIB|AAC,	    ASO|CCU|RAS|RI,	                NI  ]
CMP     =   [ PLO|MALI, PHO|MAHI, PI|MO|ILI, MO|MRH|IHI,      RAS|RO|ARI,	                RBS|RO|AUA|ASI|ARO|AIB|AAC,     ASO|CCU,	            NI  ]
LD      =   [ PLO|MALI, PHO|MAHI, PI|MO|ILI, MO|MRH|IHI,      RAS|GBO|RI|CCU,	            NI  ]
LDR     =   [ PLO|MALI, PHO|MAHI, PI|MO|ILI, MO|MRH|IHI,      RBS|RO|ARI,	                GBO|ASX|AUA|ASI|ARO|ACU,	    ASO|MALI,	            RBS|RO|RSH|AUA|ASI|ACO,	        ASO|MAHI,	    RAS|RI|MO|CCU,	            NI  ]
STR     =   [ PLO|MALI, PHO|MAHI, PI|MO|ILI, MO|MRH|IHI,      RBS|RO|ARI,	                GBO|ASX|AUA|ASI|ARO|ACU,	    ASO|MALI,	            RBS|RO|RSH|AUA|ASI|ACO,	        ASO|MAHI,	    RAS|RO|MI,	                NI  ]
PAUSE   =   [ PLO|MALI, PHO|MAHI, PI|MO|ILI, MO|MRH|IHI,      HT,                           HT,                             NI  ]
CALL    =   [ PLO|MALI, PHO|MAHI, PI|MO|ILI, MO|MRH|IHI,      SLO|MALI,	                    SHO|MAHI,	                    SI|PLO|MI|ARI,	        SLO|MALI,	                    SHO|MAHI,	            SI|PHO|MI,	    GBO|ARO|ASI|AUA|ACU,	    ASO|PLI,	    PHO|ARI,	GAO|ARO|ASI|AUA|ACO,	ASO|PHI,	NI  ]
RET     =   [ PLO|MALI, PHO|MAHI, PI|MO|ILI, MO|MRH|IHI,      SD,                           SLO|MALI,	                    SHO|MAHI,	            MO|PHI|SD,	                    SLO|MALI,	            SHO|MAHI,	    MO|PLI,	                    NI  ]
TRAP    =   [ PLO|MALI, PHO|MAHI, PI|MO|ILI, MO|MRH|IHI,      SLO|MALI,	                    SHO|MAHI,	                    SI|PLO|MI,	            SLO|MALI,	                    SHO|MAHI,	            SI|PHO|MI,	    GBO|PLI,	                GAO|PHI,	    NI  ]
SETBK   =   [ PLO|MALI, PHO|MAHI, PI|MO|ILI, MO|MRH|IHI,      NOINST,                       NI  ]
START   =   [ PLO|MALI, PHO|MAHI, PI|MO|ILI, MO|MRH|IHI,      RAS|RO|PLI,	                RAS|RO|RSH|PHI,	                NI  ]
SETSP   =   [ PLO|MALI, PHO|MAHI, PI|MO|ILI, MO|MRH|IHI,      RAS|RO|SLI,	                RAS|RO|RSH|SHI,	                NI  ]
PUSH    =   [ PLO|MALI, PHO|MAHI, PI|MO|ILI, MO|MRH|IHI,      SLO|MALI,	                    SHO|MAHI,	                    RAS|RO|MI|SI,	        NI  ]
POP     =   [ PLO|MALI, PHO|MAHI, PI|MO|ILI, MO|MRH|IHI,      SLO|MALI,	                    SHO|MAHI,	                    RAS|RI|MO|SD,	        NI  ]
OR      =   [ PLO|MALI, PHO|MAHI, PI|MO|ILI, MO|MRH|IHI,      RBS|RO|AAC|AUA|ASI|AIB,       ASO|ARI,                        RAS|RO|AAC|AUA|ASI|AIB, ASO|RAS|RI,                     RAS|RO|ARO|AUN|ASI,     ASO|RAS|RI,     RAS|RO|AAC|AUA|ASI|AIB,     ASO|RAS|RI|CCU, NI  ]
ORI     =   [ PLO|MALI, PHO|MAHI, PI|MO|ILI, MO|MRH|IHI,      RAS|RO|AAC|AUA|ASI|AIB,       ASO|ARI,                        GBO|AUN|ARO|ASI,        ASO|RAS|RI,                     RAS|RO|AAC|AUA|ASI|AIB, ASO|RAS|RI|CCU, NI  ]
CPYSP   =   [ PLO|MALI, PHO|MAHI, PI|MO|ILI, MO|MRH|IHI,      SLO|RAS|RI,                   SHO|RAS|RI|RSH,                 NI  ] 
JMP     =   [ PLO|MALI, PHO|MAHI, PI|MO|ILI, MO|MRH|IHI,      PLO|ARI,	                    GBO|ARO|ASI|AUA|ACU,	        ASO|PLI,	            PHO|ARI,	                    GAO|ARO|ASI|AUA|ACO,	ASO|PHI,	    NI  ]
JO      =   [ PLO|MALI, PHO|MAHI, PI|MO|ILI, MO|MRH|IHI,      PLO|ARI,	                    GBO|ARO|ASI|AUA|ACU,	        ASO|PLI,	            PHO|ARI,	                    GAO|ARO|ASI|AUA|ACO,	ASO|PHI,	    NI  ]
JNO     =   [ PLO|MALI, PHO|MAHI, PI|MO|ILI, MO|MRH|IHI,      PLO|ARI,	                    GBO|ARO|ASI|AUA|ACU,	        ASO|PLI,	            PHO|ARI,	                    GAO|ARO|ASI|AUA|ACO,	ASO|PHI,	    NI  ]
JZ      =   [ PLO|MALI, PHO|MAHI, PI|MO|ILI, MO|MRH|IHI,      PLO|ARI,	                    GBO|ARO|ASI|AUA|ACU,	        ASO|PLI,	            PHO|ARI,	                    GAO|ARO|ASI|AUA|ACO,	ASO|PHI,	    NI  ]
JNZ     =   [ PLO|MALI, PHO|MAHI, PI|MO|ILI, MO|MRH|IHI,      PLO|ARI,	                    GBO|ARO|ASI|AUA|ACU,	        ASO|PLI,	            PHO|ARI,	                    GAO|ARO|ASI|AUA|ACO,	ASO|PHI,	    NI  ]
JS      =   [ PLO|MALI, PHO|MAHI, PI|MO|ILI, MO|MRH|IHI,      PLO|ARI,	                    GBO|ARO|ASI|AUA|ACU,	        ASO|PLI,	            PHO|ARI,	                    GAO|ARO|ASI|AUA|ACO,	ASO|PHI,	    NI  ]
JNS     =   [ PLO|MALI, PHO|MAHI, PI|MO|ILI, MO|MRH|IHI,      PLO|ARI,	                    GBO|ARO|ASI|AUA|ACU,	        ASO|PLI,	            PHO|ARI,	                    GAO|ARO|ASI|AUA|ACO,	ASO|PHI,	    NI  ]
JC      =   [ PLO|MALI, PHO|MAHI, PI|MO|ILI, MO|MRH|IHI,      PLO|ARI,	                    GBO|ARO|ASI|AUA|ACU,	        ASO|PLI,	            PHO|ARI,	                    GAO|ARO|ASI|AUA|ACO,	ASO|PHI,	    NI  ]
JNC     =   [ PLO|MALI, PHO|MAHI, PI|MO|ILI, MO|MRH|IHI,      PLO|ARI,	                    GBO|ARO|ASI|AUA|ACU,	        ASO|PLI,	            PHO|ARI,	                    GAO|ARO|ASI|AUA|ACO,	ASO|PHI,	    NI  ]


BLANK =     [ PLO|MALI, PHO|MAHI, PI|MO|ILI, MO|MRH|IHI,      NOINST,                NI]
NOT_TAKEN = BLANK

MicroInstructions = [
ADD,    # 00000
ADDI,   # 00001
BLANK,  # 00010
NOT,    # 00011
AND,    # 00100
ANDI,   # 00101
NEG,    # 00110
CMP,    # 00111
LD,     # 01000
LDR,    # 01001
STR,    # 01010
PAUSE,  # 01011
CALL,   # 01100
RET,    # 01101
TRAP,   # 01110
SETBK,  # 01111
START,  # 10000
SETSP,  # 10001
PUSH,   # 10010
POP,    # 10011
OR,     # 10100
ORI,    # 10101
CPYSP,  # 10110
JMP,    # 10111
JO,     # 11000
JNO,    # 11001
JZ,     # 11010
JNZ,    # 11011
JS,     # 11100
JNS,    # 11101
JC,     # 11110
JNC     # 11111
]

# EEPROM Address Pinout

# A12 : CS[2]
# A11 : CS[1]
# A10 : CS[0]
# A09 : OPC[4]
# A08 : OPC[3]
# A07 : OPC[2]
# A06 : OPC[1]
# A05 : OPC[0]
# A04 : Cond_Flag
# A03 : uInst[3]
# A02 : uInst[2]
# A01 : uInst[1]
# A00 : uInst[0]

def ucode_gen(OutFile):
    NUM_UINST_BITS          =   4
    NUM_CONDFL_BITS         =   1
    NUM_OPC_BITS            =   5
    NUM_CS_BITS             =   3

    NUM_ADDRESS_PINS        =   NUM_UINST_BITS+NUM_CONDFL_BITS+NUM_OPC_BITS+NUM_CS_BITS

    POS_CS                  = 0+NUM_UINST_BITS+NUM_CONDFL_BITS+NUM_OPC_BITS
    POS_OPC                 = 0+NUM_UINST_BITS+NUM_CONDFL_BITS
    POS_CONDFL              = 0+NUM_UINST_BITS
    POS_UINST               = 0

    INVERTING_MASK          = GAO|GBO|MO|NI|PHI|PHO|PLI|PLO|RAS|RBS|RI|RO|SHO|SLO

    Data = bytearray(2 ** NUM_ADDRESS_PINS)
    InstToWrite = 0x00

    # ROMid << POS_CS | OPcode << POS_OPC | CondFL << POS_CONDFL | uInst << POS_UINST

    for ROMid in range(2**NUM_CS_BITS):
        for OPcode in range(2**NUM_OPC_BITS):
            for CondFL in range(2**NUM_CONDFL_BITS):
                for uInst in range(2**NUM_UINST_BITS):
                    # Generate a byte from the uInstructions where ROMid designates which byte (0 least significant, (2^NUM_CS_BITS) - 1 most significant)
                    if(OPcode < 24):
                        Inst = MicroInstructions[OPcode][uInst]
                    else:
                        # Programming the conditional instructions
                            # If opcode is even, then the not taken condition is when CondFL = 0
                            # For an odd opcode, not taken is when CondFL = 1
                        if(OPcode % 2 == 0):
                            # Even
                            if(CondFL == 1):
                                # Taken
                                Inst = MicroInstructions[OPcode][uInst]
                            else:
                                # Not taken
                                Inst = NOT_TAKEN[uInst]
                        else:
                            #Odd
                            if(CondFL == 0):
                                # Taken
                                Inst = MicroInstructions[OPcode][uInst]
                            else:
                                # Not taken
                                Inst = NOT_TAKEN[uInst]

                    InstToWrite = 0xFF & ((Inst ^ INVERTING_MASK) >> (ROMid*8))
                    Data[ROMid << POS_CS | OPcode << POS_OPC | CondFL << POS_CONDFL | uInst << POS_UINST] = InstToWrite
                    if(Inst & NI == NI):
                        break

    Write(Data, OutFile)

    return

class __FlagState(enum.Enum):
    OUT_FILE     = 1

    StateV = None

if __name__ == "__main__":
    if(len(sys.argv) < 2):
        OutFile = "microcode.bin"
    else:
        for arg in sys.argv[1:]:
            if(re.search(r"-o", arg, re.IGNORECASE)):
                StateV = __FlagState.OUT_FILE
            else:
                if(StateV == __FlagState.OUT_FILE):
                    OutFile = arg   
    ucode_gen(OutFile=OutFile)