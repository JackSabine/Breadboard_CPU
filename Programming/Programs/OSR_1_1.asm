; Built for ISA v1.1

.ORIG 0x0000

; registers
; r0, r1, r2, r3, r4, r5, r6, r7

; Startup OSR : set PC to program location in memory, configure stack pointer to 0x8200, mark all HSA bytes as 0x00
startup:
    ld      r0,     0x00
    ld      r1,     0x82
    setsp   r0

    ld      r1,     #16
    ld      r2,     0xFF
    ld      r3,     0xFE
    
    call    _lcd_init

; _hsa_lp:
;     str     r0,     r2,     #0
;     add     r3,     #-1
;     add     r1,     #-1
;     jnz     _hsa_lp
_config_env:
    ld      r0,     0x00        ; Default PC 0x0400
    ld      r1,     0x04
    ld      r4,     0x00        ; Default Frame Pointer
    ld      r5,     0x82
    ld      r6,     0x00        ; Default Globals TOS Pointer
    ld      r7,     0x80
    
    start   r0

_lcd_init:
    ; Need RS (4)=0, R/W (5)=0, CE (6)=1, and DB7-DB0=0x00
    ld      r3,     0x00
    ld      r2,     0x01
    str     r3,     r4,     #2      ; PortA = 0x01
    str     r2,     r4,     #3      ; PortB = 0x00

    str     r3,     r4,     #1      ; PortB output mode
    stp     
_lcd_start_fcn_set:
    ld      r1,     0x30            ; 0011 0000 for 0011 **** startup sequence
    str     r1,     r4,     #3

    ld      r0,     #3              ; Clock in 0x30 three times
_lcd_start_fcn_set_lp:
    str     r2,     r4,     #2      ; PortA = 0x00
    ld      r1,     #1              ; wait_lp_1 executes this many times
_lcd_start_fcn_set_lp_wait_lp_1:
    addi    r1,     #-1
    jnz     _lcd_start_fcn_set_lp_wait_lp_1

    str     r3,     r4,     #2      ; PortA = 0x01
    ld      r1,     #1              ; wait_lp_2 executes this many times
_lcd_start_fcn_set_lp_wait_lp_2:
    add     r1,     #-1
    jnz     _lcd_start_fcn_set_lp_wait_lp_2

    add     r0,     #-1
    jnz     _lcd_start_fcn_set_lp

    ld      r1,     0x38            ; 0011 1000 for Function Set N = 1 (multi-line display) and F = 0 (5x8 dot character)
    str     r1,     r4,     #3
    str     r2,     r4,     #2      ; PortA = 0x00
    str     r3,     r4,     #2      ; PortA = 0x01

    ld      r1,     0x08            ; 0000 1000 for Display ON/OFF control (enforced D = 0, C = 0, B = 0 during initialization)
    str     r1,     r4,     #3
    str     r2,     r4,     #2      ; PortA = 0x00
    str     r3,     r4,     #2      ; PortA = 0x01

    ld      r1,     0x01            ; 0000 0001 for Clear Display (sets 20H to all DDRAM locs, 00H to DDRAM addr, return cursor to original position)
    str     r1,     r4,     #3
    str     r2,     r4,     #2      ; PortA = 0x00
    str     r3,     r4,     #2      ; PortA = 0x01

    ld      r1,     0x06            ; 0000 0110 for Entry Mode Set with I/D = 1 for the cursor to move right and SH to 0 to not shift the display
    str     r1,     r4,     #3
    str     r2,     r4,     #2      ; PortA = 0x00
    str     r3,     r4,     #2      ; PortA = 0x01

    ld      r1,     0x0F            ; 0000 1111 for Display ON/OFF control (set Display (on) = 1, Cursor (on) = 1, cursor Blink (on) = 1)
    str     r1,     r4,     #3
    str     r2,     r4,     #2      ; PortA = 0x00
    str     r3,     r4,     #2      ; PortA = 0x01
    ; Display initialized

    ret

sprint .EXTERN: