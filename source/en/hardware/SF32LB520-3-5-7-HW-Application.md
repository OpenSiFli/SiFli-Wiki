# SF32LB52x Hardware Design Guide

:::{attention}
This document applies to chips with the numerical suffixes 0, 3, 5, and 7, which are powered by a lithium battery and support USB charging.

Chips with the suffixes B, E, G, J, and H belong to the SF32LB52X series and use a 3.3 V power supply. Refer to the [Hardware Design Guide](/hardware/SF32LB52B-E-G-J-HW-Application).
:::


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


<div align="center"> Table 2-1 Package Information Table </div>

```{table}

|Package Name|Dimensions|Pin Pitch|
|:--|:-|:-|
|QFN68L | 7x7x0.85 mm | 0.35 mm |
```


<img src="assets/52xA/sf32lb52x-A-package-layout.png" width="80%" align="center" />  

<div align="center"> Figure 2-1 QFN68L Pin Distribution </div>  <br> <br> <br>



## Typical Application Solution

The following figure shows the block diagram of a typical SF32LB52x sports watch. The main functions include display, storage, sensors, a vibration motor, and audio input and output.

<!-- This image has an issue and needs to be replaced with the B3 block diagram. -->
<img src="assets/52xA/sf32lb52x-A-watch-app-diagram-52x.png" width="80%" align="center" />  

<div align="center"> Figure 3-1 Sports Watch Block Diagram </div>   <br>  <br>  <br>


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



## Schematic Design Guidelines

### Power Supply

#### Processor Power Supply Requirements

<div align="center"> Table 4-1 Power Supply Requirements </div>

```{table}

|Power Supply pin| Minimum voltage (V) | Typical voltage (V) | Maximum voltage (V) | Maximum current (mA) |   Detailed description |
|:--|:--|:--|:--|:--|:----------------------------------------------------|
|VBUS       |4.6    |5.0    |5.5    |500    |VBUS Power Supply input 
|VBAT       |3.2    |-      |4.7    |500    |VBAT Power Supply output
|VCC        |3.2    |-      |4.7    |500    |System Power Supply input{sup}`(1)` 
|VSYS       |-      |3.3    |-      |500    |VSYS Power Supply output{sup}`(2)` 
|BUCK_LX    |-      |1.25   |-      |50     |BUCK output pin, connected to an inductor 
|BUCK_FB    |-      |1.25   |-      |50     |BUCK feedback and internal Power Supply input pin, connected to the other end of the inductor and an external capacitor 
|VDD_VOUT1  |-      |1.1    |-      |50     |Internal LDO, external capacitor, internal Power Supply, does not supply power to peripherals 
|VDD_VOUT2  |-      |0.9    |-      |20     |Internal LDO, external capacitor, internal Power Supply, does not supply power to peripherals 
|VDD_RET    |-      |0.9    |-      |1      |Internal LDO, external capacitor, internal Power Supply, does not supply power to peripherals 
|VDD_RTC    |-      |1.1    |-      |1      |Internal LDO, external capacitor, internal Power Supply, does not supply power to peripherals 
|VDD18_VOUT |-      |1.8    |-      |30     |SIP Power Supply{sup}`(3)` internal Power Supply, does not supply power to peripherals; can be supplied externally when the LDO is disabled
|VDD33_VOUT1|-      |3.3    |-      |150    |3.3V LDO output 1{sup}`(4)`, no output by default; software configuration is required for 3.3V output
|VDD33_VOUT2|-      |3.3    |-      |150    |3.3V LDO output 2, no output by default; software configuration is required for 3.3V output
|AVDD33_AUD |2.97   |3.3    |3.63   |50     |3.3V audio Power Supply input 
|AVDD_BRF   |2.97   |3.3    |3.63   |100    |RF Power Supply input 
|MIC_BIAS   |1.4    |-      |2.8    |-      |MIC Power Supply output 
```
:::{note} 

{sup}`(1)` VCC power input, powered by a lithium battery. The default software setting for the low battery voltage is 3.48 V. When powered by a constant-voltage power supply, the supply range is 3.6–4.7 V, and a 3.8 V supply is recommended. 

{sup}`(2)` VSYS power supply, supplies power to AVDD_BRF 

{sup}`(3)` VDD18_VOUTPower Supply \
SF32LB520U36, externally supplied 3.3V Power Supply \
SF32LB523UB6, SF32LB525UC6, SF32LB527UD6, use the internal LDO and do not require an external Power Supply \
When configuring the software, configure the internal VDD18 LDO according to the chip model; do not enable it when using an external Power Supply 

{sup}`(4)` VDD33_VOUT1Power Supply \
SF32LB520U36, only supplies power to VDD18_VOUT, external Flash, and AVDD33_AUD \
SF32LB523UB6, SF32LB525UC6, SF32LB527UD6, only supply power to the external Flash and AVDD33_AUD 
:::

#### Processor BUCK Inductor Selection Requirements

**Key Parameters of the Power Inductor**
:::{important}
L (inductance) = 4.7 uH ± 20%, DCR (DC resistance) ≦ 0.4 ohm, Isat (saturation current) ≧ 450 mA.
:::

<!-- The A3 version needs Battery and Charging Control content. -->
#### Battery and Charging Control

There are two usage scenarios for the charging circuit: an external charging management chip and an on-chip integrated charging management module.

##### External Charging Management Chip

External charging management chips are divided into two types: those without PPM (power path management) and those with PPM. Figure 4-1 shows a typical charging circuit using a charging chip without PPM. The battery directly supplies power to the VBAT and VCC pins of the SF32LB52x. Figure 4-2 shows a typical charging circuit using a charging chip with PPM. The VSYS of the charging chip supplies power to the VCC pin of the SF32LB52x, and the VBAT of the charging chip is connected to the battery and the SF32LB52x VBAT pin. Both solutions measure the battery voltage through the VBAT pin of the SF32LB52x. The VBAT pin has an integrated GPADC channel that can sample the VBAT voltage, with a sampling accuracy within +/-30 mV.

<img src="assets/52xA/sf32lb52x-CHG-NPPM.png" width="80%" align="center" />  

<div align="center"> Figure 4-1 Schematic Diagram of External Charging Chip Circuit without PPM Function </div>   <br>  <br>  <br>

<img src="assets/52xA/sf32lb52x-CHG-PPM.png" width="80%" align="center" />  

<div align="center"> Figure 4-2 Schematic Diagram of External Charging Chip Circuit with PPM Function </div>   <br>  <br>  <br>

##### On-Chip Integrated Charging Management Module

When using the on-chip integrated charging management module of the SF32LB52x, as shown in Figure 4-3, if the battery level is low and the device is powered off, after the charger is plugged in, the battery must be charged to the power-on voltage before the system can start normally and display the charging interface.

<img src="assets/52xA/sf32lb52x-CHG-INNER.png" width="80%" align="center" />  

<div align="center"> Figure 4-3 Schematic Diagram of Integrated Charging Management Circuit </div>   <br>  <br>  <br>

##### OVP Chip Selection When Using the On-Chip Integrated Charging Management Module

SF32LB52x VBUS pin input voltage range: 4.5 V ~ 5.5 V, so only the following two types of OVP chips can be selected:
- OVP chip with adjustable OVLO; reference chip model: AW32905FCR
- OVP chip with regulator output; reference chip models: SGM4064YDE8G, LP5305AQVF

Figure 4-4 shows a typical application circuit of an OVP chip with adjustable OVLO. The output voltage VIN_OVLO of the OVP chip should be set between 5.2V and 5.5V, and the tolerances of the chip and resistors should be considered in the calculation. The specific formula is:
<img src="assets/52xA/sf32lb52x-OVP-SET.png" width="80%" align="center" />  <br>  <br>

**Requirement: The tolerance of VOVLO_TH must be ≦3%, and the resistance tolerance of R1 and R2 must be ≦1%**

<img src="assets/52xA/sf32lb52x-OVP-OVLO.png" width="80%" align="center" />  

<div align="center"> Figure 4-4 Application Circuit Diagram of OVP Chip with Adjustable OVLO </div>   <br>  <br>  <br>

Figure 4-5 shows a typical application circuit diagram of an OVP chip with a regulator output. The fixed regulator output of the OVP chip is less than 5.5V and is used to supply power to the VBUS pin of SF32LB52x.

**Requirement: The LDO output voltage of the OVP chip must be 4.5V ~ 5.4V**

<img src="assets/52xA/sf32lb52x-OVP-REGU.png" width="80%" align="center" />  

<div align="center"> Figure 4-5 Application Circuit Diagram of OVP Chip with Regulator Output </div>   <br>  <br>  <br>

##### Notes on Using the Internal Charging Management Module and Integrated LDO

:::{important}
**Notes on using the SF32LB52x internal integrated charging management module:**
- VBUS input voltage range: 4.6V~5.5V
- VCC input voltage range: 3.2V~4.7V
- The default trickle current of the charger is 56mA.
- The default trickle-to-constant-current transition voltage of the charger is 3.0V.
- The default constant current of the Charger is 65 mA and can be adjusted. The adjustment range is 5 to 560 mA.
- The default full-charge voltage of the Charger is 4.2 V and can be adjusted. The maximum supported full-charge voltage is 4.45 V.
- The recharge voltage of the Charger is the full-charge voltage minus 0.15 V.
- The charger VBUS must provide at least 350 mA of current supply capability.
- Pay attention to the DC impedance on the VBUS path; it should not be too high. At the maximum current during the charging process, the voltage at the chip VBUS pin must not be lower than 4.6 V.
- When using wireless charging, ensure that the power supply capability of the wireless charger is greater than the constant-current charging current.

**Notes on using the SF32LB52x integrated LDO:**
- On the output paths of the internally integrated VDD33_VOUT1 and VDD33_VOUT2, the total capacitance must not exceed 9.6 uF.
- AVDD33_AUD can only be powered by VDD33_VOUT1 and cannot use VSYS.
- The LCD cannot be powered by the internal LDO; it must be powered by an external LDO.
:::

#### How to Reduce Standby Power Consumption

To meet the long battery life requirements of watch products, it is recommended to use load switches in the hardware design for dynamic power management of each functional module. For modules or paths that are always on, select appropriate devices to reduce quiescent current.

As shown in Figure 4-6, in the typical power architecture diagram of the SF32LB52x system, it is recommended to use VDD33_VOUT2 to power the Motor, VDD33_VOUT1 to power external peripherals such as Flash and Sensor, and an external LDO to power the LCD.

During design, pay attention to the hardware default state of the GPIO pin that controls the power switch, and add pull-up or pull-down resistors with MΩ-level resistance to ensure that the load switch is off by default.

When selecting power devices, choose LDO and Load Switch chips with low quiescent current Iq and low shutdown current Istb. In particular, pay attention to the Iq parameter for always-on power chips.

<img src="assets/52xA/sf32lb52x-PWR-diagram.png" width="80%" align="center" />  

<div align="center"> Figure 4-6 SF32LB52x System Power Supply Structure Diagram </div>   <br>  <br>  <br>


### Processor Operating Modes and Wake-up Sources

<div align="center"> Table 4-4 CPU Mode Table </div>

```{table}

|Operating Mode|CPU |Peripherals  |SRAM |IO   |LPTIM |Wake-up Source |Wake-up Time |
|:--|:-------|:----|:----|:----|:---- |:---- |:----   |
|Active |Run |Run |Accessible |Can toggle |Run |- |- |
|Sleep |Stop |Run |Accessible |Can toggle |Run |Any interrupt |<0.5us |
|DeepSleep |Stop |Stop |Inaccessible, fully retained |Level held |Run |RTC, wake-up IO, GPIO, LPTIM, Bluetooth |250us |
|Standby |Reset |Reset |Inaccessible, fully retained |Level held |Run |RTC, wake-up IO, LPTIM, Bluetooth |1ms |
|Hibernate |Reset |Reset |Inaccessible, not retained |High-Z |Reset |RTC, wake-up IO |>2ms |
```

As shown in Table 4-5, the full series of chips supports 15 interrupt sources that can wake up the system in Standby and Hibernate modes.

<div align="center">Table 4-5 Interrupt Wake-Up Source Table </div>

```{table}

|Interrupt Source|Pin   |Detailed Description  |
|:--|:-------|:--------|
|LWKUP_PIN0 |PA24 |Interrupt signal 0 |
|LWKUP_PIN1 |PA25 |Interrupt signal 1 |
|LWKUP_PIN2 |PA26 |Interrupt signal 2 |
|LWKUP_PIN3 |PA27 |Interrupt signal 3 |
|LWKUP_PIN10 |PA34 |Interrupt signal 10 |
|LWKUP_PIN11 |PA35 |Interrupt signal 11 |
|LWKUP_PIN12 |PA36 |Interrupt signal 12 |
|LWKUP_PIN13 |PA37 |Interrupt signal 13 |
|LWKUP_PIN14 |PA38 |Interrupt signal 14 |
|LWKUP_PIN15 |PA39 |Interrupt signal 15 |
|LWKUP_PIN16 |PA40 |Interrupt signal 16 |
|LWKUP_PIN17 |PA41 |Interrupt signal 17 |
|LWKUP_PIN18 |PA42 |Interrupt signal 18 |
|LWKUP_PIN19 |PA43 |Interrupt signal 19 |
|LWKUP_PIN20 |PA44 |Interrupt signal 20 |
```

### Clock
The chip requires two external clock sources: a 48 MHz main crystal and a 32.768 kHz RTC crystal. The detailed specification requirements and selection criteria for the crystals are as follows:

:::{important}

<div align="center"> Table 4-6 Crystal Specification Requirements </div>

```{table}
:align: center
|Crystal|Crystal specification requirements   |Detailed description  |
|:--|:-------|:--------|
|48MHz |7pF≦CL≦12pF (recommended value 8.8pF) △F/F0≦±10ppm ESR≦30 ohms (recommended value 22ohms)|Crystal oscillator power consumption is related to CL and ESR. The smaller the CL and ESR, the lower the power consumption. For optimal power performance, it is recommended to use components with relatively smaller CL and ESR values within the required range. Reserve parallel matching capacitors next to the crystal. When CL<12pF, no capacitors need to be mounted|
|32.768KHz |CL≦12.5pF (recommended value 7pF) △F/F0≦±20ppm ESR≦80k ohms (recommended value 38Kohms)|Crystal power consumption is related to CL and ESR. The smaller the CL and ESR, the lower the power consumption. For optimal power consumption performance, it is recommended to use components with relatively small CL and ESR values within the required range. Reserve parallel matching capacitors next to the crystal. When CL<12.5pF, no capacitor needs to be soldered|
```

<div align="center"> Table 4-7 Recommended Crystal List </div>

```{table}

|Model|Manufacturer   |Parameters  |
|:---|:-------|:--------|
|E1SB48E001G00E  |Hosonic     |F0 = 48.000000MHz, △F/F0 = -6 ~ 8 ppm, CL = 8.8 pF, ESR = 22 ohms Max TOPR = -30 ~ 85℃, Package = (2016 metric)|
|ETST00327000LE  |Hosonic     |F0 = 32.768KHz, △F/F0 = -20 ~ 20 ppm, CL = 7 pF, ESR = 70K ohms Max TOPR = -40 ~ 85℃, Package = (3215 metric)|
|SX20Y048000B31T-8.8  |TKD    |F0 = 48.000000MHz, △F/F0 = -10 ~ 10 ppm, CL = 8.8 pF, ESR = 40 ohms Max TOPR = -20 ~ 75℃, Package = (2016 metric)|
|SF32K32768D71T01  |TKD       |F0 = 32.768KHz, △F/F0 = -20 ~ 20 ppm, CL = 7 pF, ESR = 70K ohms Max TOPR = -40 ~ 85℃, Package = (3215 metric)|
```
**
Note: The ESR of SX20Y048000B31T-8.8 is slightly larger, and the static power consumption will also be slightly higher.
When routing the PCB, remove at least the second-layer GND copper under the crystal to reduce the parasitic load capacitance on the Clock signal.
**
:::

For detailed material certification information, refer to:
[SIFLI-MCU-AVL Certification List](index)

### RF

The RF traces require a 50-ohm characteristic impedance. If the antenna is already matched, no additional RF components are required. It is recommended to reserve a π-type matching network in the design for spurious filtering or antenna matching.

<img src="assets/52xB/sf32lb52X-B-rf-diagram.png" width="80%" align="center" />  

<div align="center"> Figure 4-7 RF Circuit Diagram </div>   <br>  <br>  <br>



### Display

The chip supports 3-Line SPI, 4-Line SPI, Dual data SPI, Quad data SPI, and serial JDI interfaces. It supports 16.7M-color (RGB888), 262K-color (RGB666), 65K-color (RGB565), and 8-color (RGB111) color depth modes. The maximum supported resolution is 512RGBx512. The list of supported LCD drivers is shown in Table 4-8.

<div align="center"> Table 4-8 LCD Driver Support List </div>

```{table}

| Model   | Manufacturer  | Resolution  | Type   | Interface |
| :-- | :-- | :-- | :-- | :-- |
| RM69090  | Raydium    | 368*448 | Amoled | 3-Line SPI，4-Line  SPI，Dual data SPI，  Quad data SPI，MIPI-DSI |
| RM69330  | Raydium    | 454*454 | Amoled | 3-Line SPI，4-Line  SPI，Dual data SPI，  Quad data SPI，8-bits  8080-Series MCU ，MIPI-DSI |
| ILI8688E | ILITEK     | 368*448 | Amoled | Quad data SPI，MIPI-DSI                                      |
| SH8601A  | Shine World Technology    | 454*454 | Amoled | 3-Line SPI, 4-Line  SPI, Dual data SPI,  Quad data SPI, 8-bits  8080-Series MCU, MIPI-DSI |
| SPD2012  | Solomon    | 356*400 | TFT    | Quad data SPI                                                |
| GC9C01   | Galaxycore | 360*360 | TFT    | Quad data SPI                                                |
| GC9B71   | Galaxycore | 320*380 | TFT    | Quad data SPI                                                |
| ST77903  | Sitronix   | 400*400 | TFT    | Quad data SPI                                                |
| ICNA3311 | Chipone    | 454*454 | Amoled | Quad data SPI                                                |
| FT2308   | FocalTech  | 410*494 | Amoled | Quad data SPI                                                |
```


#### SPI/QSPI Display Interface

The chip supports 3/4-wire SPI and Quad-SPI interfaces for connecting LCD displays. The signals are described in the table below.

<div align="center"> Table 4-9 SPI/QSPI Signal Connection Method </div>

```{table}

|spi signal|Pin   |Detailed description  |
|:--|:-------|:--------|
|CSx |PA03 |Enable signal |
|WRx_SCL |PA04 |Clock signal |
|DCx |PA06 |Data/command signal in 4-wire SPI mode; data 1 in Quad-SPI mode  |
|SDI_RDx |PA05 |Data input signal in 3/4-wire SPI mode; data 0 in Quad-SPI mode  |
|SDO |PA05 |Data output signal in 3/4-wire SPI mode; short it together with SDI_RDX |
|D[0] |PA07 |Data 2 in Quad-SPI mode |
|D[1] |PA08 |Data 3 in Quad-SPI mode |
|RESET |PA00 |Signal for resetting the Display screen |
|TE |PA02 |Tearing effect to MCU frame signal |
```

#### JDI Display Interface

The chip supports a parallel JDI interface for connecting LCD displays, as shown in the table below.

<div align="center"> Table 4-10 Parallel JDI Display Signal Connection Method </div>

```{table}


| JDI Signal  | I/O  | Detailed Description   |
|:--|:-------|:--------|
| JDI_VCK  | PA39 | Shift clock for the vertical driver                  |
| JDI_VST  | PA08 | Start signal for the vertical driver                 |
| JDI_XRST | PA40 | Reset signal for the horizontal and  vertical driver |
| JDI_HCK  | PA41 | Shift  clock for the horizontal driver               |
| JDI_HST  | PA06 | Start signal for the horizontal driver               |
| JDI_ENB  | PA07 | Write enable signal for the pixel memory             |
| JDI_R1   | PA05 | Red image data (odd pixels)                          |
| JDI_R2   | PA42 | Red image data (even pixels)                         |
| JDI_G1   | PA04 | Green image data (odd pixels)                        |
| JDI_G2   | PA43 | Green image data (even pixels)                       |
| JDI_B1   | PA03 | Blue image data (odd pixels)                         |
| JDI_B2   | PA02 | Blue image data (even pixels)                        |
```


#### Touch and Backlight Interfaces

The chip supports an I2C-format touchscreen control interface and a touch status interrupt input. It also supports one PWM signal to control the enable and brightness of the backlight power supply, as shown in the table below.

<div align="center"> Table 4-11 Touch and Backlight Control Connection Method </div>

```{table}

| Touchscreen and Backlight Signal | Pin | Detailed Description                   |
| ---------------- | ---- | -------------------------- |
| Interrupt        | PA43 | Touch status interrupt signal (wake-up capable) |
| I2C1_SCL         | PA42 | Clock signal for the touchscreen I2C        |
| I2C1_SDA         | PA41 | Data signal for the touchscreen I2C        |
| BL_PWM           | PA01 | Backlight PWM control signal            |
| Reset            | PA44 | Touch reset signal               |
```

### Storage
#### Memory Connection Interface Description
The chip supports four types of external storage media: SPI NOR Flash, SPI NAND Flash, SD NAND Flash, and eMMC.

<div align="center"> Table 4-12 SPI Nor/Nand Flash Signal Connection </div>

```{table}

| Flash Signal | I/O Signal | Detailed Description                                    |
| ---------- | ------- | ------------------------------------------- |
| CS#        | PA12    | Chip select, active low.                    |
| SO         | PA13    | Data Input (Data Input Output 1)            |
| WP#        | PA14    | Write Protect Output (Data Input Output  2) |
| SI         | PA15    | Data Output (Data Input Output 0)           |
| SCLK       | PA16    | Serial Clock Output                         |
| Hold#      | PA17    | Data Output (Data Input Output 3)           |
```


<div align="center"> Table 4-13 SD Nand Flash and eMMC Signal Connection </div>

```{table}

| Flash Signal | I/O Signal | Detailed Description |
| ---------- | ------- | -------- |
| SD2_CMD    | PA15    | Command signal |
| SD2_D1     | PA17    | Data 1    |
| SD2_D0     | PA16    | Data 0    |
| SD2_CLK    | PA14    | Clock signal |
| SD2_D2     | PA12    | Data 2    |
| SD2_D3     | PA13    | Data 3    |
```
:::{note}
The eMMC chip has two power domains, VCC and VCCQ. Method 1: the two power supplies can be controlled together, resulting in low shutdown power consumption, but the eMMC recovers slowly from sleep and the CPU average power consumption is high. Method 2: VCC can be controlled independently while VCCQ remains continuously powered; shutdown power consumption is higher than in Method 1, but the eMMC recovers quickly from sleep and the CPU average power consumption is lower than in Method 1.
:::

#### Boot Settings

The chip supports booting from internally co-packaged SPI NOR Flash, external SPI NOR Flash, external SPI NAND Flash, and external SD NAND Flash. Specifically:
- SF32LB520Ux6 has internally co-packaged flash and boots from the internally co-packaged flash by default.
- SF32LB523/5/7Ux6 has internally co-packaged PSRAM and must boot from an external storage medium.


<!-- This image needs to be updated; A3 and B3 require different versions. -->

<img src="assets/52xA/SF32LB52x-A-Bootstrap.png" width="80%" align="center" />  

<div align="center"> Figure 4-8 Recommended Circuit Diagram for Bootstrap Pins </div>   <br>  <br>  <br>

<!-- eMMC is supported only by B3 and should be removed from A3. -->
<div align="center"> Table 4-14 Boot Option Settings </div>

```{table}

|Bootstrap[1] (PA13) |Bootstrap[0] (PA17)    |Boot From ext memory  |
| ------------ | ------------ | -------------- |
| L            | L            | SPI Nor Flash  |
| L            | H            | SPI Nand Flash |
| H            | X            | SD Nand Flash  |
```

#### Boot Storage Media Power Control
The chip supports power switch control for the boot storage media to reduce shutdown power consumption. The enable pin of the power switch must be controlled by PA21, and the required enable level for the switch is [high on, low off].

:::{important}
- SF32LB520Ux6 has internally co-packaged flash. Please use VDD33_VOUT1 to power VDD18_VOUT, and set the internal LDO of VDD18_VOUT to the off state.
- SF32LB523/5/7Ux6 has internally co-packaged PSRAM, which is powered by the internal LDO. Simply connect VDD18_VOUT to the external power supply.
- When the external storage medium is NOR Flash, use VDD33_VOUT1 for power supply; no additional power switch is required in between.
- When the external storage medium is SPI NAND or SD NAND, use VDD33_VOUT1 for power supply, and a power switch must be added.
- In the reference design, pull-up resistor locations are reserved for both PA13 and PA17. Select the pull-up resistor according to the storage medium type. The recommended resistance is 7.5 kΩ.
:::

### Buttons
#### Power On/Off Button
The chip's PA34 supports a long-press reset function and can be designed as a button to implement power on/off plus long-press reset. The long-press reset function of PA34 is active high, so it should be designed with a default pull-down to low, and the level becomes high after the button is pressed, as shown in Figure 4-9.

<img src="assets/52xB/sf32lb52X-B-PWKEY.png" width="80%" align="center" />  

<div align="center">Figure 4-9 Power On/Off Button Circuit Diagram </div>   <br>  <br>  <br>


#### Mechanical Rotary Knob Button

<img src="assets/52xB/sf32lb52X-B-XNKEY.png" width="80%" align="center" />  

<div align="center">Figure 4-10 Power On/Off Button Circuit Diagram </div>   <br>  <br>  <br>

### Vibration Motor

The chip supports PWM output to control a vibration motor.

<!-- This content needs separate handling for A3 and B3. -->
<img src="assets/52xA/sf32lb52x-A-VIB.png" width="80%" align="center" />  

<div align="center"> Figure 4-11 Vibration Motor Circuit Diagram </div>  <br> <br> <br>


### Audio Interface

The chip's audio-related interfaces are shown in Table 4-15. The audio interface signals have the following characteristics:
1.	Supports one single-ended ADC input for connecting an external analog MIC. A DC-blocking capacitor with a capacitance of at least 2.2uF must be added in series, and the analog MIC power supply should be connected to the chip's MIC_BIAS power output pin;
2.	Supports one differential DAC output for connecting an external analog audio PA. The DAC output traces should be routed as differential traces with proper ground shielding. Also note: trace capacitance < 10pF, length < 2cm.

<div align="center"> Table 4-15 Audio Signal Connection Method </div>

```{table}

|Audio signal |Pin   |Detailed description |
|:---|:---|:---|
|BIAS |MIC_BIAS |Microphone Power Supply       |
|AU_ADC1P |ADCP |Single-ended analog MIC input  |
|AU_DAC1P |DACP |Differential analog output P    |
|AU_DAC1N |DACN |Differential analog output N    |
```

The recommended circuit for an analog MEMS MIC is shown in Figure 4-12, and the recommended single-ended circuit for an analog ECM MIC is shown in Figure 4-13. MEMS_MIC_ADC_IN and ECM_MIC_ADC_IN are connected to the ADCP input pin of SF32LB52x.


<img src="assets/52xB/sf32lb52X-B-MEMS-MIC.png" width="80%" align="center" />  

<div align="center"> Figure 4-12 Analog MEMS MIC Single-Ended Input Circuit Diagram </div>   <br>  <br>  <br>


<img src="assets/52xB/sf32lb52X-B-ECM-MIC.png" width="80%" align="center" />  

<div align="center"> Figure 4-13 Analog ECM Single-Ended Input Circuit Diagram </div>   <br>  <br>  <br>


The recommended circuit for analog audio output is shown in Figure 4-14. Note that the differential low-pass filter inside the dashed box should be placed close to the chip.


<img src="assets/52xB/sf32lb52X-B-DAC-PA.png" width="80%" align="center" />  

<div align="center"> Figure 4-14 Analog Audio PA Circuit Diagram </div>   <br>  <br>  <br>



### Sensors

The chip supports sensors such as heart rate, accelerometer, and geomagnetic sensors. For the sensor power supply, select a load switch with a relatively low Iq to control power switching.

### UART and I2C Pin Settings

The chip supports mapping UART and I2C functions to any pin. All PA interfaces can be mapped as UART or I2C function pins.

### GPTIM Pin Settings

The chip supports mapping the GPTIM function to any pin. All PA interfaces can be mapped as GPTIM function pins.

### Debug and Flashing Interface

The chip supports the DBG_UART interface for flashing and debugging, and connects to a PC through a UART-to-USB dongle board with a 3.3 V interface.

The SWD interface and DGB_UART interface are multiplexed on PA18 and PA19. The default configuration after power-on is the DBG_UART function.

DBG_UART supports single-step debugging and log output. For details, refer to the user manuals for SFtool and Impeller.

<div align="center">Table 4-16 Debug Port Connection Method </div>

```{table}

|DBG signal |Pin   |Detailed description |
|:---|:---|:---|
|DBG_UART_RXD |PA18 |Debug UART receive |
|DBG_UART_TXD |PA19 |Debug UART transmit |
```

### Production Line Flashing and Crystal Calibration

SiFli provides an offline downloader to complete production line firmware flashing and crystal calibration. During hardware design, be sure to reserve at least the following test points: PVDD, GND, AVDD33, DB_UART_RXD, DB_UART_RXD, PA01.

For detailed flashing and crystal calibration, see the “**_Offline Downloader User Guide.pdf” document included in the development package.



### Schematic and PCB Drawing Checklist

See the “**_Schematic checklist_**.xlsx” and “**_PCB checklist_**.xlsx” documents included in the development package.


## PCB Design Guidelines

### PCB Footprint Design

The QFN68L package dimensions of the SF32LB52x series chips are 7 mm × 7 mm × 0.85 mm; pin count: 68; pin pitch: 0.35 mm. The detailed dimensions are shown in Figure 5-1.

<img src="assets/52xB/sf32lb52X-B-QFN68L-POD.png" width="80%" align="center" />  

<div align="center"> Figure 5-1 QFN68LPackage Dimension Drawing </div>   <br>  <br>  <br>


<img src="assets/52xB/sf32lb52X-B-QFN68L-SHAPE.png" width="80%" align="center" />  

<div align="center"> Figure 5-2 QFN68LPackage Outline Drawing </div>   <br>  <br>  <br>


<img src="assets/52xB/sf32lb52X-B-QFN68L-REF.png" width="80%" align="center" />  

<div align="center"> Figure 5-3 QFN68LPackage PCB Pad Design Reference </div>   <br>  <br>  <br>



### PCB Stackup Design

The SF32LB52x series chips support single-sided and double-sided layouts. Components can be placed on one side, or capacitors and other components can be placed on the back side of the chip. The PCB supports a PTH through-hole design. A 4-layer PTH design is recommended. The recommended reference stack-up structure is shown in Figure 5-4.

<img src="assets/52xB/sf32lb52X-B-PCB-STACK.png" width="80%" align="center" />  

<div align="center"> Figure 5-4 Reference Stackup Structure Diagram </div>   <br>  <br>  <br>



### General PCB Design Rules

The general PCB design rules for a PTH board are shown in Figure 5-5.

<img src="assets/52xB/sf32lb52X-B-PCB-RULE.png" width="80%" align="center" />  

<div align="center"> Figure 5-5 General Design Rules </div>   <br>  <br>  <br>



### PCB Trace Fanout

For QFN package signal fanout, all pins are fanned out through the top layer, as shown in Figure 5-6.

<img src="assets/52xB/sf32lb52X-B-PCB-FANOUT.png" width="80%" align="center" />  

<div align="center"> Figure 5-6 Top-Layer Fanout Reference </div>   <br>  <br>  <br>



### Clock Interface Routing

The crystal must be placed inside the shielding can, with a clearance of more than 1 mm from the PCB outline. Keep it as far away as possible from components that generate significant heat, such as PA, Charge, PMU, and other circuit components. The distance should preferably be greater than 5 mm to avoid affecting the crystal frequency offset. The crystal circuit keep-out area should have a clearance greater than 0.25 mm to avoid other metals and components, as shown in Figure 5-7.

<img src="assets/52xB/sf32lb52X-B-PCB-CRYSTAL.png" width="80%" align="center" />  

<div align="center"> Figure 5-7 Crystal Layout Diagram </div>   <br>  <br>  <br>


It is recommended to route the 48 MHz crystal traces on the top layer, with the length controlled within the range of 3–10 mm and the trace width 0.1 mm. Three-dimensional ground shielding is required, and the traces must be kept away from VBAT, DC/DC, and high-speed signal lines. No plane voids or copper cutouts are allowed on the top layer under the 48 MHz crystal area or on adjacent layers. Other traces are prohibited from passing through this area, as shown in Figures 5-8, 5-9, and 5-10.

<img src="assets/52xB/sf32lb52X-B-PCB-48M-SCH.png" width="80%" align="center" />  

<div align="center"> Figure 5-8 48MHz Crystal Schematic </div>   <br>  <br>  <br>


<img src="assets/52xB/sf32lb52X-B-PCB-48M-MOD.png" width="80%" align="center" />  

<div align="center"> Figure 5-9 48MHz Crystal Routing Model </div>   <br>  <br>  <br>


<img src="assets/52xB/sf32lb52X-B-PCB-48M-ROUTE-REF.png" width="80%" align="center" />  

<div align="center"> Figure 5-10 48MHz Crystal Routing Reference </div>   <br>  <br>  <br>


It is recommended to route the 32.768 kHz crystal traces on the top layer, with the length controlled to ≤10 mm and a trace width of 0.1 mm. The spacing between the parallel 32K_XI/32_XO traces must be ≥0.15 mm, and three-dimensional ground shielding is required. No plane voids or copper cutouts are allowed on the top layer under the crystal area or on adjacent layers, and no other traces are allowed to pass through this area, as shown in Figures 5-11, 5-12, and 5-13.

<img src="assets/52xB/sf32lb52X-B-PCB-32K-SCH.png" width="80%" align="center" />  

<div align="center"> Figure 5-11 32.768KHz Crystal Schematic </div>   <br>  <br>  <br>


<img src="assets/52xB/sf32lb52X-B-PCB-32K-MOD.png" width="80%" align="center" />  

<div align="center"> Figure 5-12 32.768KHz Crystal Routing Model </div>   <br>  <br>  <br>


<img src="assets/52xB/sf32lb52X-B-PCB-32K-ROUTE-REF.png" width="80%" align="center" />  

<div align="center"> Figure 5-13 32.768KHz Crystal Routing Reference </div>   <br>  <br>  <br>



### RF Interface Routing

The RF matching circuit should be placed as close as possible to the chip side, not near the antenna side. The filter capacitor for the AVDD_BRF RF power supply should be placed as close as possible to the chip pin, and the capacitor ground pin should be connected directly to the main ground through a via. The schematic and PCB layout of the π-type network for the RF signal are shown in Figures 5-14 and 5-15, respectively.

<img src="assets/52xB/sf32lb52X-B-SCH-RF.png" width="80%" align="center" />  

<div align="center"> Figure 5-14 π-Type Network and Power Supply Circuit Schematic </div>   <br>  <br>  <br>


<img src="assets/52xB/sf32lb52X-B-PCB-RF.png" width="80%" align="center" />  

<div align="center"> Figure 5-15 π-Type Network and Power Supply PCB Layout </div>   <br>  <br>  <br>



It is recommended to route RF traces on the top layer to avoid vias and layer transitions that may affect RF performance. The trace width should preferably be greater than 10 mil. Three-dimensional ground shielding is required, and acute-angle and right-angle routing should be avoided. RF traces should be controlled to 50 Ω impedance, with plenty of shielding ground vias placed on both sides, as shown in Figures 5-16 and 5-17.

<img src="assets/52xB/sf32lb52X-B-SCH-RF-2.png" width="80%" align="center" />  

<div align="center"> Figure 5-16 RF Signal Circuit Schematic </div>   <br>  <br>  <br>


<img src="assets/52xB/sf32lb52X-B-PCB-RF-ROUTE.png" width="80%" align="center" />  

<div align="center"> Figure 5-17 RF Signal PCB Routing Diagram </div>   <br>  <br>  <br>



### Audio Interface Routing
AVDD33_AUD is the audio power supply pin, and its filter capacitor should be placed close to the corresponding pin so that the ground pin of the filter capacitor has a solid connection to the PCB main ground. MIC_BIAS is the power output pin that supplies power to the microphone peripheral, and its corresponding filter capacitor should be placed close to the corresponding pin. Similarly, the filter capacitor for the AUD_VREF pin should also be placed close to the pin, as shown in Figures 5-18a and 5-18b.

<img src="assets/52xB/sf32lb52X-B-SCH-AUDIO-PWR.png" width="80%" align="center" />  

<div align="center"> Figure 5-18a Audio-Related Power Supply Filter Circuit </div>   <br>  <br>  <br>


<img src="assets/52xB/sf32lb52X-B-PCB-AUDIO-PWR.png" width="80%" align="center" />  

<div align="center"> Figure 5-18b Reference PCB Routing for the Audio-Related Power Supply Filter Circuit </div>   <br>  <br>  <br>



For the analog signal input ADCP pin, place the corresponding circuit components as close as possible to the chip pin, keep the trace length as short as possible, apply three-dimensional ground shielding, and keep it away from other strong interference signals, as shown in Figures 5-19a and 5-19b.

<img src="assets/52xB/sf32lb52X-B-SCH-AUDIO-ADC.png" width="80%" align="center" />  

<div align="center"> Figure 5-19a Analog Audio Input Schematic </div>   <br>  <br>  <br>


<img src="assets/52xB/sf32lb52X-B-PCB-AUDIO-ADC.png" width="80%" align="center" />  

<div align="center"> Figure 5-19b Analog Audio Input PCB Design </div>   <br>  <br>  <br>



For the analog signal output DACP/DACN pins, place the corresponding circuit components as close as possible to the chip pins. Each P/N pair must be routed as differential traces, with trace lengths kept as short as possible and parasitic capacitance less than 10 pF. Three-dimensional ground shielding is required, and the traces should be kept away from other strong interference signals, as shown in Figures 5-20a and 5-20b.

<img src="assets/52xB/sf32lb52X-B-SCH-AUDIO-DAC.png" width="80%" align="center" />  

<div align="center"> Figure 5-20a Analog Audio Output Schematic </div>   <br>  <br>  <br>


<img src="assets/52xB/sf32lb52X-B-PCB-AUDIO-DAC.png" width="80%" align="center" />  

<div align="center"> Figure 5-20b Analog Audio Output PCB Design </div>   <br>  <br>  <br>



### USB Interface Routing

The USB traces PA35(USB DP)/PA36(USB_DN) must first pass through the ESD device pins and then go to the chip side. Ensure that the ESD device ground pins are properly connected to the main ground. The traces must be routed as differential traces with 90-ohm differential impedance control, and three-dimensional ground shielding must be applied, as shown in Figures 5-21a and 5-21b.


<img src="assets/52xB/sf32lb52X-B-SCH-USB.png" width="80%" align="center" />  

<div align="center"> 5-21a USB Signal Schematic </div>   <br>  <br>  <br>


<img src="assets/52xB/sf32lb52X-B-PCB-USB.png" width="80%" align="center" />  

<div align="center"> 5-21b USB Signal PCB Design </div>   <br>  <br>  <br>


Figure 5-22a is a reference diagram for the component layout of USB signals, and Figure 5-22b is the PCB routing model.


<img src="assets/52xB/sf32lb52X-B-PCB-USB-LAYOUT.png" width="80%" align="center" />  

<div align="center"> Figure 5-22a USB Signal Device Layout Reference </div>   <br>  <br>  <br>


<img src="assets/52xB/sf32lb52X-B-PCB-USB-ROUTE.png" width="80%" align="center" />  

<div align="center"> Figure 5-22b USB Signal Routing Model </div>   <br>  <br>  <br>



### SDIO Interface Routing
SDIO signal traces should be routed together as much as possible and should not be routed separately. The total trace length should be ≤50 mm, and the length matching within the group should be controlled to ≤6 mm. The clock signal of the SDIO interface requires three-dimensional ground shielding, and the DATA and CMD signals also require ground shielding, as shown in Figures 5-23a and 5-23b.

<img src="assets/52xB/sf32lb52X-B-SCH-SDIO.png" width="80%" align="center" />  

<div align="center"> Figure 5-23a SDIO Interface Circuit Diagram </div>   <br>  <br>  <br>


<img src="assets/52xB/sf32lb52X-B-PCB-SDIO.png" width="80%" align="center" />  

<div align="center"> Figure 5-23b SDIO PCB Routing Model </div>   <br>  <br>  <br>



### DCDC Circuit Routing
The power inductor and filter capacitors of the DC-DC circuit must be placed close to the chip pins. The BUCK_LX trace should be as short and wide as possible to ensure low loop inductance for the entire DC-DC circuit. The feedback trace for the BUCK_FB pin must not be too narrow and must be greater than 0.25 mm. The ground pins of all DC-DC output filter capacitors should be connected to the main ground plane with multiple vias. Copper pouring is prohibited on the top layer in the power inductor area, and the adjacent layer must be a complete reference ground. Avoid routing other traces through the inductor area, as shown in Figures 5-24a and 5-24b.

<img src="assets/52xB/sf32lb52X-B-SCH-DCDC.png" width="80%" align="center" />  

<div align="center"> Figure 5-24a DC-DC Critical Component Circuit Diagram </div>   <br>  <br>  <br>


<img src="assets/52xB/sf32lb52X-B-PCB-DCDC.png" width="80%" align="center" />  

<div align="center"> Figure 5-24b DC-DC Critical Component PCB Layout Diagram </div>   <br>  <br>  <br>



### Power Supply Routing

VCC is the power input pin for the chip's built-in PMU module. The corresponding capacitor must be placed close to the pin, and the trace should be as wide as possible and no less than 0.4 mm, as shown in Figures 5-25a and 5-25b.

<!-- This content needs separate handling for A3 and B3. -->
<img src="assets/52xA/sf32LB52x-A-SCH-VCC.png" width="80%" align="center" />  

<div align="center"> Figure 5-25a VCCPower Supply Routing Diagram </div>   <br>  <br>  <br>

<img src="assets/52xA/sf32LB52x-A-PCB-VCC.png" width="80%" align="center" />  

<div align="center"> Figure 5-25b VCCPower Supply Routing Diagram </div>   <br>  <br>  <br>


Place the filter capacitors for pins such as VDD_VOUT1, VDD_VOUT2, VDD_RET, VDD_RTC, VDD18_VOUT, VDD33_VOUT1, VDD33_VOUT2, AVDD33_AUD, and AVDD_BRF close to their corresponding pins. The trace width must meet the input current requirements, and the traces should be as short and wide as possible to reduce power ripple and improve system stability.

<!-- The A3 version needs additional charging-section content. -->
### Charging Circuit Routing

VBUS and VBAT are the input and output pins of the chip's integrated charging module, respectively. Place the corresponding filter capacitors close to the pins. Because the charging loop current is relatively high, the pin trace width must be at least 0.4 mm. Do not route sensitive signals in parallel with these traces to avoid interference during charging. Use star routing and do not share the routing path with other traces, so that charging does not interfere with other circuit modules.

<img src="assets/52xA/sf32LB52x-A-SCH-CHG.png" width="80%" align="center" />  

<div align="center"> Figure 5-26a VBUS&VBATPower Supply Routing Diagram </div>   <br>  <br>  <br>

<img src="assets/52xA/sf32LB52x-A-PCB-CHG.png" width="80%" align="center" />  

<div align="center"> Figure 5-26b VBUS&VBATPower Supply Routing Diagram </div>   <br>  <br>  <br>

### Other Interface Routing

When a pin is configured as a GPADC signal pin, three-dimensional ground shielding is required, and it must be kept away from other interfering signals, such as the battery level circuit and temperature check circuit.

### EMI&ESD
- Avoid long-distance routing on the outer layer outside the shielding can. In particular, interfering signals such as clocks and power should be routed on inner layers as much as possible and must not be routed on the outer layer.
- ESD protection devices must be placed close to the corresponding connector pins. Signal traces should first pass through the ESD protection device pins to avoid signal branches that bypass the ESD protection pins.
- The ground pins of ESD devices must be connected to the main ground through vias. Ensure that the ground pad traces are short and wide to reduce impedance and improve ESD device performance.

### Other

The USB charging cable test point must be placed in front of the TVS diode, and the battery holder TVS diode must be placed in front of the platform. The routing must ensure that the trace passes through the TVS diode first and then reaches the chip end, as shown in Figure 5-27.

<img src="assets/52xA/sf32LB52x-A-SCH-PMU-TVS.png" width="80%" align="center" />  

<div align="center"> Figure 5-27 Power SupplyTVS Layout Reference </div>   <br>  <br>  <br>

<img src="assets/52xA/sf32LB52x-A-SCH-PMU-EOS.png" width="80%" align="center" />  

<div align="center"> Figure 5-28 TVS Routing Reference </div>   <br>  <br>  <br>

Avoid routing a long trace from the ground pin of the TVS diode before connecting it to ground whenever possible, as shown in Figure 5-28.

## Revision History

```{table}
:align: left
:name: sf32lb52X-B-history

|Version |Date   |Release Notes |
|:---|:---|:---|
|0.0.1 |10/2024 |Initial version |

```
