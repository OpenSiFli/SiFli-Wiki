# Development Board Model Guide

## Development Board Numbering Rules SF32LB5x-DevKit-Xxxx-AaaaBbbbCccc

### Main Category *SF32LB5x-DevKit*

- SF: chip series
    - SiFli, company logo
- 32: chip series
    - 32: 32-bit MCU series
- LB: series attribute
    - LB：Low-power Bluetooth MCU
    - VB: Bluetooth MCU using a RISC-V processor
- 5: processor series
    - 5: based on a 32-bit Arm Cortex-M33 Star-MC1 processor, or a RISC-V processor with similar computing performance
    - 0: based on a 32-bit Arm Cortex-M0+ processor
- x: high-, mid-, or low-end positioning
    - 8: flagship product in the 5x series
    - 6/5: mid-range products in the 5x series
    - 2: value-oriented product in the 5x series

### Subcategory *Xxxx*
- 3p3: does not support lithium battery power supply; standard 3.3 V power supply series
- Vbat: series supporting lithium battery power supply
- y: subcategory dedicated to 52 modules
    - 1: series supporting lithium battery power supply, with an onboard SF32LB525UC6/SF32LB527UD6 chip
    - A: does not support lithium battery power supply; standard 3.3 V power supply series, with an onboard SF32LB52BU36/SF32LB52BU36 chip and co-packaged FLASH
    - B: does not support lithium battery power supply; standard 3.3 V power supply series, with an onboard SF32LB52DUB6/SF32LB52JUD6 chip and co-packaged PSRAM

### Configuration Category *AaaaBbbbCccc*
- Aaaa: variable Flash capacity
    - N16：16MB QSPI-NOR Flash
    - A128：128MB SPI-Nand Flash
    - D128：128MB SD-Nand Flash
    - E4：  4GB eMMC
- Bbbb: PSRAM capacity
    - R4：4MB OPI-PSRAM
    - R8：8MB OPI-PSRAM
    - R12：4MB+8MB OPI-PSRAM
    - R16：16MB OPI/HPI-PSRAM
    - R32：16+16MB HPI-PSRAM
    - R64：32+32MB HPI-PSRAM
- Cccc: standard Flash capacity
    - N1：1MB QSPI-NOR Flash
    - N4：4MB QSPI-NOR Flash


## SF32LB52-DevKit-Nano

Development board code| Chip code | Variable Flash capacity | PSRAM capacity | Standard Flash | Ambient temperature | Development board dimensions (mm)
:- | :-|:-|:-|:-|:-|:-
SF32LB52-DevKit-Nano-N4      | SF32LB52BU56 | None            | None           | 4MB QSPI-NOR | -40~85C | 51*20.32
SF32LB52-DevKit-Nano-N16R16  | SF32LB52JUD6 | 16MB QSPI-NOR   | 16MB OPI-PSRAM | None         | -40~85C | 51*20.32
SF32LB52-DevKit-Nano-A128R16 | SF32LB52JUD6 | 128MB QSPI-NAND | 16MB OPI-PSRAM | None         | -40~85C | 51*20.32

## SF32LB52-DevKit-Core

Development board code| Chip code | Variable Flash capacity | PSRAM capacity | Standard Flash | Ambient temperature | Development board dimensions (mm)
:- | :-|:-|:-|:-|:-|:-
SF32LB52-DevKit-Core-3p3-N4      | SF32LB52BU56 | None            | None           | 4MB QSPI-NOR | -40~85C | 68*31
SF32LB52-DevKit-Core-3p3-N16R16  | SF32LB52JUD6 | 16MB QSPI-NOR   | 16MB OPI-PSRAM | None         | -40~85C | 68*31
SF32LB52-DevKit-Wlan-Core-3p3-N16R16  | SF32LB52JUD6 | 16MB QSPI-NOR   | 16MB OPI-PSRAM | None         | -40~85C | 82*62


## SF32LB52-DevKit-LCD

* For use with SF32LB52-MOD-1, SF32LB52-MOD-A, and SF32LB52-MOD-B series modules
* Recommended model: SF32LB52-DevKit-LCD-1
* Development board power supply: USB-Type-C or lithium-ion battery
* Supports charging. A 450 mAh single-cell polymer lithium battery is recommended, with a nominal voltage of 3.7 V and a fully charged voltage of 4.2 V
* Onboard CH343P chip, supporting one USB-to-UART debug port
* Onboard 1x switch button, 1x function button, and 1x reset button
* Onboard SPI, DSPI, QSPI, and 8080 display interfaces, using a 22p, 0.5 mm-pitch FPC adapter connector
* Onboard 40p, 2x20p dual-row header signal adapter interface
* Onboard 1-channel MEMS MIC
* Onboard 1-channel audio amplifier, supporting connection of 1-channel SPK (up to 3 W/4 ohms)
* Onboard 1x RGBLED, 1x Charger LED, 1x GPIO-controlled LED, and 1x power indicator LED
* Onboard TF card socket with SPI interface
* SF32LB52-DevKit-LCD-A can connect to an external NOR Flash or external SDIO peripherals, including WiFi, SD-NAND, or eMMC (4-line mode)


Development board code| Module code | Flash capacity | PSRAM capacity | Ambient temperature | Development board dimensions (mm)
:- | :-|:-|:-|:-|:-
SF32LB52-DevKit-LCD-1-N16R8   | SF32LB52-MOD-1-N16R8   | 16MB QSPI-NOR   | 8MB OPI-PSRAM  | -40~85C | 65*38
SF32LB52-DevKit-LCD-1-A128R16 | SF32LB52-MOD-1-A128R16 | 128MB QSPI-NAND | 16MB OPI-PSRAM | -40~85C | 65*38
<!-- SF32LB52-DevKit-LCD-A-N1      | SF32LB52-MOD-A-N1      | 1MB QSPI-NOR    | n/a            | -40~85C | 65*38 -->
<!-- SF32LB52-DevKit-LCD-B-N16R4   | SF32LB52-MOD-B-N16R4   | 16MB QSPI-NOR   | 4MB OPI-PSRAM  | -40~85C | 65*38 -->



## SF32LB56-DevKit-LCD

* For use with SF32LB56-MOD series modules
* Development board power supply: USB-Type-C
* Onboard CH343K chip, supporting two USB-to-UART debug ports
* Onboard SWD interface, 4p-2.54 mm-pitch single-row header
* Supports Mode boot mode jumper
* Onboard 1x switch button, 1x function button, and 1x reset button
* Onboard MIPI-DPI (RGB-24bit) display interface, using a 40p, 0.5 mm-pitch FPC adapter connector, compatible with the ALIENTEK RGB interface pin order
* Onboard 40p, 2x20p dual-row header signal adapter interface
* Onboard 1-channel MEMS MIC
* Onboard 1-channel audio amplifier, supporting connection of 1-channel SPK (up to 3 W/4 ohms)
* Onboard 1x RGBLED, 1x GPIO-controlled LED, and 1x power indicator LED
* Onboard TF card socket with SDIO interface


Development board code| Module code | Flash capacity | PSRAM capacity | Standard Flash | Ambient temperature | Development board dimensions (mm)
:-| :-|:-|:-|:-|:-|:-
SF32LB56-DevKit-LCD-N16R12N1  | SF32LB56-MOD-N16R12N1  | 16MB QSPI-NOR   | 4+8MB OPI-PSRAM | 1MB QSPI-NOR | -40~85C | 65*38
SF32LB56-DevKit-LCD-A128R12N1 | SF32LB56-MOD-A128R12N1 | 128MB QSPI-NAND | 4+8MB OPI-PSRAM | 1MB QSPI-NOR | -40~85C | 65*38

## SF32LB58-DevKit-LCD

* For use with SF32LB58-MOD series modules
* Development board power supply: USB-Type-C
* Onboard CH343K chip, supporting two USB-to-UART debug ports
* Onboard SWD interface, included in the 40p dual-row header
* Supports Mode boot mode jumper
* Onboard 1x switch button, 1x function button, and 1x reset button
* Onboard MIPI-DSI (2lane) display interface, using a 30p, 0.5 mm-pitch FPC adapter connector
* Onboard MIPI-DPI (RGB-24bit) display interface, using a 40p, 0.5 mm-pitch FPC adapter connector, compatible with the ALIENTEK RGB interface pin order
* Onboard dual 40p, 2x20p dual-row header signal adapter interfaces
* Onboard 1-channel MEMS MIC
* Supports 2-channel audio ADC input, included in the 40p dual-row header
* Onboard 2-channel audio amplifier outputs, supporting connection of 2-channel SPK (up to 3 W/4 ohms), included in the 40p dual-row header
* Onboard 1x RGBLED, 2x GPIO-controlled LEDs, and 1x power indicator LED
* Onboard TF card socket with SDIO interface


Development board code| Module code | Flash capacity | PSRAM capacity | Standard Flash capacity | Ambient temperature | Development board dimensions (mm)
:-| :-|:-|:-|:-|:-|:-
SF32LB58-DevKit-LCD-N16R32N1  | SF32LB58-MOD-N16R32N1  | 16MB QSPI-NOR   | 16+16MB HPI-PSRAM | 1MB QSPI-NOR | -40~85C | 65*50
SF32LB58-DevKit-LCD-A128R32N1 | SF32LB58-MOD-A128R32N1 | 128MB QSPI-NAND | 16+16MB HPI-PSRAM | 1MB QSPI-NOR | -40~85C | 65*50


## SF32-OED-6'-EDP

* For use with the SF32LB52-MOD-1 module
* Development board power supply: lithium-ion battery
* Supports charging, with a USB-Type-C charging port. A 1500 mAh single-cell polymer lithium battery is recommended, with a nominal voltage of 3.7 V and a fully charged voltage of 4.2 V
* Onboard CH340N chip, supporting one USB-to-UART debug port
* Onboard 3 GPADC buttons
* Onboard x8 EDP display interface, using a 34p, 0.5 mm-pitch FPC adapter connector
* Onboard touchscreen interface, using an 8p, 0.5 mm-pitch FPC adapter connector
* Onboard 1-channel MEMS MIC
* Onboard 1-channel audio amplifier, supporting connection of 1-channel SPK (up to 3 W/4 ohms)
* Onboard 6-axis (accelerometer and gyroscope) IMU and temperature/humidity sensor
* Onboard TF card socket with SPI interface


Development board code| Module code | Flash capacity | PSRAM capacity | Ambient temperature | Development board dimensions (mm)
:- | :-|:-|:-|:-|:-
SF32-OED-6'-EDP-N16R8   | SF32LB52-MOD-1-N16R8   | 16MB QSPI-NOR   | 8MB OPI-PSRAM  | -40~85C | 106*64
SF32-OED-6'-EDP-A128R16 | SF32LB52-MOD-1-A128R16 | 128MB QSPI-NAND | 16MB OPI-PSRAM | -40~85C | 106*64
