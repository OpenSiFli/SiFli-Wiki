## Basic Introduction

The main purpose of this document is to assist developers in completing the development of watch solutions based on the SF32LB52X series of chips. This document focuses on hardware design considerations during the development process, aiming to minimize the workload of developers and shorten the product's time to market.

The SF32LB52X is a series of highly integrated, high-performance MCU chips designed for ultra-low power artificial intelligence of things (AIoT) scenarios. The chip features a big.LITTLE architecture based on the Arm Cortex-M33 STAR-MC1 processor, integrated high-performance 2D/2.5D graphics engine, artificial intelligence neural network accelerator, dual-mode Bluetooth 5.3, and audio CODEC. It can be widely used in various applications, including wearable electronic devices, smart mobile terminals, and smart home devices.

:::{attention}
The SF32LB52X is the **standard power supply version of the SF32LB52 series, with a supply voltage of 2.97~3.63V and no support for charging**. It includes the following models:\
SF32LB52BU36, with 1MB QSPI-NOR Flash \
SF32LB52EUB6, with 4MB OPI-PSRAM \
SF32LB52GUC6, with 8MB OPI-PSRAM \
SF32LB52JUD6, with 16MB OPI-PSRAM
:::

The processor peripheral resources are as follows:

- 45x GPIO
- 3x UART
- 4x I2C
- 2x GPTIM
- 2x SPI
- 1x I2S audio interface
- 1x SDIO storage interface
- 1x PDM audio interface
- 1x differential analog audio output
- 1x single-ended analog audio input
- Support for single, dual, and quad data line SPI display interfaces, and support for serial JDI mode display interfaces
- Support for displays with and without GRAM
- Support for UART download and software debugging

## Packaging

<div align="center"> Packaging Information Table </div>

```{table}

| Package Name | Size | Pin Pitch |
|:--|:-|:-|
| QFN68L | 7x7x0.85 mm | 0.35 mm |
```

<img src="assets/52xB/sf32lb52X-B-package-layout.png" width="80%" align="center" />  

<div align="center"> SF32LB52X QFN68L Pin Distribution </div>

## Typical Application Solution

The following diagram is a typical block diagram of the SF32LB52A/52D sports watch, which includes display, storage, sensors, vibration motor, and audio input and output functions.

<img src="assets/52xB/sf32lb52X-B-watch-app-diagram-52X.png" width="80%" align="center" />  

<div align="center"> SF32LB52B/52E Sports Watch Block Diagram </div>

:::{Note} 
   - Big.LITTLE dual-CPU architecture, balancing high performance and low power design requirements
   - Integrated charging management and PMU module
   - Support for TFT or AMOLED displays with QSPI interface, up to 512*512 resolution
   - Support for PWM backlight control
   - Support for external QSPI Nor/Nand Flash and SD Nand Flash storage chips
   - Support for dual-mode Bluetooth 5.3
   - Support for analog audio input
   - Support for analog audio output
   - Support for PWM vibration motor control
   - Support for SPI/I2C interface acceleration/magnetic/gyroscope sensors
   - Support for SPI/I2C interface heart rate/blood oxygen/EKG/magnetic sensors
   - Support for UART debugging print interface and programming tools
   - Support for Bluetooth HCI debugging interface
   - Support for one-to-many program burning in production lines
   - Support for crystal calibration in production lines
   - Support for OTA online upgrade function
:::