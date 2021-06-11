import sys

from writer import Write

def main():
    """
    if(len(sys.argv) < 2):
        raise Exception("Provide an input file to compile")
    
    FileToCompile = sys.argv[1]
    FileToWrite = sys.argv[2] if len(sys.argv) >= 3 else "a.bin"
    """
    FileToCompile = "File.txt"
    FileToWrite = "a.bin"

    Binary = bytearray(2 ** 15)
    Binary[0] = 0x0a
    Write(Binary, FileToWrite)

    return

if __name__ == "__main__":
    main()