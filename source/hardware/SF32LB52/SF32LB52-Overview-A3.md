## Basic Introduction

The main purpose of this document is to assist developers in completing the development of watch solutions based on the SF32LB52x series of chips. This document focuses on hardware design considerations during the development process, aiming to minimize the workload of developers and shorten the product's time to market.

The SF32LB52x is a series of highly integrated, high-performance MCU chips designed for ultra-low-power artificial intelligence of things (AIoT) scenarios. The chip adopts a big.LITTLE architecture based on the Arm Cortex-M33 STAR-MC1 processor, integrating a high-performance 2D/2.5D graphics engine, an artificial intelligence neural network accelerator, dual-mode Bluetooth 5.3, and an audio CODEC. It can be widely used in various applications, including wearable electronic devices, smart mobile terminals, and smart home devices.

:::{attention}
The SF32LB52x is the **lithium battery-powered version of the SF32LB52 series, with a supply voltage of 3.2~4.7V and support for charging**. It includes the following models: \
SF32LB520U36, with 1MB QSPI-NOR Flash \
SF32LB523UB6, with 4MB OPI-PSRAM \
SF32LB525UC6, with 8MB OPI-PSRAM \
SF32LB527UD6, with 16MB OPI-PSRAM
:::

The processor peripheral resources are as follows:

- 44x GPIO
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
- Support for both GRAM and non-GRAM displays
- Support for UART download and software debugging

## Packaging

```{table} Packaging Information Table

:name: sf32lb52x-B-package-info

| Package Name | Size            | Pin Pitch  |
|:--|:-----------------------|:-----------|
| QFN68L      | 7x7x0.85 mm       | 0.35 mm       |

```

```{figure} assets/sf32lb52x-A-package-layout.png

:scale: 60%
:name: sf32lb52X-B-package-layout
SF32LB52x QFN68L Pin Distribution
```

## Typical Application Solutions

{numref}`Figure {number} <sf32lb52X-B-watch-app-diagram-52xU>` is a typical block diagram of the SF32LB520/521/523/525/527 sports watch, featuring display, storage, sensors, vibration motor, and audio input and output.

```{figure} assets/sf32lb52X-B-watch-app-diagram-52xU.png

:scale: 60%
:name: sf32lb52X-B-watch-app-diagram-52xU
Block Diagram of SF32LB520/521/523/525/527 Sports Watch
```

:::{Note} 
   - Big.LITTLE dual-CPU architecture, balancing high performance and low power consumption design requirements
   - Integrated charging management and PMU modules
   - Support for TFT or AMOLED displays with QSPI interface, with a maximum resolution of 512*512
   - Support for PWM backlight control
   - Support for external QSPI Nor/Nand Flash and SD Nand Flash storage chips
   - Support for dual-mode Bluetooth 5.3
   - Support for analog audio input
   - Support for analog audio output
   - Support for PWM vibration motor control
   - Support for SPI/I2C interface accelerometer/magnetometer/gyroscope sensors
   - Support for SPI/I2C interface heart rate/blood oxygen/EKG/magnetometer sensors
   - Support for UART debugging print interface and programming tools
   - Support for Bluetooth HCI debugging interface
   - Support for mass production programming
   - Support for crystal calibration function in production
   - Support for OTA online upgrade function
:::