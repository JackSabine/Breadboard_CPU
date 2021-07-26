.ORIG 0x0400

helloworld:
_lcd_init:
    ; Need RS (4), R/W (5), CE (6) and DB7-DB0 at 0
    ld      r2,     0x00
    ld      r3,     0xFF
    ld      r0,     0x00
    str     r0,     r2,     #2
    str     r0,     r2,     #3
    str     r0,     r2,     #1
    ld      r1,     0x30            ; 0011 0000 for 0011 **** startup sequence
    str     r1,     r2,     #3

    ; Initialization
    ld      r0,     0x01
    str     r0,     r2      #2
    ld      r0,     0x00
    str     r0,     r2      #2
    ld      r0,     0x01
    str     r0,     r2      #2
    ld      r0,     0x00
    str     r0,     r2      #2
    ld      r0,     0x01
    str     r0,     r2      #2
    ld      r0,     0x00
    str     r0,     r2      #2      ; Cycle 0011 **** three times

    ld      r1,     0x38            ; 0011 1000 for Function Set N = 1 (multi-line display) and F = 0 (5x8 dot character)
    str     r1,     r2,     #3
    ld      r0,     0x01
    str     r0,     r2      #2
    ld      r0,     0x00
    str     r0,     r2      #2

    ld      r1,     0x08            ; 0000 1000 for Display ON/OFF control (enforced D = 0, C = 0, B = 0 during initialization)
    str     r1,     r2,     #3
    ld      r0,     0x01
    str     r0,     r2      #2
    ld      r0,     0x00
    str     r0,     r2      #2

    ld      r1,     0x01            ; 0000 0001 for Clear Display (sets 20H to all DDRAM locs, 00H to DDRAM addr, return cursor to original position)
    str     r1,     r2,     #3
    ld      r0,     0x01
    str     r0,     r2      #2
    ld      r0,     0x00
    str     r0,     r2      #2

    ld      r1,     0x06            ; 0000 0110 for Entry Mode Set with I/D = 1 for the cursor to move right and SH to 0 to not shift the display
    str     r1,     r2,     #3
    ld      r0,     0x01
    str     r0,     r2      #2
    ld      r0,     0x00
    str     r0,     r2      #2
    ; Display initialized

    ld      r1,     0x0F            ; 0000 1111 for Display ON/OFF D = 1, C = 1, B = 1
    str     r1,     r2,     #3
    ld      r0,     0x01
    str     r0,     r2      #2
    ld      r0,     0x00
    str     r0,     r2      #2

    pause

    ld      r0,     0x55

    


_INF_LP:
    j       _INF_LP