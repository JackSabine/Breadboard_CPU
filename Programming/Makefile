.DEFAULT_GOAL 	= all

BASE 			:= $(PWD)
UTIL_DIR 		:= $(BASE)/Assembler/v1_1
WORK_DIR		:= $(UTIL_DIR)/work
SRC_DIR			:= $(BASE)/Programs
PROG_DIR		:= C:/cygwin64/home/jack/minipro
PROG_CHIP		= AT28C256
UCODE_CHIP		= AT28C64B
NUM_MICROCODE_ROMS	= 5

obj_files 		= OSR_1_1.bin HelloWorld_1_1.bin

all: workspace $(obj_files) merge

$(filter %.bin,$(obj_files)): %.bin: $(SRC_DIR)/%.asm
	py $(UTIL_DIR)/asm.py -c $< -o $(WORK_DIR)/$@
	
workspace:
	@[ -d $(WORK_DIR) ] || mkdir $(WORK_DIR)

# Merge two binaries
merge:
	cd $(WORK_DIR); py $(UTIL_DIR)/merge.py -m $(obj_files) -o $(WORK_DIR)/a.bin; cp $(WORK_DIR)/a.bin $(PROG_DIR)/binaries/a.bin;

# Write the program binary to the program NVRAM
progc:
	@cd $(PROG_DIR) ; \
	./minipro.exe -p $(PROG_CHIP) -w binaries/a.bin;

# Program microcode loop
pml:
	@cd $(PROG_DIR) ; \
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
	@cd $(PROG_DIR) ; \
	./minipro.exe -p $(UCODE_CHIP) -w binaries/microcode.bin

# Generate microcode binary and move to programmer directory
ucode: workspace
	@py $(UTIL_DIR)/ucode_gen.py -o $(WORK_DIR)/microcode.bin; cp $(WORK_DIR)/microcode.bin $(PROG_DIR)/binaries/microcode.bin;

.PHONY: clean

clean:
	@if [ -d "$(WORK_DIR)" ]; then \
		rm -r $(WORK_DIR); \
	fi

	@if [ -d "$(UTIL_DIR)/__pycache__" ]; then \
		rm -r $(UTIL_DIR)/__pycache__; \
	fi
