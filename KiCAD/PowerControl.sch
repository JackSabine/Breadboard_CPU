EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 2 9
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
L Breadboard_CPU-rescue:Q_PMOS_GDS-Device Q201
U 1 1 5EFC0CE7
P 3900 2900
F 0 "Q201" V 4242 2900 50  0000 C CNN
F 1 "Q_PMOS_GDS" V 4151 2900 50  0000 C CNN
F 2 "" H 4100 3000 50  0001 C CNN
F 3 "~" H 3900 2900 50  0001 C CNN
	1    3900 2900
	0    -1   -1   0   
$EndComp
Wire Wire Line
	3250 2800 3700 2800
$Comp
L Breadboard_CPU-rescue:GND-power #PWR0202
U 1 1 5EFC2D0B
P 3450 3550
F 0 "#PWR0202" H 3450 3300 50  0001 C CNN
F 1 "GND" H 3455 3377 50  0000 C CNN
F 2 "" H 3450 3550 50  0001 C CNN
F 3 "" H 3450 3550 50  0001 C CNN
	1    3450 3550
	1    0    0    -1  
$EndComp
Wire Wire Line
	3300 3100 3450 3100
Wire Wire Line
	3450 3100 3450 3550
$Comp
L Breadboard_CPU-rescue:R-Device R201
U 1 1 5EFC37FA
P 3900 3350
F 0 "R201" H 3970 3396 50  0000 L CNN
F 1 "10k" H 3970 3305 50  0000 L CNN
F 2 "" V 3830 3350 50  0001 C CNN
F 3 "~" H 3900 3350 50  0001 C CNN
	1    3900 3350
	1    0    0    -1  
$EndComp
$Comp
L Breadboard_CPU-rescue:LM1085-5.0-Regulator_Linear U201
U 1 1 5EFC3C14
P 5600 2800
F 0 "U201" H 5600 3042 50  0000 C CNN
F 1 "LM1085-5.0" H 5600 2951 50  0000 C CNN
F 2 "" H 5600 3050 50  0001 C CIN
F 3 "http://www.ti.com/lit/ds/symlink/lm1085.pdf" H 5600 2800 50  0001 C CNN
	1    5600 2800
	1    0    0    -1  
$EndComp
$Comp
L Breadboard_CPU-rescue:C_Small-Device C201
U 1 1 5EFC5530
P 4900 3250
F 0 "C201" H 4992 3296 50  0000 L CNN
F 1 "10u" H 4992 3205 50  0000 L CNN
F 2 "" H 4900 3250 50  0001 C CNN
F 3 "~" H 4900 3250 50  0001 C CNN
	1    4900 3250
	1    0    0    -1  
$EndComp
$Comp
L Breadboard_CPU-rescue:C_Small-Device C202
U 1 1 5EFC61B4
P 5600 3250
F 0 "C202" H 5692 3296 50  0000 L CNN
F 1 "10u" H 5692 3205 50  0000 L CNN
F 2 "" H 5600 3250 50  0001 C CNN
F 3 "~" H 5600 3250 50  0001 C CNN
	1    5600 3250
	1    0    0    -1  
$EndComp
$Comp
L Breadboard_CPU-rescue:C_Small-Device C203
U 1 1 5EFC64B7
P 6000 3250
F 0 "C203" H 6092 3296 50  0000 L CNN
F 1 "100u" H 6092 3205 50  0000 L CNN
F 2 "" H 6000 3250 50  0001 C CNN
F 3 "~" H 6000 3250 50  0001 C CNN
	1    6000 3250
	1    0    0    -1  
$EndComp
$Comp
L Breadboard_CPU-rescue:GND-power #PWR0205
U 1 1 5EFC6BF9
P 5600 3550
F 0 "#PWR0205" H 5600 3300 50  0001 C CNN
F 1 "GND" H 5605 3377 50  0000 C CNN
F 2 "" H 5600 3550 50  0001 C CNN
F 3 "" H 5600 3550 50  0001 C CNN
	1    5600 3550
	1    0    0    -1  
$EndComp
$Comp
L Breadboard_CPU-rescue:GND-power #PWR0206
U 1 1 5EFC748C
P 6000 3550
F 0 "#PWR0206" H 6000 3300 50  0001 C CNN
F 1 "GND" H 6005 3377 50  0000 C CNN
F 2 "" H 6000 3550 50  0001 C CNN
F 3 "" H 6000 3550 50  0001 C CNN
	1    6000 3550
	1    0    0    -1  
$EndComp
$Comp
L Breadboard_CPU-rescue:GND-power #PWR0203
U 1 1 5EFC834C
P 3900 3550
F 0 "#PWR0203" H 3900 3300 50  0001 C CNN
F 1 "GND" H 3905 3377 50  0000 C CNN
F 2 "" H 3900 3550 50  0001 C CNN
F 3 "" H 3900 3550 50  0001 C CNN
	1    3900 3550
	1    0    0    -1  
$EndComp
$Comp
L Breadboard_CPU-rescue:GND-power #PWR0204
U 1 1 5EFC8352
P 4900 3550
F 0 "#PWR0204" H 4900 3300 50  0001 C CNN
F 1 "GND" H 4905 3377 50  0000 C CNN
F 2 "" H 4900 3550 50  0001 C CNN
F 3 "" H 4900 3550 50  0001 C CNN
	1    4900 3550
	1    0    0    -1  
$EndComp
Wire Wire Line
	5900 2800 6000 2800
Wire Wire Line
	6000 3150 6000 2800
Connection ~ 6000 2800
Wire Wire Line
	6000 3350 6000 3550
Wire Wire Line
	5600 3100 5600 3150
Wire Wire Line
	5600 3350 5600 3550
Wire Wire Line
	4900 3350 4900 3550
Wire Wire Line
	4900 3150 4900 2800
Connection ~ 4900 2800
Wire Wire Line
	4900 2800 5300 2800
Wire Wire Line
	3900 3500 3900 3550
Wire Wire Line
	6400 3500 6400 3550
Wire Wire Line
	6400 3150 6400 3200
$Comp
L Breadboard_CPU-rescue:GND-power #PWR0207
U 1 1 5EFD7367
P 6400 3550
F 0 "#PWR0207" H 6400 3300 50  0001 C CNN
F 1 "GND" H 6405 3377 50  0000 C CNN
F 2 "" H 6400 3550 50  0001 C CNN
F 3 "" H 6400 3550 50  0001 C CNN
	1    6400 3550
	1    0    0    -1  
$EndComp
$Comp
L Breadboard_CPU-rescue:R-Device R202
U 1 1 5EFD633B
P 6400 3350
F 0 "R202" H 6470 3396 50  0000 L CNN
F 1 "4.7k" H 6470 3305 50  0000 L CNN
F 2 "" V 6330 3350 50  0001 C CNN
F 3 "~" H 6400 3350 50  0001 C CNN
	1    6400 3350
	1    0    0    -1  
$EndComp
$Comp
L Breadboard_CPU-rescue:LED-Device D202
U 1 1 5EFD4D26
P 6400 3000
F 0 "D202" V 6439 2882 50  0000 R CNN
F 1 "Power" V 6348 2882 50  0000 R CNN
F 2 "" H 6400 3000 50  0001 C CNN
F 3 "~" H 6400 3000 50  0001 C CNN
	1    6400 3000
	0    -1   -1   0   
$EndComp
Wire Wire Line
	6000 2800 6400 2800
Wire Wire Line
	6400 2800 6400 2850
Connection ~ 6400 2800
$Comp
L Breadboard_CPU-rescue:VS-power #PWR0201
U 1 1 5F035B21
P 3250 2800
F 0 "#PWR0201" H 3050 2650 50  0001 C CNN
F 1 "VS" V 3268 2928 50  0000 L CNN
F 2 "" H 3250 2800 50  0001 C CNN
F 3 "" H 3250 2800 50  0001 C CNN
	1    3250 2800
	0    -1   -1   0   
$EndComp
Text GLabel 3300 3100 0    50   Input ~ 0
GND
Wire Wire Line
	3900 3100 3900 3200
Wire Wire Line
	4100 2800 4900 2800
$Comp
L power:+5V #PWR?
U 1 1 61C195D7
P 6600 2800
AR Path="/5F05F116/61C195D7" Ref="#PWR?"  Part="1" 
AR Path="/5EFC0AE0/61C195D7" Ref="#PWR?"  Part="1" 
F 0 "#PWR?" H 6600 2650 50  0001 C CNN
F 1 "+5V" H 6615 2973 50  0000 C CNN
F 2 "" H 6600 2800 50  0001 C CNN
F 3 "" H 6600 2800 50  0001 C CNN
	1    6600 2800
	1    0    0    -1  
$EndComp
Wire Wire Line
	6400 2800 6600 2800
$EndSCHEMATC
