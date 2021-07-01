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

    with open(FileToCompile, 'r') as F:
        Raw = F.readlines()
        print(Raw)
        Trimmed = []
        for Line in Raw:
            # Remove any lines that start with a comment or have no contents (newline only)
            if(Line != '\n' and not Line.startswith(';')):
                Trimmed.append(Line.replace('\n', ''))
            

        print(Trimmed)               

    Write(Binary, FileToWrite)

    return

if __name__ == "__main__":
    main()