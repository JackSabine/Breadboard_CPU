# Version 1.1

def Write(Data, FileName):
    """
    View contents of the binary file in PS with ```format-hex a.bin | more```
    """

    with open(FileName, "wb") as output_file:
        output_file.write(Data)

    return