import asm
import merge


def main():
    asm.Assemble(r"OSR.asm", r"OSR.bin")
    asm.Assemble(r"HelloWorld.asm", r"HelloWorld.bin")
    merge.Merge([r"OSR.bin", r"HelloWorld.bin"], r"Program_01_Hello!.bin")

if __name__ == "__main__":
    main()