# Version 1.00

def FlipByte(Data):
    New = 0x00
    for i in range(8):
        New = New << 1

        if(Data & 1):
            New |= 1
        
        Data = Data >> 1

    
    return New

def Write(Data, FileName, Flip=False):
    """
    View contents of the binary file in PS with ```format-hex a.bin | more```
    """
    if Flip:
        for i in range(len(Data)):
            Data[i] = FlipByte(Data[i])

    with open(FileName, "wb") as output_file:
        output_file.write(Data)
        output_file.close()

    return