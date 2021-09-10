.INCLUDE    OSR_1_1
; Built for ISA v1.1

HelloWorld:
    lea     r0,     MyLabel
    trap    sprint_routine
    jmp     around

MyLabel         .STRINGZ    "Hello, World!"
MyOtherLabel    .BLKW       0xF

around:
    pause