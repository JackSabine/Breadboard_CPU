from aliases import *
from writer import Write

NUM_ADDR_BITS = 15

def main():
    Code = bytearray(2**NUM_ADDR_BITS)
    for i in range(len(Code)):
        if(i % 2 == 0):
            Code[i] = 0x00
        else:
            Code[i] = 0x91
        
    Write(Code, FileName="Program.bin", Flip=True)

    return


if __name__ == "__main__":
    main()