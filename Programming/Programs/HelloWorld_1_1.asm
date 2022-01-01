; Built for ISA v1.1

.INCLUDE    Budgetlake.h
.ORIG       0x0400
HelloWorld:
    lea     r0,     MyLabel
    trap    SPRINT
    jmp     around

MyLabel:        .STRINGZ    "Hello, World!"

around:
    pause