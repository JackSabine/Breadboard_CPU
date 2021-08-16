.ORIG 0x0400

helloworld:
    ld      r2,     0x00
    ld      r3,     0xFF

    ld      r0,     0x04        ; Alternate between 0x04 and 0x05 (CE clock for the display)

    str     r0,     r2,     #2  ; PortA = 0x04 (CE low, Write data to RAM command)
    str     r2,     r2,     #1  ; PortB output mode


    ld      r1,     0x6E        ; n
    str     r1,     r2,     #3  ; PortB = 'n'

    ld      r0,     0x05
    str     r0,     r2,     #2  ; PortA = 0x05 (CE high, Write data to RAM command)
    ld      r0,     0x04
    str     r0,     r2,     #2  ; PortA = 0x04 (CE low, Write data to RAM command)


    ld      r1,     0x6F        ; o
    str     r1,     r2,     #3  ; PortB = 'o'
    ld      r0,     0x05
    str     r0,     r2,     #2  ; PortA = 0x05 (CE high, Write data to RAM command)
    ld      r0,     0x04
    str     r0,     r2,     #2  ; PortA = 0x04 (CE low, Write data to RAM command)

    ld      r0,     0x05
    str     r0,     r2,     #2  ; PortA = 0x05 (CE high, Write data to RAM command)
    ld      r0,     0x04
    str     r0,     r2,     #2  ; PortA = 0x04 (CE low, Write data to RAM command)

    
    ld      r1,     0x74        ; t
    str     r1,     r2,     #3  ; PortB = 't'
    
    ld      r0,     0x05
    str     r0,     r2,     #2  ; PortA = 0x05 (CE high, Write data to RAM command)
    ld      r0,     0x04
    str     r0,     r2,     #2  ; PortA = 0x04 (CE low, Write data to RAM command)

    
    ld      r1,     0x20        ; 
    str     r1,     r2,     #3  ; PortB = ' '
    
    ld      r0,     0x05
    str     r0,     r2,     #2  ; PortA = 0x05 (CE high, Write data to RAM command)
    ld      r0,     0x04
    str     r0,     r2,     #2  ; PortA = 0x04 (CE low, Write data to RAM command)

    
    ld      r1,     0x63        ; c
    str     r1,     r2,     #3  ; PortB = 'c'
    
    ld      r0,     0x05
    str     r0,     r2,     #2  ; PortA = 0x05 (CE high, Write data to RAM command)
    ld      r0,     0x04
    str     r0,     r2,     #2  ; PortA = 0x04 (CE low, Write data to RAM command)


    ld      r1,     0x75        ; u
    str     r1,     r2,     #3  ; PortB = 'u'
    
    ld      r0,     0x05
    str     r0,     r2,     #2  ; PortA = 0x05 (CE high, Write data to RAM command)
    ld      r0,     0x04
    str     r0,     r2,     #2  ; PortA = 0x04 (CE low, Write data to RAM command)

    
    ld      r1,     0x74        ; t
    str     r1,     r2,     #3  ; PortB = 't'
    
    ld      r0,     0x05
    str     r0,     r2,     #2  ; PortA = 0x05 (CE high, Write data to RAM command)
    ld      r0,     0x04
    str     r0,     r2,     #2  ; PortA = 0x04 (CE low, Write data to RAM command)

    
    ld      r1,     0x65        ; e
    str     r1,     r2,     #3  ; PortB = 'e'
    
    ld      r0,     0x05
    str     r0,     r2,     #2  ; PortA = 0x05 (CE high, Write data to RAM command)
    ld      r0,     0x04
    str     r0,     r2,     #2  ; PortA = 0x04 (CE low, Write data to RAM command)

    pause