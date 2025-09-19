#### Processor BUCK Inductor Selection Requirements

**Key Parameters of Power Inductor**
:::{important}
L (Inductance) = 4.7uH ± 20%, DCR (DC Resistance) ≦ 0.4 ohm, Isat (Saturation Current) ≧ 450mA.
:::
#### How to Reduce Standby Power Consumption

To meet the long battery life requirements of watch products, it is recommended to use load switches for dynamic power management of various functional modules in hardware design; if the module or path is always on, select appropriate components to reduce the static current.

When designing, pay attention to the hardware default state of the GPIO pins controlling the power switches, and add pull-up or pull-down resistors with M-level resistance to ensure that the load switches are off by default.

In the selection of power components, choose LDO and Load Switch chips with low static current Iq and low shutdown current Istb, especially for always-on power chips, pay attention to the Iq parameter.

### Processor Operating Modes and Wake-up Sources

<div align="center"> CPU Mode Table </div>

```{table}

|Operating Mode|CPU |Peripherals |SRAM |IO |LPTIM |Wake-up Source |Wake-up Time |
|:--|:-------|:----|:----|:----|:---- |:---- |:----   |
|Active |Run |Run |Accessible |Flippable |Run |- |- |
|Sleep |Stop |Run |Accessible |Flippable |Run |Any Interrupt |<0.5us |
|DeepSleep |Stop |Stop |Not Accessible, Fully Retained |Level Held |Run |RTC, Wake-up IO, GPIO, LPTIM, Bluetooth |250us |
|Standby |Reset |Reset |Not Accessible, Fully Retained |Level Held |Run |RTC, Wake-up IO, LPTIM, Bluetooth |1ms |
|Hibernate |Reset |Reset |Not Accessible, Not Retained |High Impedance |Reset |RTC, Wake-up IO |>2ms |
```

<div align="center"> Interrupt Wake-up Source Table </div>

```{table}

|Interrupt Source|Pin |Detailed Description |
|:--|:-------|:--------|
|LWKUP_PIN0 |PA24 |Interrupt Signal 0 |
|LWKUP_PIN1 |PA25 |Interrupt Signal 1 |
|LWKUP_PIN2 |PA26 |Interrupt Signal 2 |
|LWKUP_PIN3 |PA27 |Interrupt Signal 3 |
|LWKUP_PIN10 |PA34 |Interrupt Signal 10 |
|LWKUP_PIN11 |PA35 |Interrupt Signal 11 |
|LWKUP_PIN12 |PA36 |Interrupt Signal 12 |
|LWKUP_PIN13 |PA37 |Interrupt Signal 13 |
|LWKUP_PIN14 |PA38 |Interrupt Signal 14 |
|LWKUP_PIN15 |PA39 |Interrupt Signal 15 |
|LWKUP_PIN16 |PA40 |Interrupt Signal 16 |
|LWKUP_PIN17 |PA41 |Interrupt Signal 17 |
|LWKUP_PIN18 |PA42 |Interrupt Signal 18 |
|LWKUP_PIN19 |PA43 |Interrupt Signal 19 |
|LWKUP_PIN20 |PA44 |Interrupt Signal 20 |
```

### Clock
The chip requires two external clock sources, a 48MHz main crystal and a 32.768KHz RTC crystal. The specific specifications and selection criteria for the crystals are as follows:

:::{important}

<div align="center"> Crystal Specifications </div>

```{table}

|Crystal|Crystal Specifications |Detailed Description |
|:--|:-------|:--------|
|48MHz |CL≦12pF (Recommended 7pF) △F/F0≦±10ppm ESR≦30 ohms (Recommended 22ohms)|Crystal power consumption is related to CL and ESR. The smaller the CL and ESR, the lower the power consumption. For optimal power performance, it is recommended to use CL≦7pF and ESR≦22 ohms. Reserve parallel matching capacitors next to the crystal. When CL<9pF, no capacitors need to be soldered.|
|32.768KHz |CL≦12.5pF (Recommended 7pF) △F/F0≦±20ppm ESR≦80k ohms (Recommended 38Kohms)|Crystal power consumption is related to CL and ESR. The smaller the CL and ESR, the lower the power consumption. For optimal power performance, it is recommended to use CL≦9pF and ESR≦40K ohms. Reserve parallel matching capacitors next to the crystal. When CL<12.5pF, no capacitors need to be soldered.|
```

<div align="center"> Recommended Crystal List </div>

```{table}

|Model|Manufacturer |Parameters |
|:---|:-------|:--------|
|E1SB48E001G00E  |Hosonic     |F0 = 48.000000MHz, △F/F0 = -6 ~ 8 ppm, CL = 8.8 pF, ESR = 22 ohms Max TOPR = -30 ~ 85℃, Package = (2016 Metric)|
|ETST00327000LE  |Hosonic     |F0 = 32.768KHz, △F/F0 = -20 ~ 20 ppm, CL = 7 pF, ESR = 70K ohms Max TOPR = -40 ~ 85℃, Package = (3215 Metric)|
|SX20Y048000B31T-8.8  |TKD    |F0 = 48.000000MHz, △F/F0 = -10 ~ 10 ppm, CL = 8.8 pF, ESR = 40 ohms Max TOPR = -20 ~ 75℃, Package = (2016 Metric)|
|SF32K32768D71T01  |TKD       |F0 = 32.768KHz, △F/F0 = -20 ~ 20 ppm, CL = 7 pF, ESR = 70K ohms Max TOPR = -40 ~ 85℃, Package = (3215 Metric)|
```
:::

### RF

The RF trace requirement is a 50ohms characteristic impedance. If the antenna is already matched, no additional components are needed on the RF path. It is recommended to reserve a π-type matching network for stray filtering or antenna matching during design.

<img src="assets/52xB/sf32lb52X-B-rf-diagram.png" width="80%" align="center" />  

<div align="center"> RF Circuit Diagram </div>

### Display

The chip supports 3-Line SPI, 4-Line SPI, Dual Data SPI, Quad Data SPI, and Serial JDI interfaces. It supports 16.7M-colors (RGB888), 262K-colors (RGB666), 65K-colors (RGB565), and 8-color (RGB111) color depth modes. It supports a maximum resolution of 512RGBx512.

#### SPI/QSPI Display Interface

The chip supports 3/4-wire SPI and Quad-SPI interfaces to connect to LCD displays. The signal descriptions are as follows:

<div align="center"> SPI/QSPI Signal Connection Methods </div>

```{table}

|spi signal|Pin   |Detailed Description  |
|:--|:-------|:--------|
|CSx |PA03 |Enable signal |
|WRx_SCL |PA04 |Clock signal |
|DCx |PA06 |Data/command signal in 4-wire SPI mode, Data1 in Quad-SPI mode  |
|SDI_RDx |PA05 |Data input signal in 3/4-wire SPI mode, Data0 in Quad-SPI mode  |
|SDO |PA05 |Data output signal in 3/4-wire SPI mode, please short to SDI_RDX |
|D[0] |PA07 |Data2 in Quad-SPI mode |
|D[1] |PA08 |Data3 in Quad-SPI mode |
|RESET |PA00 |Reset display signal |
|TE |PA02 |Tearing effect to MCU frame signal |
```

#### JDI Display Interface

The chip supports a parallel JDI interface to connect to an LCD display, as shown in the table below.

<div align="center"> Parallel JDI Screen Signal Connection Method </div>

```{table}

|spi signal|Pin   |Detailed Description  |
|:--|:-------|:--------|
|CSx |PA03 |Enable signal |
|WRx_SCL |PA04 |Clock signal |
|DCx |PA06 |Data/command signal in 4-wire SPI mode, Data1 in Quad-SPI mode  |
|SDI_RDx |PA05 |Data input signal in 3/4-wire SPI mode, Data0 in Quad-SPI mode  |
|SDO |PA05 |Data output signal in 3/4-wire SPI mode, please short to SDI_RDX |
|D[0] |PA07 |Data2 in Quad-SPI mode |
|D[1] |PA08 |Data3 in Quad-SPI mode |
|RESET |PA00 |Reset display signal |
|TE |PA02 |Tearing effect to MCU frame signal |
```

#### Touch and Backlight Interface

The chip supports an I2C format touch screen control interface and touch status interrupt input, and also supports one PWM signal to control the enable and brightness of the backlight power, as shown in the table below.

<div align="center"> Touch and Backlight Control Connection Method </div>

```{table}

|spi signal|Pin   |Detailed Description  |
|:--|:-------|:--------|
|CSx |PA03 |Enable signal |
|WRx_SCL |PA04 |Clock signal |
|DCx |PA06 |Data/command signal in 4-wire SPI mode, Data1 in Quad-SPI mode  |
|SDI_RDx |PA05 |Data input signal in 3/4-wire SPI mode, Data0 in Quad-SPI mode  |
|SDO |PA05 |Data output signal in 3/4-wire SPI mode, please short to SDI_RDX |
|D[0] |PA07 |Data2 in Quad-SPI mode |
|D[1] |PA08 |Data3 in Quad-SPI mode |
|RESET |PA00 |Reset display signal |
|TE |PA02 |Tearing effect to MCU frame signal |
```

### Storage
#### Storage Interface Description
The chip supports four types of storage media: external SPI Nor Flash, SPI NAND Flash, SD NAND Flash, and eMMC.

<div align="center"> SPI Nor/Nand Flash Signal Connection </div>

```{table}

|spi signal|Pin   |Detailed Description  |
|:--|:-------|:--------|
|CSx |PA03 |Enable signal |
|WRx_SCL |PA04 |Clock signal |
|DCx |PA06 |Data/command signal in 4-wire SPI mode, Data1 in Quad-SPI mode  |
|SDI_RDx |PA05 |Data input signal in 3/4-wire SPI mode, Data0 in Quad-SPI mode  |
|SDO |PA05 |Data output signal in 3/4-wire SPI mode, please short to SDI_RDX |
|D[0] |PA07 |Data2 in Quad-SPI mode |
|D[1] |PA08 |Data3 in Quad-SPI mode |
|RESET |PA00 |Reset display signal |
|TE |PA02 |Tearing effect to MCU frame signal |
```

<div align="center"> SD Nand Flash and eMMC Signal Connection </div>

```{table}

|spi signal|Pin   |Detailed Description  |
|:--|:-------|:--------|
|CSx |PA03 |Enable signal |
|WRx_SCL |PA04 |Clock signal |
|DCx |PA06 |Data/command signal in 4-wire SPI mode, Data1 in Quad-SPI mode  |
|SDI_RDx |PA05 |Data input signal in 3/4-wire SPI mode, Data0 in Quad-SPI mode  |
|SDO |PA05 |Data output signal in 3/4-wire SPI mode, please short to SDI_RDX |
|D[0] |PA07 |Data2 in Quad-SPI mode |
|D[1] |PA08 |Data3 in Quad-SPI mode |
|RESET |PA00 |Reset display signal |
|TE |PA02 |Tearing effect to MCU frame signal |
```


#### Boot Configuration

The chip supports booting from internal integrated Spi Nor Flash, external Spi Nor Flash, external Spi Nand Flash, external SD Nand Flash, and external eMMC. Among these:
- SF32LB52AUx6 has an internal integrated flash and boots from the internal integrated flash by default
- SF32LB52D/F/HUx6 has an internal integrated psram and must boot from an external storage medium


<div align="center"> Boot Option Configuration </div>

```{table}

|Bootstrap[1] (PA13) |Bootstrap[0] (PA17)    |Boot From External Memory  |
|:----:|:----:|:---|
|L |L |Spi Nor Flash  |
|L |H |Spi Nand Flash |
|H |L |SD Nand Flash  |
|H |H |eMMC           |
```

#### Boot Storage Medium Power Control
The chip supports power switch control for the boot storage medium to reduce power consumption during shutdown. The power switch enable pin must use PA21 to control, and the enable level requirement is [high to open, low to close].

:::{important}
- SF32LB52AUx6 has an internal flash, please add a power switch to VDD_SIP.
- SF32LB52D/F/HUx6 has an internal PSRAM. If PVDD=3.3V and VDD_SIP is powered by the internal LDO, a power switch for VDD_SIP is not required; if PVDD=1.8V, a power switch for VDD_SIP is required.
- The power supply for external storage media is independent of VDD_SIP and should have a separate power switch.
- **The enable pin of all power switches related to booting must be controlled by PA21.**
:::

### Buttons
#### Power On/Off Button
The PA34 pin of the chip supports long-press reset functionality and can be designed as a button to achieve power on/off and long-press reset functions. The long-press reset function requires a high level to be effective, so it is designed to be pulled low by default, and the level becomes high when the button is pressed, as shown in {numref}`图 {number} <sf32lb52X-B-PWKEY>`.

<img src="assets/52xB/sf32lb52X-B-PWKEY.png" width="80%" align="center" />  

<div align="center"> Power On/Off Button Circuit Diagram </div>

#### General GPIO Button

#### Mechanical Knob Button

### Vibration Motor
The chip supports PWM output to control the vibration motor.

<img src="assets/52xB/sf32lb52X-B-VIB.png" width="80%" align="center" />  

<div align="center"> Vibration Motor Circuit Diagram </div>

### Audio Interface
The audio-related interfaces of the chip are shown in Table 4-16. The audio interface signals have the following characteristics:
1. Supports one single-ended ADC input, connected to an external analog MIC, with a coupling capacitor of at least 2.2uF, and the power supply for the analog MIC is connected to the MIC_BIAS power output pin of the chip.
2. Supports one differential DAC output, connected to an external analog audio PA. The DAC output traces should be routed as differential lines with proper ground shielding, and the following should be noted: Trace Capacitance < 10pF, Length < 2cm.

<div align="center"> Audio Signal Connection Method </div>

```{table}

|Audio Signal |Pin   |Detailed Description |
|:---|:---|:---|
|BIAS |MIC_BIAS |Microphone Power       |
|AU_ADC1P |ADCP |Single-ended Analog MIC Input  |
|AU_DAC1P |DACP |Differential Analog Output P    |
|AU_DAC1N |DACN |Differential Analog Output N    |
```

The recommended circuit for an analog MEMS MIC is shown in {numref}`图 {number} <sf32lb52X-B-MEMS-MIC>`, and the recommended circuit for an analog ECM MIC is shown in {numref}`图 {number} <sf32lb52X-B-ECM-MIC>`. The MEMS_MIC_ADC_IN and ECM_MIC_ADC_IN are connected to the ADCP input pin of the SF32LB52X.

<img src="assets/52xB/sf32lb52X-B-MEMS-MIC.png" width="80%" align="center" />  

<div align="center"> Analog MEMS MIC Single-ended Input Circuit Diagram </div>

<img src="assets/52xB/sf32lb52X-B-ECM-MIC.png" width="80%" align="center" />  

<div align="center"> Analog ECM Single-ended Input Circuit Diagram </div>

The recommended circuit for analog audio output is shown in {numref}`图 {number} <sf32lb52X-B-DAC-PA>`. Note that the differential low-pass filter within the dashed line should be placed close to the chip.

<img src="assets/52xB/sf32lb52X-B-DAC-PA.png" width="80%" align="center" />  

<div align="center"> Analog Audio PA Circuit Diagram </div>

### Sensors
The chip supports heart rate, acceleration, and magnetic sensors. The power supply for the sensors should use a Load Switch with a low Iq for power control.

### UART and I2C Pin Configuration
The chip supports arbitrary pin mapping for UART and I2C functions, and all PA interfaces can be mapped to UART or I2C function pins.

### GPTIM Pin Configuration
The chip supports arbitrary pin mapping for GPTIM functions, and all PA interfaces can be mapped to GPTIM function pins.

### Debug and Download Interface
The chip supports the DBG_UART interface for downloading and debugging, connected to a PC via a UART-to-USB dongle with a 3.3V interface. The chip can output debug information through the DBG_UART. For more details, refer to Table `{number} <sf32lb52x-B-P-JDI-LCD-table>`.

<div align="center"> Debug Port Connection Method </div>

```{table}

|DBG Signal |Pin   |Detailed Description |
|:---|:---|:---|
|DBG_UART_RXD |PA18 |Debug UART Receive |
|DBG_UART_TXD |PA19 |Debug UART Transmit |
```

### Production Programming and Crystal Calibration
Sichip Technology provides an offline programmer to complete the production programming and crystal calibration. When designing the hardware, please ensure that at least the following test points are reserved: PVDD, GND, AVDD33, DB_UART_RXD, DB_UART_RXD, PA01.

For detailed programming and crystal calibration, refer to the “**_Offline Programmer User Guide.pdf_**” document, which is included in the development package.

### Schematic and PCB Drawing Checklists
Refer to the “**_Schematic checklist_**.xlsx” and “**_PCB checklist_**.xlsx” documents, which are included in the development package.