import os, sys
path: str = os.path.dirname(__file__)
while(not path.endswith("Assembler")):
    path = os.path.dirname(path)
sys.path.append(os.path.dirname(path))

from Assembler.v1_1.ucode.macros import *

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
POP     =   [ PLO|MALI, PHO|MAHI, PI|MO|ILI, MO|MRH|IHI,      SLO|MALI,	                    SHO|MAHI,	                    RAS|RI|MO|SD|CCU,       NI  ]
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
STP     =   [ PLO|MALI, PHO|MAHI, PI|MO|ILI, MO|MRH|IHI,      MAHI,                         GAO|MALI,                       RBS|RO|MI,              NI ]
STPI    =   [ PLO|MALI, PHO|MAHI, PI|MO|ILI, MO|MRH|IHI,      MAHI,                         GAO|MALI,                       GBO|MI,                 NI ]
LEA     =   [ PLO|MALI, PHO|MAHI, PI|MO|ILI, MO|MRH|IHI,      PLO|ARI,	                    GBO|ARO|ASI|AUA|ACU,	        ASO|RI|RAS,	            PHO|ARI,	                    GAO|ARO|ASI|AUA|ACO,	ASO|RAS|RSH|RI, NI  ]

BLANK =     [ PLO|MALI, PHO|MAHI, PI|MO|ILI, MO|MRH|IHI,      NOINST,                NI]
NOT_TAKEN = BLANK


MicroInstructions = {
    0b00000: PAUSE,
    0b00001: ADDI,
    0b00010: LEA,
    0b00011: NOT,
    0b00100: AND,
    0b00101: ANDI,
    0b00110: STP,
    0b00111: CMP,
    0b01000: LD,
    0b01001: LDR,
    0b01010: STR,
    0b01011: ADD,
    0b01100: CALL,
    0b01101: RET,
    0b01110: TRAP,
    0b01111: STPI,
    0b10000: START,
    0b10001: SETSP,
    0b10010: PUSH,
    0b10011: POP,
    0b10100: OR,
    0b10101: ORI,
    0b10110: CPYSP,
    0b10111: JMP,
    0b11000: JO,
    0b11001: JNO,
    0b11010: JZ,
    0b11011: JNZ,
    0b11100: JS,
    0b11101: JNS,
    0b11110: JC,
    0b11111: JNC
}
