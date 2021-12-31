OPCODE_DICT: dict[str, int] = {
    "PAUSE":  0b00000,
    "ADDI":   0b00001,
    "LEA":    0b00010,
    "NOT":    0b00011,
    "AND":    0b00100,
    "ANDI":   0b00101,
    "STP":    0b00110,
    "CMP":    0b00111,
    "LD":     0b01000,
    "LDR":    0b01001,
    "STR":    0b01010,
    "ADD":    0b01011,
    "CALL":   0b01100,
    "RET":    0b01101,
    "TRAP":   0b01110,
    "STPI":   0b01111,
    "START":  0b10000,
    "SETSP":  0b10001,
    "PUSH":   0b10010,
    "POP":    0b10011,
    "OR":     0b10100,
    "ORI":    0b10101,
    "CPYSP":  0b10110,
    "JMP":    0b10111,
    "JO":     0b11000,
    "JNO":    0b11001,
    "JZ":     0b11010,
    "JNZ":    0b11011,
    "JS":     0b11100,
    "JNS":    0b11101,
    "JC":     0b11110,
    "JNC":    0b11111
}

OPERATION_DICT: dict[int, str] = {
    0b00000: "PAUSE",
    0b00001: "ADDI",
    0b00010: "LEA",
    0b00011: "NOT",
    0b00100: "AND",
    0b00101: "ANDI",
    0b00110: "STP",
    0b00111: "CMP",
    0b01000: "LD",
    0b01001: "LDR",
    0b01010: "STR",
    0b01011: "ADD",
    0b01100: "CALL",
    0b01101: "RET",
    0b01110: "TRAP",
    0b01111: "STPI",
    0b10000: "START",
    0b10001: "SETSP",
    0b10010: "PUSH",
    0b10011: "POP",
    0b10100: "OR",
    0b10101: "ORI",
    0b10110: "CPYSP",
    0b10111: "JMP",
    0b11000: "JO",
    0b11001: "JNO",
    0b11010: "JZ",
    0b11011: "JNZ",
    0b11100: "JS",
    0b11101: "JNS",
    0b11110: "JC",
    0b11111: "JNC"    
}

TWOREG:     set[str] = {"ADD", "AND", "OR", "CMP"}
REGIMM:     set[str] = {"ADDI", "ANDI", "ORI", "LD"}
SINGR:      set[str] = {"NOT", "START", "SETSP", "PUSH", "POP", "CPYSP"}
PCOFF:      set[str] = {"JMP", "JO", "JNO", "JZ", "JNZ", "JS", "JNS", "JC", "JNC", "CALL"}
NOARG:      set[str] = {"PAUSE", "RET"}
BASER:      set[str] = {"LDR", "STR"}
PORTIMM:    set[str] = {"STPI"}
PORTREG:    set[str] = {"STP"}

OTHER:      set[str] = {"TRAP", "LEA"}
