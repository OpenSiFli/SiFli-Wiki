# SF32LB52-DevKit-LCD Development Board User Guide




## Overview of the Development Board


The SF32LB52-DevKit-LCD is a development board based on the SF32LB52x series chip module, primarily used for developing various applications with displays based on `SPI`/`DSPI`/`QSPI` or `MCU/8080` interfaces.

The development board also features an analog MIC input, analog audio output, SDIO interface, USB-C interface, and supports TF cards, providing a rich set of hardware interface resources for developers. This allows for the development of various peripheral drivers, simplifying the hardware development process and reducing the time to market for products.

The appearance of the SF32LB52_DevKit-LCD is shown in {numref}`Figure {number} <SF32LB52x_DevKit-LCD_Front_Look>` and {numref}`Figure {number} <SF32LB52x_DevKit-LCD_Back_Look>`.

```{figure} assets/SF32LB52x-DevKit-LCD_Front_Look.png

:scale: 20%
:name: SF32LB52x_DevKit-LCD_Front_Look
Front view of the SF32LB52x_DevKit-LCD development board
```

```{figure} assets/SF32LB52x-DevKit-LCD_Back_Look.png

:scale: 20%
:name: SF32LB52x_DevKit-LCD_Back_Look
Back view of the SF32LB52x_DevKit-LCD development board
```

### Feature List
The development board has the following features:
1. Module: Equipped with the SF32LB52x-MOD-N16R8 module based on the SF32LB52x chip, with the following configuration:
    - Standard configuration: SF32LB525UC6 chip, with integrated package:
        - 8MB OPI-PSRAM, interface frequency 144MHz (subject to change upon official release)
    - 128Mb QSPI-NOR Flash, interface frequency 72MHz, STR mode (subject to change upon official release)
    - 48MHz crystal
    - 32.768KHz crystal
    - On-board antenna or IPEX antenna connector, selected via 0Ω resistor, default is on-board antenna
    - RF matching network and other resistive, capacitive, and inductive components
2. Dedicated screen interface
    - SPI/DSPI/QSPI, supports DDR mode QSPI, connected via 22-pin FPC and 40-pin header
    - 8-bit MCU/8080, connected via 22-pin FPC and 40-pin header
    - Supports I2C interface touch screen
3. Audio
    - Supports analog MIC input
    - Analog audio output, with on-board Class-D audio PA
4. USB
    - Type C interface, supports on-board USB-to-serial chip for program download and software debugging, can provide power
    - Type C interface, supports USB2.0 FS, can provide power
5. SD Card
    - Supports SPI interface TF card, with on-board Micro SD card slot


### Functional Block Diagram

```{figure} assets/SF32LB52x_DevKit-LCD_Block_Diagram.png

:scale: 110%
Functional block diagram of the development board
```

### Component Introduction

The main board of the SF32LB52-DevKit-LCD development kit is the core of the entire kit. This main board integrates the SF32LB52-MOD-N16R8 module and provides QSPI and MUC8 LCD connection sockets.

```{figure} assets/52KIT-LCD-T-Notes.png

:scale: 70%
SF32LB52-DevKit-LCD Board - Front (Click to enlarge)
```

```{figure} assets/52KIT-LCD-B-Notes.png

:scale: 70%
SF32LB52-DevKit-LCD Board - Back (Click to enlarge)
```


## Application Development

This section mainly introduces the setup methods for hardware and software, as well as the instructions for burning firmware to the development board and developing applications.

### Required Hardware

- 1 x SF32LB52-DevKit-LCD (with SF32-LB52X-MOD module)
- 1 x LCD module
- 1 x USB2.0 data cable (Standard A to Type-C)
- 1 x Computer (Windows, Linux, or macOS)

```{note}

1. If you need to debug via UART and also use the USB interface, you will need two USB2.0 data cables.
2. Ensure that you use an appropriate USB data cable. Some cables are only suitable for charging and cannot be used for data transmission or firmware burning.

```

### Optional Hardware

- 1 x Speaker
- 1 x TF Card
- 1 x Lithium battery with a capacity greater than 450mAh

### Hardware Setup

Prepare the development board and load the first example application:

1. Connect the screen module to the corresponding LCD connector interface;
2. Open the SifliTrace tool software from Sicheng, and select the correct COM port;
3. Insert the USB data cable to connect the PC to the USB to UART port of the development board;
4. The LCD screen will light up, and you can interact with the touch screen using your fingers.

Once the hardware setup is complete, you can proceed to the software setup.


### Software Setup

For quick setup of the development environment for the SF32LB52-DevKit-LCD development board, please refer to the relevant software documentation.

## Hardware Reference

This section provides more information about the hardware of the development board.

### GPIO Allocation List

The following table lists the GPIO allocation for the SF32LB52-MOD-N16R8 module, used to control specific components or functions of the development board.

```{table} SF32LB52-MOD-N16R8 GPIO Allocation

:name: SF32LB52-MOD-N16R8-GPIO-LIST

|Pin| Pin Name | Function |
|:--|:-----------------------|:-----------|
|1 | GND   | Ground                     |
|2 | PA_44 | VBUS_DET, charger insertion detection   |
|3 | PA_43 | MCU 8080 DB7, LCD interface signal |
|4 | PA_42 | MCU 8080 DB6, LCD interface signal |
|5 | PA_23 | XTAL32K_XO, default NC       |
|6 | PA_22 | XTAL32K_XI, default NC       |
|7 | PA_41 | MCU 8080 DB5, LCD interface signal |
|8 | PA_40 | MCU 8080 DB4, LCD interface signal |
|9 | PA_39 | MCU 8080 DB3, LCD interface signal |
|10 | PA_38 | GPIO                    |
|11 | PA_37 | MCU 8080 DB2, LCD interface signal |
|12 | PA_36 | USB_DM                  |
|13 | PA_35 | USB_DP                  |
|14 | PA_34 | HOME and long press reset button        |
|15 | PA_33 | Touchscreen I2C_SDA            |
|16 | PA_32 | RGB LED                 |
|17 | VDD33_VOUT2/AVDD33 | 3.3V power output when SF32LB-MOD-1 module is used (default no output, requires software configuration), 3.3V power input when SF32LB-MOD-A/B is used  |
|18 | PA_24 | SPI1_DIO, SD card interface signal    |
|19 | PA_25 | SPI1_DI, SD card interface signal     |
|20 | PA_26 | SD card_CD signal, LED          |
|21 | PA_27 | UART_TXD                |
|22 | PA_28 | SPI1_CLK, SD card interface signal    |
|23 | PA_29 | SPI1_CS, SD card interface signal     |
|24 | PA_30 | Touchscreen I2C_SCL            |
|25 | PA_31 | Touchscreen interrupt INT             |
|26 | GND | Ground                       |
|27 | VBAT  | 3.2~4.7V power input when SF32LB-MOD-1 module is used, 3.3V power input when SF32LB-MOD-A/B is used     |
|28 | PA_20 | UART_RXD                |
|29 | PA_19 | DB_UART_TXD, program download and software debugging interface |
|30 | PA_18 | DB_UART_RXD, program download and software debugging interface |
|31 | PA_11 | KEY, function button             |
|32 | PA_10 | AU_PA_EN, audio amplifier control signal |
|33 | AU_DAC1P_OUT | Analog audio output signal    |
|34 | AU_DAC1N_OUT | Analog audio output signal    |
|35 | GND | Ground                       |
|36 | MIC_BIAS | MIC bias voltage            |
|37 | MIC_ADC_IN | MIC input signal          |
|38 | PA_09 | Touchscreen interrupt RST             |
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
|61 | VBATS | Battery voltage detection input          |
|62 | PA_21 | GPIO, only available on SF32LB52-MOD-A/B        |
|63 | PA_15 | MPI2_D0, SD1_CMD        |
|64 | PA_16 | MPI2_CLK, SD1_D0        |
|65 | PA_17 | MPI2_D3, SD1_D1         |
|66 | PA_14 | MPI2_D2, SD1_CLK        |
|67 | PA_13 | MPI2_D1, SD1_D3         |
|68 | PA_12 | MPI2_CS, SD1_D2         |

```

```{important}
1. The SF32LB52-DevKit-LCD is compatible with three modules: SF32LB-MOD-1, SF32LB-MOD-A, and SF32LB-MOD-B.
2. Pin 17 VDD33_VOUT2/AVDD33 of the module: For the SF32LB-MOD-1 module, it is a 3.3V power output (default no output, requires software configuration to enable output); for the SF32LB-MOD-A/B modules, it is a 3.3V power input.
3. Pin 27 VBAT of the module: For the SF32LB-MOD-1 module, it is a 3.2~4.7V power input; for the SF32LB-MOD-A/B modules, it is a 3.3V power input.
4. The power-on threshold for the VBAT power supply of the SF32LB-MOD-1 module is set to 3.58V, and the power-off threshold is set to 3.48V. For non-battery applications, it is recommended to supply 3.8V to VBAT.
5. Pin 62 PA21 of the module is supported only by the SF32LB52-MOD-A/B modules; it is NC (Not Connected) for the SF32LB-MOD-1 module.
6. Pins 62~68 of the module are default connected to the internal Nor Flash and cannot be used on the development board; if you need to use the SDIO interface, please choose a module without the flash.
```

### 40P Header Pin Definition

```{figure} assets/SF32LB52x_DevKit-40p-define.png

:scale: 10%
:name: SF32LB52x_DevKit-40p-define
40p header pin definition on the development board (click to enlarge)
```

### 22p QSPI Line Order FPC Interface Definition

```{table} QSPI-FPC-J0102 Signal Definition
:name: QSPI-FPC-J0102-GPIO-LIST

| Pin | Pin Name | Function |
|:---:|:---------|:---------|
| 1   | LEDK     | LCD backlight diode cathode |
| 2   | LEDA     | LCD backlight diode anode |
| 3   | PA_07    | MIPI-DBI(8080) B0, QSPI D2, LCD interface signal |
| 4   | PA_08    | MIPI-DBI(8080) B1, QSPI D3, LCD interface signal |
| 5   | PA_37    | MIPI-DBI(8080) B2, LCD interface signal |
| 6   | PB_39    | MIPI-DBI(8080) B3, LCD interface signal |
| 7   | PB_40    | MIPI-DBI(8080) B4, LCD interface signal |
| 8   | PA_41    | MIPI-DBI(8080) B5, LCD interface signal |
| 9   | PA_42    | MIPI-DBI(8080) B6, LCD interface signal |
| 10  | PA_43    | MIPI-DBI(8080) B7, LCD interface signal |
| 11  | PA_02    | MIPI-DBI(8080) TE, QSPI TE, LCD interface signal |
| 12  | PA_00    | LCD Reset, LCD interface signal |
| 13  | PA_04    | MIPI-DBI(8080) WRx, QSPI CLK, SPI CLK, LCD interface signal |
| 14  | PB_05    | MIPI-DBI(8080) RDx, QSPI D0, SPI SDI, LCD interface signal |
| 15  | PA_03    | MIPI-DBI(8080) CSx, QSPI CS, SPI CS, LCD interface signal |
| 16  | PA_06    | MIPI-DBI(8080) DCx, QSPI D1, SPI DC, LCD interface signal |
| 17  | VDD_3V3  | 3.3V power output |
| 18  | PA_31    | Touchscreen INT interrupt signal |
| 19  | PA_33    | Touchscreen I2C_SDA signal |
| 20  | PA_30    | Touchscreen I2C_SCL signal |
| 21  | PA_09    | Touchscreen RTN reset signal |
| 22  | GND      | Ground |

```

### Power Supply Description

The SF32LB52-DevKit-LCD development board has two power supply methods: USB Type-C and battery power.

1. Both USB Type-C ports on the board can power the board. Use the USB-to-UART port for downloading and debugging.
2. The board can be powered by a battery alone, which is convenient for independent operation without a computer.

### Hardware Configuration Options

Connect the USB cable to the USB-to-UART port, open the Sifli Technology program download tool, and select the corresponding COM port and program.
1. Download Mode
- Check the BOOT item, power on, and enter the download mode after startup to complete the program download.
2. Software Development Mode
- Uncheck the BOOT item, power on, and enter the serial port log print mode to enter the software debugging mode.

**For more details, please refer to the [Firmware Burn Tool Impeller](烧录工具)**

### Charging and Battery Selection

The SF32LB52-DevKit-LCD development board integrates the ETA9640P linear charging chip, which supports a maximum charging current of 1A, with a default setting of 450mA constant current.

It is recommended to use a 450mAh~500mAh single-cell polymer lithium battery. The battery connector is a 2.0mm HDR female socket. Refer to the battery holder silk screen on the development board for polarity.

### LCD Display Interface

The SF32LB52-DevKit-LCD development board supports QSPI interface LCD screens. The connector is a 22p-0.5pitch FPC, with the upper side for contact and the lower side for connection. Refer to the signal definitions above. If the signal order is different, a conversion board is required for testing. Please refer to the "SF32LB52-DevKit-LCD Adapter Board Manufacturing Guide."
* Supported screen models: [TFT-H043A28WQISTKN22_V0-3](鑫洪泰)

### Audio Interface

The SF32LB52-DevKit-LCD development board integrates a MEMS MIC and an audio amplifier chip.
* Supports audio signal input from the onboard mic.
* Supports external speakers (up to 3W/4 ohms), with a connector specification of 2.0mm pitch HDR female socket.

## Sample Acquisition

Retail samples and small batches can be purchased directly from [Taobao](https://sifli.taobao.com/). Bulk customers can send an email to sales@sifli.com or contact customer service on Taobao for sales information.
Participating in open-source projects can allow you to apply for free samples. You can join QQ group 674699679 for discussions.

## Related Documents
```

- [SF32LB52x Chip Technical Specification](https://downloads.sifli.com/silicon/DS0052-SF32LB52x-%E8%8A%AF%E7%89%87%E6%8A%80%E6%9C%AF%E8%A7%84%E6%A0%BC%E4%B9%A6%20V2p4.pdf?)
- [SF32LB52x User Manual](https://downloads.sifli.com/silicon/UM0052-SF32LB52x-%E7%94%A8%E6%88%B7%E6%89%8B%E5%86%8C%20V0p3.pdf?)
- [SF32LB52-MOD-1 Technical Specification](https://downloads.sifli.com/silicon/DS5203-SF32LB52-MOD-1%E6%8A%80%E6%9C%AF%E8%A7%84%E6%A0%BC%E4%B9%A6%20V0p1.pdf?)
- [SF32LB52-MOD-1 Design Drawings](https://downloads.sifli.com/hardware/files/documentation/SF32LB52-MOD-1-V1.0.0.zip?)
- [SF32LB52-DevKit-LCD Design Drawings](https://downloads.sifli.com/hardware/files/documentation/SF32LB52-DevKit-LCD_V1.2.0.zip?)
- [SF32LB52-DevKit-LCD Adapter Board Manufacturing Guide](SF32LB52-DevKit-LCD-Adapter)



## Development Board Version Information:

* V1.2.0: Uses the SF32LB52-MOD-1/A/B module, and the upcoming SF32LB52-MOD-1 (SF32LB525UC6)
```{table} 
| No. | V1.2.0 Update Content |
|:-- |:------ |
| 1 | Modified the SD card insertion detection signal input pin to PA26, shared with the external Flash2 chip select and GPIO LED.   
```
* V1.1.0: Uses the SF32LB52-MOD-A/B module, currently available (-A: SF32LB52BU36 and -B: SF32LB52EUB6)
```{table} 
| No. | V1.1.0 Update Content |
|:-- |:------ |
| 1 | Updated the charging chip schematic library to resolve the issue of incorrect 5V output from the charging chip.   
| 2 | Removed the MOSFET VBUS and VBAT switching circuit, and powered the downstream circuit entirely from the 5V output of the charging chip, resolving the issue of abnormal VBUS and VBAT switching. 
| 3 | Adjusted the gain of the audio PA.
| 4 | Resolved the issue of the Reset button malfunctioning. 
| 5 | Removed the level shifting part of the RGBLED circuit, as it did not meet the timing requirements of the RGBLED.
| 6 | Updated the module pin definitions, adding 2 IOs to resolve the compatibility issue between the -1 module and the -A/B modules.
| 7 | Updated the power supply section, changing the AVDD of -A/B to LDO power supply to resolve the issue of high ripple in the original DCDC output causing RF sensitivity problems.
| 8 | Added support for dual flash.
| 9 | Added SD card insertion detection functionality, supported only by -A/B.
| 10 | Added SDIO WiFi functionality option, supported only by -A.
| 11 | Modified the type of positioning holes and the PCB slot on the back of the antenna.
| 12 | Modified the connection point of the EOS protection device for VBUS input.
```
* V1.0.0: Uses the SF32LB52-MOD module, current version