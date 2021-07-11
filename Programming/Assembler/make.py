import asm
import merge


def main():
    asm.Assemble(r"OSR.asm", r"OSR.bin")
    asm.Assemble(r"Programs/Fibonacci.asm", r"Fib.bin")
    merge.Merge([r"OSR.bin", r"Fib.bin"], r"Program_00.bin")

if __name__ == "__main__":
    main()