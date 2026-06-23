# SF32LB52-DevKit-LCD Adapter Board Fabrication Guide

This document describes how to make a companion adapter board for the SF32LB52-DevKit-LCD development board, for debugging third-party displays, WiFi modules, and other devices.

## QSPI-LCD Interface Adapter Board

The QSPI-LCD adapter board can be adapted from the 22-pin FPC connector or from the 40-pin dual-row header.

### 22-pin FPC Adaptation Method


```{figure} assets/52Kit-22p-FPC-pin-define.png

:scale: 60%
:name: sf32lb5x-lcd-board-back
SF32LB52-DevKit-LCD board 22-pin FPC connector signal definition
```

```{table} SF32LB52-DevKit-LCD 22-pin assignment
:name: SF32LB52-DevKit-LCD-22P-LIST

|Pin|	Pin Name           	   |   Function  |
|:--|:-----------------------|:-----------|
|1  | LEDK    | LCD backlight diode cathode                     
|2  | LEDA    | LCD backlight diode anode    
|3  | PA_07   | MIPI-DBI(8080) B0, QSPI D2, LCD interface signal 
|4  | PA_08   | MIPI-DBI(8080) B1, QSPI D3, LCD interface signal 
|5  | PA_37   | MIPI-DBI(8080) B2, LCD interface signal 
|6  | PB_39   | MIPI-DBI(8080) B3, LCD interface signal 
|7  | PB_40   | MIPI-DBI(8080) B4, LCD interface signal 
|8  | PA_41   | MIPI-DBI(8080) B5, LCD interface signal  
|9  | PA_42   | MIPI-DBI(8080) B6, LCD interface signal 
|10 | PA_43   | MIPI-DBI(8080) B7, LCD interface signal                 
|11 | PA_02   | MIPI-DBI(8080) TE, QSPI TE, LCD interface signal                   
|12 | PA_00   | LCD Reset, LCD interface signal 
|13 | PA_04   | MIPI-DBI(8080) WRx, QSPI CLK, SPI CLK, LCD interface signal 
|14 | PB_05   | MIPI-DBI(8080) RDx, QSPI D0, SPI SDI, LCD interface signal         
|15 | PA_03   | MIPI-DBI(8080) CSx, QSPI CS, SPI CS, LCD interface signal             
|16 | PA_06   | MIPI-DBI(8080) DCx, QSPI D1, SPI DC, LCD interface signal 
|17 | VDD_3V3 | 3.3V power output 
|18 | PA_31   | Touchscreen INT interrupt signal
|19 | PA_33   | Touchscreen I2C_SDA signal 
|20 | PA_30   | Touchscreen I2C_SCL signal 
|21 | PA_09   | Touchscreen RTN reset signal 
|22 | GND     | Ground                         

```
The 22-pin FPC connector on the SF32LB52-DevKit-LCD development board supports MIPI-DBI (8080) and SPI (3-/4-wire, 2-/4-data) interfaces. The data format can be adapted by configuring the I/O MUX in software.

```{figure} assets/52Kit-LED-driver.png

:scale: 50%
:name: sf32lb5x-lcd-board-back1
SF32LB52-DevKit-LCD board 22-pin FPC connector LED driver circuit
```

The SF32LB52-DevKit-LCD development board provides one LED driver with a default drive current of 40 mA. The LED drive current can be adjusted by changing the resistance of R0110 according to the LED circuit structure and current requirements of the LCD display.

```{important}
1. The adapter board is connected to the SF32LB52-DevKit-LCD development board through an FPC cable. During design, pay attention to the FPC pin sequence on the adapter board; it must be crossed over relative to the signal definitions on the development board.
2. The VDD_3V3 power supply in the FPC connector interface can power the display driver and touchscreen driver on the adapter board.
3. The I/O level of the development board is 3.3 V. If the I/O level of the driver chip on the LCD adapter board is 1.8 V, use a level shifter for level conversion.
4. If the adapter board requires a 5 V power supply, use the 40-pin dual-row header as the adapter interface.
5. Series resistors have already been added to the display interface on the development board, so no additional series resistors are required on the adapter board.
```

### 40-pin Dual-Row Header Adapter Method

```{figure} assets/52Kit-2x20p-pin-define.png

:scale: 60%
:name: sf32lb5x-lcd-board-back2
SF32LB52-DevKit-LCD board 40-pin dual-row header signal definition
```
```{table} SF32LB56-DevKit-LCD 40-pin signal definition
:name: SF32LB56-DevKit-LCD-40P-LIST

|Pin|	Pin Name           	   |   Function  |
|:--|:-----------------------|:-----------|
|1   | 3V3      | 3v3 power                 
|2   | 5V       | 5v power   
|3   | IO2      | PA_42 or PA_14   
|4   | 5V       | 5v power        
|5   | IO3      | PA_41 or PA_12     
|6   | GND      | Ground    
|7   | IO4      | PA_43 or PA_13    
|8   | IO14     | PA_27   
|9   | GND      | Ground    
|10  | IO15     | PA_20     
|11  | IO17     | PA_08, **MIPI-DBI(8080) B1, QSPI D3, LCD interface signal**   
|12  | IO18     | PA_05, **MIPI-DBI(8080) RDx, QSPI D0, SPI SDI, LCD interface signal** 
|13  | IO27     | PA_40 or PA_17  &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp;               
|14  | GND      | Ground         
|15  | IO22     | PA_39 or PA_16         
|16  | IO23     | PA_37 or PA_15                  
|17  | 3V3      | 3v3 power       
|18  | IO24     | PA_38    
|19  | IO10     | PA_24    
|20  | GND      | Ground      
|21  | IO9      | PA_25       
|22  | IO25     | PA_07, **MIPI-DBI(8080) B0, QSPI D2, LCD interface signal**       
|23  | IO11     | PA_28       
|24  | IO8      | PA_29       
|25  | GND      | Ground       
|26  | IO7      | PA_31, **Touchscreen INT interrupt signal**       
|27  | IO0      | PA_30, **Touchscreen I2C_SCL signal**       
|28  | IO1      | PA_22       
|29  | IO5      | PA_23       
|30  | GND      | Ground      
|31  | IO6      | PA_33, **Touchscreen I2C_SDA signal**       
|32  | IO12     | PA_00, **LCD Reset, LCD interface signal**       
|33  | IO13     | PA_01, **BL PWM, LCD interface signal**       
|34  | GND      | Ground       
|35  | IO19     | PA06, **MIPI-DBI(8080) DCx, QSPI D1, SPI DC, LCD interface signal**        
|36  | IO16     | PA02, **MIPI-DBI(8080) TE, QSPI TE, LCD interface signal**        
|37  | IO26     | PA09, **Touchscreen RTN reset signal**      
|38  | IO20     | PA04, **MIPI-DBI(8080) WRx, QSPI CLK, SPI CLK, LCD interface signal**      
|39  | GND      | Ground       
|40  | IO21     | PA03, **MIPI-DBI(8080) CSx, QSPI CS, SPI CS, LCD interface signal**            

```
```{important}
1. The adapter board is connected to the SF32LB52-DevKit-LCD development board through a 40p dual-row header, and the adapter board is mounted on top of the development board.
2. The 3V3 and 5V power supplies in the 40p dual-row header interface can power the display driver and touchscreen driver on the adapter board.
3. The I/O level of the development board is 3.3 V. If the I/O level of the driver chip on the LCD adapter board is 1.8 V, use a level shifter for level conversion.
4. The display backlight circuit needs to be integrated on the adapter board.
5. Series resistors have already been added to the display interface on the development board, so no additional series resistors are required on the adapter board.
```
## MIPI-DBI (8080) Interface Adapter Board

Refer to the QSPI-LCD Interface Adapter Board section.

## EDP E-Paper Display Interface Adapter Board


## WiFi Module Adapter Board
