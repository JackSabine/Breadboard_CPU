EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 9 9
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
L 74xx:74LS163 U11
U 1 1 5F362EFB
P 4900 5500
F 0 "U11" H 5000 6250 50  0000 C CNN
F 1 "74LS161AN" H 5150 6150 50  0000 C CNN
F 2 "" H 4900 5500 50  0001 C CNN
F 3 "http://www.ti.com/lit/gpn/sn74LS163" H 4900 5500 50  0001 C CNN
	1    4900 5500
	1    0    0    -1  
$EndComp
Wire Wire Line
	4350 3600 4400 3600
Wire Wire Line
	4350 3400 4400 3400
Wire Wire Line
	4350 3100 4400 3100
$Comp
L power:VCC #PWR023
U 1 1 5F366104
P 4900 2200
F 0 "#PWR023" H 4900 2050 50  0001 C CNN
F 1 "VCC" H 4917 2373 50  0000 C CNN
F 2 "" H 4900 2200 50  0001 C CNN
F 3 "" H 4900 2200 50  0001 C CNN
	1    4900 2200
	1    0    0    -1  
$EndComp
Wire Wire Line
	4900 2200 4900 2250
Wire Wire Line
	4900 2250 3800 2250
Connection ~ 4900 2250
Wire Wire Line
	4900 2250 4900 2300
Text HLabel 4350 2600 0    50   Input ~ 0
B0
Text HLabel 4350 2700 0    50   Input ~ 0
B1
Text HLabel 4350 2800 0    50   Input ~ 0
B2
Text HLabel 4350 2900 0    50   Input ~ 0
B3
Wire Wire Line
	4350 2600 4400 2600
Wire Wire Line
	4350 2700 4400 2700
Wire Wire Line
	4350 2800 4400 2800
Wire Wire Line
	4350 2900 4400 2900
$Comp
L power:GND #PWR024
U 1 1 5F36BFAA
P 4900 4000
F 0 "#PWR024" H 4900 3750 50  0001 C CNN
F 1 "GND" H 4905 3827 50  0000 C CNN
F 2 "" H 4900 4000 50  0001 C CNN
F 3 "" H 4900 4000 50  0001 C CNN
	1    4900 4000
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR028
U 1 1 5F36CA53
P 8200 4000
F 0 "#PWR028" H 8200 3750 50  0001 C CNN
F 1 "GND" H 8205 3827 50  0000 C CNN
F 2 "" H 8200 4000 50  0001 C CNN
F 3 "" H 8200 4000 50  0001 C CNN
	1    8200 4000
	1    0    0    -1  
$EndComp
Wire Wire Line
	8200 3900 8200 3950
Wire Wire Line
	4900 3900 4900 3950
Text HLabel 8700 2600 2    50   Output ~ 0
B0
Text HLabel 8700 2700 2    50   Output ~ 0
B1
Text HLabel 8700 2800 2    50   Output ~ 0
B2
Text HLabel 8700 2900 2    50   Output ~ 0
B3
Text HLabel 8700 3000 2    50   Output ~ 0
B4
Text HLabel 8700 3100 2    50   Output ~ 0
B5
Text HLabel 8700 3200 2    50   Output ~ 0
B6
Text HLabel 8700 3300 2    50   Output ~ 0
B7
$Comp
L power:VCC #PWR025
U 1 1 5F37576B
P 4900 4600
F 0 "#PWR025" H 4900 4450 50  0001 C CNN
F 1 "VCC" H 4917 4773 50  0000 C CNN
F 2 "" H 4900 4600 50  0001 C CNN
F 3 "" H 4900 4600 50  0001 C CNN
	1    4900 4600
	1    0    0    -1  
$EndComp
Wire Wire Line
	5400 3100 5450 3100
Wire Wire Line
	5450 3100 5450 4300
Wire Wire Line
	5450 4300 3750 4300
Wire Wire Line
	4900 4600 4900 4650
Wire Wire Line
	4350 5500 4400 5500
Text HLabel 4350 5000 0    50   Input ~ 0
B4
Text HLabel 4350 5100 0    50   Input ~ 0
B5
Text HLabel 4350 5200 0    50   Input ~ 0
B6
Text HLabel 4350 5300 0    50   Input ~ 0
B7
Wire Wire Line
	4350 5000 4400 5000
Wire Wire Line
	4400 5100 4350 5100
Wire Wire Line
	4350 5200 4400 5200
Wire Wire Line
	4400 5300 4350 5300
Wire Wire Line
	4350 6000 4400 6000
Wire Wire Line
	4900 4650 3800 4650
Connection ~ 4900 4650
Wire Wire Line
	4900 4650 4900 4700
Text HLabel 4300 3250 0    50   Input ~ 0
PC_INC
Text HLabel 4350 3100 0    50   Input ~ 0
~PC_IN
$Comp
L Device:C_Small C16
U 1 1 5F39FCC5
P 3800 3800
F 0 "C16" H 3892 3846 50  0000 L CNN
F 1 "0.1u" H 3892 3755 50  0000 L CNN
F 2 "" H 3800 3800 50  0001 C CNN
F 3 "~" H 3800 3800 50  0001 C CNN
	1    3800 3800
	1    0    0    -1  
$EndComp
Wire Wire Line
	3800 3900 3800 3950
Wire Wire Line
	3800 3950 4900 3950
Connection ~ 4900 3950
Wire Wire Line
	4900 3950 4900 4000
$Comp
L power:GND #PWR026
U 1 1 5F3A930D
P 4900 6400
F 0 "#PWR026" H 4900 6150 50  0001 C CNN
F 1 "GND" H 4905 6227 50  0000 C CNN
F 2 "" H 4900 6400 50  0001 C CNN
F 3 "" H 4900 6400 50  0001 C CNN
	1    4900 6400
	1    0    0    -1  
$EndComp
Wire Wire Line
	5400 5000 5600 5000
Wire Wire Line
	5600 5000 5600 3000
Wire Wire Line
	5400 5100 5700 5100
Wire Wire Line
	5700 5100 5700 3100
Wire Wire Line
	5400 5200 5800 5200
Wire Wire Line
	5800 5200 5800 3200
Wire Wire Line
	5400 5300 5900 5300
Wire Wire Line
	5900 5300 5900 3300
$Comp
L Device:C_Small C17
U 1 1 5F3B1B61
P 9150 3800
F 0 "C17" H 9242 3846 50  0000 L CNN
F 1 "0.1u" H 9242 3755 50  0000 L CNN
F 2 "" H 9150 3800 50  0001 C CNN
F 3 "~" H 9150 3800 50  0001 C CNN
	1    9150 3800
	1    0    0    -1  
$EndComp
Wire Wire Line
	8200 3950 9150 3950
Wire Wire Line
	9150 3950 9150 3900
Connection ~ 8200 3950
Wire Wire Line
	8200 3950 8200 4000
Wire Wire Line
	8200 2250 9150 2250
Wire Wire Line
	9150 2250 9150 3700
Connection ~ 8200 2250
Wire Wire Line
	8200 2250 8200 2300
Text HLabel 7600 3550 0    50   Input ~ 0
~PC_OUT
Wire Wire Line
	7600 3550 7650 3550
Wire Wire Line
	7650 3550 7650 3500
Wire Wire Line
	7650 3500 7700 3500
Wire Wire Line
	7650 3550 7650 3600
Wire Wire Line
	7650 3600 7700 3600
Connection ~ 7650 3550
Text HLabel 5450 5500 2    50   Output ~ 0
TR_HALT
Wire Wire Line
	5400 5500 5450 5500
Wire Wire Line
	5400 2700 5800 2700
Wire Wire Line
	5400 2600 5500 2600
$Comp
L 74xx:74LS163 U10
U 1 1 5F361F47
P 4900 3100
F 0 "U10" H 5000 3850 50  0000 C CNN
F 1 "74LS161AN" H 5150 3750 50  0000 C CNN
F 2 "" H 4900 3100 50  0001 C CNN
F 3 "http://www.ti.com/lit/gpn/sn74LS163" H 4900 3100 50  0001 C CNN
	1    4900 3100
	1    0    0    -1  
$EndComp
Wire Wire Line
	5400 2900 6400 2900
Wire Wire Line
	5700 3100 7000 3100
Wire Wire Line
	5800 3200 7300 3200
Wire Wire Line
	5900 3300 7600 3300
$Comp
L Device:LED D6
U 1 1 5F459092
P 5500 2050
F 0 "D6" V 5447 2128 50  0000 L CNN
F 1 "Blue" V 5538 2128 50  0000 L CNN
F 2 "" H 5500 2050 50  0001 C CNN
F 3 "~" H 5500 2050 50  0001 C CNN
	1    5500 2050
	0    1    1    0   
$EndComp
$Comp
L Device:LED D7
U 1 1 5F45B9CE
P 5800 2050
F 0 "D7" V 5747 2128 50  0000 L CNN
F 1 "Blue" V 5838 2128 50  0000 L CNN
F 2 "" H 5800 2050 50  0001 C CNN
F 3 "~" H 5800 2050 50  0001 C CNN
	1    5800 2050
	0    1    1    0   
$EndComp
$Comp
L Device:LED D8
U 1 1 5F473631
P 6100 2050
F 0 "D8" V 6047 2128 50  0000 L CNN
F 1 "Blue" V 6138 2128 50  0000 L CNN
F 2 "" H 6100 2050 50  0001 C CNN
F 3 "~" H 6100 2050 50  0001 C CNN
	1    6100 2050
	0    1    1    0   
$EndComp
$Comp
L Device:LED D9
U 1 1 5F473637
P 6400 2050
F 0 "D9" V 6347 2128 50  0000 L CNN
F 1 "Blue" V 6438 2128 50  0000 L CNN
F 2 "" H 6400 2050 50  0001 C CNN
F 3 "~" H 6400 2050 50  0001 C CNN
	1    6400 2050
	0    1    1    0   
$EndComp
$Comp
L Device:LED D10
U 1 1 5F4757D5
P 6700 2050
F 0 "D10" V 6647 2128 50  0000 L CNN
F 1 "Blue" V 6738 2128 50  0000 L CNN
F 2 "" H 6700 2050 50  0001 C CNN
F 3 "~" H 6700 2050 50  0001 C CNN
	1    6700 2050
	0    1    1    0   
$EndComp
$Comp
L Device:LED D11
U 1 1 5F4757DB
P 7000 2050
F 0 "D11" V 6947 2128 50  0000 L CNN
F 1 "Blue" V 7038 2128 50  0000 L CNN
F 2 "" H 7000 2050 50  0001 C CNN
F 3 "~" H 7000 2050 50  0001 C CNN
	1    7000 2050
	0    1    1    0   
$EndComp
$Comp
L Device:LED D12
U 1 1 5F478185
P 7300 2050
F 0 "D12" V 7247 2128 50  0000 L CNN
F 1 "Blue" V 7338 2128 50  0000 L CNN
F 2 "" H 7300 2050 50  0001 C CNN
F 3 "~" H 7300 2050 50  0001 C CNN
	1    7300 2050
	0    1    1    0   
$EndComp
$Comp
L Device:LED D13
U 1 1 5F47818B
P 7600 2050
F 0 "D13" V 7547 2128 50  0000 L CNN
F 1 "Blue" V 7638 2128 50  0000 L CNN
F 2 "" H 7600 2050 50  0001 C CNN
F 3 "~" H 7600 2050 50  0001 C CNN
	1    7600 2050
	0    1    1    0   
$EndComp
Wire Wire Line
	5500 2550 5500 2600
Connection ~ 5500 2600
Wire Wire Line
	5500 2600 7700 2600
Wire Wire Line
	5800 2550 5800 2700
Connection ~ 5800 2700
Wire Wire Line
	5800 2700 7700 2700
Wire Wire Line
	6100 2550 6100 2800
Wire Wire Line
	5400 2800 6100 2800
Connection ~ 6100 2800
Wire Wire Line
	6100 2800 7700 2800
Wire Wire Line
	6400 2550 6400 2900
Connection ~ 6400 2900
Wire Wire Line
	6400 2900 7700 2900
Wire Wire Line
	6700 2550 6700 3000
Wire Wire Line
	5600 3000 6700 3000
Connection ~ 6700 3000
Wire Wire Line
	6700 3000 7700 3000
Wire Wire Line
	7000 2550 7000 3100
Connection ~ 7000 3100
Wire Wire Line
	7000 3100 7700 3100
Wire Wire Line
	7300 2550 7300 3200
Connection ~ 7300 3200
Wire Wire Line
	7300 3200 7700 3200
Wire Wire Line
	7600 2550 7600 3300
Connection ~ 7600 3300
Wire Wire Line
	7600 3300 7700 3300
Wire Wire Line
	5500 2200 5500 2250
Wire Wire Line
	5800 2250 5800 2200
Wire Wire Line
	6100 2200 6100 2250
Wire Wire Line
	6400 2200 6400 2250
Wire Wire Line
	6700 2200 6700 2250
Wire Wire Line
	7000 2200 7000 2250
Wire Wire Line
	7300 2200 7300 2250
Wire Wire Line
	7600 2200 7600 2250
Wire Wire Line
	8200 2200 8200 2250
$Comp
L power:VCC #PWR027
U 1 1 5F36BC24
P 8200 2200
F 0 "#PWR027" H 8200 2050 50  0001 C CNN
F 1 "VCC" H 8217 2373 50  0000 C CNN
F 2 "" H 8200 2200 50  0001 C CNN
F 3 "" H 8200 2200 50  0001 C CNN
	1    8200 2200
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR029
U 1 1 5F4B1E72
P 7900 1800
F 0 "#PWR029" H 7900 1550 50  0001 C CNN
F 1 "GND" H 7905 1627 50  0000 C CNN
F 2 "" H 7900 1800 50  0001 C CNN
F 3 "" H 7900 1800 50  0001 C CNN
	1    7900 1800
	1    0    0    -1  
$EndComp
Wire Wire Line
	7900 1800 7900 1750
Wire Wire Line
	7900 1750 7600 1750
Wire Wire Line
	5500 1750 5500 1900
Wire Wire Line
	5800 1900 5800 1750
Connection ~ 5800 1750
Wire Wire Line
	5800 1750 5500 1750
Wire Wire Line
	6100 1900 6100 1750
Connection ~ 6100 1750
Wire Wire Line
	6100 1750 5800 1750
Wire Wire Line
	6400 1900 6400 1750
Connection ~ 6400 1750
Wire Wire Line
	6400 1750 6100 1750
Wire Wire Line
	6700 1900 6700 1750
Connection ~ 6700 1750
Wire Wire Line
	6700 1750 6400 1750
Wire Wire Line
	7000 1750 7000 1900
Connection ~ 7000 1750
Wire Wire Line
	7000 1750 6700 1750
Wire Wire Line
	7300 1900 7300 1750
Connection ~ 7300 1750
Wire Wire Line
	7300 1750 7000 1750
Wire Wire Line
	7600 1900 7600 1750
Connection ~ 7600 1750
Wire Wire Line
	7600 1750 7300 1750
$Comp
L 74xx:74LS541 U12
U 1 1 5F36314F
P 8200 3100
F 0 "U12" H 8300 3850 50  0000 C CNN
F 1 "74HCT541N" H 8450 3750 50  0000 C CNN
F 2 "" H 8200 3100 50  0001 C CNN
F 3 "http://www.ti.com/lit/gpn/sn74LS541" H 8200 3100 50  0001 C CNN
	1    8200 3100
	1    0    0    -1  
$EndComp
$Comp
L Device:R R12
U 1 1 5F4E3AC0
P 5500 2400
F 0 "R12" H 5570 2446 50  0000 L CNN
F 1 "4.7k" H 5570 2355 50  0000 L CNN
F 2 "" V 5430 2400 50  0001 C CNN
F 3 "~" H 5500 2400 50  0001 C CNN
	1    5500 2400
	1    0    0    -1  
$EndComp
$Comp
L Device:R R13
U 1 1 5F4E3AC6
P 5800 2400
F 0 "R13" H 5870 2446 50  0000 L CNN
F 1 "4.7k" H 5870 2355 50  0000 L CNN
F 2 "" V 5730 2400 50  0001 C CNN
F 3 "~" H 5800 2400 50  0001 C CNN
	1    5800 2400
	1    0    0    -1  
$EndComp
$Comp
L Device:R R14
U 1 1 5F4E70B3
P 6100 2400
F 0 "R14" H 6170 2446 50  0000 L CNN
F 1 "4.7k" H 6170 2355 50  0000 L CNN
F 2 "" V 6030 2400 50  0001 C CNN
F 3 "~" H 6100 2400 50  0001 C CNN
	1    6100 2400
	1    0    0    -1  
$EndComp
$Comp
L Device:R R15
U 1 1 5F4E70B9
P 6400 2400
F 0 "R15" H 6470 2446 50  0000 L CNN
F 1 "4.7k" H 6470 2355 50  0000 L CNN
F 2 "" V 6330 2400 50  0001 C CNN
F 3 "~" H 6400 2400 50  0001 C CNN
	1    6400 2400
	1    0    0    -1  
$EndComp
$Comp
L Device:R R16
U 1 1 5F4EA520
P 6700 2400
F 0 "R16" H 6770 2446 50  0000 L CNN
F 1 "4.7k" H 6770 2355 50  0000 L CNN
F 2 "" V 6630 2400 50  0001 C CNN
F 3 "~" H 6700 2400 50  0001 C CNN
	1    6700 2400
	1    0    0    -1  
$EndComp
$Comp
L Device:R R17
U 1 1 5F4EA526
P 7000 2400
F 0 "R17" H 7070 2446 50  0000 L CNN
F 1 "4.7k" H 7070 2355 50  0000 L CNN
F 2 "" V 6930 2400 50  0001 C CNN
F 3 "~" H 7000 2400 50  0001 C CNN
	1    7000 2400
	1    0    0    -1  
$EndComp
$Comp
L Device:R R18
U 1 1 5F4ED843
P 7300 2400
F 0 "R18" H 7370 2446 50  0000 L CNN
F 1 "4.7k" H 7370 2355 50  0000 L CNN
F 2 "" V 7230 2400 50  0001 C CNN
F 3 "~" H 7300 2400 50  0001 C CNN
	1    7300 2400
	1    0    0    -1  
$EndComp
$Comp
L Device:R R19
U 1 1 5F4ED849
P 7600 2400
F 0 "R19" H 7670 2446 50  0000 L CNN
F 1 "4.7k" H 7670 2355 50  0000 L CNN
F 2 "" V 7530 2400 50  0001 C CNN
F 3 "~" H 7600 2400 50  0001 C CNN
	1    7600 2400
	1    0    0    -1  
$EndComp
Text HLabel 4350 6000 0    50   Input ~ 0
~RST
Text HLabel 4350 3600 0    50   Input ~ 0
~RST
Wire Wire Line
	3800 2250 3800 3700
Wire Wire Line
	4300 3250 4350 3250
Wire Wire Line
	4350 3250 4350 3200
Wire Wire Line
	4350 3200 4400 3200
Wire Wire Line
	4350 3250 4350 3300
Wire Wire Line
	4350 3300 4400 3300
Connection ~ 4350 3250
Text HLabel 4350 5500 0    50   Input ~ 0
~PC_IN
$Comp
L Device:C_Small C15
U 1 1 5F3A023B
P 3800 6200
F 0 "C15" H 3892 6246 50  0000 L CNN
F 1 "0.1u" H 3892 6155 50  0000 L CNN
F 2 "" H 3800 6200 50  0001 C CNN
F 3 "~" H 3800 6200 50  0001 C CNN
	1    3800 6200
	1    0    0    -1  
$EndComp
Wire Wire Line
	4900 6300 4900 6350
Wire Wire Line
	3800 6300 3800 6350
Wire Wire Line
	3800 6350 4900 6350
Connection ~ 4900 6350
Wire Wire Line
	4900 6350 4900 6400
Wire Wire Line
	3800 4650 3800 6100
Text Notes 1450 5400 0    50   ~ 0
The carry out from the above counter is fed into CP,\nwhich is Clock Pulse.  PC_INC will be set on the falling\nedge by the uCode EEPROMS.  CP will be an output from \nthe previous counter.  No CLK necessary since we never\nwant to count this with the CLK, only as a carryout.
Text HLabel 4350 3400 0    50   Input ~ 0
CLK
Wire Wire Line
	3750 4300 3750 5650
Wire Wire Line
	3750 5650 4350 5650
Wire Wire Line
	4350 5650 4350 5600
Wire Wire Line
	4350 5600 4400 5600
Wire Wire Line
	4350 5650 4350 5700
Wire Wire Line
	4350 5700 4400 5700
Connection ~ 4350 5650
Wire Wire Line
	4350 5800 4400 5800
Text HLabel 4350 5800 0    50   Input ~ 0
CLK
$EndSCHEMATC
