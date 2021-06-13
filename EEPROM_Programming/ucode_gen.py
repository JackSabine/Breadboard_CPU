from writer import Write
from aliases import *
import os

print("cd \"", os.path.dirname(os.path.abspath(__file__)), "\"", sep="")
print("format-hex a.bin | more")

# uInstructions per the excel (not automatically copied)

MicroInstructions = [
    [   PLO|MALI, PHO|MAHI, PI|MO|ILI, MO|MRH|IHI,      RAS|RO|ARI,	        RBS|RO|AUA|ASI|ARO,	            ASO|CC|RAS|RI,	    NI                                                                                                                                                  ], # ADD
    [   PLO|MALI, PHO|MAHI, PI|MO|ILI, MO|MRH|IHI,      RAS|RO|ARI,	        GBO|AUA|ASI|ARO,	            ASO|CC|RAS|RI,	    NI                                                                                                                                                  ], # ADDI
    [   PLO|MALI, PHO|MAHI, PI|MO|ILI, MO|MRH|IHI,      RAS|RO|ARI,	        RBS|RO|AUA|ASI|ARO|AIB|AAC,	    ASO|CC|RAS|RI,	    NI                                                                                                                                                  ], # SUB
    [   PLO|MALI, PHO|MAHI, PI|MO|ILI, MO|MRH|IHI,      GBO|ARI,	        RAS|RO|AUA|ASI|ARO|AIB,	        ASO|CC|RAS|RI,	    NI                                                                                                                                                  ], # NOT
    [   PLO|MALI, PHO|MAHI, PI|MO|ILI, MO|MRH|IHI,      RAS|RO|ARI,	        RBS|RO|AUN|ASI|ARO,	            ASO|CC|RAS|RI,	    NI                                                                                                                                                  ], # AND
    [   PLO|MALI, PHO|MAHI, PI|MO|ILI, MO|MRH|IHI,      RAS|RO|ARI,	        GBO|AUN|ARI|ASI|ARO,	        ASO|CC|RAS|RI,	    NI                                                                                                                                                  ], # ANDI
    [   PLO|MALI, PHO|MAHI, PI|MO|ILI, MO|MRH|IHI,      GBO|ARI,	        RAS|RO|AUA|ASI|ARO|AIB,	        ASO|CC|RAS|RI,	    NI                                                                                                                                                  ], # NEG
    [   PLO|MALI, PHO|MAHI, PI|MO|ILI, MO|MRH|IHI,      RAS|RO|ARI,	        RBS|RO|AUA|ASI|ARO|AIB|AAC,	    ASO|CC,	            NI                                                                                                                                                  ], # CMP
    [   PLO|MALI, PHO|MAHI, PI|MO|ILI, MO|MRH|IHI,      RAS|GBO|RI|CC,	    NI                                                                                                                                                                                                      ], # LDimm
    [   PLO|MALI, PHO|MAHI, PI|MO|ILI, MO|MRH|IHI,      RBS|RO|ARI,	        GBO|ASX|AUA|ASI|ARO|ACU,	    ASO|MALI,	        RBS|RO|ARI|RS0,	    AUA|ASI|ARO|ACO,	    ASO|MAHI,	    RAS|RI|MO|CC,	        NI                                                              ], # LDR
    [   PLO|MALI, PHO|MAHI, PI|MO|ILI, MO|MRH|IHI,      RBS|RO|ARI,	        GBO|ASX|AUA|ASI|ARO|ACU,	    ASO|MALI,	        RBS|RO|ARI|RS0,	    AUA|ASI|ARO|ACO,	    ASO|MAHI,	    RAS|RO|MI,	            NI                                                              ], # STR
    [   PLO|MALI, PHO|MAHI, PI|MO|ILI, MO|MRH|IHI,      HT,                 NI                                                                                                                                                                                                      ], # HLT
    [   PLO|MALI, PHO|MAHI, PI|MO|ILI, MO|MRH|IHI,      SLO|MALI,	        SHO|MAHI,	                    SD|PLO|MI|ARI,	    SLO|MALI,	        SHO|MAHI,	            SD|PHO|MI,	    GBO|ARO|ASI|AUA|ACU,	ASO|PLI,	PHO|ARI,	GAO|ARO|ASI|AUA|ACO,	ASO|PHI,	NI  ], # CALL
    [   PLO|MALI, PHO|MAHI, PI|MO|ILI, MO|MRH|IHI,      SLO|MALI,	        SHO|MAHI,	                    SI|MO|PHI,	        SLO|MALI,	        SLO|MAHI,	            SI|MO|PLI,	    NI                                                                                      ], # RET
    [   PLO|MALI, PHO|MAHI, PI|MO|ILI, MO|MRH|IHI,      SLO|MALI,	        SHO|MAHI,	                    SD|PLO|MI,	        SLO|MALI,	        SHO|MAHI,	            SD|PHO|MI,	    GBO|PLI,	            GAO|PHI,	NI                                                  ], # TRAP
    [   PLO|MALI, PHO|MAHI, PI|MO|ILI, MO|MRH|IHI,      NOINST,             NI                                                                                                                                                                                                      ], # NOP
    [   PLO|MALI, PHO|MAHI, PI|MO|ILI, MO|MRH|IHI,      RAS|RO|PLI,	        RAS|RO|RS0|PHI,	                NI                                                                                                                                                                      ], # SETPC
    [   PLO|MALI, PHO|MAHI, PI|MO|ILI, MO|MRH|IHI,      RAS|RO|SLI,	        RAS|RO|RS0|SHI,	                NI                                                                                                                                                                      ], # SETSP
    [   PLO|MALI, PHO|MAHI, PI|MO|ILI, MO|MRH|IHI,      SLO|MALI,	        SHO|MAHI,	                    RAS|RO|MI|SD,	    NI                                                                                                                                                  ], # PUSH
    [   PLO|MALI, PHO|MAHI, PI|MO|ILI, MO|MRH|IHI,      SLO|MALI,	        SHO|MAHI,	                    RAS|RI|MO|SI,	    NI                                                                                                                                                  ], # POP
    [   PLO|MALI, PHO|MAHI, PI|MO|ILI, MO|MRH|IHI,      NOINST,             NI                                                                                                                                                                                                      ], #
    [   PLO|MALI, PHO|MAHI, PI|MO|ILI, MO|MRH|IHI,      NOINST,             NI                                                                                                                                                                                                      ], #
    [   PLO|MALI, PHO|MAHI, PI|MO|ILI, MO|MRH|IHI,      NOINST,             NI                                                                                                                                                                                                      ], #
    [   PLO|MALI, PHO|MAHI, PI|MO|ILI, MO|MRH|IHI,      PLO|ARI,	        GBO|ARO|ASI|AUA|ACU,	        ASO|PLI,	        PHO|ARI,	        GAO|ARO|ASI|AUA|ACO,	ASO|PHI,	    NI                                                                                      ], # JMP
    [   PLO|MALI, PHO|MAHI, PI|MO|ILI, MO|MRH|IHI,      PLO|ARI,	        GBO|ARO|ASI|AUA|ACU,	        ASO|PLI,	        PHO|ARI,	        GAO|ARO|ASI|AUA|ACO,	ASO|PHI,	    NI                                                                                      ], # JO
    [   PLO|MALI, PHO|MAHI, PI|MO|ILI, MO|MRH|IHI,      PLO|ARI,	        GBO|ARO|ASI|AUA|ACU,	        ASO|PLI,	        PHO|ARI,	        GAO|ARO|ASI|AUA|ACO,	ASO|PHI,	    NI                                                                                      ], # JNO
    [   PLO|MALI, PHO|MAHI, PI|MO|ILI, MO|MRH|IHI,      PLO|ARI,	        GBO|ARO|ASI|AUA|ACU,	        ASO|PLI,	        PHO|ARI,	        GAO|ARO|ASI|AUA|ACO,	ASO|PHI,	    NI                                                                                      ], # JZ
    [   PLO|MALI, PHO|MAHI, PI|MO|ILI, MO|MRH|IHI,      PLO|ARI,	        GBO|ARO|ASI|AUA|ACU,	        ASO|PLI,	        PHO|ARI,	        GAO|ARO|ASI|AUA|ACO,	ASO|PHI,	    NI                                                                                      ], # JNZ
    [   PLO|MALI, PHO|MAHI, PI|MO|ILI, MO|MRH|IHI,      PLO|ARI,	        GBO|ARO|ASI|AUA|ACU,	        ASO|PLI,	        PHO|ARI,	        GAO|ARO|ASI|AUA|ACO,	ASO|PHI,	    NI                                                                                      ], # JS
    [   PLO|MALI, PHO|MAHI, PI|MO|ILI, MO|MRH|IHI,      PLO|ARI,	        GBO|ARO|ASI|AUA|ACU,	        ASO|PLI,	        PHO|ARI,	        GAO|ARO|ASI|AUA|ACO,	ASO|PHI,	    NI                                                                                      ], # JNS
    [   PLO|MALI, PHO|MAHI, PI|MO|ILI, MO|MRH|IHI,      PLO|ARI,	        GBO|ARO|ASI|AUA|ACU,	        ASO|PLI,	        PHO|ARI,	        GAO|ARO|ASI|AUA|ACO,	ASO|PHI,	    NI                                                                                      ], # JC
    [   PLO|MALI, PHO|MAHI, PI|MO|ILI, MO|MRH|IHI,      PLO|ARI,	        GBO|ARO|ASI|AUA|ACU,	        ASO|PLI,	        PHO|ARI,	        GAO|ARO|ASI|AUA|ACO,	ASO|PHI,	    NI                                                                                      ], # JNC
]

NotTaken = [
        PLO|MALI, PHO|MAHI, PI|MO|ILI, MO|MRH|IHI,      NOINST,             NI
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

NUM_UINST_BITS          =   4
NUM_CONDFL_BITS         =   1
NUM_OPC_BITS            =   5
NUM_CS_BITS             =   3

NUM_ADDRESS_PINS        =   NUM_UINST_BITS+NUM_CONDFL_BITS+NUM_OPC_BITS+NUM_CS_BITS

POS_CS                  = 0+NUM_UINST_BITS+NUM_CONDFL_BITS+NUM_OPC_BITS
POS_OPC                 = 0+NUM_UINST_BITS+NUM_CONDFL_BITS
POS_CONDFL              = 0+NUM_UINST_BITS
POS_UINST               = 0

def main():

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
                                Inst = NotTaken[uInst]
                        else:
                            #Odd
                            if(CondFL == 0):
                                # Taken
                                Inst = MicroInstructions[OPcode][uInst]
                            else:
                                # Not taken
                                Inst = NotTaken[uInst]

                    InstToWrite = 0xFF & (Inst >> (ROMid*8))
                    Data[ROMid << POS_CS | OPcode << POS_OPC | CondFL << POS_CONDFL | uInst << POS_UINST] = InstToWrite
                    if(Inst & NI == NI):
                        break

    Write(Data, "microcode.bin")

    return

if __name__ == "__main__":
    main()