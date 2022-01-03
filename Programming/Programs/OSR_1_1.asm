; Built for ISA v1.1
.INCLUDE    Budgetlake.h
.ORIG       0x0000

; registers
; r0, r1, r2, r3, r4, r5, r6, r7

; Startup OSR : set PC to program location in memory, configure stack pointer to 0x8200, mark all HSA bytes as 0x00
startup:
    ld      r0,     0x00
    ld      r1,     0x82
    setsp   r0

    call    lcd_init

    ; ld      r1,     #16
    ; ld      r2,     0xFF
    ; ld      r3,     0xFE

; hsa_lp:
;     str     r0,     r2,     #0
;     add     r3,     #-1
;     add     r1,     #-1
;     jnz     hsa_lp
config_env:
    ld      r0,     0x00        ; Default PC 0x0400
    ld      r1,     0x04
    ld      r4,     0x00        ; Default Frame Pointer
    ld      r5,     0x82
    ld      r6,     0x00        ; Default Globals TOS Pointer
    ld      r7,     0x80
    
    start   r0

lcd_init:
    ; Need RS (4)=0, R/W (5)=0, CE (6)=1, and DB7-DB0=0x00
    stpi    PBDIR,  0x00            ; Set PortB to output 

    stpi    PORTA,  0x01
    stpi    PORTB,  0x00

lcd_start_fcn_set:
    stpi    PORTB,  0x30            ; 0011 0000 for 0011 **** startup sequence

    ld      r1,     #3              ; Clock in 0x30 three times
lcd_start_fcn_set_lp:
    stpi    PORTA,  0x00            ; CE = 0

    ld      r0,     #1              ; wait_lp iter 1 time
    trap    SLEEP

    stpi    PORTA,  0x01            ; CE = 1

    ld      r0,     #1
    trap    SLEEP

    addi    r1,     #-1
    jnz     lcd_start_fcn_set_lp

    stpi    PORTB,  0x38            ; 0011 1000 for Function Set N = 1 (multi-line display) and F = 0 (5x8 dot character)
    stpi    PORTA,  0x00
    stpi    PORTA,  0x01

    stpi    PORTB,  0x08            ; 0000 1000 for Display ON/OFF control (enforced D = 0, C = 0, B = 0 during initialization)
    stpi    PORTA,  0x00
    stpi    PORTA,  0x01

    stpi    PORTB,  0x01            ; 0000 0001 for Clear Display (sets 20H to all DDRAM locs, 00H to DDRAM addr, return cursor to original position)
    stpi    PORTA,  0x00
    stpi    PORTA,  0x01

    stpi    PORTB,  0x06            ; 0000 0110 for Entry Mode Set with I/D = 1 for the cursor to move right and SH to 0 to not shift the display
    stpi    PORTA,  0x00
    stpi    PORTA,  0x01

    stpi    PORTB,  0x0F            ; 0000 1111 for Display ON/OFF control (set Display (on) = 1, Cursor (on) = 1, cursor Blink (on) = 1)
    stpi    PORTA,  0x00
    stpi    PORTA,  0x01
    ; Display initialized

    ret

; TRAP TABLE
.ORIG   0x0100
__wait:
    jmp     wait_lp_routine
__sprint:
    jmp     sprint_routine
__display_rst:
    jmp     display_rst_routine




.ORIG 0x0120

; WAIT trap routine
; Num loop cycles value present in r0
wait_lp_routine:
    addi    r0,     #-1
    jnz     wait_lp_routine
    ret



; SPRINT trap routine
; {r1, r0}: String pointer present
; r2:       Remaining horizontal characters
; r3:       Remaining vertical rows (when 0, stop even if *strptr != NULL) --- use for char data after pushing remaining rows
sprint_routine:
    ; Clears display and sets cursor to home
    trap    DISPLAY_RST

    stpi    PORTA,  0x05
    ld      r2,     #16
    ld      r3,     #1
    push    r3
sprint_routine_lp:
    ldr     r3,     r0,     #0
    jz      sprint_routine_exit_popr3

    stp     PORTB,  r3
    stpi    PORTA,  0x04
    stpi    PORTA,  0x05

    addi    r2,     #-1
    jz      sprint_routine_checkrows
sprint_routine_increment_srcptr:
    addi    r0,     #1
    jnc     sprint_routine_lp
    addi    r1,     #1
    jmp     sprint_routine_lp

sprint_routine_checkrows:
    pop     r3
    jz      sprint_routine_exit
    addi    r3,     #-1
    push    r3
    ld      r2,     #16

    ; Set DDRAM address to 0x40 (row 2 column 1) (RS=0 W=0)
    stpi    PORTA,  0x01
    stpi    PORTB,  0xC0    ; 0x80 | 0x40
    stpi    PORTA,  0x00
    stpi    PORTA,  0x01
    stpi    PORTA,  0x05

    jmp     sprint_routine_increment_srcptr

sprint_routine_exit_popr3:
    pop     r3
sprint_routine_exit:
    stpi    PORTA,  0x01
    ret



; DISPLAY_RST trap routine
display_rst_routine:
    stpi    PORTB,  0x01            ; 0000 0001 for Clear Display (sets 20H to all DDRAM locs, 00H to DDRAM addr, return cursor to original position)
    stpi    PORTA,  0x00
    stpi    PORTA,  0x01
    ret