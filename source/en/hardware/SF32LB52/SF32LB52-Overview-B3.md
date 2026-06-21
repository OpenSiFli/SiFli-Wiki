## Basic Introduction

The main purpose of this document is to help developers develop watch solutions based on the SF32LB52X series chips. This document focuses on hardware design considerations during solution development, with the goal of minimizing developer workload and shortening the product time to market.

SF32LB52X is a series of highly integrated, high-performance MCU chips for ultra-low-power artificial intelligence Internet of Things (AIoT) scenarios. The chip uses a big-core/little-core architecture based on the Arm Cortex-M33 STAR-MC1 processor and integrates a high-performance 2D/2.5D graphics engine, an artificial intelligence neural network accelerator, dual-mode Bluetooth 5.3, and an audio CODEC. It can be widely used in wrist-worn wearable electronic devices, smart mobile terminals, smart homes, and various other application scenarios.

:::{attention}
SF32LB52X is the **standard power-supply version of the SF32LB52 series, with a supply voltage of 2.97~3.63V and no charging support**. It specifically includes the following models:\
SF32LB52BU36, co-packaged 1MB QSPI-NOR Flash \
SF32LB52EUB6, co-packaged 4MB OPI-PSRAM \
SF32LB52GUC6, co-packaged 8MB OPI-PSRAM \
SF32LB52JUD6, co-packaged 16MB OPI-PSRAM
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
- Supports single-/dual-/quad-data-line SPI display interfaces and serial JDI-mode display interfaces
- Supports both displays with GRAM and displays without GRAM
- Supports UART firmware download and software debugging


## Package


<div align="center"> Package Information Table </div>

```{table}

|Package Name|Dimensions|Pin Pitch|
|:--|:-|:-|
|QFN68L | 7x7x0.85 mm | 0.35 mm |
```


<img src="assets/52xB/sf32lb52X-B-package-layout.png" width="80%" align="center" />  

<div align="center"> SF32LB52X QFN68L Pinout </div>



## Typical Application Solution

The figure below is a block diagram of a typical SF32LB52A/52D sports watch. Its main function blocks include display, storage, sensors, a vibration motor, and audio input and output.

<img src="assets/52xB/sf32lb52X-B-watch-app-diagram-52X.png" width="80%" align="center" />  

<div align="center"> SF32LB52B/52E Sports Watch Block Diagram </div>


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
