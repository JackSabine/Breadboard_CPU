import re
from typing import Union

def DecOrHexSearch(str) -> Union[int, None]:
    MatchDec = re.search(r"#(-?[0-9]+)",str,re.IGNORECASE)
    MatchHex = re.search(r"0?x([0-9A-F]+)",str,re.IGNORECASE)
    RetVal = None

    if(MatchDec is not None):
        RetVal = int(MatchDec.groups()[0])
    elif(MatchHex is not None):
        RetVal = int(MatchHex.groups()[0],base=16)

    return (RetVal)

def Write(Data, FileName):
    """
    View contents of the binary file in PS with ```format-hex a.bin | more```
    """

    with open(FileName, "wb") as output_file:
        output_file.write(Data)

    return