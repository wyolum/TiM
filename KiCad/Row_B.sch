EESchema Schematic File Version 2  date 2/16/2013 3:37:27 PM
LIBS:RowGB_sym
LIBS:power
LIBS:TiM-cache
EELAYER 25  0
EELAYER END
$Descr A4 11700 8267
encoding utf-8
Sheet 8 9
Title "TiM - The Intelligent Matrix"
Date "16 feb 2013"
Rev ""
Comp "WyoLum"
Comment1 "www.wyolum.com"
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
Text Label 950  900  0    60   ~ 0
DI_B
Text HLabel 950  3100 0    60   Output ~ 0
DO_B
Text HLabel 950  2350 0    60   Input ~ 0
GND
Text HLabel 950  900  0    60   Input ~ 0
DI_B
Text HLabel 950  750  0    60   Input ~ 0
5V
$Comp
L RGB_WS2811 U201
U 1 1 5118ABBA
P 1525 1575
F 0 "U201" V 1300 1575 60  0000 C CNN
F 1 "RGB_WS2811" V 1925 1550 60  0000 C CNN
F 2 "RGB_WS2811" H 1425 1975 60  0001 C CNN
	1    1525 1575
	1    0    0    -1  
$EndComp
NoConn ~ 1400 2200
NoConn ~ 2550 2200
NoConn ~ 3700 2200
NoConn ~ 4850 2200
NoConn ~ 6000 2200
NoConn ~ 7150 2200
NoConn ~ 8300 2200
NoConn ~ 9450 2200
NoConn ~ 9450 4900
NoConn ~ 8300 4900
NoConn ~ 7150 4900
NoConn ~ 6000 4900
NoConn ~ 4850 4900
NoConn ~ 3700 4900
NoConn ~ 2550 4900
NoConn ~ 1400 4900
Text Label 950  750  0    60   ~ 0
5V
Text Label 950  2350 0    60   ~ 0
GND
Text Label 950  2850 0    60   ~ 0
5V
Text Label 950  3100 0    60   ~ 0
DO_B
Text Label 950  3450 0    60   ~ 0
5V
Text Label 950  5050 0    60   ~ 0
GND
Text Label 950  5550 0    60   ~ 0
5V
Text Label 1800 900  0    60   ~ 0
B_02
Text Label 2950 900  0    60   ~ 0
B_03
Text Label 4100 900  0    60   ~ 0
B_04
Text Label 5250 900  0    60   ~ 0
B_05
Text Label 6400 900  0    60   ~ 0
B_06
Text Label 7550 900  0    60   ~ 0
B_07
Text Label 8700 900  0    60   ~ 0
B_08
Text Label 9850 900  0    60   ~ 0
B_09
Text Label 1800 3600 0    60   ~ 0
B_10
Text Label 2950 3600 0    60   ~ 0
B_11
Text Label 4100 3600 0    60   ~ 0
B_12
Text Label 5250 3600 0    60   ~ 0
B_13
Text Label 6400 3600 0    60   ~ 0
B_14
Text Label 7550 3600 0    60   ~ 0
B_15
Text Label 8700 3600 0    60   ~ 0
B_16
$Comp
L C2 C201
U 1 1 5118AB58
P 1800 2600
F 0 "C201" H 1825 2700 50  0000 L CNN
F 1 "100n" H 1825 2500 50  0000 L CNN
F 2 "c_0805" H 1800 2600 50  0001 C CNN
F 4 "CAP CER 0.1UF 25V 10% X7R 0805" H 1800 2800 60  0001 L CNN "Field4"
F 5 "100nF, 25V" H 1800 2900 60  0001 L CNN "Field5"
F 6 "Surface Mount, MLCC" H 1800 3000 60  0001 L CNN "Field6"
F 7 "Kemet" H 1800 3100 60  0001 L CNN "Field7"
F 8 "C0805C104K3RACTU" H 1800 3200 60  0001 L CNN "Field8"
F 9 "Digikey" H 1800 3300 60  0001 L CNN "Field9"
F 10 "399-1168-1-ND" H 1800 3400 60  0001 L CNN "Field10"
F 11 "http://www.digikey.com/product-detail/en/C0805C104K3RACTU/399-1168-1-ND/411443" H 1800 3500 60  0001 L CNN "Field11"
	1    1800 2600
	1    0    0    -1  
$EndComp
$Comp
L C2 C202
U 1 1 5118ABB0
P 2950 2600
F 0 "C202" H 2975 2700 50  0000 L CNN
F 1 "100n" H 2975 2500 50  0000 L CNN
F 2 "c_0805" H 2950 2600 50  0001 C CNN
F 4 "CAP CER 0.1UF 25V 10% X7R 0805" H 2950 2800 60  0001 L CNN "Field4"
F 5 "100nF, 25V" H 2950 2900 60  0001 L CNN "Field5"
F 6 "Surface Mount, MLCC" H 2950 3000 60  0001 L CNN "Field6"
F 7 "Kemet" H 2950 3100 60  0001 L CNN "Field7"
F 8 "C0805C104K3RACTU" H 2950 3200 60  0001 L CNN "Field8"
F 9 "Digikey" H 2950 3300 60  0001 L CNN "Field9"
F 10 "399-1168-1-ND" H 2950 3400 60  0001 L CNN "Field10"
F 11 "http://www.digikey.com/product-detail/en/C0805C104K3RACTU/399-1168-1-ND/411443" H 2950 3500 60  0001 L CNN "Field11"
	1    2950 2600
	1    0    0    -1  
$EndComp
$Comp
L C2 C203
U 1 1 5118AB51
P 4100 2600
F 0 "C203" H 4125 2700 50  0000 L CNN
F 1 "100n" H 4125 2500 50  0000 L CNN
F 2 "c_0805" H 4100 2600 50  0001 C CNN
F 4 "CAP CER 0.1UF 25V 10% X7R 0805" H 4100 2800 60  0001 L CNN "Field4"
F 5 "100nF, 25V" H 4100 2900 60  0001 L CNN "Field5"
F 6 "Surface Mount, MLCC" H 4100 3000 60  0001 L CNN "Field6"
F 7 "Kemet" H 4100 3100 60  0001 L CNN "Field7"
F 8 "C0805C104K3RACTU" H 4100 3200 60  0001 L CNN "Field8"
F 9 "Digikey" H 4100 3300 60  0001 L CNN "Field9"
F 10 "399-1168-1-ND" H 4100 3400 60  0001 L CNN "Field10"
F 11 "http://www.digikey.com/product-detail/en/C0805C104K3RACTU/399-1168-1-ND/411443" H 4100 3500 60  0001 L CNN "Field11"
	1    4100 2600
	1    0    0    -1  
$EndComp
$Comp
L C2 C204
U 1 1 5118AB49
P 5250 2600
F 0 "C204" H 5275 2700 50  0000 L CNN
F 1 "100n" H 5275 2500 50  0000 L CNN
F 2 "c_0805" H 5250 2600 50  0001 C CNN
F 4 "CAP CER 0.1UF 25V 10% X7R 0805" H 5250 2800 60  0001 L CNN "Field4"
F 5 "100nF, 25V" H 5250 2900 60  0001 L CNN "Field5"
F 6 "Surface Mount, MLCC" H 5250 3000 60  0001 L CNN "Field6"
F 7 "Kemet" H 5250 3100 60  0001 L CNN "Field7"
F 8 "C0805C104K3RACTU" H 5250 3200 60  0001 L CNN "Field8"
F 9 "Digikey" H 5250 3300 60  0001 L CNN "Field9"
F 10 "399-1168-1-ND" H 5250 3400 60  0001 L CNN "Field10"
F 11 "http://www.digikey.com/product-detail/en/C0805C104K3RACTU/399-1168-1-ND/411443" H 5250 3500 60  0001 L CNN "Field11"
	1    5250 2600
	1    0    0    -1  
$EndComp
$Comp
L C2 C205
U 1 1 5116895D
P 6400 2600
F 0 "C205" H 6425 2700 50  0000 L CNN
F 1 "100n" H 6425 2500 50  0000 L CNN
F 2 "c_0805" H 6400 2600 50  0001 C CNN
F 4 "CAP CER 0.1UF 25V 10% X7R 0805" H 6400 2800 60  0001 L CNN "Field4"
F 5 "100nF, 25V" H 6400 2900 60  0001 L CNN "Field5"
F 6 "Surface Mount, MLCC" H 6400 3000 60  0001 L CNN "Field6"
F 7 "Kemet" H 6400 3100 60  0001 L CNN "Field7"
F 8 "C0805C104K3RACTU" H 6400 3200 60  0001 L CNN "Field8"
F 9 "Digikey" H 6400 3300 60  0001 L CNN "Field9"
F 10 "399-1168-1-ND" H 6400 3400 60  0001 L CNN "Field10"
F 11 "http://www.digikey.com/product-detail/en/C0805C104K3RACTU/399-1168-1-ND/411443" H 6400 3500 60  0001 L CNN "Field11"
	1    6400 2600
	1    0    0    -1  
$EndComp
$Comp
L C2 C206
U 1 1 5118AB3A
P 7550 2600
F 0 "C206" H 7575 2700 50  0000 L CNN
F 1 "100n" H 7575 2500 50  0000 L CNN
F 2 "c_0805" H 7550 2600 50  0001 C CNN
F 4 "CAP CER 0.1UF 25V 10% X7R 0805" H 7550 2800 60  0001 L CNN "Field4"
F 5 "100nF, 25V" H 7550 2900 60  0001 L CNN "Field5"
F 6 "Surface Mount, MLCC" H 7550 3000 60  0001 L CNN "Field6"
F 7 "Kemet" H 7550 3100 60  0001 L CNN "Field7"
F 8 "C0805C104K3RACTU" H 7550 3200 60  0001 L CNN "Field8"
F 9 "Digikey" H 7550 3300 60  0001 L CNN "Field9"
F 10 "399-1168-1-ND" H 7550 3400 60  0001 L CNN "Field10"
F 11 "http://www.digikey.com/product-detail/en/C0805C104K3RACTU/399-1168-1-ND/411443" H 7550 3500 60  0001 L CNN "Field11"
	1    7550 2600
	1    0    0    -1  
$EndComp
$Comp
L C2 C207
U 1 1 5118AB32
P 8700 2600
F 0 "C207" H 8725 2700 50  0000 L CNN
F 1 "100n" H 8725 2500 50  0000 L CNN
F 2 "c_0805" H 8700 2600 50  0001 C CNN
F 4 "CAP CER 0.1UF 25V 10% X7R 0805" H 8700 2800 60  0001 L CNN "Field4"
F 5 "100nF, 25V" H 8700 2900 60  0001 L CNN "Field5"
F 6 "Surface Mount, MLCC" H 8700 3000 60  0001 L CNN "Field6"
F 7 "Kemet" H 8700 3100 60  0001 L CNN "Field7"
F 8 "C0805C104K3RACTU" H 8700 3200 60  0001 L CNN "Field8"
F 9 "Digikey" H 8700 3300 60  0001 L CNN "Field9"
F 10 "399-1168-1-ND" H 8700 3400 60  0001 L CNN "Field10"
F 11 "http://www.digikey.com/product-detail/en/C0805C104K3RACTU/399-1168-1-ND/411443" H 8700 3500 60  0001 L CNN "Field11"
	1    8700 2600
	1    0    0    -1  
$EndComp
$Comp
L C2 C208
U 1 1 5118AB2A
P 9850 2600
F 0 "C208" H 9875 2700 50  0000 L CNN
F 1 "100n" H 9875 2500 50  0000 L CNN
F 2 "c_0805" H 9850 2600 50  0001 C CNN
F 4 "CAP CER 0.1UF 25V 10% X7R 0805" H 9850 2800 60  0001 L CNN "Field4"
F 5 "100nF, 25V" H 9850 2900 60  0001 L CNN "Field5"
F 6 "Surface Mount, MLCC" H 9850 3000 60  0001 L CNN "Field6"
F 7 "Kemet" H 9850 3100 60  0001 L CNN "Field7"
F 8 "C0805C104K3RACTU" H 9850 3200 60  0001 L CNN "Field8"
F 9 "Digikey" H 9850 3300 60  0001 L CNN "Field9"
F 10 "399-1168-1-ND" H 9850 3400 60  0001 L CNN "Field10"
F 11 "http://www.digikey.com/product-detail/en/C0805C104K3RACTU/399-1168-1-ND/411443" H 9850 3500 60  0001 L CNN "Field11"
	1    9850 2600
	1    0    0    -1  
$EndComp
$Comp
L C2 C209
U 1 1 5118AB23
P 1800 5300
F 0 "C209" H 1825 5400 50  0000 L CNN
F 1 "100n" H 1825 5200 50  0000 L CNN
F 2 "c_0805" H 1800 5300 50  0001 C CNN
F 4 "CAP CER 0.1UF 25V 10% X7R 0805" H 1800 5500 60  0001 L CNN "Field4"
F 5 "100nF, 25V" H 1800 5600 60  0001 L CNN "Field5"
F 6 "Surface Mount, MLCC" H 1800 5700 60  0001 L CNN "Field6"
F 7 "Kemet" H 1800 5800 60  0001 L CNN "Field7"
F 8 "C0805C104K3RACTU" H 1800 5900 60  0001 L CNN "Field8"
F 9 "Digikey" H 1800 6000 60  0001 L CNN "Field9"
F 10 "399-1168-1-ND" H 1800 6100 60  0001 L CNN "Field10"
F 11 "http://www.digikey.com/product-detail/en/C0805C104K3RACTU/399-1168-1-ND/411443" H 1800 6200 60  0001 L CNN "Field11"
	1    1800 5300
	1    0    0    -1  
$EndComp
$Comp
L C2 C210
U 1 1 5118ABAA
P 2950 5300
F 0 "C210" H 2975 5400 50  0000 L CNN
F 1 "100n" H 2975 5200 50  0000 L CNN
F 2 "c_0805" H 2950 5300 50  0001 C CNN
F 4 "CAP CER 0.1UF 25V 10% X7R 0805" H 2950 5500 60  0001 L CNN "Field4"
F 5 "100nF, 25V" H 2950 5600 60  0001 L CNN "Field5"
F 6 "Surface Mount, MLCC" H 2950 5700 60  0001 L CNN "Field6"
F 7 "Kemet" H 2950 5800 60  0001 L CNN "Field7"
F 8 "C0805C104K3RACTU" H 2950 5900 60  0001 L CNN "Field8"
F 9 "Digikey" H 2950 6000 60  0001 L CNN "Field9"
F 10 "399-1168-1-ND" H 2950 6100 60  0001 L CNN "Field10"
F 11 "http://www.digikey.com/product-detail/en/C0805C104K3RACTU/399-1168-1-ND/411443" H 2950 6200 60  0001 L CNN "Field11"
	1    2950 5300
	1    0    0    -1  
$EndComp
$Comp
L C2 C211
U 1 1 5118ABA6
P 4100 5300
F 0 "C211" H 4125 5400 50  0000 L CNN
F 1 "100n" H 4125 5200 50  0000 L CNN
F 2 "c_0805" H 4100 5300 50  0001 C CNN
F 4 "CAP CER 0.1UF 25V 10% X7R 0805" H 4100 5500 60  0001 L CNN "Field4"
F 5 "100nF, 25V" H 4100 5600 60  0001 L CNN "Field5"
F 6 "Surface Mount, MLCC" H 4100 5700 60  0001 L CNN "Field6"
F 7 "Kemet" H 4100 5800 60  0001 L CNN "Field7"
F 8 "C0805C104K3RACTU" H 4100 5900 60  0001 L CNN "Field8"
F 9 "Digikey" H 4100 6000 60  0001 L CNN "Field9"
F 10 "399-1168-1-ND" H 4100 6100 60  0001 L CNN "Field10"
F 11 "http://www.digikey.com/product-detail/en/C0805C104K3RACTU/399-1168-1-ND/411443" H 4100 6200 60  0001 L CNN "Field11"
	1    4100 5300
	1    0    0    -1  
$EndComp
$Comp
L C2 C212
U 1 1 5118AB22
P 5250 5300
F 0 "C212" H 5275 5400 50  0000 L CNN
F 1 "100n" H 5275 5200 50  0000 L CNN
F 2 "c_0805" H 5250 5300 50  0001 C CNN
F 4 "CAP CER 0.1UF 25V 10% X7R 0805" H 5250 5500 60  0001 L CNN "Field4"
F 5 "100nF, 25V" H 5250 5600 60  0001 L CNN "Field5"
F 6 "Surface Mount, MLCC" H 5250 5700 60  0001 L CNN "Field6"
F 7 "Kemet" H 5250 5800 60  0001 L CNN "Field7"
F 8 "C0805C104K3RACTU" H 5250 5900 60  0001 L CNN "Field8"
F 9 "Digikey" H 5250 6000 60  0001 L CNN "Field9"
F 10 "399-1168-1-ND" H 5250 6100 60  0001 L CNN "Field10"
F 11 "http://www.digikey.com/product-detail/en/C0805C104K3RACTU/399-1168-1-ND/411443" H 5250 6200 60  0001 L CNN "Field11"
	1    5250 5300
	1    0    0    -1  
$EndComp
$Comp
L C2 C213
U 1 1 5118AB9E
P 6400 5300
F 0 "C213" H 6425 5400 50  0000 L CNN
F 1 "100n" H 6425 5200 50  0000 L CNN
F 2 "c_0805" H 6400 5300 50  0001 C CNN
F 4 "CAP CER 0.1UF 25V 10% X7R 0805" H 6400 5500 60  0001 L CNN "Field4"
F 5 "100nF, 25V" H 6400 5600 60  0001 L CNN "Field5"
F 6 "Surface Mount, MLCC" H 6400 5700 60  0001 L CNN "Field6"
F 7 "Kemet" H 6400 5800 60  0001 L CNN "Field7"
F 8 "C0805C104K3RACTU" H 6400 5900 60  0001 L CNN "Field8"
F 9 "Digikey" H 6400 6000 60  0001 L CNN "Field9"
F 10 "399-1168-1-ND" H 6400 6100 60  0001 L CNN "Field10"
F 11 "http://www.digikey.com/product-detail/en/C0805C104K3RACTU/399-1168-1-ND/411443" H 6400 6200 60  0001 L CNN "Field11"
	1    6400 5300
	1    0    0    -1  
$EndComp
$Comp
L C2 C214
U 1 1 5118AB96
P 7550 5300
F 0 "C214" H 7575 5400 50  0000 L CNN
F 1 "100n" H 7575 5200 50  0000 L CNN
F 2 "c_0805" H 7550 5300 50  0001 C CNN
F 4 "CAP CER 0.1UF 25V 10% X7R 0805" H 7550 5500 60  0001 L CNN "Field4"
F 5 "100nF, 25V" H 7550 5600 60  0001 L CNN "Field5"
F 6 "Surface Mount, MLCC" H 7550 5700 60  0001 L CNN "Field6"
F 7 "Kemet" H 7550 5800 60  0001 L CNN "Field7"
F 8 "C0805C104K3RACTU" H 7550 5900 60  0001 L CNN "Field8"
F 9 "Digikey" H 7550 6000 60  0001 L CNN "Field9"
F 10 "399-1168-1-ND" H 7550 6100 60  0001 L CNN "Field10"
F 11 "http://www.digikey.com/product-detail/en/C0805C104K3RACTU/399-1168-1-ND/411443" H 7550 6200 60  0001 L CNN "Field11"
	1    7550 5300
	1    0    0    -1  
$EndComp
$Comp
L C2 C215
U 1 1 5118AB1B
P 8700 5300
F 0 "C215" H 8725 5400 50  0000 L CNN
F 1 "100n" H 8725 5200 50  0000 L CNN
F 2 "c_0805" H 8700 5300 50  0001 C CNN
F 4 "CAP CER 0.1UF 25V 10% X7R 0805" H 8700 5500 60  0001 L CNN "Field4"
F 5 "100nF, 25V" H 8700 5600 60  0001 L CNN "Field5"
F 6 "Surface Mount, MLCC" H 8700 5700 60  0001 L CNN "Field6"
F 7 "Kemet" H 8700 5800 60  0001 L CNN "Field7"
F 8 "C0805C104K3RACTU" H 8700 5900 60  0001 L CNN "Field8"
F 9 "Digikey" H 8700 6000 60  0001 L CNN "Field9"
F 10 "399-1168-1-ND" H 8700 6100 60  0001 L CNN "Field10"
F 11 "http://www.digikey.com/product-detail/en/C0805C104K3RACTU/399-1168-1-ND/411443" H 8700 6200 60  0001 L CNN "Field11"
	1    8700 5300
	1    0    0    -1  
$EndComp
$Comp
L C2 C216
U 1 1 5118AB0E
P 9850 5300
F 0 "C216" H 9875 5400 50  0000 L CNN
F 1 "100n" H 9875 5200 50  0000 L CNN
F 2 "c_0805" H 9850 5300 50  0001 C CNN
F 4 "CAP CER 0.1UF 25V 10% X7R 0805" H 9850 5500 60  0001 L CNN "Field4"
F 5 "100nF, 25V" H 9850 5600 60  0001 L CNN "Field5"
F 6 "Surface Mount, MLCC" H 9850 5700 60  0001 L CNN "Field6"
F 7 "Kemet" H 9850 5800 60  0001 L CNN "Field7"
F 8 "C0805C104K3RACTU" H 9850 5900 60  0001 L CNN "Field8"
F 9 "Digikey" H 9850 6000 60  0001 L CNN "Field9"
F 10 "399-1168-1-ND" H 9850 6100 60  0001 L CNN "Field10"
F 11 "http://www.digikey.com/product-detail/en/C0805C104K3RACTU/399-1168-1-ND/411443" H 9850 6200 60  0001 L CNN "Field11"
	1    9850 5300
	1    0    0    -1  
$EndComp
$Comp
L RGB_WS2811 U202
U 1 1 5116894B
P 2675 1575
F 0 "U202" V 2450 1575 60  0000 C CNN
F 1 "RGB_WS2811" V 3075 1550 60  0000 C CNN
F 2 "RGB_WS2811" H 2575 1975 60  0001 C CNN
	1    2675 1575
	1    0    0    -1  
$EndComp
$Comp
L RGB_WS2811 U203
U 1 1 5118AB01
P 3825 1575
F 0 "U203" V 3600 1575 60  0000 C CNN
F 1 "RGB_WS2811" V 4225 1550 60  0000 C CNN
F 2 "RGB_WS2811" H 3725 1975 60  0001 C CNN
	1    3825 1575
	1    0    0    -1  
$EndComp
$Comp
L RGB_WS2811 U204
U 1 1 5118AB90
P 4975 1575
F 0 "U204" V 4750 1550 60  0000 C CNN
F 1 "RGB_WS2811" V 5375 1550 60  0000 C CNN
F 2 "RGB_WS2811" H 4875 1975 60  0001 C CNN
	1    4975 1575
	1    0    0    -1  
$EndComp
$Comp
L RGB_WS2811 U205
U 1 1 5118AAFB
P 6125 1575
F 0 "U205" V 5900 1550 60  0000 C CNN
F 1 "RGB_WS2811" V 6525 1525 60  0000 C CNN
F 2 "RGB_WS2811" H 6025 1975 60  0001 C CNN
	1    6125 1575
	1    0    0    -1  
$EndComp
$Comp
L RGB_WS2811 U206
U 1 1 5118AAF5
P 7275 1575
F 0 "U206" V 7050 1550 60  0000 C CNN
F 1 "RGB_WS2811" V 7675 1550 60  0000 C CNN
F 2 "RGB_WS2811" H 7175 1975 60  0001 C CNN
	1    7275 1575
	1    0    0    -1  
$EndComp
$Comp
L RGB_WS2811 U207
U 1 1 5118AAEE
P 8425 1575
F 0 "U207" V 8200 1550 60  0000 C CNN
F 1 "RGB_WS2811" V 8825 1550 60  0000 C CNN
F 2 "RGB_WS2811" H 8325 1975 60  0001 C CNN
	1    8425 1575
	1    0    0    -1  
$EndComp
$Comp
L RGB_WS2811 U208
U 1 1 5118AAEA
P 9575 1575
F 0 "U208" V 9350 1550 60  0000 C CNN
F 1 "RGB_WS2811" V 9975 1550 60  0000 C CNN
F 2 "RGB_WS2811" H 9475 1975 60  0001 C CNN
	1    9575 1575
	1    0    0    -1  
$EndComp
$Comp
L RGB_WS2811 U209
U 1 1 5118AAE1
P 1525 4275
F 0 "U209" V 1300 4250 60  0000 C CNN
F 1 "RGB_WS2811" V 1925 4250 60  0000 C CNN
F 2 "RGB_WS2811" H 1425 4675 60  0001 C CNN
	1    1525 4275
	1    0    0    -1  
$EndComp
$Comp
L RGB_WS2811 U210
U 1 1 5118AB86
P 2675 4275
F 0 "U210" V 2450 4250 60  0000 C CNN
F 1 "RGB_WS2811" V 3050 4225 60  0000 C CNN
F 2 "RGB_WS2811" H 2575 4675 60  0001 C CNN
	1    2675 4275
	1    0    0    -1  
$EndComp
$Comp
L RGB_WS2811 U211
U 1 1 5118AB7F
P 3825 4275
F 0 "U211" V 3600 4250 60  0000 C CNN
F 1 "RGB_WS2811" V 4225 4250 60  0000 C CNN
F 2 "RGB_WS2811" H 3725 4675 60  0001 C CNN
	1    3825 4275
	1    0    0    -1  
$EndComp
$Comp
L RGB_WS2811 U212
U 1 1 5118AAD6
P 4975 4275
F 0 "U212" V 4750 4250 60  0000 C CNN
F 1 "RGB_WS2811" V 5375 4250 60  0000 C CNN
F 2 "RGB_WS2811" H 4875 4675 60  0001 C CNN
	1    4975 4275
	1    0    0    -1  
$EndComp
$Comp
L RGB_WS2811 U213
U 1 1 5118AACF
P 6125 4275
F 0 "U213" V 5900 4250 60  0000 C CNN
F 1 "RGB_WS2811" V 6525 4250 60  0000 C CNN
F 2 "RGB_WS2811" H 6025 4675 60  0001 C CNN
	1    6125 4275
	1    0    0    -1  
$EndComp
$Comp
L RGB_WS2811 U214
U 1 1 5118AACA
P 7275 4275
F 0 "U214" V 7050 4250 60  0000 C CNN
F 1 "RGB_WS2811" V 7675 4225 60  0000 C CNN
F 2 "RGB_WS2811" H 7175 4675 60  0001 C CNN
	1    7275 4275
	1    0    0    -1  
$EndComp
$Comp
L RGB_WS2811 U215
U 1 1 5118AAC3
P 8425 4275
F 0 "U215" V 8200 4250 60  0000 C CNN
F 1 "RGB_WS2811" V 8825 4250 60  0000 C CNN
F 2 "RGB_WS2811" H 8325 4675 60  0001 C CNN
	1    8425 4275
	1    0    0    -1  
$EndComp
$Comp
L RGB_WS2811 U216
U 1 1 5118AABD
P 9575 4275
F 0 "U216" V 9350 4250 60  0000 C CNN
F 1 "RGB_WS2811" V 9975 4250 60  0000 C CNN
F 2 "RGB_WS2811" H 9475 4675 60  0001 C CNN
	1    9575 4275
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR010
U 1 1 5118AAB3
P 1150 2400
F 0 "#PWR010" H 1150 2400 30  0001 C CNN
F 1 "GND" H 1150 2330 30  0001 C CNN
	1    1150 2400
	1    0    0    -1  
$EndComp
Text Label 1250 6350 0    60   ~ 0
5V
Text Label 1250 7200 0    60   ~ 0
GND
$Comp
L C_POL_1 C217
U 1 1 5118AB5B
P 1250 6750
F 0 "C217" H 1375 6725 50  0000 L CNN
F 1 "47u,8V" H 1375 6625 50  0000 L CNN
F 2 "c_2917" H 1250 6700 50  0001 C CNN
F 4 "CAP ALUM 47UF 8V 20% SMD" H 1250 6950 60  0001 L CNN "Field4"
F 5 "47u,8V" H 1250 7050 60  0001 L CNN "Field5"
F 6 "2917 (7343 Metric)" H 1250 7150 60  0001 L CNN "Field6"
F 7 "Panasonic Electronic Components" H 1250 7250 60  0001 L CNN "Field7"
F 8 "EEF-CD0K470R" H 1250 7350 60  0001 L CNN "Field8"
F 9 "Digikey" H 1250 7450 60  0001 L CNN "Field9"
F 10 "PCE3606CT-ND" H 1250 7550 60  0001 L CNN "Field10"
F 11 "http://www.digikey.com/product-detail/en/EEF-CD0K470R/PCE3606CT-ND/614442" H 1250 7650 60  0001 L CNN "Field11"
	1    1250 6750
	1    0    0    -1  
$EndComp
Wire Wire Line
	1250 7000 1250 7200
Wire Wire Line
	1150 2400 1150 2350
Wire Wire Line
	1400 1000 1400 750 
Connection ~ 1800 5550
Wire Wire Line
	1800 5550 1800 5500
Connection ~ 2950 5550
Wire Wire Line
	2950 5550 2950 5500
Connection ~ 4100 5550
Wire Wire Line
	4100 5550 4100 5500
Connection ~ 5250 5550
Wire Wire Line
	5250 5550 5250 5500
Wire Wire Line
	6400 4900 6400 5100
Connection ~ 7550 5550
Wire Wire Line
	7550 5550 7550 5500
Wire Wire Line
	8700 4900 8700 5100
Connection ~ 9650 5550
Wire Wire Line
	950  5550 9850 5550
Wire Wire Line
	9850 5550 9850 5500
Connection ~ 9850 2350
Wire Wire Line
	9850 2200 9850 2400
Connection ~ 8700 2850
Wire Wire Line
	8700 2850 8700 2800
Connection ~ 7550 2850
Wire Wire Line
	7550 2850 7550 2800
Wire Wire Line
	6400 2200 6400 2400
Connection ~ 5250 2850
Wire Wire Line
	5250 2850 5250 2800
Connection ~ 4100 2850
Wire Wire Line
	4100 2850 4100 2800
Wire Wire Line
	2950 2200 2950 2400
Connection ~ 1800 2850
Wire Wire Line
	1800 2850 1800 2800
Wire Wire Line
	950  3100 9850 3100
Wire Wire Line
	9850 3100 9850 3700
Wire Wire Line
	8500 3700 8500 3600
Wire Wire Line
	8500 3600 7550 3600
Wire Wire Line
	7550 3600 7550 3700
Wire Wire Line
	6200 3700 6200 3600
Wire Wire Line
	6200 3600 5250 3600
Wire Wire Line
	5250 3600 5250 3700
Wire Wire Line
	3900 3700 3900 3600
Wire Wire Line
	3900 3600 2950 3600
Wire Wire Line
	2950 3600 2950 3700
Connection ~ 1600 5550
Connection ~ 2950 5050
Connection ~ 5250 5050
Connection ~ 7550 5050
Connection ~ 3900 5550
Wire Wire Line
	3900 5550 3900 4900
Connection ~ 6200 5550
Wire Wire Line
	6200 5550 6200 4900
Connection ~ 8500 5550
Wire Wire Line
	8500 5550 8500 4900
Connection ~ 3700 3450
Wire Wire Line
	3700 3450 3700 3700
Connection ~ 6000 3450
Wire Wire Line
	6000 3450 6000 3700
Connection ~ 8300 3450
Wire Wire Line
	8300 3700 8300 3450
Wire Wire Line
	1400 3450 1400 3700
Wire Wire Line
	9450 3700 9450 3450
Wire Wire Line
	7150 3450 7150 3700
Connection ~ 7150 3450
Wire Wire Line
	4850 3450 4850 3700
Connection ~ 4850 3450
Wire Wire Line
	2550 3450 2550 3700
Connection ~ 2550 3450
Wire Wire Line
	1600 5550 1600 4900
Wire Wire Line
	9650 4900 9650 5550
Wire Wire Line
	7350 5550 7350 4900
Connection ~ 7350 5550
Wire Wire Line
	5050 5550 5050 4900
Connection ~ 5050 5550
Wire Wire Line
	2750 5550 2750 4900
Connection ~ 2750 5550
Connection ~ 8700 5050
Connection ~ 6400 5050
Connection ~ 4100 5050
Wire Wire Line
	9450 3450 950  3450
Connection ~ 1400 3450
Wire Wire Line
	950  5050 9850 5050
Connection ~ 1800 5050
Wire Wire Line
	1800 3700 1800 3600
Wire Wire Line
	1800 3600 2750 3600
Wire Wire Line
	2750 3600 2750 3700
Wire Wire Line
	4100 3700 4100 3600
Wire Wire Line
	4100 3600 5050 3600
Wire Wire Line
	5050 3600 5050 3700
Wire Wire Line
	6400 3700 6400 3600
Wire Wire Line
	6400 3600 7350 3600
Wire Wire Line
	7350 3600 7350 3700
Wire Wire Line
	8700 3700 8700 3600
Wire Wire Line
	8700 3600 9650 3600
Wire Wire Line
	9650 3600 9650 3700
Wire Wire Line
	9650 1000 9650 900 
Wire Wire Line
	9650 900  8700 900 
Wire Wire Line
	8700 900  8700 1000
Wire Wire Line
	7350 1000 7350 900 
Wire Wire Line
	7350 900  6400 900 
Wire Wire Line
	6400 900  6400 1000
Wire Wire Line
	5050 1000 5050 900 
Wire Wire Line
	5050 900  4100 900 
Wire Wire Line
	4100 900  4100 1000
Wire Wire Line
	2750 1000 2750 900 
Wire Wire Line
	2750 900  1800 900 
Wire Wire Line
	1800 900  1800 1000
Connection ~ 1800 2350
Wire Wire Line
	950  2350 9850 2350
Connection ~ 1400 750 
Wire Wire Line
	950  750  9450 750 
Connection ~ 4100 2350
Connection ~ 6400 2350
Connection ~ 8700 2350
Connection ~ 2750 2850
Wire Wire Line
	2750 2850 2750 2200
Connection ~ 5050 2850
Wire Wire Line
	5050 2850 5050 2200
Connection ~ 7350 2850
Wire Wire Line
	7350 2850 7350 2200
Wire Wire Line
	9650 2200 9650 2850
Wire Wire Line
	1600 2850 1600 2200
Connection ~ 2550 750 
Wire Wire Line
	2550 750  2550 1000
Connection ~ 4850 750 
Wire Wire Line
	4850 750  4850 1000
Connection ~ 7150 750 
Wire Wire Line
	7150 750  7150 1000
Wire Wire Line
	9450 750  9450 1000
Wire Wire Line
	8300 1000 8300 750 
Connection ~ 8300 750 
Wire Wire Line
	6000 750  6000 1000
Connection ~ 6000 750 
Wire Wire Line
	3700 750  3700 1000
Connection ~ 3700 750 
Wire Wire Line
	8500 2850 8500 2200
Connection ~ 8500 2850
Wire Wire Line
	6200 2850 6200 2200
Connection ~ 6200 2850
Wire Wire Line
	3900 2850 3900 2200
Connection ~ 3900 2850
Connection ~ 7550 2350
Connection ~ 5250 2350
Connection ~ 2950 2350
Connection ~ 1600 2850
Wire Wire Line
	950  900  1600 900 
Wire Wire Line
	1600 900  1600 1000
Wire Wire Line
	2950 1000 2950 900 
Wire Wire Line
	2950 900  3900 900 
Wire Wire Line
	3900 900  3900 1000
Wire Wire Line
	5250 1000 5250 900 
Wire Wire Line
	5250 900  6200 900 
Wire Wire Line
	6200 900  6200 1000
Wire Wire Line
	7550 1000 7550 900 
Wire Wire Line
	7550 900  8500 900 
Wire Wire Line
	8500 900  8500 1000
Wire Wire Line
	1600 3700 1600 3200
Wire Wire Line
	1600 3200 10200 3200
Wire Wire Line
	10200 3200 10200 900 
Wire Wire Line
	10200 900  9850 900 
Wire Wire Line
	9850 900  9850 1000
Wire Wire Line
	1800 2200 1800 2400
Wire Wire Line
	2950 2850 2950 2800
Connection ~ 2950 2850
Wire Wire Line
	4100 2200 4100 2400
Wire Wire Line
	5250 2200 5250 2400
Wire Wire Line
	6400 2850 6400 2800
Connection ~ 6400 2850
Wire Wire Line
	7550 2200 7550 2400
Wire Wire Line
	8700 2200 8700 2400
Wire Wire Line
	9850 2800 9850 2850
Wire Wire Line
	9850 2850 950  2850
Connection ~ 9650 2850
Wire Wire Line
	9850 4900 9850 5100
Connection ~ 9850 5050
Wire Wire Line
	8700 5550 8700 5500
Connection ~ 8700 5550
Wire Wire Line
	7550 4900 7550 5100
Wire Wire Line
	6400 5550 6400 5500
Connection ~ 6400 5550
Wire Wire Line
	5250 4900 5250 5100
Wire Wire Line
	4100 4900 4100 5100
Wire Wire Line
	2950 4900 2950 5100
Wire Wire Line
	1800 4900 1800 5100
Connection ~ 1150 2350
Wire Wire Line
	1250 6550 1250 6350
$EndSCHEMATC
