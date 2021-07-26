.DEFAULT_GOAL 	= all

BASE 			:= $(PWD)
UTIL_DIR 		:= $(BASE)/Utils
WORK_DIR		:= $(UTIL_DIR)/work
SRC_DIR			:= $(BASE)/Programs
PROG_DIR		:= C:/cygwin64/home/jack/minipro
PROG_CHIP		= AT28C256
UCODE_CHIP		= AT28C64B
NUM_MICROCODE_ROMS	= 5

obj_files 		= OSR.bin HelloWorld.bin

all: workspace $(obj_files) merge

$(filter %.bin,$(obj_files)): %.bin: %.asm
	py $(UTIL_DIR)/asm.py -c $(SRC_DIR)/$< -o $(WORK_DIR)/$@
	
workspace:
	[ -d $(WORK_DIR) ] || mkdir $(WORK_DIR)

merge:
	cd $(WORK_DIR); py $(UTIL_DIR)/merge.py -m $(obj_files) -o $(WORK_DIR)/a.bin; cp $(WORK_DIR)/a.bin $(PROG_DIR)/binaries/a.bin;

progc:
	$(PROG_DIR)/minipro.exe -w $(PROG_CHIP) -p $(PROG_DIR)/binaries/a.bin;


pml:
	count=$(NUM_MICROCODE_ROMS); while [[ $$count -gt 0 ]] ; do \
		$(PROG_DIR)/minipro.exe -w $(UCODE_CHIP) -p $(PROG_DIR)/binaries/microcode.bin ; \
		((count = count - 1)) ; \
		read -p "Press any key to continue ($(count) ROMs remaining)" -n 1 -s -r ; \
	done
	
pm:
	$(PROG_DIR)/minipro.exe -w $(UCODE_CHIP) -p $(PROG_DIR)/binaries/microcode.bin ;

ucode:
	py $(UTIL_DIR)/ucode_gen.py; cp $(UTIL_DIR)/microcode.bin $(PROG_DIR)/binaries/microcode.bin;

.PHONY: clean

clean:
	if [ -d "$(WORK_DIR)" ]; then \
		rm -r $(WORK_DIR); \
	fi

	if [ -d "$(UTIL_DIR)/__pycache__" ]; then \
		rm -r $(UTIL_DIR)/__pycache__; \
	fi
