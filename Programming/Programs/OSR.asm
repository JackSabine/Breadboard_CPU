; Built for ISA v1.0

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
    ld      r4,     0x00
    ld      r5,     0xFF
    ld      r3,     0x00
    ld      r2,     0x01
    str     r3,     r4,     #2      ; PortA = 0x01
    str     r2,     r4,     #3      ; PortB = 0x00

    str     r3,     r4,     #1      ; PortB output mode
_lcd_start_fcn_set:
    ld      r1,     0x30            ; 0011 0000 for 0011 **** startup sequence
    str     r1,     r4,     #3

    ld      r0,     #3              ; Clock in 0x30 three times
_lcd_start_fcn_set_lp:
    str     r2,     r4,     #2      ; PortA = 0x00
    ld      r1,     #1              ; wait_lp_1 executes this many times
_lcd_start_fcn_set_lp_wait_lp_1:
    add     r1,     #-1
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

; Begin OSR code
sprint:
    ret

; Alloc OSR : need N passed on stack consecutive blocks in heap (using first fit algorithm)
; STACK
;   5+  HSAPL and Mask pair bytes
;   4   HSAP[H]
;   3   HSAP[L]
;   2   i
;   1   TOBins
;   0   COBins
;  -1   OldFramePointer[H]
;  -2   OldFramePointer[L]
;  -3   RetVal[H]
;  -4   RetVal[L]
;  -5   N
alloc:
    ld      r0,     #0              ; Reset r0 to 0
    push    r0                      ; Make space for RetVal
    push    r0                      ; ""
    push    r4                      ; Save FramePointer
    push    r5                      ; ""
    cpysp   r4                      ; Get new FramePointer
    push    r0                      ; Make space for COBins
    push    r0                      ; TOBins
    ld      r2,     #16             ; For loop iteration i = 16
    push    r2                      ; Set i in stack
    ld      r0,     xFF             ; HSAP
    push    r0
    ld      r0,     xFE
    push    r0
_BLK_FINDER_LP:
    ld      r2,     #1              ; Configure mask
    ld      r3,     #8              ; Internal for loop iteration j = 8
_INNER_LP:
    ldr     r0,     r4,     #3      ; Get low byte of HSAP
    ldr     r1,     r4,     #4      ; Get high byte of HSAP
    ldr     r1,     r0,     #0      ; Get value at HSAP
    and     r1,     r2              ; Test r1 with Mask in r2
    jz      _OPEN_FOUND
    ; Blocked section... reset contiguous bin counter and pop off all pairs pushed
    ldr     r0,     r4,     #0      ; Load COBins
    jz      _OPEN_NOT_FOUND_FIN
_OPEN_NOT_FOUND_PAIR_POP_LP:
    ; If COBins is not zero, then we have to pop the HSAP low byte and mask pairs off the stack
    pop     r1
    pop     r1
    add     r0,     #-1
    jnz     _OPEN_NOT_FOUND_PAIR_POP_LP
_OPEN_NOT_FOUND_RESTORE_COBINS:
    str     r0,     r4,     #0      ; Set COBins back to 0
_OPEN_NOT_FOUND_FIN:
    add     r2,     r2              ; Mask = Mask + Mask (or effectively Mask = Mask << 1)
    j     _INC_INNER
_OPEN_FOUND:
    ; Coming into this block with HSAP low byte in r0 and mask in r2
    ; Next, push the low byte HSAP to the stack along with its mask
    push    r0
    push    r2

    ldr     r0,     r4,     #1      ; Load TOBins
    add     r0,     #1              ; Increment TOBins
    str     r0,     r4,     #1      ; Store TOBins back on stack
    ldr     r0,     r4,     #0      ; Load COBins
    add     r0,     #1              ; Increment COBins
    ldr     r1,     r4,     #-5     ; Load N
    cmp     r0,     r1              ; Is N == COBins ?
    jz      _PREP_RET_ADDR
    str     r0,     r4,     #0      ; Store COBins for next iteration
    ; Fall into _INC_INNER
_INC_INNER:
    ldr     r0,     r4,     #3      ; Decrement the low byte of the HSAP
    add     r0,     #-1             ;   No need to check for underflow conditions ->  HSA is 16 bytes long and at the top of its local 8-bit address range
    str     r0,     r4,     #3

    add     r3,     #-1             ; Decrement j for next loop
    jnz      _INNER_LP              ; Test if j > 0 else leave this INNER loop and fall into the outer loop inc _BLK_FINDER_INC
_BLK_FINDER_INC:
    ldr     r0,     r4,     #2      ; Load i (outer loop iterator)
    add     r0,     #-1             ; Decrement i
    jz      _CLEAN_UP_PAIRS             ; i == 0, no more status registers to check
    str     r0,     r4,     #2      ; Continue looping, so store i
    jnz     _BLK_FINDER_LP
_CLEAN_UP_PAIRS:
    ; How many pairs do we have... Given by COBins.
    ldr     r0,     r4,     #0
    jz      _END_ALLOC
_CLEAN_UP_PAIRS_LP:
    pop     r1
    pop     r1
    add     r0,     #-1
    jnz     _CLEAN_UP_PAIRS_LP
    jz      _END_ALLOC

_PREP_RET_ADDR:
    ; N contiguous heap blocks were found.  Entering this block, we have:
    ; r0, r1, r2: unassigned
    ; r3: j
    ; r4, r5: Frame Pointer (L,H)
    ; r6, r7: Global Pointer (L,H)

    ld      r0,     x70             ; Case 1 (Default): HBA low byte will be unaltered.
    ld      r2,     #0              ; r2 will be used to count the num iterations to decrement the given HBA (heap base address) high byte
    neg     r3
    add     r3,     #8              ; r3 = 8 - j
_DIV_LP:                        ; r2 = ceil((8-j)/2)
    jz      _ADJ_HB
    add     r2,     #1
    add     r3,     #-2
    jns     _DIV_LP                 ; if signed, then load decremented value of low byte (r3 = -1 in this case, so 8-j not divisible by 2.  Needs Case 2 HBA low byte.)
    ld      r0,     xF0
_ADJ_HB:
    str     r0,    r4,      #-4     ; Store low byte in retaddr low
    ; r0, r1, r3: unassigned
    ; r2: number of times to decrement HBA high byte
    ; r4, r5: Frame Pointer (L,H)
    ; r6, r7: Global Pointer (L,H)
    ld      r0,     xFE             ; r0 will hold the HBA high byte
    ldr     r1,     r4,     #2      ; load i
    neg     r1
    add     r1,     #16             ; r1 = 16 - i
    add     r2,     r3              ; r2 = 16 - i + ceil((8-j)/2) ---- number of times to decrement from xFE
    jz      _SUB_FIN
_SUB_LP:
    add     r0,     #-4             ; want to subtract 1024 from the whole BaseAddr.  1024 = 0x400.  Take away 4 from r1.
    add     r2,     #-1
    jnz     _SUB_LP
_SUB_FIN:
    str     r0,     r4,     #-3     ; Store high byte in retaddr high
_MARK_OCCUPIED_BLOCKS:
    ; Now we must mark the blocks that we are allocating as used leveraging the HSAPL and Mask pair bytes
    ; r0, r1, r2, r3: unassigned
    ; r4, r5: Frame Pointer (L,H)
    ; r6, r7: Global Pointer (L,H)
    ldr     r3,     r4,     #-5     ; Load N (known to be non-zero as integer values < 1 are invalid)
_MARK_OCCUPIED_BLOCKS_LP:
    ld      r1,     xFE             ; HSA high byte (constant xFE)
    pop     r2                      ; Mask comes off first
    pop     r0                      ; Low byte comes off second
    ldr     r1,     r0,     #0      ; Load the status reg
    or      r2,     r1
    ld      r1,     xFE             ; HSA high byte (constant xFE)
    str     r2,     r0,     #0      ; Restore the status reg updated with the mask overlayed

    add     r3,     #-1
    jnz     _MARK_OCCUPIED_BLOCKS_LP
 
_END_ALLOC:
    ; Cleanup stack
    ; N/A all popped                ;   5+  HSAPL and Mask pair bytes
    pop     r2                      ;   4   HSAP[H]
    pop     r2                      ;   3   HSAP[L]
    pop     r2                      ;   2   i
    pop     r2                      ;   1   TOBins
    pop     r2                      ;   0   COBins
    pop     r5                      ;  -1   OldFramePointer[H]
    pop     r4                      ;  -2   OldFramePointer[L]
    pop     r1                      ;  -3   RetVal[H]
    pop     r0                      ;  -4   RetVal[L]
    pop     r2                      ;  -5   N

    ret

; defshape OSR : define a custom shape to the connected GPU to leverage simplified draw commands later in the program given heap addr for data, and NxM
; STACK
;   5+  HSAPL and Mask pair bytes
;   4   HSAP[H]
;   3   HSAP[L]
;   2   i
;   1   TOBins
;   0   COBins
;  -1   OldFramePointer[H]
;  -2   OldFramePointer[L]
;  -3   HeapDataPointer[H]
;  -4   HeapDataPointer[L]
;  -5   N (object height)
;  -6   M (object width)
defshape:   