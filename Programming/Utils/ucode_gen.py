import sys,re,enum
from writer import Write
from ISA.Macros import *

# print("cd \"", os.path.dirname(os.path.abspath(__file__)), "\"", sep="")
# print("format-hex a.bin | more")

import ISA.v1_0.ucodedef as ucode

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
    Data = bytearray(2 ** NUM_ADDRESS_PINS)
    InstToWrite = 0x00

    for ROMid in range(2**NUM_CS_BITS):
        for OPcode in range(2**NUM_OPC_BITS):
            for CondFL in range(2**NUM_CONDFL_BITS):
                for uInst in range(2**NUM_UINST_BITS):
                    # Generate a byte from the uInstructions where ROMid designates which byte (0 least significant, (2^NUM_CS_BITS) - 1 most significant)
                    if(OPcode < 24):
                        Inst = ucode.MicroInstructions[OPcode][uInst]
                    else:
                        # Programming the conditional instructions
                            # If opcode is even, then the not taken condition is when CondFL = 0
                            # For an odd opcode, not taken is when CondFL = 1
                        if(OPcode % 2 == 0):
                            # Even
                            if(CondFL == 1):
                                # Taken
                                Inst = ucode.MicroInstructions[OPcode][uInst]
                            else:
                                # Not taken
                                Inst = ucode.NOT_TAKEN[uInst]
                        else:
                            #Odd
                            if(CondFL == 0):
                                # Taken
                                Inst = ucode.MicroInstructions[OPcode][uInst]
                            else:
                                # Not taken
                                Inst = ucode.NOT_TAKEN[uInst]

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