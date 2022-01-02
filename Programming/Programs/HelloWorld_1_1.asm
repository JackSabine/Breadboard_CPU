; Built for ISA v1.1

.INCLUDE    Budgetlake.h
.ORIG       0x0400
HelloWorld:
    lea     r0,     EpicMessage
    trap    SPRINT
    jmp     around

EpicMessage:        .STRINGZ    "new year pog"

around:
    pause