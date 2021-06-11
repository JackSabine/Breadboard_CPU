def Write(Data, FileName):
    """
    View contents of the binary file in PS with ```format-hex a.bin | more```
    """

    output_file = open(FileName, "wb")

    output_file.write(Data)

    output_file.close()

    return