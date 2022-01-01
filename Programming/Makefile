.DEFAULT_GOAL 	= all

BASE 			:= $(PWD)
ASSEMBLER_DIR 	:= $(BASE)/Assembler/v1_1
WORK_DIR		:= $(ASSEMBLER_DIR)/work
SRC_DIR			:= $(BASE)/Programs
PROGRAMMER_DIR	:= C:/cygwin64/home/jack/minipro
PROG_CHIP		= AT28C256
UCODE_CHIP		= AT28C64B
NUM_MICROCODE_ROMS	= 5

obj_files 		= OSR_1_1.bin HelloWorld_1_1.bin

all: workspace $(obj_files) merge

$(filter %.bin,$(obj_files)): %.bin: $(SRC_DIR)/%.asm
	py $(ASSEMBLER_DIR)/asm.py -c $< -o $(WORK_DIR)/$@
	
workspace:
	@[ -d $(WORK_DIR) ] || mkdir $(WORK_DIR)

# Merge two binaries
merge:
	cd $(WORK_DIR); py $(ASSEMBLER_DIR)/merge.py -m $(obj_files) -o $(WORK_DIR)/a.bin; cp $(WORK_DIR)/a.bin $(PROGRAMMER_DIR)/binaries/a.bin;

# Write the program binary to the program NVRAM
progc:
	@cd $(PROGRAMMER_DIR) ; \
	./minipro.exe -p $(PROG_CHIP) -w binaries/a.bin;

# Program microcode loop
pml:
	@cd $(PROGRAMMER_DIR) ; \
	while [ true ] ; do \
		./minipro.exe -p $(UCODE_CHIP) -w binaries/microcode.bin; \
		read -n 1 -s -r -p "Press any key to continue ('q' to exit)" key; \
		if [ $$key = 'q' ]; then \
			exit ; \
		fi ; \
		echo ; \
	done

# Program microcode
pm:
	@cd $(PROGRAMMER_DIR) ; \
	./minipro.exe -p $(UCODE_CHIP) -w binaries/microcode.bin

# Generate microcode binary and move to programmer directory
ucode: workspace
	@py $(ASSEMBLER_DIR)/ucode_gen.py -o $(WORK_DIR)/microcode.bin; cp $(WORK_DIR)/microcode.bin $(PROGRAMMER_DIR)/binaries/microcode.bin;

# Run the decoder on the output binary a.bin
dec:
	@py $(ASSEMBLER_DIR)/inst_decoder.py -b $(WORK_DIR)/a.bin -o $(WORK_DIR)/Decoded.txt

.PHONY: clean

clean:
	@if [ -d "$(WORK_DIR)" ]; then \
		rm -r $(WORK_DIR); \
	fi

	@if [ -d "$(ASSEMBLER_DIR)/__pycache__" ]; then \
		rm -r $(ASSEMBLER_DIR)/__pycache__; \
	fi
