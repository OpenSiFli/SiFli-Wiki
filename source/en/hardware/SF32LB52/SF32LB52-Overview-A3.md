## Basic Introduction

The main purpose of this document is to help developers develop watch solutions based on the SF32LB52x series chips. This document focuses on hardware design considerations during solution development, with the goal of minimizing developers' workload and shortening the product time to market.

SF32LB52x is a series of highly integrated, high-performance MCU chips for ultra-low-power artificial intelligence Internet of Things (AIoT) scenarios. The chips use a big/little-core architecture based on the Arm Cortex-M33 STAR-MC1 processor, and integrate a high-performance 2D/2.5D graphics engine, an artificial intelligence neural network accelerator, dual-mode Bluetooth 5.3, and an audio CODEC. They can be widely used in various application scenarios, such as wristband-type wearable electronic devices, smart mobile terminals, and smart homes.

:::{attention}
SF32LB52x is the **lithium-battery-powered version of the SF32LB52 series, with a supply voltage of 3.2~4.7V and charging support**. It specifically includes the following models: \
SF32LB520U36, co-packaged 1MB QSPI-NOR Flash \
SF32LB523UB6, co-packaged 4MB OPI-PSRAM \
SF32LB525UC6, co-packaged 8MB OPI-PSRAM \
SF32LB527UD6, co-packaged 16MB OPI-PSRAM
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
- Supports single-/dual-/quad-data-line SPI display interfaces and serial JDI-mode display interfaces
- Supports both displays with GRAM and displays without GRAM
- Supports UART firmware download and software debugging


## Package


```{table} Package Information Table
:name: sf32lb52x-B-package-info

|Package Name|	Dimensions           	   |   Pin Pitch  |
|:--|:-----------------------|:-----------|
|QFN68L      | 7x7x0.85 mm       | 0.35 mm       |

```

```{figure} assets/sf32lb52x-A-package-layout.png
:scale: 60%
:name: sf32lb52X-B-package-layout

SF32LB52x QFN68L pinout
```


## Typical Application Solution

{numref}`Figure {number} <sf32lb52X-B-watch-app-diagram-52xU>` is a block diagram of a typical SF32LB520/521/523/525/527 sports watch. Its main functions include display, storage, sensors, a vibration motor, and audio input/output.

```{figure} assets/sf32lb52X-B-watch-app-diagram-52xU.png
:scale: 60%
:name: sf32lb52X-B-watch-app-diagram-52xU

SF32LB520/521/523/525/527 sports watch block diagram
```

:::{Note} 
   - Big/little dual-CPU architecture, meeting both high-performance and low-power design requirements
   - Integrates charging management and PMU modules on-chip
   - Supports TFT or AMOLED displays with a QSPI interface, with support for resolutions up to 512*512
   - Supports PWM backlight control
   - Supports external QSPI NOR/NAND Flash and SD NAND Flash memory chips
   - Supports dual-mode Bluetooth 5.3
   - Supports analog audio input
   - Supports analog audio output
   - Supports PWM vibration motor control
   - Supports accelerometer/geomagnetic/gyroscope sensors with SPI/I2C interfaces
   - Supports heart rate/blood oxygen/ECG/geomagnetic sensors with SPI/I2C interfaces
   - Supports UART debug print interface and flashing tools
   - Supports Bluetooth HCI debug interface
   - Supports one-to-many firmware flashing on the production line
   - Supports crystal calibration on the production line
   - Supports OTA online upgrade functionality
:::
