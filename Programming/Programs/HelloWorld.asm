; Built for ISA v1.0

.ORIG 0x0400

helloworld:
    ld      r2,     0x00
    ld      r3,     0xFF

    ld      r0,     0x04        ; Alternate between 0x04 and 0x05 (CE clock for the display)

    str     r0,     r2,     #2  ; PortA = 0x04 (CE low, Write data to RAM command)
    str     r2,     r2,     #1  ; PortB output mode


    ld      r1,     0x48        ; H
    str     r1,     r2,     #3  ; PortB = 'H'
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


    ld      r1,     0x6C        ; l
    str     r1,     r2,     #3  ; PortB = 'l'

    ld      r0,     0x05
    str     r0,     r2,     #2  ; PortA = 0x05 (CE high, Write data to RAM command)
    ld      r0,     0x04
    str     r0,     r2,     #2  ; PortA = 0x04 (CE low, Write data to RAM command)
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
    

    ld      r1,     0x2C        ; ,
    str     r1,     r2,     #3  ; PortB = ','

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


    ld      r1,     0x57        ; W
    str     r1,     r2,     #3  ; PortB = 'W'

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


    ld      r1,     0x72        ; r
    str     r1,     r2,     #3  ; PortB = 'r'

    ld      r0,     0x05
    str     r0,     r2,     #2  ; PortA = 0x05 (CE high, Write data to RAM command)
    ld      r0,     0x04
    str     r0,     r2,     #2  ; PortA = 0x04 (CE low, Write data to RAM command)


    ld      r1,     0x6C        ; l
    str     r1,     r2,     #3  ; PortB = 'l'

    ld      r0,     0x05
    str     r0,     r2,     #2  ; PortA = 0x05 (CE high, Write data to RAM command)
    ld      r0,     0x04
    str     r0,     r2,     #2  ; PortA = 0x04 (CE low, Write data to RAM command)


    ld      r1,     0x64        ; d
    str     r1,     r2,     #3  ; PortB = 'd'

    ld      r0,     0x05
    str     r0,     r2,     #2  ; PortA = 0x05 (CE high, Write data to RAM command)
    ld      r0,     0x04
    str     r0,     r2,     #2  ; PortA = 0x04 (CE low, Write data to RAM command)


    ld      r1,     0x21        ; !
    str     r1,     r2,     #3  ; PortB = '!'

    ld      r0,     0x05
    str     r0,     r2,     #2  ; PortA = 0x05 (CE high, Write data to RAM command)
    ld      r0,     0x04
    str     r0,     r2,     #2  ; PortA = 0x04 (CE low, Write data to RAM command)

    pause
_INF_LP:
    j       _INF_LP