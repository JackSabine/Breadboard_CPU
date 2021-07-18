.ORIG 0x0400

fibonacci:
    ld      r0,         #0
    ld      r2,         0x00
    ld      r3,         0xFF
    str     r0,         r2,     #1
_fib_RST:
    ld      r0,         #0
    ld      r1,         #1
    str     r0,         r2,     #3
_fib_LP:
    add     r1,         r0
    jo      _fib_RST
    str     r1,         r2,     #3
    add     r0,         r1
    jo      _fib_RST
    str     r0,         r2,     #3
    j       _fib_LP