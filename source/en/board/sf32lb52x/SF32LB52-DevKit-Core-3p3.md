# SF32LB52-DevKit-Core-3p3 Development Board User Guide

## Development Board Version Information

* *-N1-V1.0.0: equipped with the SF32LB52BU36 chip (internally stacked with 1MB NOR Flash)
* *-N4-V1.0.0: equipped with the SF32LB52BU56 chip (internally stacked with 4MB NOR Flash)
* *-R4N16-V1.0.0: equipped with SF32LB52EUB6 (internally stacked with 8MB PSRAM) + 16MB NOR Flash
* *-R8N16-V1.0.0: equipped with SF32LB52GUC6 (internally stacked with 8MB PSRAM) + 16MB NOR Flash
* *-R16N16-V1.0.0: equipped with SF32LB52JUD6 (internally stacked with 16MB PSRAM) + 16MB NOR Flash, current version

## 1. Development Board Overview

The SF32LB52-DevKit-Core-3p3 is a development board based on SiFli Technology's SF32LB52BU56/SF32LB52JUD6 chips. It measures only 30.88 mm x 68 mm. The pin headers use a castellated through-hole edge design, so headers can be inserted into the board without soldering. The board supports GPIO, UART, I2C, SPI, LCD, I2S, GPADC, PWM, and analog audio input/output.

```{image} assets/Core-3p3_Front_look.png
:width: 20%
:align: center
```

<div align="center"> Front view of the development board </div>  <br>  <br>  <br>

```{image} assets/Core-3p3_Back_look.png
:width: 20%
:align: center
```

<div align="center"> Rear view of the development board </div>  <br>  <br>  <br>

## 2. Feature List

This development board provides the following features:

1. Board variants:
    - -N1: onboard SF32LB52BU36 chip with the following configuration:

        - Stacked memory:
            - 1MB NOR Flash, 96 MHz interface frequency

    - -N4: onboard SF32LB52BU56 chip with the following configuration:

        - Stacked memory:
            - 4MB NOR Flash, 96 MHz interface frequency
    - -R4N16: onboard SF32LB52EUB6 chip with the following configuration:

        - Stacked memory:
            - 4MB OPI-PSRAM, 144 MHz interface frequency

        - Onboard 16MB QSPI-NOR Flash, 72 MHz interface frequency, STR mode

    - -R8N16: onboard SF32LB52GUC6 chip with the following configuration:

        - Stacked memory:
            - 8MB OPI-PSRAM, 144 MHz interface frequency

        - Onboard 16MB QSPI-NOR Flash, 72 MHz interface frequency, STR mode

    - -R16N16: onboard SF32LB52JUD6 chip with the following configuration:

        - Stacked memory:
            - 16MB OPI-PSRAM, 144 MHz interface frequency

        - Onboard 16MB QSPI-NOR Flash, 72 MHz interface frequency, STR mode
2. Crystals
    - 48 MHz crystal
    - 32.768 KHz crystal
3. Antenna
    - Onboard PCBA antenna
    - Onboard I-PEX antenna connector
4. GPIO
    - Supports 37 GPIOs
5. UART-I2C-GPTIM
    - 3x UART
    - 4x I2C
    - 2x GPTIM
    - All GPIOs can be configured as UART, I2C, or GPTIM
6. SPI
    - 2x SPI
7. GPADC
    - 6x GPADC
8. Display
    - FPC16P, 0.5 mm pitch connector for display expansion
    - SPI/DSPI/Quad SPI, supports DDR-mode QSPI display interface
    - Supports touch panels with an I2C interface
    - Supports the **1.85inch AMOLED Module** display through a 16p flat cable
9. Audio
    - Supports audio ADC input for analog microphones or MEMS microphones
    - Supports PDM digital microphone input
    - Analog audio output requires an external Class-AB/D audio PA to drive a speaker
10. USB
    - Type-C UART interface with onboard CH340N serial chip for firmware download, software debug, and power supply
    - USB interface, supports USB 2.0 FS, routed out through pin headers
11. Buttons
    - 1x function button
    - 1x power button, supports long-press reset for 10 seconds
12. LEDs
    - 1x LED, GPIO controlled
13. Power supply
    - Powered through the USB Type-C interface
    - Onboard LDO converts VBUS 5 V to 3.3 V
    - Onboard power switch can be enabled through the CH340N RTS# pin to reset the MCU
    - Supports jumper configuration for 1.8 V or 3.3 V MCU power supply
    - Supports measuring single-rail power current by connecting an ammeter in series
    - Supports single-MCU power test, minimum-system power test, and whole-board power test

## 3. Pin Definition

```{image} assets/SF32LB52-DevKit-Core-3p3-T-pinout.svg
:width: 100%
:align: center
```

<div align="center"> Development board pinout (click to enlarge) </div>  <br>  <br>  <br>

### Detailed Pin Description

The following table provides detailed descriptions of the pins on the SF32LB52-DevKit-Core-3p3 development board.

<div align="center"> LEFT PIN (J1) pin description table </div>

```{table}
:align: center
:width: 100%
:widths: 10 16 64 10
:class: devkit-pin-table

|Pin|Pin Name|Reset Default and Multiplexed Functions|Pull|
|:--|:-----------------------|:-----------|------|
|1  | GND   | Ground                     |  |
|2  | PA_44 | **PA44**, UART, I2C, GPTIM, and WKUP20                    | PD |
|3  | PA_43 | **PA43**, UART, I2C, GPTIM, and WKUP19                    | PD |
|4  | PA_42 | **PA42**, UART, I2C, GPTIM, and WKUP18                    | PU |
|5  | PA_41 | **PA41**, UART, I2C, GPTIM, and WKUP17                    | PU |
|6  | PA_40 | **PA40**, UART, I2C, GPTIM, SPI2_CS, and WKUP16            | PU |
|7  | PA_39 | **PA39**, UART, I2C, GPTIM, SPI2_CLK, and WKUP15           | PU |
|8  | PA_38 | **PA38**, UART, I2C, GPTIM, SPI2_DI, and WKUP14            | PD |
|9  | PA_37 | **PA37**, UART, I2C, GPTIM, SPI2_DIO, and WKUP13           | PD |
|10 | PA_36 | **PA36**, UART, I2C, GPTIM, USB_DM, and WKUP12             | PD |
|11 | PA_35 | **PA35**, UART, I2C, GPTIM, USB_DP, and WKUP11             | PD |
|12 | PA_31 | **PA31**, UART, I2C, GPTIM, and GPADC3                     | PD |
|13 | PA_30 | **PA30**, UART, I2C, GPTIM, I2S1_LRCK, and GPADC2          | PD |
|14 | PA_29 | **PA29**, UART, I2C, GPTIM, SPI1_CS, I2S1_BCK, and GPADC1  | PD |
|15 | PA_28 | **PA28**, UART, I2C, GPTIM, SPI1_CLK, I2S1_SDI, and GPADC0 | PD |
|16 | GND   | Ground                     |  |
|17 | 3.3V  | 3.3 V power. When USB Type-C is not connected, it can be used as a 3.3 V input; when USB Type-C is connected, it can be used as a 3.3 V output |  |
|18 | PA_27 | **PA27**, UART, I2C, GPTIM, and WKUP3                     | PU |
|19 | PA_26 | **PA26**, UART, I2C, GPTIM, and WKUP2                     | PU |
|20 | PA_25 | **PA25**, UART, I2C, GPTIM, SPI1_DI, I2S1_SDO, and WKUP1   | PD |
|21 | PA_24 | **PA24**, UART, I2C, GPTIM, SPI1_DIO, I2S1_MCLK, and WKUP0 | PD |
|22 | PA_34 | **PA34**, UART, I2C, GPTIM, GPADC6, and WKUP10             | PD |
|23 | PA_33 | **PA33**, UART, I2C, GPTIM, and GPADC5                    | PD |
|24 | PA_32 | **PA32**, UART, I2C, GPTIM, and GPADC4                    | PD |
```

<div align="center"> RIGHT PIN (J2) pin description table </div>

```{table}
:align: center
:width: 100%
:widths: 10 16 64 10
:class: devkit-pin-table

|Pin|Pin Name|Reset Default and Multiplexed Functions|Pull|
|:--|:-----------------------|:-----------|------|
|1  | GND   | Ground                     |  |
|2  | PA_00 | **PA00**, UART, I2C, GPTIM, and LCD_RST                   | PD |
|3  | PA_01 | **PA01**, UART, I2C, GPTIM, and BL_PWM                    | PD |
|4  | PA_02 | **PA02**, UART, I2C, GPTIM, LCD_TE, and I2S1_MCLK          | PD |
|5  | PA_03 | **PA03**, UART, I2C, GPTIM, LCD_CS, and I2S1_SDO           | PU |
|6  | PA_04 | **PA04**, UART, I2C, GPTIM, LCD_CLK, and I2S1_SDI          | PD |
|7  | PA_05 | **PA05**, UART, I2C, GPTIM, LCD_D0, and I2S1_BCK           | PD |
|8  | PA_06 | **PA06**, UART, I2C, GPTIM, LCD_D1, and I2S1_LRCK          | PD |
|9  | PA_07 | **PA07**, UART, I2C, GPTIM, LCD_D2, and PDM1_CLK           | PD |
|10 | PA_08 | **PA08**, UART, I2C, GPTIM, LCD_D3, and PDM1_DAT           | PD |
|11 | PA_09 | **PA09**, UART, I2C, GPTIM, and CTP_INT                    | PD |
|12 | MIC_ADC  | MIC input signal           |  |
|13 | MIC_BIAS | MIC bias voltage           |  |
|14 | DACP  | Analog audio output signal          |  |
|15 | DACN  | Analog audio output signal          |  |
|16 | GND   | Ground                    |  |
|17 | 1.8V  | 1.8 V power. When USB Type-C is not connected, it can be used as a 1.8 V input; when USB Type-C is connected, it can be used as a 1.8 V output |  |
|18 | PA_10 | **PA10**, UART, I2C, GPTIM, and CTP_RST                    | PD |
|19 | PA_11 | **PA11**, UART, I2C, GPTIM, and CTP_SDA                    | PU |
|20 | PA_20 | **PA20**, UART, I2C, GPTIM, and CTP_SCL                    | PD |
|21 | PA_21 | **PA21**, UART, I2C, and GPTIM                            | PD |
|22 | PA_18 | **UART0_RXD**, debug and download port, PA18, SWDIO, I2C, and GPTIM     | PU |
|23 | PA_19 | **UART0_TXD**, debug and download port, PA19, SWCLK, I2C, and GPTIM     | None |
|24 | 5V    | 5 V power. When USB Type-C is not connected, it can be used as a 5 V input; when USB Type-C is connected, it can be used as a 5 V output |  |
```

### 16p QSPI FPC Interface Pin Sequence Definition

<div align="center"> 16p FPC interface signal definition </div>

```{table}
:align: center
:width: 100%
:widths: 10 16 64 10
:class: devkit-pin-table

|Pin|Pin Name|Reset Default and Multiplexed Functions|Pull|
|:--|:-----------------------|:-----------|------|
|1  | GND    | Ground                        |      |
|2  | PA_00 | **PA00**, UART, I2C, GPTIM, and LCD_RST   | PD   |
|3  | PA_01 | **PA01**, UART, I2C, GPTIM, and BL_PWM    | PD   |
|4  | PA_02 | **PA02**, UART, I2C, GPTIM, LCD_TE, and I2S1_MCLK   | PD   |
|5  | PA_03 | **PA03**, UART, I2C, GPTIM, LCD_CS, and I2S1_SDO    | PU   |
|6  | PA_04 | **PA04**, UART, I2C, GPTIM, LCD_CLK, and I2S1_SDI   | PD   |
|7  | PA_05 | **PA05**, UART, I2C, GPTIM, LCD_D0, and I2S1_BCK    | PD   |
|8  | PA_06 | **PA06**, UART, I2C, GPTIM, LCD_D1, and I2S1_LRCK   | PD   |
|9  | PA_07 | **PA07**, UART, I2C, GPTIM, LCD_D2, and PDM1_CLK    | PD   |
|10 | PA_08 | **PA08**, UART, I2C, GPTIM, LCD_D3, and PDM1_DAT    | PD   |
|11 | 3.3V  | 3.3 V power output                  |      |
|12 | GND    | Ground                        |      |
|13 | PA_09 | **PA09**, UART, I2C, GPTIM, and CTP_INT    | PD   |
|14 | PA_11 | **PA11**, UART, I2C, GPTIM, and CTP_SDA    | PU   |
|15 | PA_20 | **PA20**, UART, I2C, GPTIM, and CTP_SCL    | PD   |
|16 | PA_10 | **PA10**, UART, I2C, GPTIM, and CTP_RST    | PD   |
```

## 4. Function Introduction

### Power Supply Description

The development board supports the following three power supply methods:

- USB Type-C power supply (default)
- 5 V and GND pin-header power supply
- 3.3 V and GND pin-header power supply

The recommended power supply method during debugging is the Type-C USB interface.

### LED Control

The development board has one onboard LED. Developers can control the corresponding pin according to the table below.

<div align="center"> LED signal control table </div>

```{table}
:align: center
:width: 100%
:widths: 20 20 60
:class: devkit-simple-table

|LED No.|GPIO|Description|
|:--|:-----------------------|:-----------|
|LED  | PA32    | Active high                 |
```

### External Flash

The development board has one onboard Flash device depending on the board variant. Some variants mount it and some do not. Supported types:

- SPI NOR Flash, WSON8-8x6mm or WSON8-6x5mm
- SPI NAND Flash, WSON8-8x6mm
- SD NAND Flash, WSON8-8x6mm

<div align="center"> Flash signal definition </div>

```{table}
:align: center
:width: 100%
:widths: 10 16 64 10
:class: devkit-pin-table

|Pin|Pin Name|Reset Default and Multiplexed Functions|Pull|
|:--|:-----------------------|:-----------|------|
|1  | PA_12 | **PA12**, UART, I2C, GPTIM, MPI2_CS, and SD1_D2    | PU   |
|2  | PA_13 | **PA13**, UART, I2C, GPTIM, MPI2_D1, and SD1_D3    | PD   |
|3  | PA_14 | **PA14**, UART, I2C, GPTIM, MPI2_D2, and SD1_CLK   | PD   |
|4  | PA_15 | **PA15**, UART, I2C, GPTIM, MPI2_D0, and SD1_CMD   | PD   |
|5  | PA_16 | **PA16**, UART, I2C, GPTIM, MPI2_CLK, and SD1_D0    | PD   |
|6  | PA_17 | **PA17**, UART, I2C, GPTIM, MPI2_D3, and SD1_D1    | PD   |
```

<div align="center"> Board variant and Flash information table </div>

```{table}
:align: center
:width: 100%
:widths: 42 28 30
:class: devkit-model-table

|Development Board Model|MCU Stacked Memory Specification|Onboard Specification|
|:--|:-----------------------|:-----------|
|SF32LB52-DevKit-Core-3p3-N1      | 1MB SPI NOR Flash | None    |
|SF32LB52-DevKit-Core-3p3-N4      | 4MB SPI NOR Flash | None    |
|SF32LB52-DevKit-Core-3p3-R4N16   | 4MB OPI PSRAM  | 16MB SPI NOR Flash    |
|SF32LB52-DevKit-Core-3p3-R8N16   | 8MB OPI PSRAM  | 16MB SPI NOR Flash    |
|SF32LB52-DevKit-Core-3p3-R16N16  | 16MB OPI PSRAM | 16MB SPI NOR Flash    |
```

### Buttons

The development board has two onboard buttons whose functions are defined by software. KEY1 supports a hardware reset after a 10-second long press. Developers can control the corresponding pins according to the table below.

<div align="center"> Button signal control table </div>

```{table}
:align: center
:width: 100%
:widths: 20 20 60
:class: devkit-simple-table

|Button No.|GPIO|Description|
|:--|:-----------------------|:-----------|
|KEY1  | PA34    | Active high, supports 10-second long-press reset |
|KEY2  | PA33    | Active high                |
```

### Download and Debug

Connect the USB cable to the USB-to-UART port, open SiFli Technology's firmware download tool, and select the corresponding COM port and firmware.

1. Download mode
    - Select the BOOT option, power on the board, and enter download mode after startup to complete firmware download.
2. Software development mode
    - Clear the BOOT option, power on the board, and enter serial log output mode for software debugging.
3. Development board reset
    - Use the host-side tool to control the CH340N RTS# pin to reset the MCU.

**For details, refer to&emsp;[Firmware Flashing Tool Impeller](../../tools/烧录工具)**

### LCD Display Interface

The development board supports QSPI-interface LCD screens. The connector is a vertical 16p-0.5pitch FPC, flip-up, bottom-contact type.
Refer to the signal pin sequence defined above. If the pin sequence differs, use an adapter board for testing; see the SF32LB52-DevKit-LCD Adapter Board Fabrication Guide.

The **1.85inch AMOLED Module** can be connected directly through an FPC-22p flat cable.

```{image} assets/FPC-22P.png
:width: 80%
:align: center
```

<div align="center"> FPC adapter cable </div>  <br>  <br>  <br>

### Audio Expansion

The development board requires an external microphone and differential audio power amplifier.

- [Reference electret microphone board](https://item.taobao.com/item.htm?id=891546819215&pisk=g3ttX5NYqXciCTxOKdu3mg2lmpDkD2vNvCJ7msfglBdphC1GiNsbdM6A3l1f5K6fDBOmQ1vj_IKAOG_2SsfGMip2wFhoq0vwQiSSZbmk_owrJgP_f1Ncdk6RDONxuxqpQiSjZbmoqdJwNSry3l6fdvBG3tsfGl1IpT6lcl_bfyNCT6sbfO__Ry6fhSZ1GIwIAtX8crZf5D_CnTIfGI6jpp1Fhi1j9jlAOR10DUgQANrLBEqbcHBORwv11a7-n97T3dfac9-NB05WC6Ebm14gj8ppIfEyKG-MwTAiAldJhL8fJnFIws-pdhTXL5hAXpAw2Gt-6lXhv1Q5d3M0z6xdsItORYqRoMtlPGTn8fbcXts1zek4SsTXe3IMsXrfsUpB9ax3tujWzBKAPgsr_3xJmCVlwt4tpna4uN6E_bxHypqU4QWdZAnYur7ELo49mA44uw-Pp_DtWrzV8X5..&spm=a21xtw.29178619.product_shelf.3.34d33772zuSkO1&skuId=5740404937614)
- [Reference MEMS microphone board](https://detail.tmall.com/item.htm?id=814534179060&ns=1&pisk=g53Se-TCQTXSM7adOuA4GovZEnUEB2t27L5IsfeFzMU-hJej6Q2yx3DIcvH048eyZyZKpYHQxQ2UpJME90oW7FloZy4KRd8w7X1wqAH79uIJ9ZF_9IPRFEzkwy4pQd8w7bcu-A0VoWbdDSe0NMFKpuIvk72Y9gUKp-EY65W8JvHpksF3TaILvWIvG7VCJge8prBYaWILpvUpGje09yF-pyhh41NBV8cWwk_r8dRlbJwfJw3bMJDrGUSQ3cNSvRGRYjGxlNq7Bbef8d9YgqwQnVp2cjDr2YPmdF9bWcDjRlUBPOVSDfaYUPLRkzuowcEKWpjKNzwSpkiDCNP7zmZsP0AhHbHaFcUoT19rGkFsrzo2FNetfbnai2JcyJixv4ru-TpQKqGxyDsrmNy1kVsCGlbLGgAXGMjHuIb4G5SWKTq8i7Z2GI6-xObd8iRXGTnu2SV77IOfevf..&priceTId=213e054e17429838198525727ea59a&skuId=5678321102126&spm=a21n57.1.hoverItem.1&utparam=%7B%22aplus_abtest%22%3A%22730abba11fa183522caa7f9e2e59074c%22%7D&xxc=ad_ztc)
- [Reference audio power amplifier board](https://item.taobao.com/item.htm?id=12602258834&pisk=g0_-U1DKS-2uuY_Ji_rm-FD4yzVGJofPMT5s-pvoAtBAOT9kKBTBGjOptDiCOpYdp9BpEHwyrwBvzZjo-L2yJ66MWR2gSPfPaF8QIRD0Vn9v5CJINvAShrTH9SVDsp5Pae8QIR4gS_kKdDDKAB9QMrOBteOBRHNYlBpjPBgWOxNv3KgWN3tWhrOkwQiCd3tjcBRHO0gIRKOX3BTBd9TQMs92OfrQpKGWK2I_ccEC086nR2_vwntcNLGv-ZOJCdCSx2gIYQKJC_94QNZ2_n1evwlEJnf5b9R1FYwpLZCfPG6_n0v5XBCGvOUs8IS5eZtdoWzNMUIAkUb7Lc5cMLt9oiq4EHYReGJwVoyVChCGjU7_HV9dVTWebw2ZzL1C_NSMWzHwwi19kgyOSNQhEAv9t0FARDoeVIyzIZjt6G1omIpgwynEYnPq-0Q3ZDoe0NRvI7E-YD-43&spm=a21xtw.29178619.product_shelf.2.654a20dbhEwOYd)

### PCB Component Position Lookup

<a href="../../_static/SF32LB52-DevKit-Core-3p3-%E8%BE%85%E5%8A%A9%E7%84%8A%E6%8E%A5.html">SF32LB52-DevKit-Core-3p3-PCB</a>

## 5. Sample Acquisition

Retail samples and small batches can be purchased directly from [Taobao](https://sifli.taobao.com/). For volume customers, email sales@sifli.com or contact Taobao customer service to obtain sales contact information.
Open-source contributors can apply for free samples and join QQ group 674699679 for discussion.

## 6. Related Documents

- [SF32LB52X Chip Datasheet](https://downloads.sifli.com/user%20manual/DS5202-SF32LB52X-Datasheet%20V0p2p5.pdf)
- [SF32LB52X User Manual](https://downloads.sifli.com/docs/user%20manual/SF32LB52x/UM5201%E2%80%90SF32LB52x%E2%80%90EN.pdf)
- [SF32LB52-DevKit-Core-3p3 Design Drawings](https://downloads.sifli.com/hardware/files/documentation/ProPrj_SF32LB52-DevKit-Core-3p3-V100_2025-06-10.epro?)
- [SF32LB52-DevKit-LCD Adapter Board Fabrication Guide](SF-DevKit-LCM-Adapter)
