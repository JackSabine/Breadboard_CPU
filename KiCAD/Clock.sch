EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A3 16535 11693
encoding utf-8
Sheet 3 9
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L Breadboard_CPU-rescue:LM555-Timer U?
U 1 1 5F00FC3F
P 3100 2000
AR Path="/5F00FC3F" Ref="U?"  Part="1" 
AR Path="/5EFC09F3/5F00FC3F" Ref="U303"  Part="1" 
F 0 "U303" H 3200 2450 50  0000 C CNN
F 1 "LM555" H 3250 2350 50  0000 C CNN
F 2 "" H 3100 2000 50  0001 C CNN
F 3 "http://www.ti.com/lit/ds/symlink/lm555.pdf" H 3100 2000 50  0001 C CNN
	1    3100 2000
	1    0    0    -1  
$EndComp
$Comp
L Breadboard_CPU-rescue:LM555-Timer U?
U 1 1 5F010A80
P 3100 4150
AR Path="/5F010A80" Ref="U?"  Part="1" 
AR Path="/5EFC09F3/5F010A80" Ref="U304"  Part="1" 
F 0 "U304" H 3200 4600 50  0000 C CNN
F 1 "LM555" H 3250 4500 50  0000 C CNN
F 2 "" H 3100 4150 50  0001 C CNN
F 3 "http://www.ti.com/lit/ds/symlink/lm555.pdf" H 3100 4150 50  0001 C CNN
	1    3100 4150
	1    0    0    -1  
$EndComp
$Comp
L Breadboard_CPU-rescue:R-Device R301
U 1 1 5F0141BE
P 2500 3750
F 0 "R301" H 2570 3796 50  0000 L CNN
F 1 "4.7k" H 2570 3705 50  0000 L CNN
F 2 "" V 2430 3750 50  0001 C CNN
F 3 "~" H 2500 3750 50  0001 C CNN
	1    2500 3750
	1    0    0    -1  
$EndComp
$Comp
L Breadboard_CPU-rescue:C_Small-Device C308
U 1 1 5F0158C4
P 4050 2550
F 0 "C308" H 4142 2596 50  0000 L CNN
F 1 "4.7u" H 4142 2505 50  0000 L CNN
F 2 "" H 4050 2550 50  0001 C CNN
F 3 "~" H 4050 2550 50  0001 C CNN
	1    4050 2550
	1    0    0    -1  
$EndComp
$Comp
L Breadboard_CPU-rescue:R-Device R303
U 1 1 5F015E4C
P 3750 3750
F 0 "R303" H 3820 3796 50  0000 L CNN
F 1 "1M" H 3820 3705 50  0000 L CNN
F 2 "" V 3680 3750 50  0001 C CNN
F 3 "~" H 3750 3750 50  0001 C CNN
	1    3750 3750
	1    0    0    -1  
$EndComp
$Comp
L Breadboard_CPU-rescue:R-Device R306
U 1 1 5F017222
P 4650 2000
F 0 "R306" H 4720 2046 50  0000 L CNN
F 1 "4.7k" H 4720 1955 50  0000 L CNN
F 2 "" V 4580 2000 50  0001 C CNN
F 3 "~" H 4650 2000 50  0001 C CNN
	1    4650 2000
	1    0    0    -1  
$EndComp
$Comp
L Breadboard_CPU-rescue:C_Small-Device C304
U 1 1 5F0180E8
P 2050 2200
F 0 "C304" H 2142 2246 50  0000 L CNN
F 1 "0.1u" H 2142 2155 50  0000 L CNN
F 2 "" H 2050 2200 50  0001 C CNN
F 3 "~" H 2050 2200 50  0001 C CNN
	1    2050 2200
	1    0    0    -1  
$EndComp
Wire Wire Line
	2050 2100 2050 2000
Wire Wire Line
	2050 2000 2600 2000
Wire Wire Line
	2050 2300 2050 2700
Wire Wire Line
	2050 2700 3100 2700
Wire Wire Line
	3100 2400 3100 2700
Connection ~ 3100 2700
$Comp
L Breadboard_CPU-rescue:R-Device R304
U 1 1 5F019A19
P 3950 2000
F 0 "R304" V 4157 2000 50  0000 C CNN
F 1 "1000" V 4066 2000 50  0000 C CNN
F 2 "" V 3880 2000 50  0001 C CNN
F 3 "~" H 3950 2000 50  0001 C CNN
	1    3950 2000
	0    1    1    0   
$EndComp
$Comp
L Breadboard_CPU-rescue:R-Device R302
U 1 1 5F01AE8F
P 3750 1550
F 0 "R302" H 3820 1596 50  0000 L CNN
F 1 "1000" H 3820 1505 50  0000 L CNN
F 2 "" V 3680 1550 50  0001 C CNN
F 3 "~" H 3750 1550 50  0001 C CNN
F 4 "Two 1.8k's in series" H 3750 1550 50  0001 C CNN "Note"
	1    3750 1550
	1    0    0    -1  
$EndComp
Wire Wire Line
	2300 1350 2300 2200
Wire Wire Line
	2300 2200 2600 2200
Wire Wire Line
	3100 1200 3100 1350
Wire Wire Line
	2600 1800 2550 1800
Wire Wire Line
	2550 1800 2550 2500
Wire Wire Line
	3600 2200 3650 2200
Wire Wire Line
	3650 2200 3650 2400
Wire Wire Line
	2550 2500 3650 2500
Wire Wire Line
	3100 1350 3750 1350
Wire Wire Line
	3750 1350 3750 1400
Connection ~ 3100 1350
Wire Wire Line
	3750 1700 3750 2000
Wire Wire Line
	3750 2000 3600 2000
Wire Wire Line
	4250 2000 4100 2000
Connection ~ 3750 2000
Wire Wire Line
	3800 2000 3750 2000
Wire Wire Line
	4250 2000 4250 2050
Connection ~ 3650 2400
Wire Wire Line
	3650 2400 3650 2500
Wire Wire Line
	4450 2200 4400 2200
$Comp
L Breadboard_CPU-rescue:LED-Device D302
U 1 1 5F022248
P 4650 2400
F 0 "D302" V 4689 2283 50  0000 R CNN
F 1 "Blue" V 4598 2283 50  0000 R CNN
F 2 "" H 4650 2400 50  0001 C CNN
F 3 "~" H 4650 2400 50  0001 C CNN
	1    4650 2400
	0    -1   -1   0   
$EndComp
Wire Wire Line
	4650 2150 4650 2250
Wire Wire Line
	4650 2550 4650 2700
Wire Wire Line
	3600 1800 4650 1800
Wire Wire Line
	4650 1800 4650 1850
Wire Wire Line
	4650 1800 4750 1800
Connection ~ 4650 1800
Wire Wire Line
	3100 2700 4050 2700
Wire Wire Line
	4050 2400 4050 2450
Wire Wire Line
	4050 2650 4050 2700
Connection ~ 4050 2700
Wire Wire Line
	4050 2700 4650 2700
Wire Wire Line
	3650 2400 4050 2400
Wire Wire Line
	4100 2200 4050 2200
Wire Wire Line
	4050 2200 4050 2400
Connection ~ 4050 2400
$Comp
L Breadboard_CPU-rescue:R_POT-Device RV301
U 1 1 5F01B3E1
P 4250 2200
F 0 "RV301" V 4150 2250 50  0000 R CNN
F 1 "0-10k" V 4050 2300 50  0000 R CNN
F 2 "" H 4250 2200 50  0001 C CNN
F 3 "~" H 4250 2200 50  0001 C CNN
	1    4250 2200
	0    -1   -1   0   
$EndComp
$Comp
L Breadboard_CPU-rescue:GND-power #PWR0305
U 1 1 5F031B94
P 3100 2800
F 0 "#PWR0305" H 3100 2550 50  0001 C CNN
F 1 "GND" H 3105 2627 50  0000 C CNN
F 2 "" H 3100 2800 50  0001 C CNN
F 3 "" H 3100 2800 50  0001 C CNN
	1    3100 2800
	1    0    0    -1  
$EndComp
Wire Wire Line
	3100 2700 3100 2800
Wire Wire Line
	2600 4350 2300 4350
Wire Wire Line
	2300 4350 2300 3500
Wire Wire Line
	2300 3500 2500 3500
Wire Wire Line
	3100 3500 3100 3350
Wire Wire Line
	3600 4150 3750 4150
Wire Wire Line
	3750 4150 3750 4350
Wire Wire Line
	3750 4350 3600 4350
$Comp
L Breadboard_CPU-rescue:C_Small-Device C305
U 1 1 5F045E40
P 2050 4350
F 0 "C305" H 2142 4396 50  0000 L CNN
F 1 "0.1u" H 2142 4305 50  0000 L CNN
F 2 "" H 2050 4350 50  0001 C CNN
F 3 "~" H 2050 4350 50  0001 C CNN
	1    2050 4350
	1    0    0    -1  
$EndComp
Wire Wire Line
	2050 4250 2050 4150
Wire Wire Line
	2050 4150 2600 4150
$Comp
L Breadboard_CPU-rescue:C_Small-Device C307
U 1 1 5F0477B9
P 3750 4500
F 0 "C307" H 3842 4546 50  0000 L CNN
F 1 "0.1u" H 3842 4455 50  0000 L CNN
F 2 "" H 3750 4500 50  0001 C CNN
F 3 "~" H 3750 4500 50  0001 C CNN
	1    3750 4500
	1    0    0    -1  
$EndComp
Wire Wire Line
	3750 4350 3750 4400
Connection ~ 3750 4350
Wire Wire Line
	3750 3900 3750 4150
Connection ~ 3750 4150
$Comp
L Breadboard_CPU-rescue:SW_Push-Switch SW301
U 1 1 5F04F258
P 2050 3950
F 0 "SW301" H 2050 4235 50  0000 C CNN
F 1 "PULSE_CLK" H 2050 4144 50  0000 C CNN
F 2 "" H 2050 4150 50  0001 C CNN
F 3 "~" H 2050 4150 50  0001 C CNN
	1    2050 3950
	1    0    0    -1  
$EndComp
Wire Wire Line
	2500 3600 2500 3500
Connection ~ 2500 3500
Wire Wire Line
	2500 3500 3100 3500
Wire Wire Line
	2500 3900 2500 3950
Wire Wire Line
	2500 3950 2600 3950
Wire Wire Line
	2250 3950 2500 3950
Connection ~ 2500 3950
Wire Wire Line
	3100 3500 3750 3500
Wire Wire Line
	3750 3500 3750 3600
Connection ~ 3100 3500
$Comp
L Breadboard_CPU-rescue:GND-power #PWR0301
U 1 1 5F0555E2
P 1800 4000
F 0 "#PWR0301" H 1800 3750 50  0001 C CNN
F 1 "GND" H 1805 3827 50  0000 C CNN
F 2 "" H 1800 4000 50  0001 C CNN
F 3 "" H 1800 4000 50  0001 C CNN
	1    1800 4000
	1    0    0    -1  
$EndComp
Wire Wire Line
	1850 3950 1800 3950
Wire Wire Line
	1800 3950 1800 4000
$Comp
L Breadboard_CPU-rescue:R-Device R305
U 1 1 5F061991
P 4200 4150
F 0 "R305" H 4270 4196 50  0000 L CNN
F 1 "4.7k" H 4270 4105 50  0000 L CNN
F 2 "" V 4130 4150 50  0001 C CNN
F 3 "~" H 4200 4150 50  0001 C CNN
	1    4200 4150
	1    0    0    -1  
$EndComp
Wire Wire Line
	3600 3950 4200 3950
Wire Wire Line
	4200 3950 4200 4000
Wire Wire Line
	4200 3950 4300 3950
Connection ~ 4200 3950
Wire Wire Line
	2050 4700 3100 4700
Wire Wire Line
	2050 4450 2050 4700
Connection ~ 3100 4700
Wire Wire Line
	3100 4550 3100 4700
Wire Wire Line
	3100 4700 3100 4750
Wire Wire Line
	3750 4700 3100 4700
Wire Wire Line
	3750 4600 3750 4700
$Comp
L Breadboard_CPU-rescue:GND-power #PWR0307
U 1 1 5F056C27
P 3100 4750
F 0 "#PWR0307" H 3100 4500 50  0001 C CNN
F 1 "GND" H 3105 4577 50  0000 C CNN
F 2 "" H 3100 4750 50  0001 C CNN
F 3 "" H 3100 4750 50  0001 C CNN
	1    3100 4750
	1    0    0    -1  
$EndComp
Wire Wire Line
	4200 4300 4200 4350
Wire Wire Line
	4200 4650 4200 4700
$Comp
L Breadboard_CPU-rescue:LED-Device D301
U 1 1 5F061998
P 4200 4500
F 0 "D301" V 4239 4383 50  0000 R CNN
F 1 "Blue" V 4148 4383 50  0000 R CNN
F 2 "" H 4200 4500 50  0001 C CNN
F 3 "~" H 4200 4500 50  0001 C CNN
	1    4200 4500
	0    -1   -1   0   
$EndComp
Wire Wire Line
	3750 4700 4200 4700
Connection ~ 3750 4700
$Comp
L Breadboard_CPU-rescue:74LS32-74xx U301
U 1 1 5F17E838
P 12725 3225
F 0 "U301" H 12725 3550 50  0000 C CNN
F 1 "74HCT32N" H 12725 3459 50  0000 C CNN
F 2 "" H 12725 3225 50  0001 C CNN
F 3 "http://www.ti.com/lit/gpn/sn74LS32" H 12725 3225 50  0001 C CNN
	1    12725 3225
	1    0    0    -1  
$EndComp
$Comp
L Breadboard_CPU-rescue:R-Device R310
U 1 1 5F1F0144
P 14725 3425
F 0 "R310" H 14795 3471 50  0000 L CNN
F 1 "4.7k" H 14795 3380 50  0000 L CNN
F 2 "" V 14655 3425 50  0001 C CNN
F 3 "~" H 14725 3425 50  0001 C CNN
	1    14725 3425
	1    0    0    -1  
$EndComp
$Comp
L Breadboard_CPU-rescue:LED-Device D303
U 1 1 5F1F1588
P 14725 3775
F 0 "D303" V 14764 3658 50  0000 R CNN
F 1 "LED" V 14673 3658 50  0000 R CNN
F 2 "" H 14725 3775 50  0001 C CNN
F 3 "~" H 14725 3775 50  0001 C CNN
	1    14725 3775
	0    -1   -1   0   
$EndComp
$Comp
L Breadboard_CPU-rescue:GND-power #PWR0314
U 1 1 5F1F225D
P 14725 3975
F 0 "#PWR0314" H 14725 3725 50  0001 C CNN
F 1 "GND" H 14730 3802 50  0000 C CNN
F 2 "" H 14725 3975 50  0001 C CNN
F 3 "" H 14725 3975 50  0001 C CNN
	1    14725 3975
	1    0    0    -1  
$EndComp
Wire Wire Line
	14725 3975 14725 3925
Wire Wire Line
	14725 3625 14725 3575
$Comp
L Breadboard_CPU-rescue:74LS32-74xx U301
U 5 1 5F204533
P 2600 6125
F 0 "U301" H 2830 6171 50  0000 L CNN
F 1 "74HCT32N" H 2830 6080 50  0000 L CNN
F 2 "" H 2600 6125 50  0001 C CNN
F 3 "http://www.ti.com/lit/gpn/sn74LS32" H 2600 6125 50  0001 C CNN
	5    2600 6125
	1    0    0    -1  
$EndComp
Wire Wire Line
	2600 6675 2600 6625
Text HLabel 8375 3325 0    50   Input ~ 0
HALT_A
Text HLabel 14875 3225 2    50   Output ~ 0
CLK
Text HLabel 14875 2575 2    50   Output ~ 0
~CLK
Wire Wire Line
	3100 3750 3100 3500
Wire Wire Line
	2300 1350 3100 1350
Text HLabel 8375 3425 0    50   Input ~ 0
HALT_B
$Comp
L Breadboard_CPU-rescue:74LS32-74xx U301
U 2 1 5FB8BB70
P 11950 3125
F 0 "U301" H 12025 3450 50  0000 R CNN
F 1 "74HCT32N" H 12150 3350 50  0000 R CNN
F 2 "" H 11950 3125 50  0001 C CNN
F 3 "http://www.ti.com/lit/gpn/sn74LS32" H 11950 3125 50  0001 C CNN
	2    11950 3125
	1    0    0    -1  
$EndComp
$Comp
L Breadboard_CPU-rescue:74LS32-74xx U301
U 3 1 5FBACFE5
P 12775 4775
F 0 "U301" H 12775 5100 50  0000 C CNN
F 1 "74HCT32N" H 12775 5009 50  0000 C CNN
F 2 "" H 12775 4775 50  0001 C CNN
F 3 "http://www.ti.com/lit/gpn/sn74LS32" H 12775 4775 50  0001 C CNN
	3    12775 4775
	1    0    0    -1  
$EndComp
$Comp
L Breadboard_CPU-rescue:74LS32-74xx U301
U 4 1 5FBAEB0C
P 11950 3875
F 0 "U301" H 11950 4200 50  0000 C CNN
F 1 "74HCT32N" H 11950 4109 50  0000 C CNN
F 2 "" H 11950 3875 50  0001 C CNN
F 3 "http://www.ti.com/lit/gpn/sn74LS32" H 11950 3875 50  0001 C CNN
	4    11950 3875
	1    0    0    -1  
$EndComp
Text Notes 5325 1625 2    118  ~ 0
Astable clock
Text Notes 3900 3525 0    118  ~ 0
Debounced button
Text Notes 15425 1675 2    118  ~ 0
Clock selector
$Comp
L Breadboard_CPU-rescue:74LS08-74xx U?
U 1 1 617D15EB
P 11175 2625
AR Path="/5EFC06D4/617D15EB" Ref="U?"  Part="1" 
AR Path="/5EFC09F3/617D15EB" Ref="U305"  Part="1" 
F 0 "U305" H 11175 2950 50  0000 C CNN
F 1 "74HCT08N" H 11175 2859 50  0000 C CNN
F 2 "" H 11175 2625 50  0001 C CNN
F 3 "http://www.ti.com/lit/gpn/sn74LS08" H 11175 2625 50  0001 C CNN
	1    11175 2625
	1    0    0    -1  
$EndComp
$Comp
L Breadboard_CPU-rescue:74LS08-74xx U?
U 2 1 617D15F1
P 11175 3225
AR Path="/5EFC06D4/617D15F1" Ref="U?"  Part="2" 
AR Path="/5EFC09F3/617D15F1" Ref="U305"  Part="2" 
F 0 "U305" H 11175 3550 50  0000 C CNN
F 1 "74HCT08N" H 11175 3459 50  0000 C CNN
F 2 "" H 11175 3225 50  0001 C CNN
F 3 "http://www.ti.com/lit/gpn/sn74LS08" H 11175 3225 50  0001 C CNN
	2    11175 3225
	1    0    0    -1  
$EndComp
$Comp
L Breadboard_CPU-rescue:74LS08-74xx U?
U 3 1 617D15F7
P 11175 3775
AR Path="/5EFC06D4/617D15F7" Ref="U?"  Part="3" 
AR Path="/5EFC09F3/617D15F7" Ref="U305"  Part="3" 
F 0 "U305" H 11175 4100 50  0000 C CNN
F 1 "74HCT08N" H 11175 4009 50  0000 C CNN
F 2 "" H 11175 3775 50  0001 C CNN
F 3 "http://www.ti.com/lit/gpn/sn74LS08" H 11175 3775 50  0001 C CNN
	3    11175 3775
	1    0    0    -1  
$EndComp
$Comp
L Breadboard_CPU-rescue:74LS08-74xx U?
U 4 1 617D15FD
P 11175 4325
AR Path="/5EFC06D4/617D15FD" Ref="U?"  Part="4" 
AR Path="/5EFC09F3/617D15FD" Ref="U305"  Part="4" 
F 0 "U305" H 11175 4650 50  0000 C CNN
F 1 "74HCT08N" H 11175 4559 50  0000 C CNN
F 2 "" H 11175 4325 50  0001 C CNN
F 3 "http://www.ti.com/lit/gpn/sn74LS08" H 11175 4325 50  0001 C CNN
	4    11175 4325
	1    0    0    -1  
$EndComp
$Comp
L Breadboard_CPU-rescue:74LS08-74xx U?
U 5 1 617D1603
P 4275 6100
AR Path="/5EFC06D4/617D1603" Ref="U?"  Part="5" 
AR Path="/5EFC09F3/617D1603" Ref="U305"  Part="5" 
F 0 "U305" H 4505 6146 50  0000 L CNN
F 1 "74HCT08N" H 4505 6055 50  0000 L CNN
F 2 "" H 4275 6100 50  0001 C CNN
F 3 "http://www.ti.com/lit/gpn/sn74LS08" H 4275 6100 50  0001 C CNN
	5    4275 6100
	1    0    0    -1  
$EndComp
$Comp
L Breadboard_CPU-rescue:GND-power #PWR?
U 1 1 617D1615
P 4275 6725
AR Path="/5EFC06D4/617D1615" Ref="#PWR?"  Part="1" 
AR Path="/5EFC09F3/617D1615" Ref="#PWR0311"  Part="1" 
F 0 "#PWR0311" H 4275 6475 50  0001 C CNN
F 1 "GND" H 4280 6552 50  0000 C CNN
F 2 "" H 4275 6725 50  0001 C CNN
F 3 "" H 4275 6725 50  0001 C CNN
	1    4275 6725
	1    0    0    -1  
$EndComp
$Comp
L Breadboard_CPU-rescue:74LS04-74xx U?
U 7 1 62D47ABF
P 3475 6100
AR Path="/5F05F116/62D47ABF" Ref="U?"  Part="7" 
AR Path="/5EFC09F3/62D47ABF" Ref="U302"  Part="7" 
F 0 "U302" H 3705 6146 50  0000 L CNN
F 1 "74LS04" H 3705 6055 50  0000 L CNN
F 2 "" H 3475 6100 50  0001 C CNN
F 3 "http://www.ti.com/lit/gpn/sn74LS04" H 3475 6100 50  0001 C CNN
	7    3475 6100
	1    0    0    -1  
$EndComp
$Comp
L Breadboard_CPU-rescue:74LS04-74xx U?
U 6 1 62D47AC9
P 10300 3325
AR Path="/5F05F116/62D47AC9" Ref="U?"  Part="6" 
AR Path="/5EFC09F3/62D47AC9" Ref="U302"  Part="6" 
F 0 "U302" H 10300 3642 50  0000 C CNN
F 1 "74LS04" H 10300 3551 50  0000 C CNN
F 2 "" H 10300 3325 50  0001 C CNN
F 3 "http://www.ti.com/lit/gpn/sn74LS04" H 10300 3325 50  0001 C CNN
	6    10300 3325
	1    0    0    -1  
$EndComp
$Comp
L Breadboard_CPU-rescue:74LS04-74xx U?
U 5 1 62D47ACF
P 10300 4425
AR Path="/5F05F116/62D47ACF" Ref="U?"  Part="5" 
AR Path="/5EFC09F3/62D47ACF" Ref="U302"  Part="5" 
F 0 "U302" H 10300 4742 50  0000 C CNN
F 1 "74LS04" H 10300 4651 50  0000 C CNN
F 2 "" H 10300 4425 50  0001 C CNN
F 3 "http://www.ti.com/lit/gpn/sn74LS04" H 10300 4425 50  0001 C CNN
	5    10300 4425
	1    0    0    -1  
$EndComp
$Comp
L Breadboard_CPU-rescue:74LS04-74xx U?
U 4 1 62D47AD5
P 10300 3875
AR Path="/5F05F116/62D47AD5" Ref="U?"  Part="4" 
AR Path="/5EFC09F3/62D47AD5" Ref="U302"  Part="4" 
F 0 "U302" H 10300 4192 50  0000 C CNN
F 1 "74LS04" H 10300 4101 50  0000 C CNN
F 2 "" H 10300 3875 50  0001 C CNN
F 3 "http://www.ti.com/lit/gpn/sn74LS04" H 10300 3875 50  0001 C CNN
	4    10300 3875
	1    0    0    -1  
$EndComp
$Comp
L Breadboard_CPU-rescue:74LS04-74xx U?
U 3 1 62D47ADB
P 10300 2725
AR Path="/5F05F116/62D47ADB" Ref="U?"  Part="3" 
AR Path="/5EFC09F3/62D47ADB" Ref="U302"  Part="3" 
F 0 "U302" H 10300 3042 50  0000 C CNN
F 1 "74LS04" H 10300 2951 50  0000 C CNN
F 2 "" H 10300 2725 50  0001 C CNN
F 3 "http://www.ti.com/lit/gpn/sn74LS04" H 10300 2725 50  0001 C CNN
	3    10300 2725
	1    0    0    -1  
$EndComp
$Comp
L Breadboard_CPU-rescue:74LS04-74xx U?
U 2 1 62D47AE1
P 13500 3225
AR Path="/5F05F116/62D47AE1" Ref="U?"  Part="2" 
AR Path="/5EFC09F3/62D47AE1" Ref="U302"  Part="2" 
F 0 "U302" H 13500 3542 50  0000 C CNN
F 1 "74LS04" H 13500 3451 50  0000 C CNN
F 2 "" H 13500 3225 50  0001 C CNN
F 3 "http://www.ti.com/lit/gpn/sn74LS04" H 13500 3225 50  0001 C CNN
	2    13500 3225
	1    0    0    -1  
$EndComp
$Comp
L Breadboard_CPU-rescue:74LS04-74xx U?
U 1 1 62D47AE7
P 14300 3225
AR Path="/5F05F116/62D47AE7" Ref="U?"  Part="1" 
AR Path="/5EFC09F3/62D47AE7" Ref="U302"  Part="1" 
F 0 "U302" H 14300 3542 50  0000 C CNN
F 1 "74LS04" H 14300 3451 50  0000 C CNN
F 2 "" H 14300 3225 50  0001 C CNN
F 3 "http://www.ti.com/lit/gpn/sn74LS04" H 14300 3225 50  0001 C CNN
	1    14300 3225
	1    0    0    -1  
$EndComp
$Comp
L 74xx:74LS138 U?
U 1 1 60D9114B
P 8925 3025
F 0 "U?" H 9025 3575 50  0000 C CNN
F 1 "74LS138" H 9125 3475 50  0000 C CNN
F 2 "" H 8925 3025 50  0001 C CNN
F 3 "http://www.ti.com/lit/gpn/sn74LS138" H 8925 3025 50  0001 C CNN
	1    8925 3025
	1    0    0    -1  
$EndComp
$Comp
L Device:R R?
U 1 1 60DA54FE
P 7825 3125
F 0 "R?" H 7895 3171 50  0000 L CNN
F 1 "1k" H 7895 3080 50  0000 L CNN
F 2 "" V 7755 3125 50  0001 C CNN
F 3 "~" H 7825 3125 50  0001 C CNN
	1    7825 3125
	1    0    0    -1  
$EndComp
Wire Wire Line
	8425 3225 8375 3225
Wire Wire Line
	8375 3225 8375 2375
Wire Wire Line
	8375 2375 8925 2375
Wire Wire Line
	8925 2375 8925 2425
Wire Wire Line
	8425 2925 7825 2925
Wire Wire Line
	7825 2925 7825 2975
Wire Wire Line
	8925 3775 8925 3725
Wire Wire Line
	8925 3775 8925 3825
Connection ~ 8925 3775
Wire Wire Line
	8925 2375 8925 2325
Connection ~ 8925 2375
$Comp
L power:GND #PWR?
U 1 1 60DF0A3A
P 8925 3825
F 0 "#PWR?" H 8925 3575 50  0001 C CNN
F 1 "GND" H 8930 3652 50  0000 C CNN
F 2 "" H 8925 3825 50  0001 C CNN
F 3 "" H 8925 3825 50  0001 C CNN
	1    8925 3825
	1    0    0    -1  
$EndComp
Wire Wire Line
	7825 3275 7825 3775
NoConn ~ 9425 3125
NoConn ~ 9425 3225
NoConn ~ 9425 3325
NoConn ~ 9425 3425
Wire Wire Line
	9425 2725 10000 2725
Wire Wire Line
	9425 2825 9950 2825
Wire Wire Line
	9950 2825 9950 3325
Wire Wire Line
	9950 3325 10000 3325
Wire Wire Line
	9425 2925 9900 2925
Wire Wire Line
	9900 2925 9900 3875
Wire Wire Line
	9900 3875 10000 3875
Wire Wire Line
	9425 3025 9850 3025
Wire Wire Line
	9850 3025 9850 4425
Wire Wire Line
	9850 4425 10000 4425
Wire Wire Line
	11650 3025 11600 3025
Wire Wire Line
	11600 3025 11600 2625
Wire Wire Line
	11600 2625 11475 2625
Wire Wire Line
	11475 3225 11650 3225
Wire Wire Line
	10600 2725 10875 2725
Wire Wire Line
	10600 3325 10875 3325
Wire Wire Line
	10600 3875 10875 3875
Wire Wire Line
	10600 4425 10875 4425
Wire Wire Line
	11475 3775 11650 3775
Wire Wire Line
	11650 3975 11600 3975
Wire Wire Line
	11600 3975 11600 4325
Wire Wire Line
	11600 4325 11475 4325
Wire Wire Line
	12250 3125 12425 3125
Wire Wire Line
	12425 3325 12375 3325
Wire Wire Line
	12375 3325 12375 3875
Wire Wire Line
	12375 3875 12250 3875
Wire Wire Line
	7825 3775 8925 3775
Wire Wire Line
	8375 3325 8425 3325
Wire Wire Line
	8375 3425 8425 3425
Wire Wire Line
	13025 3225 13200 3225
Wire Wire Line
	13800 3225 13900 3225
Wire Wire Line
	13900 3225 13900 2575
Wire Wire Line
	13900 2575 14875 2575
Connection ~ 13900 3225
Wire Wire Line
	13900 3225 14000 3225
Wire Wire Line
	14600 3225 14725 3225
Wire Wire Line
	14725 3275 14725 3225
Wire Wire Line
	14725 3225 14875 3225
Connection ~ 14725 3225
Wire Wire Line
	12425 4675 12425 4625
Wire Wire Line
	12425 4675 12475 4675
Wire Wire Line
	12425 4675 12425 4875
Wire Wire Line
	12425 4875 12475 4875
Connection ~ 12425 4675
NoConn ~ 13075 4775
$Comp
L Device:R R?
U 1 1 61260004
P 7600 3125
F 0 "R?" H 7670 3171 50  0000 L CNN
F 1 "1k" H 7670 3080 50  0000 L CNN
F 2 "" V 7530 3125 50  0001 C CNN
F 3 "~" H 7600 3125 50  0001 C CNN
	1    7600 3125
	1    0    0    -1  
$EndComp
$Comp
L Device:R R?
U 1 1 6126AD6D
P 7375 3125
F 0 "R?" H 7445 3171 50  0000 L CNN
F 1 "1k" H 7445 3080 50  0000 L CNN
F 2 "" V 7305 3125 50  0001 C CNN
F 3 "~" H 7375 3125 50  0001 C CNN
	1    7375 3125
	1    0    0    -1  
$EndComp
Wire Wire Line
	7375 2975 7375 2725
Wire Wire Line
	7375 2725 8425 2725
Wire Wire Line
	7600 2975 7600 2825
Wire Wire Line
	7600 2825 8425 2825
Wire Wire Line
	7375 3275 7375 3775
Wire Wire Line
	7375 3775 7600 3775
Connection ~ 7825 3775
Wire Wire Line
	7600 3275 7600 3775
Wire Wire Line
	7600 3775 7825 3775
Connection ~ 7600 3775
Wire Wire Line
	7600 2825 7600 2400
Connection ~ 7600 2825
Wire Wire Line
	7375 2725 7375 2500
Wire Wire Line
	7375 2500 7325 2500
Connection ~ 7375 2725
Wire Wire Line
	7325 2400 7600 2400
Text Label 7325 2500 2    50   ~ 0
CLK_SEL_0
Text Label 7325 2400 2    50   ~ 0
CLK_SEL_1
Text Label 10875 2525 2    50   ~ 0
CLK_IN_0
Text Label 10875 3125 2    50   ~ 0
CLK_IN_1
Text Label 10875 3675 2    50   ~ 0
CLK_IN_2
Text Label 10875 4225 2    50   ~ 0
CLK_IN_3
Text Label 4300 3950 0    50   ~ 0
CLK_IN_0
Text Label 4750 1800 0    50   ~ 0
CLK_IN_1
$Comp
L power:+5V #PWR?
U 1 1 61C212E6
P 3100 1200
AR Path="/5F05F116/61C212E6" Ref="#PWR?"  Part="1" 
AR Path="/5EFC09F3/61C212E6" Ref="#PWR?"  Part="1" 
F 0 "#PWR?" H 3100 1050 50  0001 C CNN
F 1 "+5V" H 3115 1373 50  0000 C CNN
F 2 "" H 3100 1200 50  0001 C CNN
F 3 "" H 3100 1200 50  0001 C CNN
	1    3100 1200
	1    0    0    -1  
$EndComp
$Comp
L power:+5V #PWR?
U 1 1 61C2E494
P 3100 3350
AR Path="/5F05F116/61C2E494" Ref="#PWR?"  Part="1" 
AR Path="/5EFC09F3/61C2E494" Ref="#PWR?"  Part="1" 
F 0 "#PWR?" H 3100 3200 50  0001 C CNN
F 1 "+5V" H 3115 3523 50  0000 C CNN
F 2 "" H 3100 3350 50  0001 C CNN
F 3 "" H 3100 3350 50  0001 C CNN
	1    3100 3350
	1    0    0    -1  
$EndComp
$Comp
L power:+5V #PWR?
U 1 1 61C48A99
P 4275 5500
AR Path="/5F05F116/61C48A99" Ref="#PWR?"  Part="1" 
AR Path="/5EFC09F3/61C48A99" Ref="#PWR?"  Part="1" 
F 0 "#PWR?" H 4275 5350 50  0001 C CNN
F 1 "+5V" H 4290 5673 50  0000 C CNN
F 2 "" H 4275 5500 50  0001 C CNN
F 3 "" H 4275 5500 50  0001 C CNN
	1    4275 5500
	1    0    0    -1  
$EndComp
$Comp
L power:+5V #PWR?
U 1 1 61C78623
P 8925 2325
AR Path="/5F05F116/61C78623" Ref="#PWR?"  Part="1" 
AR Path="/5EFC09F3/61C78623" Ref="#PWR?"  Part="1" 
F 0 "#PWR?" H 8925 2175 50  0001 C CNN
F 1 "+5V" H 8940 2498 50  0000 C CNN
F 2 "" H 8925 2325 50  0001 C CNN
F 3 "" H 8925 2325 50  0001 C CNN
	1    8925 2325
	1    0    0    -1  
$EndComp
$Comp
L power:+5V #PWR?
U 1 1 61C85947
P 12425 4625
AR Path="/5F05F116/61C85947" Ref="#PWR?"  Part="1" 
AR Path="/5EFC09F3/61C85947" Ref="#PWR?"  Part="1" 
F 0 "#PWR?" H 12425 4475 50  0001 C CNN
F 1 "+5V" H 12440 4798 50  0000 C CNN
F 2 "" H 12425 4625 50  0001 C CNN
F 3 "" H 12425 4625 50  0001 C CNN
	1    12425 4625
	1    0    0    -1  
$EndComp
Wire Wire Line
	3100 1350 3100 1600
Wire Wire Line
	4275 5500 4275 5550
Wire Wire Line
	4275 6600 4275 6675
Wire Wire Line
	4275 5550 3475 5550
Wire Wire Line
	3475 5550 3475 5600
Connection ~ 4275 5550
Wire Wire Line
	4275 5550 4275 5600
Wire Wire Line
	2600 5625 2600 5550
Wire Wire Line
	2600 5550 3475 5550
Connection ~ 3475 5550
Wire Wire Line
	2600 6675 3475 6675
Connection ~ 4275 6675
Wire Wire Line
	4275 6675 4275 6725
Wire Wire Line
	3475 6600 3475 6675
Connection ~ 3475 6675
Wire Wire Line
	3475 6675 4275 6675
$EndSCHEMATC
