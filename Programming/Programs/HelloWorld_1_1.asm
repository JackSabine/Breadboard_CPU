; Built for ISA v1.1

.INCLUDE    OSR_1_1
.ORIG       0x0400
HelloWorld:
    lea     r0,     MyLabel
    trap    sprint
    jmp     around

MyLabel         .STRINGZ    "Hello, World!"
MyOtherLabel    .BLKW       0xF

around:
    pause