.DEFAULT_GOAL 	= all

BASE 			:= $(PWD)
UTIL_DIR 		:= $(BASE)/Utils
WORK_DIR		:= $(UTIL_DIR)/work
SRC_DIR			:= $(BASE)/Programs
PROG_DIR		:= C:/cygwin64/home/jack/minipro
CHIP_NAME		= AT28C256

obj_files 		= OSR.bin HelloWorld.bin

all: workspace $(obj_files)

$(filter %.bin,$(obj_files)): %.bin: %.asm
	py $(UTIL_DIR)/asm.py -c $(SRC_DIR)/$< -o $(WORK_DIR)/$@
	
workspace:
	[ -d $(WORK_DIR) ] || mkdir $(WORK_DIR)

compile:
	mkdir $(ASSEMBLER_DIR)/work; py $(ASSEMBLER_DIR)/asm.py -c $(OS_FILES) $(SRC_FILES) -o $(WORK_DIR); 
	
merge:
	py $(ASSEMBLER_DIR)/merge.py -m  -o $(WORK_DIR)/a.bin;

prog:
	mv $(WORK_DIR)/a.bin $(PROG_DIR)/binaries; $(PROG_DIR)/minipro.exe -w $(CHIP_NAME) -p $(PROG_DIR)/binaries/a.bin;

do_all: compile merge

.PHONY: clean

clean:
	if [ -d "$(WORK_DIR)" ]; then \
        rm -r $(WORK_DIR); \
	fi