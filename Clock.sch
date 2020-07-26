EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 5 9
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
L Timer:LM555 U2
U 1 1 5F00FC3F
P 3100 2000
F 0 "U2" H 3200 2450 50  0000 C CNN
F 1 "LM555" H 3250 2350 50  0000 C CNN
F 2 "" H 3100 2000 50  0001 C CNN
F 3 "http://www.ti.com/lit/ds/symlink/lm555.pdf" H 3100 2000 50  0001 C CNN
	1    3100 2000
	1    0    0    -1  
$EndComp
$Comp
L Timer:LM555 U4
U 1 1 5F010A80
P 3100 4150
F 0 "U4" H 3200 4600 50  0000 C CNN
F 1 "LM555" H 3250 4500 50  0000 C CNN
F 2 "" H 3100 4150 50  0001 C CNN
F 3 "http://www.ti.com/lit/ds/symlink/lm555.pdf" H 3100 4150 50  0001 C CNN
	1    3100 4150
	1    0    0    -1  
$EndComp
$Comp
L Timer:LM555 U3
U 1 1 5F010F36
P 6550 2850
F 0 "U3" H 6450 3300 50  0000 C CNN
F 1 "LM555" H 6400 3200 50  0000 C CNN
F 2 "" H 6550 2850 50  0001 C CNN
F 3 "http://www.ti.com/lit/ds/symlink/lm555.pdf" H 6550 2850 50  0001 C CNN
	1    6550 2850
	-1   0    0    -1  
$EndComp
$Comp
L Device:R R4
U 1 1 5F0141BE
P 2500 3750
F 0 "R4" H 2570 3796 50  0000 L CNN
F 1 "4.7k" H 2570 3705 50  0000 L CNN
F 2 "" V 2430 3750 50  0001 C CNN
F 3 "~" H 2500 3750 50  0001 C CNN
	1    2500 3750
	1    0    0    -1  
$EndComp
$Comp
L Device:C_Small C9
U 1 1 5F0158C4
P 4050 2550
F 0 "C9" H 4142 2596 50  0000 L CNN
F 1 "1u" H 4142 2505 50  0000 L CNN
F 2 "" H 4050 2550 50  0001 C CNN
F 3 "~" H 4050 2550 50  0001 C CNN
	1    4050 2550
	1    0    0    -1  
$EndComp
$Comp
L Device:C_Small C5
U 1 1 5F015A16
P 7250 3200
F 0 "C5" H 7158 3246 50  0000 R CNN
F 1 "0.1u" H 7158 3155 50  0000 R CNN
F 2 "" H 7250 3200 50  0001 C CNN
F 3 "~" H 7250 3200 50  0001 C CNN
	1    7250 3200
	-1   0    0    -1  
$EndComp
$Comp
L Device:R R3
U 1 1 5F015E4C
P 3750 3750
F 0 "R3" H 3820 3796 50  0000 L CNN
F 1 "1M" H 3820 3705 50  0000 L CNN
F 2 "" V 3680 3750 50  0001 C CNN
F 3 "~" H 3750 3750 50  0001 C CNN
	1    3750 3750
	1    0    0    -1  
$EndComp
$Comp
L Device:R R11
U 1 1 5F017222
P 4650 2000
F 0 "R11" H 4720 2046 50  0000 L CNN
F 1 "4.7k" H 4720 1955 50  0000 L CNN
F 2 "" V 4580 2000 50  0001 C CNN
F 3 "~" H 4650 2000 50  0001 C CNN
	1    4650 2000
	1    0    0    -1  
$EndComp
$Comp
L Device:C_Small C4
U 1 1 5F0180E8
P 2050 2200
F 0 "C4" H 2142 2246 50  0000 L CNN
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
L Device:R R8
U 1 1 5F019A19
P 3950 2000
F 0 "R8" V 4157 2000 50  0000 C CNN
F 1 "1800" V 4066 2000 50  0000 C CNN
F 2 "" V 3880 2000 50  0001 C CNN
F 3 "~" H 3950 2000 50  0001 C CNN
	1    3950 2000
	0    1    1    0   
$EndComp
Text Label 4750 1800 0    50   ~ 0
Astable
$Comp
L Device:R R6
U 1 1 5F01AE8F
P 3750 1550
F 0 "R6" H 3820 1596 50  0000 L CNN
F 1 "3600" H 3820 1505 50  0000 L CNN
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
L Device:LED D3
U 1 1 5F022248
P 4650 2400
F 0 "D3" V 4689 2283 50  0000 R CNN
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
L Device:R_POT RV1
U 1 1 5F01B3E1
P 4250 2200
F 0 "RV1" V 4150 2250 50  0000 R CNN
F 1 "0-1.5M" V 4050 2300 50  0000 R CNN
F 2 "" H 4250 2200 50  0001 C CNN
F 3 "~" H 4250 2200 50  0001 C CNN
	1    4250 2200
	0    -1   -1   0   
$EndComp
$Comp
L power:VCC #PWR07
U 1 1 5F0312AD
P 3100 1200
F 0 "#PWR07" H 3100 1050 50  0001 C CNN
F 1 "VCC" H 3117 1373 50  0000 C CNN
F 2 "" H 3100 1200 50  0001 C CNN
F 3 "" H 3100 1200 50  0001 C CNN
	1    3100 1200
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR08
U 1 1 5F031B94
P 3100 2800
F 0 "#PWR08" H 3100 2550 50  0001 C CNN
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
$Comp
L power:VCC #PWR012
U 1 1 5F0434B3
P 3100 3350
F 0 "#PWR012" H 3100 3200 50  0001 C CNN
F 1 "VCC" H 3117 3523 50  0000 C CNN
F 2 "" H 3100 3350 50  0001 C CNN
F 3 "" H 3100 3350 50  0001 C CNN
	1    3100 3350
	1    0    0    -1  
$EndComp
Wire Wire Line
	3600 4150 3750 4150
Wire Wire Line
	3750 4150 3750 4350
Wire Wire Line
	3750 4350 3600 4350
$Comp
L Device:C_Small C10
U 1 1 5F045E40
P 2050 4350
F 0 "C10" H 2142 4396 50  0000 L CNN
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
L Device:C_Small C11
U 1 1 5F0477B9
P 3750 4500
F 0 "C11" H 3842 4546 50  0000 L CNN
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
L Switch:SW_Push SW1
U 1 1 5F04F258
P 2050 3950
F 0 "SW1" H 2050 4235 50  0000 C CNN
F 1 "SW_Push" H 2050 4144 50  0000 C CNN
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
L power:GND #PWR011
U 1 1 5F0555E2
P 1800 4000
F 0 "#PWR011" H 1800 3750 50  0001 C CNN
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
L Device:R R5
U 1 1 5F061991
P 4200 4150
F 0 "R5" H 4270 4196 50  0000 L CNN
F 1 "4.7k" H 4270 4105 50  0000 L CNN
F 2 "" V 4130 4150 50  0001 C CNN
F 3 "~" H 4200 4150 50  0001 C CNN
	1    4200 4150
	1    0    0    -1  
$EndComp
Text Label 4300 3950 0    50   ~ 0
Monostable
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
L power:GND #PWR013
U 1 1 5F056C27
P 3100 4750
F 0 "#PWR013" H 3100 4500 50  0001 C CNN
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
L Device:LED D4
U 1 1 5F061998
P 4200 4500
F 0 "D4" V 4239 4383 50  0000 R CNN
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
L 74xx:74LS08 U6
U 1 1 5F070257
P 6400 3950
F 0 "U6" H 6400 4275 50  0000 C CNN
F 1 "74HC08" H 6400 4184 50  0000 C CNN
F 2 "" H 6400 3950 50  0001 C CNN
F 3 "http://www.ti.com/lit/gpn/sn74LS08" H 6400 3950 50  0001 C CNN
	1    6400 3950
	1    0    0    -1  
$EndComp
$Comp
L 74xx:74LS08 U6
U 2 1 5F0724F5
P 8450 4150
F 0 "U6" H 8450 4475 50  0000 C CNN
F 1 "74HC08" H 8450 4384 50  0000 C CNN
F 2 "" H 8450 4150 50  0001 C CNN
F 3 "http://www.ti.com/lit/gpn/sn74LS08" H 8450 4150 50  0001 C CNN
	2    8450 4150
	1    0    0    -1  
$EndComp
$Comp
L Device:R R9
U 1 1 5F08E808
P 7400 2450
F 0 "R9" H 7470 2496 50  0000 L CNN
F 1 "4.7k" H 7470 2405 50  0000 L CNN
F 2 "" V 7330 2450 50  0001 C CNN
F 3 "~" H 7400 2450 50  0001 C CNN
	1    7400 2450
	-1   0    0    -1  
$EndComp
$Comp
L Device:R R7
U 1 1 5F08F0D6
P 7100 2450
F 0 "R7" H 7030 2496 50  0000 R CNN
F 1 "4.7k" H 7030 2405 50  0000 R CNN
F 2 "" V 7030 2450 50  0001 C CNN
F 3 "~" H 7100 2450 50  0001 C CNN
	1    7100 2450
	1    0    0    1   
$EndComp
$Comp
L Switch:SW_SPDT SW2
U 1 1 5F090C97
P 7750 2850
F 0 "SW2" H 7750 3135 50  0000 C CNN
F 1 "SW_SPDT" H 7750 3044 50  0000 C CNN
F 2 "" H 7750 2850 50  0001 C CNN
F 3 "~" H 7750 2850 50  0001 C CNN
	1    7750 2850
	-1   0    0    -1  
$EndComp
Wire Wire Line
	7050 2850 7250 2850
Wire Wire Line
	7250 2850 7250 3100
Wire Wire Line
	7550 2950 7400 2950
Wire Wire Line
	7400 2950 7400 3050
Wire Wire Line
	7400 3050 7100 3050
Wire Wire Line
	7400 2600 7400 2950
Connection ~ 7400 2950
Wire Wire Line
	7100 2600 7100 3050
Connection ~ 7100 3050
Wire Wire Line
	7100 3050 7050 3050
Wire Wire Line
	7550 2750 7250 2750
Wire Wire Line
	7250 2750 7250 2650
Wire Wire Line
	7250 2650 7050 2650
Wire Wire Line
	6550 2050 6550 2200
Wire Wire Line
	7100 2200 7100 2300
Wire Wire Line
	7400 2200 7100 2200
Wire Wire Line
	7400 2200 7400 2300
Connection ~ 7100 2200
$Comp
L power:GND #PWR015
U 1 1 5F0C95EE
P 6550 3400
F 0 "#PWR015" H 6550 3150 50  0001 C CNN
F 1 "GND" H 6555 3227 50  0000 C CNN
F 2 "" H 6550 3400 50  0001 C CNN
F 3 "" H 6550 3400 50  0001 C CNN
	1    6550 3400
	-1   0    0    -1  
$EndComp
Wire Wire Line
	7250 3300 7250 3350
Wire Wire Line
	7250 3350 6550 3350
Wire Wire Line
	6550 3350 6550 3400
Wire Wire Line
	6550 3250 6550 3350
Connection ~ 6550 3350
Wire Wire Line
	6550 3350 6000 3350
Wire Wire Line
	6000 3350 6000 3050
Wire Wire Line
	6000 3050 6050 3050
Wire Wire Line
	6050 2850 6000 2850
Wire Wire Line
	6000 2850 6000 3050
Connection ~ 6000 3050
Text Label 6000 3850 2    50   ~ 0
Astable
$Comp
L power:VCC #PWR014
U 1 1 5F114345
P 6550 2050
F 0 "#PWR014" H 6550 1900 50  0001 C CNN
F 1 "VCC" H 6567 2223 50  0000 C CNN
F 2 "" H 6550 2050 50  0001 C CNN
F 3 "" H 6550 2050 50  0001 C CNN
	1    6550 2050
	1    0    0    -1  
$EndComp
Text Label 6000 4950 2    50   ~ 0
Monostable
$Comp
L 74xx:74LS08 U6
U 3 1 5F073F35
P 6400 4850
F 0 "U6" H 6400 5175 50  0000 C CNN
F 1 "74HC08" H 6400 5084 50  0000 C CNN
F 2 "" H 6400 4850 50  0001 C CNN
F 3 "http://www.ti.com/lit/gpn/sn74LS08" H 6400 4850 50  0001 C CNN
	3    6400 4850
	1    0    0    -1  
$EndComp
Wire Wire Line
	6000 4950 6100 4950
Wire Wire Line
	6000 3850 6100 3850
Wire Wire Line
	6050 2650 5650 2650
Wire Wire Line
	5650 4050 6100 4050
Wire Wire Line
	5650 2650 5650 4050
Wire Wire Line
	5650 4700 5650 4750
Wire Wire Line
	5650 4750 6100 4750
Wire Wire Line
	5650 4050 5650 4100
Connection ~ 5650 4050
$Comp
L 74xx:74LS32 U7
U 1 1 5F17E838
P 7350 4050
F 0 "U7" H 7350 4375 50  0000 C CNN
F 1 "74HC32" H 7350 4284 50  0000 C CNN
F 2 "" H 7350 4050 50  0001 C CNN
F 3 "http://www.ti.com/lit/gpn/sn74LS32" H 7350 4050 50  0001 C CNN
	1    7350 4050
	1    0    0    -1  
$EndComp
Wire Wire Line
	6700 3950 7050 3950
Wire Wire Line
	6700 4850 6850 4850
Wire Wire Line
	6850 4850 6850 4150
Wire Wire Line
	6850 4150 7050 4150
Wire Wire Line
	7300 4900 7350 4900
Wire Wire Line
	8000 4350 8000 4250
Wire Wire Line
	8000 4250 8150 4250
Wire Wire Line
	7650 4050 8150 4050
Wire Wire Line
	8750 4150 8800 4150
Wire Wire Line
	8800 4150 8800 3800
Wire Wire Line
	8800 3800 8850 3800
Wire Wire Line
	9450 3800 9500 3800
Wire Wire Line
	8800 4150 9500 4150
Connection ~ 8800 4150
$Comp
L Device:R R10
U 1 1 5F1F0144
P 8800 4350
F 0 "R10" H 8870 4396 50  0000 L CNN
F 1 "4.7k" H 8870 4305 50  0000 L CNN
F 2 "" V 8730 4350 50  0001 C CNN
F 3 "~" H 8800 4350 50  0001 C CNN
	1    8800 4350
	1    0    0    -1  
$EndComp
$Comp
L Device:LED D5
U 1 1 5F1F1588
P 8800 4700
F 0 "D5" V 8839 4583 50  0000 R CNN
F 1 "LED" V 8748 4583 50  0000 R CNN
F 2 "" H 8800 4700 50  0001 C CNN
F 3 "~" H 8800 4700 50  0001 C CNN
	1    8800 4700
	0    -1   -1   0   
$EndComp
$Comp
L power:GND #PWR016
U 1 1 5F1F225D
P 8800 4900
F 0 "#PWR016" H 8800 4650 50  0001 C CNN
F 1 "GND" H 8805 4727 50  0000 C CNN
F 2 "" H 8800 4900 50  0001 C CNN
F 3 "" H 8800 4900 50  0001 C CNN
	1    8800 4900
	1    0    0    -1  
$EndComp
Wire Wire Line
	8800 4900 8800 4850
Wire Wire Line
	8800 4550 8800 4500
Wire Wire Line
	8800 4200 8800 4150
$Comp
L 74xx:74LS32 U7
U 5 1 5F204533
P 3950 5950
F 0 "U7" H 4180 5996 50  0000 L CNN
F 1 "74HC32" H 4180 5905 50  0000 L CNN
F 2 "" H 3950 5950 50  0001 C CNN
F 3 "http://www.ti.com/lit/gpn/sn74LS32" H 3950 5950 50  0001 C CNN
	5    3950 5950
	1    0    0    -1  
$EndComp
$Comp
L 74xx:74LS08 U6
U 5 1 5F20829F
P 6550 5950
F 0 "U6" H 6780 5996 50  0000 L CNN
F 1 "74HC08" H 6780 5905 50  0000 L CNN
F 2 "" H 6550 5950 50  0001 C CNN
F 3 "http://www.ti.com/lit/gpn/sn74LS08" H 6550 5950 50  0001 C CNN
	5    6550 5950
	1    0    0    -1  
$EndComp
$Comp
L power:VCC #PWR017
U 1 1 5F20EAAD
P 3950 5400
F 0 "#PWR017" H 3950 5250 50  0001 C CNN
F 1 "VCC" H 3967 5573 50  0000 C CNN
F 2 "" H 3950 5400 50  0001 C CNN
F 3 "" H 3950 5400 50  0001 C CNN
	1    3950 5400
	1    0    0    -1  
$EndComp
$Comp
L power:VCC #PWR019
U 1 1 5F20F670
P 5250 5400
F 0 "#PWR019" H 5250 5250 50  0001 C CNN
F 1 "VCC" H 5267 5573 50  0000 C CNN
F 2 "" H 5250 5400 50  0001 C CNN
F 3 "" H 5250 5400 50  0001 C CNN
	1    5250 5400
	1    0    0    -1  
$EndComp
$Comp
L power:VCC #PWR021
U 1 1 5F21059E
P 6550 5400
F 0 "#PWR021" H 6550 5250 50  0001 C CNN
F 1 "VCC" H 6567 5573 50  0000 C CNN
F 2 "" H 6550 5400 50  0001 C CNN
F 3 "" H 6550 5400 50  0001 C CNN
	1    6550 5400
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR018
U 1 1 5F21C883
P 3950 6500
F 0 "#PWR018" H 3950 6250 50  0001 C CNN
F 1 "GND" H 3955 6327 50  0000 C CNN
F 2 "" H 3950 6500 50  0001 C CNN
F 3 "" H 3950 6500 50  0001 C CNN
	1    3950 6500
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR020
U 1 1 5F21D044
P 5250 6500
F 0 "#PWR020" H 5250 6250 50  0001 C CNN
F 1 "GND" H 5255 6327 50  0000 C CNN
F 2 "" H 5250 6500 50  0001 C CNN
F 3 "" H 5250 6500 50  0001 C CNN
	1    5250 6500
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR022
U 1 1 5F21D778
P 6550 6500
F 0 "#PWR022" H 6550 6250 50  0001 C CNN
F 1 "GND" H 6555 6327 50  0000 C CNN
F 2 "" H 6550 6500 50  0001 C CNN
F 3 "" H 6550 6500 50  0001 C CNN
	1    6550 6500
	1    0    0    -1  
$EndComp
$Comp
L Device:C_Small C14
U 1 1 5F21DEF8
P 5900 5950
F 0 "C14" H 5992 5996 50  0000 L CNN
F 1 "0.1u" H 5992 5905 50  0000 L CNN
F 2 "" H 5900 5950 50  0001 C CNN
F 3 "~" H 5900 5950 50  0001 C CNN
	1    5900 5950
	1    0    0    -1  
$EndComp
$Comp
L Device:C_Small C13
U 1 1 5F22D32F
P 4600 5950
F 0 "C13" H 4692 5996 50  0000 L CNN
F 1 "0.1u" H 4692 5905 50  0000 L CNN
F 2 "" H 4600 5950 50  0001 C CNN
F 3 "~" H 4600 5950 50  0001 C CNN
	1    4600 5950
	1    0    0    -1  
$EndComp
$Comp
L Device:C_Small C12
U 1 1 5F235737
P 3300 5950
F 0 "C12" H 3392 5996 50  0000 L CNN
F 1 "0.1u" H 3392 5905 50  0000 L CNN
F 2 "" H 3300 5950 50  0001 C CNN
F 3 "~" H 3300 5950 50  0001 C CNN
	1    3300 5950
	1    0    0    -1  
$EndComp
Wire Wire Line
	5900 5850 5900 5450
Wire Wire Line
	5900 5450 6550 5450
Wire Wire Line
	6550 5400 6550 5450
Connection ~ 6550 5450
Wire Wire Line
	5900 6050 5900 6450
Wire Wire Line
	5900 6450 6550 6450
Wire Wire Line
	6550 6450 6550 6500
Connection ~ 6550 6450
Wire Wire Line
	5250 5400 5250 5450
Wire Wire Line
	5250 5450 4600 5450
Wire Wire Line
	4600 5450 4600 5850
Wire Wire Line
	4600 6050 4600 6450
Wire Wire Line
	4600 6450 5250 6450
Wire Wire Line
	5250 6500 5250 6450
Wire Wire Line
	3950 6500 3950 6450
Wire Wire Line
	3950 6450 3300 6450
Wire Wire Line
	3300 6450 3300 6050
Connection ~ 3950 6450
Wire Wire Line
	3300 5850 3300 5450
Wire Wire Line
	3300 5450 3950 5450
Wire Wire Line
	3950 5450 3950 5400
Connection ~ 3950 5450
$Comp
L Device:C_Small C8
U 1 1 5F27912D
P 5350 2800
F 0 "C8" H 5442 2846 50  0000 L CNN
F 1 "0.1u" H 5442 2755 50  0000 L CNN
F 2 "" H 5350 2800 50  0001 C CNN
F 3 "~" H 5350 2800 50  0001 C CNN
	1    5350 2800
	1    0    0    -1  
$EndComp
Wire Wire Line
	5350 2900 5350 3350
Wire Wire Line
	5350 3350 6000 3350
Connection ~ 6000 3350
Wire Wire Line
	2300 3500 1450 3500
Wire Wire Line
	1450 3500 1450 3950
Connection ~ 2300 3500
$Comp
L Device:C_Small C6
U 1 1 5F28FC1A
P 1450 4050
F 0 "C6" H 1542 4096 50  0000 L CNN
F 1 "0.1u" H 1542 4005 50  0000 L CNN
F 2 "" H 1450 4050 50  0001 C CNN
F 3 "~" H 1450 4050 50  0001 C CNN
	1    1450 4050
	1    0    0    -1  
$EndComp
Wire Wire Line
	1450 4150 1450 4700
Wire Wire Line
	1450 4700 2050 4700
Connection ~ 2050 4700
$Comp
L Device:C_Small C7
U 1 1 5F2BC955
P 1550 1950
F 0 "C7" H 1642 1996 50  0000 L CNN
F 1 "0.1u" H 1642 1905 50  0000 L CNN
F 2 "" H 1550 1950 50  0001 C CNN
F 3 "~" H 1550 1950 50  0001 C CNN
	1    1550 1950
	1    0    0    -1  
$EndComp
Wire Wire Line
	1550 1550 1550 1850
Wire Wire Line
	1550 2050 1550 2700
Wire Wire Line
	1550 2700 2050 2700
Connection ~ 2050 2700
Wire Wire Line
	7950 2850 8000 2850
Wire Wire Line
	8000 2850 8000 3350
Wire Wire Line
	8000 3350 7250 3350
Connection ~ 7250 3350
Text HLabel 7300 4900 0    50   Input ~ 0
HALT_A
Text HLabel 9500 4150 2    50   Input ~ 0
CLK
Text HLabel 9500 3800 2    50   Input ~ 0
~CLK
Wire Wire Line
	3100 3750 3100 3500
Wire Wire Line
	2300 1350 3100 1350
Wire Wire Line
	3100 1350 3100 1550
Wire Wire Line
	1550 1550 3100 1550
Connection ~ 3100 1550
Wire Wire Line
	3100 1550 3100 1600
Wire Wire Line
	6550 2200 7100 2200
Wire Wire Line
	5350 2400 6550 2400
Wire Wire Line
	6550 2400 6550 2450
Wire Wire Line
	5350 2400 5350 2700
Wire Wire Line
	6550 2200 6550 2400
Connection ~ 6550 2200
Connection ~ 6550 2400
$Comp
L 74xx:74HC04 U28
U 1 1 5F446CD2
P 5650 4400
F 0 "U28" V 5604 4580 50  0000 L CNN
F 1 "74HC05" V 5695 4580 50  0000 L CNN
F 2 "" H 5650 4400 50  0001 C CNN
F 3 "https://assets.nexperia.com/documents/data-sheet/74HC_HCT04.pdf" H 5650 4400 50  0001 C CNN
	1    5650 4400
	0    1    1    0   
$EndComp
$Comp
L 74xx:74HC04 U28
U 2 1 5F448193
P 9150 3800
F 0 "U28" H 9150 4117 50  0000 C CNN
F 1 "74HC05" H 9150 4026 50  0000 C CNN
F 2 "" H 9150 3800 50  0001 C CNN
F 3 "https://assets.nexperia.com/documents/data-sheet/74HC_HCT04.pdf" H 9150 3800 50  0001 C CNN
	2    9150 3800
	1    0    0    -1  
$EndComp
$Comp
L 74xx:74HC04 U28
U 3 1 5F448D9E
P 8000 4650
F 0 "U28" H 8000 4967 50  0000 C CNN
F 1 "74HC05" H 8000 4876 50  0000 C CNN
F 2 "" H 8000 4650 50  0001 C CNN
F 3 "https://assets.nexperia.com/documents/data-sheet/74HC_HCT04.pdf" H 8000 4650 50  0001 C CNN
	3    8000 4650
	0    -1   -1   0   
$EndComp
$Comp
L 74xx:74HC04 U28
U 7 1 5F449D6E
P 5250 5950
F 0 "U28" H 5480 5996 50  0000 L CNN
F 1 "74HC05" H 5480 5905 50  0000 L CNN
F 2 "" H 5250 5950 50  0001 C CNN
F 3 "https://assets.nexperia.com/documents/data-sheet/74HC_HCT04.pdf" H 5250 5950 50  0001 C CNN
	7    5250 5950
	1    0    0    -1  
$EndComp
Connection ~ 5250 5450
Connection ~ 5250 6450
Text HLabel 7300 5100 0    50   Input ~ 0
HALT_B
$Comp
L 74xx:74LS32 U7
U 2 1 5FB8BB70
P 7650 5000
F 0 "U7" V 7696 4820 50  0000 R CNN
F 1 "74HC32" V 7605 4820 50  0000 R CNN
F 2 "" H 7650 5000 50  0001 C CNN
F 3 "http://www.ti.com/lit/gpn/sn74LS32" H 7650 5000 50  0001 C CNN
	2    7650 5000
	1    0    0    -1  
$EndComp
Wire Wire Line
	7350 5100 7300 5100
Wire Wire Line
	7950 5000 8000 5000
Wire Wire Line
	8000 5000 8000 4950
$EndSCHEMATC
