.ORIG 0x0400

fibonacci:
    ld      r0,         #0
    ld      vari,         0x00
    ld      r3,         0xFF
    str     r0,         vari,     #1
_fib_RST:
    ld      r0,         #0
    ld      r1,         #1
    str     r0,         vari,     #3
_fib_LP:
    add     r1,         r0
    jc      _fib_RST
    str     r1,         vari,     #3
    add     r0,         r1
    jc      _fib_RST
    str     r0,         vari,     #3
    j       _fib_LP