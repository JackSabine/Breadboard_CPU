; Built for ISA v1.1

.INCLUDE    Budgetlake.h
.ORIG       0x0400
HelloWorld:
    lea     r0,     LongMessage
    trap    SPRINT
    jmp     around

LongMessage:        .STRINGZ    "This is a long message 31 chars"

around:
    pause