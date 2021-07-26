.DEFAULT_GOAL 	= all

BASE 			:= $(PWD)
UTIL_DIR 		:= $(BASE)/Utils
WORK_DIR		:= $(UTIL_DIR)/work
SRC_DIR			:= $(BASE)/Programs
PROG_DIR		:= C:/cygwin64/home/jack/minipro
CHIP_NAME		= AT28C256

obj_files 		= OSR.bin HelloWorld.bin

all: workspace $(obj_files) merge

$(filter %.bin,$(obj_files)): %.bin: %.asm
	py $(UTIL_DIR)/asm.py -c $(SRC_DIR)/$< -o $(WORK_DIR)/$@
	
workspace:
	[ -d $(WORK_DIR) ] || mkdir $(WORK_DIR)
	
merge:
	cd $(WORK_DIR); py $(UTIL_DIR)/merge.py -m $(obj_files) -o $(WORK_DIR)/a.bin;

prog:
	mv $(WORK_DIR)/a.bin $(PROG_DIR)/binaries; $(PROG_DIR)/minipro.exe -w $(CHIP_NAME) -p $(PROG_DIR)/binaries/a.bin;

.PHONY: clean

clean:
	if [ -d "$(WORK_DIR)" ]; then \
        rm -r $(WORK_DIR); \
	fi

	if [ -d "$(UTIL_DIR)/__pycache__" ]; then \
		rm -r $(UTIL_DIR)/__pycache__; \
	fi