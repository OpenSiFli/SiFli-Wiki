# SF32LB52-DevKit-LCD Adapter Board Manufacturing Guide

This document guides you on how to create an adapter board for the SF32LB52-DevKit-LCD development board, which can be used to debug third-party displays, WiFi modules, etc.

## QSPI-LCD Interface Adapter Board

The QSPI-LCD adapter board can be used to convert from a 22-pin FPC connector or a 40-pin dual-row pin header.

### 22-pin FPC Conversion Method

```{figure} assets/52Kit-22p-FPC-pin-define.png

:scale: 60%
:name: sf32lb5x-lcd-board-back
Signal definitions for the 22-pin FPC connector on the SF32LB52-DevKit-LCD board
```

```{table} SF32LB52-DevKit-LCD-22P Allocation

:name: SF32LB52-DevKit-LCD-22P-LIST

|Pin| Pin Name            | Function  |
|:--|:---------------------|:-----------|
|1  | LEDK    | LCD backlight diode cathode                     |
|2  | LEDA    | LCD backlight diode anode                       |
|3  | PA_07   | MIPI-DBI(8080) B0, QSPI D2, LCD interface signal |
|4  | PA_08   | MIPI-DBI(8080) B1, QSPI D3, LCD interface signal |
|5  | PA_37   | MIPI-DBI(8080) B2, LCD interface signal         |
|6  | PB_39   | MIPI-DBI(8080) B3, LCD interface signal         |
|7  | PB_40   | MIPI-DBI(8080) B4, LCD interface signal         |
|8  | PA_41   | MIPI-DBI(8080) B5, LCD interface signal         |
|9  | PA_42   | MIPI-DBI(8080) B6, LCD interface signal         |
|10 | PA_43   | MIPI-DBI(8080) B7, LCD interface signal         |
|11 | PA_02   | MIPI-DBI(8080) TE, QSPI TE, LCD interface signal |
|12 | PA_00   | LCD Reset, LCD interface signal                 |
|13 | PA_04   | MIPI-DBI(8080) WRx, QSPI CLK, SPI CLK, LCD interface signal |
|14 | PB_05   | MIPI-DBI(8080) RDx, QSPI D0, SPI SDI, LCD interface signal |
|15 | PA_03   | MIPI-DBI(8080) CSx, QSPI CS, SPI CS, LCD interface signal |
|16 | PA_06   | MIPI-DBI(8080) DCx, QSPI D1, SPI DC, LCD interface signal |
|17 | VDD_3V3 | 3.3V power output                               |
|18 | PA_31   | Touchscreen INT interrupt signal                |
|19 | PA_33   | Touchscreen I2C_SDA signal                     |
|20 | PA_30   | Touchscreen I2C_SCL signal                     |
|21 | PA_09   | Touchscreen RTN reset signal                   |
|22 | GND     | Ground                                         |

```
The 22-pin FPC connector on the SF32LB52-DevKit-LCD development board supports MIPI-DBI(8080) and SPI (3/4-wire, 2/4-data) interfaces. The IO MUX can be configured via software to adapt to the data format.

```{figure} assets/52Kit-LED-driver.png

:scale: 50%
:name: sf32lb5x-lcd-board-back1
LED driver circuit for the 22-pin FPC connector on the SF32LB52-DevKit-LCD board
```

The SF32LB52-DevKit-LCD development board provides an LED driver with a default drive current of 40mA. The drive current can be adjusted by changing the resistance value of R0110 based on the LED circuit structure and current requirements of the LCD display.

```{important}
1. The adapter board is connected to the SF32LB52-DevKit-LCD development board via an FPC cable. When designing the adapter board, pay attention to the FPC pin order, which needs to match the signal definitions on the development board.
2. The VDD_3V3 power supply in the FPC connector can power the screen driver and touch driver on the adapter board.
3. The IO level on the development board is 3.3V. If the IO level of the driver chip on the LCD adapter board is 1.8V, use a level shift chip to convert the voltage.
4. If the adapter board requires a 5V power supply, use a 40-pin dual-row pin header for the interface.
5. The development board already has resistors in series with the display interface, so no additional resistors are needed on the adapter board.
```

### 40-pin Dual-Row Pin Header Conversion Method

```{figure} assets/52Kit-2x20p-pin-define.png

:scale: 60%
:name: sf32lb5x-lcd-board-back2
Signal definitions for the 40-pin dual-row pin header on the SF32LB52-DevKit-LCD board
```

```{table} SF32LB56-DevKit-LCD-40P Signal Definitions

:name: SF32LB56-DevKit-LCD-40P-LIST

|Pin|	Pin Name           	   |   Function  |
|:--|:-----------------------|:-----------|
|1   | 3V3      | 3.3V power                 
|2   | 5V       | 5V power   
|3   | IO2      | PA_42 or PA_14   
|4   | 5V       | 5V power        
|5   | IO3      | PA_41 or PA_12     
|6   | GND      | Ground    
|7   | IO4      | PA_43 or PA_13    
|8   | IO14     | PA_27   
|9   | GND      | Ground    
|10  | IO15     | PA_20     
|11  | IO17     | PA_08，**MIPI-DBI(8080) B1，QSPI D3，LCD interface signal**   
|12  | IO18     | PA_05，**MIPI-DBI(8080) RDx，QSPI D0，SPI SDI，LCD interface signal** 
|13  | IO27     | PA_40 or PA_17  &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp;               
|14  | GND      | Ground         
|15  | IO22     | PA_39 or PA_16         
|16  | IO23     | PA_37 or PA_15                  
|17  | 3V3      | 3.3V power       
|18  | IO24     | PA_38    
|19  | IO10     | PA_24    
|20  | GND      | Ground      
|21  | IO9      | PA_25       
|22  | IO25     | PA_07，**MIPI-DBI(8080) B0，QSPI D2，LCD interface signal**       
|23  | IO11     | PA_28       
|24  | IO8      | PA_29       
|25  | GND      | Ground       
|26  | IO7      | PA_31，**Touchscreen INT interrupt signal**       
|27  | IO0      | PA_30，**Touchscreen I2C_SCL signal**       
|28  | IO1      | PA_22       
|29  | IO5      | PA_23       
|30  | GND      | Ground      
|31  | IO6      | PA_33，**Touchscreen I2C_SDA signal**       
|32  | IO12     | PA_00，**LCD Reset，LCD interface signal**       
|33  | IO13     | PA_01，**BL PWM，LCD interface signal**       
|34  | GND      | Ground       
|35  | IO19     | PA06，**MIPI-DBI(8080) DCx，QSPI D1，SPI DC，LCD interface signal**        
|36  | IO16     | PA02，**MIPI-DBI(8080) TE，QSPI TE，LCD interface signal**        
|37  | IO26     | PA09，**Touchscreen RTN reset signal**      
|38  | IO20     | PA04，**MIPI-DBI(8080) WRx，QSPI CLK，SPI CLK，LCD interface signal**      
|39  | GND      | Ground       
|40  | IO21     | PA03，**MIPI-DBI(8080) CSx，QSPI CS，SPI CS，LCD interface signal**            

```
```{important}
1. The adapter board is connected to the SF32LB52-DevKit-LCD development board via a 40-pin dual-row header, and the adapter board is mounted on top of the development board.
2. The 3.3V and 5V power from the 40-pin dual-row header can supply power to the screen driver and touch driver on the adapter board.
3. The IO of the development board is 3.3V level. If the IO level of the driver chip on the LCD adapter board is 1.8V, a level shift chip should be used to convert the level.
4. The adapter board should integrate a display backlight circuit.
5. The display interface on the development board already has series resistors, so no additional resistors are needed on the adapter board.
```
## MIPI-DBI(8080) Interface Adapter Board

Refer to the QSPI-LCD Interface Adapter Board section

## EDP E-Ink Display Interface Adapter Board


## WiFi Module Adapter Board