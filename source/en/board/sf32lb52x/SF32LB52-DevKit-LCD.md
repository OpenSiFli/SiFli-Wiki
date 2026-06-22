# SF32LB52-DevKit-LCD Development Board User Guide




## Development Board Overview


SF32LB52-DevKit-LCD is a development board based on the SF32LB52x series chip module, mainly used to develop various applications for displays with `SPI`/`DSPI`/`QSPI` or `MCU/8080` interfaces.

The development board also includes analog MIC input, analog audio output, an SDIO interface, a USB-C interface, and TF card support, providing developers with abundant hardware interface resources. It can be used to develop drivers for peripherals with various interfaces, helping developers simplify the hardware development process and shorten product time to market.

The appearance of the SF32LB52_DevKit-LCD is shown in {numref}`Figure {number} <SF32LB52x_DevKit-LCD_Front_Look>` and {numref}`Figure {number} <SF32LB52x_DevKit-LCD_Back_Look>`.

```{figure} assets/SF32LB52x-DevKit-LCD_Front_Look.png

:scale: 20%
:name: SF32LB52x_DevKit-LCD_Front_Look
Front photo of the SF32LB52x_DevKit-LCD development board
```

```{figure} assets/SF32LB52x_DevKit-LCD_Back_Look.png

:scale: 20%
:name: SF32LB52x_DevKit-LCD_Back_Look
Rear photo of the SF32LB52x_DevKit-LCD development board
```
### Feature List
This development board has the following features:
1.	Module: Onboard SF32LB52x-MOD-N16R8 module based on the SF32LB52x chip. The module configuration is as follows:
    - Standard SF32LB525UC6 chip, with the following built-in co-packaged configuration:
        - 8 MB OPI-PSRAM, interface frequency 144 MHz (may change in the official release)
    - 128 Mb QSPI-NOR Flash, interface frequency 72 MHz, STR mode (may change in the official release)
    - 48 MHz crystal
    - 32.768 kHz crystal
    - Onboard antenna or IPEX antenna connector, selected through a 0-ohm resistor; onboard antenna by default
    - RF matching network and other resistor, capacitor, and inductor components
2.	Dedicated display interface
    - SPI/DSPI/QSPI, supporting QSPI in DDR mode, routed out through a 22-pin FPC and a 40-pin header
    - 8-bit MCU/8080, routed out through a 22-pin FPC and a 40-pin header
     - Supports touchscreens with an I2C interface
3.	Audio
    - Supports analog MIC input
    - Analog audio output, onboard Class-D audio PA
4.	USB
    - Type-C interface, supports the onboard USB-to-serial chip for firmware flashing and software DEBUG, and can be used to supply power
    - Type-C interface, supports USB2.0 FS, and can be used to supply power
5.	SD Card
    - Supports TF cards using the SPI interface, with an onboard Micro SD card slot


### Functional Block Diagram

```{figure} assets/SF32LB52x_DevKit-LCD_Block_Diagram.png

:scale: 110%
Development board functional block diagram
```
### Component Introduction

The main board of the SF32LB52-DevKit-LCD development board is the core of the entire kit. This main board integrates the SF32LB52-MOD-N16R8 module and provides QSPI and MUC8 LCD connectors.

```{figure} assets/52KIT-LCD-T-Notes.png

:scale: 70%
SF32LB52-DevKit-LCD board - front (click to enlarge)
```

```{figure} assets/52KIT-LCD-B-Notes.png

:scale: 70%
SF32LB52-DevKit-LCD board - rear (click to enlarge)
```


## Application Development

This section mainly describes how to set up the hardware and software, flash firmware to the development board, and develop applications.

### Required Hardware

- 1 x SF32LB52-DevKit-LCD (including the SF32-LB52X-MOD module)
- 1 x LCD module
- 1 x USB 2.0 data cable (standard Type-A to Type-C)
- 1 x computer (Windows, Linux, or macOS)

```{note}

1. If you need both UART debugging and the USB interface, two USB 2.0 data cables are required;
2. Make sure to use an appropriate USB data cable. Some cables are for charging only and cannot be used for data transfer or firmware flashing.

```
### Optional Hardware

- 1 x speaker
- 1 x TF Card
- 1 x lithium battery greater than 450 mAh

### Hardware Setup

Prepare the development board and load the first sample application:

1.	Connect the display module to the corresponding LCD connector interface;
2.	Open SiFli's SifliTrace tool software and select the correct COM port;
3.	Plug in the USB data cable to connect the PC to the USB-to-UART port on the development board;
4.	The LCD display lights up, and you can interact with the touchscreen using your finger.

Hardware setup is complete. You can now proceed with software setup.


### Software Setup

For instructions on how to quickly set up the development environment for the SF32LB52-DevKit-LCD development board, refer to the software-related documentation. 

## Hardware Reference

This section provides more information about the development board hardware.

### GPIO Assignment List

The following table provides the GPIO assignment list for the pins of the SF32LB52-MOD-N16R8 module, used to control specific components or functions of the development board.

```{table} SF32LB52-MOD-N16R8 GPIO Assignment

:name: SF32LB52-MOD-N16R8-GPIO-LIST

| Pin |	Pin Name           	   |   Function  |
|:--|:-----------------------|:-----------|
|1 | GND   | Ground                     |
|2 | PA_44 | VBUS_DET, charger insertion detection   |
|3 | PA_43 | MCU 8080 DB7, LCD interface signal |
|4 | PA_42 | MCU 8080 DB6, LCD interface signal |
|5 | PA_23 | XTAL32K_XO, NC by default       |
|6 | PA_22 | XTAL32K_XI, NC by default       |
|7 | PA_41 | MCU 8080 DB5, LCD interface signal |
|8 | PA_40 | MCU 8080 DB4, LCD interface signal |
|9 | PA_39 | MCU 8080 DB3, LCD interface signal |
|10 | PA_38 | GPIO                    |
|11 | PA_37 | MCU 8080 DB2, LCD interface signal |
|12 | PA_36 | USB_DM                  |
|13 | PA_35 | USB_DP                  |
|14 | PA_34 | HOME and long-press reset button        |
|15 | PA_33 | touchscreen I2C_SDA            |
|16 | PA_32 | RGB LED                 |
|17 | VDD33_VOUT2/AVDD33 | 3.3 V power output when using the SF32LB-MOD-1 module (no output by default; available only after software configuration), and 3.3 V power input when using SF32LB-MOD-A/B  |
|18 | PA_24 | SPI1_DIO, SD Card interface signal    |
|19 | PA_25 | SPI1_DI, SD Card interface signal     |
|20 | PA_26 | SD Card CD signal, LED          |
|21 | PA_27 | UART_TXD                |
|22 | PA_28 | SPI1_CLK, SD Card interface signal    |
|23 | PA_29 | SPI1_CS, SD Card interface signal     |
|24 | PA_30 | touchscreen I2C_SCL            |
|25 | PA_31 | touchscreen INT interrupt             |
|26 | GND | Ground                       |
|27 | VBAT  | 3.2~4.7 V power input when using the SF32LB-MOD-1 module, and 3.3 V power input when using SF32LB-MOD-A/B     |
|28 | PA_20 | UART_RXD                |
|29 | PA_19 | DB_UART_TXD, firmware download and software debug interface |
|30 | PA_18 | DB_UART_RXD, firmware download and software debug interface |
|31 | PA_11 | KEY, function button             |
|32 | PA_10 | AU_PA_EN, audio PA control signal |
|33 | AU_DAC1P_OUT | Analog audio output signal    |
|34 | AU_DAC1N_OUT | Analog audio output signal    |
|35 | GND | Ground                       |
|36 | MIC_BIAS | MIC bias voltage            |
|37 | MIC_ADC_IN | MIC input signal          |
|38 | PA_09 | touchscreen RST interrupt             |
|39 | PA_08 | MCU 8080 DB1, QSPI D3, LCD interface signal |
|40 | PA_07 | MCU 8080 DB0, QSPI D2, LCD interface signal |
|41 | PA_06 | MCU 8080 DC, QSPI D1, E-Paper DC, LCD interface signal |
|42 | PA_05 | MCU 8080 RD, QSPI D0, E-Paper SDI, LCD interface signal |
|43 | PA_04 | MCU 8080 WR, QSPI CLK, E-Paper SCLK, LCD interface signal |
|44 | PA_03 | MCU 8080 CS, QSPI CS, E-Paper CS, LCD interface signal |
|45 | PA_02 | MCU 8080 TE, QSPI TE, E-Paper BUSY, LCD interface signal |
|46 | PA_01 | BL PWM, LCD interface signal      |
|47 | PA_00 | RSTB, LCD interface signal        |
|48 | GND | Ground                      |
|49 | GND | Ground                      |
|50 | GND | Ground                      |
|51 | GND | Ground                      |
|52 | GND | Ground                      |
|53 | GND | Ground                      |
|54 | GND | Ground                      |
|55 | GND | Ground                      |
|56 | GND | Ground                      |
|57 | GND | Ground                      |
|58 | GND | Ground                      |
|58 | GND | Ground                      |
|60 | GND | Ground                      |
|61 | VBATS | battery voltage sense input          |
|62 | PA_21 | GPIO, available only on SF32LB52-MOD-A/B        |
|63 | PA_15 | MPI2_D0, SD1_CMD        |
|64 | PA_16 | MPI2_CLK, SD1_D0        |
|65 | PA_17 | MPI2_D3, SD1_D1         |
|66 | PA_14 | MPI2_D2, SD1_CLK        |
|67 | PA_13 | MPI2_D1, SD1_D3         |
|68 | PA_12 | MPI2_CS, SD1_D2         |

```

```{important}
1. The SF32LB52-DevKit-LCD is compatible with three modules: SF32LB-MOD-1, SF32LB-MOD-A, and SF32LB-MOD-B.
2. Module pin 17, VDD33_VOUT2/AVDD33, is a 3.3 V power output when using the SF32LB-MOD-1 module (no output by default; output is available only after software configuration), and a 3.3 V power input when using SF32LB-MOD-A/B.
3. Module pin 27, VBAT, is a 3.2–4.7 V power input when using the SF32LB-MOD-1 module, and a 3.3 V power input when using SF32LB-MOD-A/B.
4. For the SF32LB-MOD-1 module, the power-on threshold of the VBAT power supply is set to 3.58 V, and the power-off threshold is set to 3.48 V. For non-battery-powered applications, it is recommended to supply 3.8 V to VBAT.
5. Module pin 62, PA21, is supported only by SF32LB52-MOD-A/B; it is NC on SF32LB-MOD-1.
6. Module pins 62–68 are connected to the module's internal NOR Flash by default and cannot be used by the development board. To use the SDIO interface, select a module version without flash.
```

### 40P Pin Header Interface Definition

```{figure} assets/SF32LB52x_DevKit-40p-define.png

:scale: 10%
:name: SF32LB52x_DevKit-40p-define
Development board 40-pin header interface definition (click to enlarge)
```
### 22p QSPI Pin Sequence FPC Interface Definition


```{table} QSPI-FPC-J0102 Signal Definition
:name: QSPI-FPC-J0102-GPIO-LIST

| Pin |	Pin Name           	   |   Function  |
|:--|:-----------------------|:-----------|
|1  | LEDK    | LCD backlight LED cathode                     
|2  | LEDA    | LCD backlight LED anode    
|3  | PA_07   | MIPI-DBI(8080) B0, QSPI D2, LCD interface signal 
|4  | PA_08   | MIPI-DBI(8080) B1, QSPI D3, LCD interface signal 
|5  | PA_37   | MIPI-DBI(8080) B2, LCD interface signal 
|6  | PA_39   | MIPI-DBI(8080) B3, LCD interface signal 
|7  | PA_40   | MIPI-DBI(8080) B4, LCD interface signal 
|8  | PA_41   | MIPI-DBI(8080) B5, LCD interface signal  
|9  | PA_42   | MIPI-DBI(8080) B6, LCD interface signal 
|10 | PA_43   | MIPI-DBI(8080) B7, LCD interface signal                 
|11 | PA_02   | MIPI-DBI(8080) TE, QSPI TE, LCD interface signal                   
|12 | PA_00   | LCD Reset, LCD interface signal 
|13 | PA_04   | MIPI-DBI(8080) WRx, QSPI CLK, SPI CLK, LCD interface signal 
|14 | PA_05   | MIPI-DBI(8080) RDx, QSPI D0, SPI SDI, LCD interface signal         
|15 | PA_03   | MIPI-DBI(8080) CSx, QSPI CS, SPI CS, LCD interface signal             
|16 | PA_06   | MIPI-DBI(8080) DCx, QSPI D1, SPI DC, LCD interface signal 
|17 | VDD_3V3 | 3.3 V power output 
|18 | PA_31   | touchscreen INT interrupt signal
|19 | PA_33   | touchscreen I2C_SDA signal 
|20 | PA_30   | touchscreen I2C_SCL signal 
|21 | PA_09   | touchscreen RTN reset signal 
|22 | GND     | Ground      

```

### Power Supply Description

The SF32LB52-DevKit-LCD development board supports two power supply methods: USB Type-C and battery power.

1.  Both onboard USB Type-C ports can power the board. For flashing and debugging, use the USB-to-UART port.
2.  It can be powered by a battery alone, allowing standalone operation without a computer.

### Hardware Setup Options

Connect a USB cable to the USB-to-UART port, open SiFli Technology's firmware flashing tool, and select the corresponding COM port and firmware.
1.  Download Mode
- Check the BOOT option and power on. After startup, the board enters download mode, and firmware flashing can be completed.
2.  Software Development Mode
- Clear the BOOT option and power on. After startup, the board enters serial port log output mode, which is software debugging mode.

**For details, refer to&emsp;[Firmware Flashing Tool Impeller](烧录工具)**

### Charging and Battery Selection

The SF32LB52-DevKit-LCD development board integrates the ETA9640P linear charger IC, which supports a maximum charging current of 1 A and is set by default to a 450 mA constant current.

It is recommended to select a 450 mAh–500 mAh single-cell polymer lithium battery. The battery interface is a 2.0 mm HDR female connector. For polarity, refer to the silkscreen of the battery connector on the development board.

### LCD Display Interface

The SF32LB52-DevKit-LCD development board supports QSPI-interface LCD screens. The connector is a 22p-0.5pitch FPC, flip-up, bottom-contact type.
Refer to the signal pin sequence defined above. If the pin sequence differs, use an adapter board for testing; see the SF32LB52-DevKit-LCD Adapter Board Fabrication Guide.
* Supported display model: [TFT-H043A28WQISTKN22_V0-3](鑫洪泰)

### Audio Interface

The SF32LB52-DevKit-LCD development board integrates a MEMS MIC and an audio power amplifier chip.
* Supports audio signal input from the onboard mic.
* Supports an external speaker (up to 3 W/4 ohms). Speaker connector specification: 2.0 mm pitch HDR female connector.

## Obtaining Samples

Retail samples and small batches can be purchased directly from [Taobao](https://sifli.taobao.com/). Volume customers can email sales@sifli.com or contact customer service on Taobao for sales contact information.
Open-source contributors may apply for free samples and can join QQ group 674699679 for discussion.

## Related Documents

- [SF32LB52x Chip Datasheet](https://wiki.sifli.com/silicon/index.html)
- [SF32LB52x User Manual](https://wiki.sifli.com/silicon/index.html)
- [SF32LB52-MOD-1 Datasheet](https://wiki.sifli.com/silicon/index.html)
- [SF32LB52-MOD-1 Design Drawings](https://downloads.sifli.com/hardware/files/documentation/SF32LB52-MOD-1-V1.0.0.zip?)
- [SF32LB52-DevKit-LCD Design Drawings](https://downloads.sifli.com/hardware/files/documentation/SF32LB52-DevKit-LCD_V1.2.0.zip?)
- [SF32LB52-DevKit-LCD Adapter Board Fabrication Guide](SF32LB52-DevKit-LCD-Adapter)



## Development board version information:

* V1.2.0: Uses the SF32LB52-MOD-1/A/B modules. SF32LB52-MOD-1 (SF32LB525UC6) will be released soon.
```{table} 
|No. | V1.2.0 Updates |
|:-- |:------ |
|1 | Modified the SD Card insertion/removal check signal input pin to use PA26, sharing one IO with the external Flash2 chip select and GPIO LED.   
```
* V1.1.0: Uses the SF32LB52-MOD-A/B modules. Currently available physical units include (-A: SF32LB52BU36 and -B: SF32LB52EUB6).
```{table} 
|No. | V1.1.0 Updates |
|:-- |:------ |
|1 | Updated the charging IC schematic library to resolve the issue of incorrect 5V output from the charging IC.   
|2 | Removed the MOSFET VBUS and VBAT switching circuit. All downstream circuits are powered by the 5V output of the charging IC, resolving the abnormal VBUS and VBAT switching issue. 
|3 | Adjusted the gain of AudioPA.
|4 | Resolved the Reset button abnormality. 
|5 | Removed the level-shifting section in the RGBLED circuit; this circuit did not meet the RGBLED timing requirements.
|6 | Updated the module pin definitions and added 2 IOs to resolve compatibility issues between the -1 module and the -A/B modules.
|7 | Updated the power supply section. The AVDD of -A/B was changed to LDO power supply to resolve the RF sensitivity issue caused by high ripple from the original DCDC output.
|8 | Added support for dual flash.
|9 | Added the SD Card insertion/removal detection function. Only -A/B support this function.
|10 | Added the SDIO WiFi function option. Only -A supports this function.
|11 | Modified the mounting hole type, and added a PCB slot on the back side of the antenna.
|12 | Modified the connection point of the EOS protection device for the VBUS input.
```
* V1.0.0: Uses the SF32LB52-MOD module. Current version.
