#### Processor BUCK Inductor Selection Requirements

**Key Parameters of the Power Inductor**
:::{important}
L (inductance) = 4.7 uH ± 20%, DCR (DC resistance) ≦ 0.4 ohm, Isat (saturation current) ≧ 450 mA.
:::
#### How to Reduce Standby Power Consumption

To meet the long battery life requirements of watch products, it is recommended to use load switches in the hardware design for dynamic power management of each functional module. For modules or paths that are always on, select appropriate devices to reduce quiescent current.

During design, pay attention to the hardware default state of the GPIO pin that controls the power switch, and add pull-up or pull-down resistors with MΩ-level resistance to ensure that the load switch is off by default.

When selecting power devices, choose LDO and Load Switch chips with low quiescent current Iq and low shutdown current Istb. In particular, pay attention to the Iq parameter for always-on power chips.

### Processor Operating Modes and Wake-up Sources

<div align="center"> CPU Mode Table </div>

```{table}

|Operating Mode|CPU |Peripherals  |SRAM |IO   |LPTIM |Wake-up Source |Wake-up Time |
|:--|:-------|:----|:----|:----|:---- |:---- |:----   |
|Active |Run |Run |Accessible |Can toggle |Run |- |- |
|Sleep |Stop |Run |Accessible |Can toggle |Run |Any interrupt |<0.5us |
|DeepSleep |Stop |Stop |Inaccessible, fully retained |Level held |Run |RTC, wake-up IO, GPIO, LPTIM, Bluetooth |250us |
|Standby |Reset |Reset |Inaccessible, fully retained |Level held |Run |RTC, wake-up IO, LPTIM, Bluetooth |1ms |
|Hibernate |Reset |Reset |Inaccessible, not retained |High-Z |Reset |RTC, wake-up IO |>2ms |
```

<div align="center"> Interrupt wake up source Table </div>

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

<div align="center"> Crystal Specification Requirements </div>

```{table}

|Crystal|Crystal specification requirements   |Detailed description  |
|:--|:-------|:--------|
|48MHz |CL≦12pF (recommended value 7pF) △F/F0≦±10ppm ESR≦30 ohms (recommended value 22ohms)|Crystal oscillator power consumption is related to CL and ESR. The smaller the CL and ESR, the lower the power consumption. For optimal power performance, it is recommended to use the recommended values CL≦7pF and ESR≦22 ohms. Reserve parallel matching capacitors next to the crystal. When CL<9pF, no capacitors need to be mounted|
|32.768KHz |CL≦12.5pF (recommended value 7pF) △F/F0≦±20ppm ESR≦80k ohms (recommended value 38Kohms)|Crystal oscillator power consumption is related to CL and ESR. The smaller the CL and ESR, the lower the power consumption. For optimal power performance, it is recommended to use the recommended values CL≦9pF and ESR≦40K ohms. Reserve parallel matching capacitors next to the crystal. When CL<12.5pF, no capacitors need to be mounted|
```

<div align="center"> Recommended Crystal List </div>

```{table}

|Model|Manufacturer   |Parameters  |
|:---|:-------|:--------|
|E1SB48E001G00E  |Hosonic     |F0 = 48.000000MHz, △F/F0 = -6 ~ 8 ppm, CL = 8.8 pF, ESR = 22 ohms Max TOPR = -30 ~ 85℃, Package = (2016 metric)|
|ETST00327000LE  |Hosonic     |F0 = 32.768KHz, △F/F0 = -20 ~ 20 ppm, CL = 7 pF, ESR = 70K ohms Max TOPR = -40 ~ 85℃, Package = (3215 metric)|
|SX20Y048000B31T-8.8  |TKD    |F0 = 48.000000MHz, △F/F0 = -10 ~ 10 ppm, CL = 8.8 pF, ESR = 40 ohms Max TOPR = -20 ~ 75℃, Package = (2016 metric)|
|SF32K32768D71T01  |TKD       |F0 = 32.768KHz, △F/F0 = -20 ~ 20 ppm, CL = 7 pF, ESR = 70K ohms Max TOPR = -40 ~ 85℃, Package = (3215 metric)|
```
:::

### RF

The RF traces require a 50-ohm characteristic impedance. If the antenna is already matched, no additional RF components are required. It is recommended to reserve a π-type matching network in the design for spurious filtering or antenna matching.

<img src="assets/52xB/sf32lb52X-B-rf-diagram.png" width="80%" align="center" />  

<div align="center"> RF Circuit Diagram </div>



### Display

The chip supports 3-Line SPI, 4-Line SPI, Dual data SPI, Quad data SPI, and serial JDI interfaces. It supports 16.7M-color (RGB888), 262K-color (RGB666), 65K-color (RGB565), and 8-color (RGB111) color-depth modes. The maximum supported resolution is 512RGBx512.

#### SPI/QSPI Display Interface

The chip supports 3/4-wire SPI and Quad-SPI interfaces for connecting LCD displays. The signals are described in the table below.

<div align="center"> SPI/QSPI Signal Connection Method </div>

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

<div align="center"> Parallel JDI Display Signal Connection Method </div>

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

#### Touch and Backlight Interfaces

The chip supports an I2C-format touchscreen control interface and a touch status interrupt input. It also supports one PWM signal to control the enable and brightness of the backlight power supply, as shown in the table below.

<div align="center"> Touch and Backlight Control Connection Method </div>

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

### Storage
#### Memory Connection Interface Description
The chip supports four types of external storage media: SPI NOR Flash, SPI NAND Flash, SD NAND Flash, and eMMC.

<div align="center"> SPI Nor/Nand Flash Signal Connection </div>

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

<div align="center"> SD Nand Flash and eMMC Signal Connection </div>

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


#### Boot Settings

The chip supports booting from internally co-packaged SPI NOR Flash, external SPI NOR Flash, external SPI NAND Flash, external SD NAND Flash, and external eMMC. Specifically:
- SF32LB52AUx6 has internally co-packaged flash and boots from the internally co-packaged flash by default.
- SF32LB52D/F/HUx6 has internally co-packaged PSRAM and must boot from external storage media.


<div align="center"> Boot Option Settings </div>

```{table}

|Bootstrap[1] (PA13) |Bootstrap[0] (PA17)    |Boot From ext memory  |
|:----:|:----:|:---|
|L |L |Spi Nor Flash  |
|L |H |Spi Nand Flash |
|H |L |SD Nand Flash  |
|H |H |eMMC           |
```

#### Boot Storage Media Power Control
The chip supports power switch control for the boot storage media to reduce shutdown power consumption. The enable pin of the power switch must be controlled by PA21, and the required enable level for the switch is [high on, low off].

:::{important}
- SF32LB52AUx6 has internally co-packaged flash. Add a power switch to VDD_SIP.
- SF32LB52D/F/HUx6 has internally co-packaged PSRAM. If PVDD=3.3V and VDD_SIP is powered by the internal LDO, VDD_SIP does not need a power switch. If PVDD=1.8V, VDD_SIP requires a power switch.
- The power supply for the external storage media is independent of VDD_SIP; add a separate power switch.
- **The enable pins of the power switches for all boot-related memories must be controlled by PA21.**
:::

### Buttons
#### Power On/Off Button
The chip's PA34 supports a long-press reset function and can be designed as a button to implement power on/off + long-press reset. The long-press reset function of PA34 is active high, so it should be designed with a default pull-down to low; when the button is pressed, the level is high, as shown in {numref}`Figure {number} <sf32lb52X-B-PWKEY>`.

<img src="assets/52xB/sf32lb52X-B-PWKEY.png" width="80%" align="center" />  

<div align="center"> Power On/Off Button Circuit Diagram </div>


#### Standard GPIO Button

#### Mechanical Rotary Knob Button


### Vibration Motor

The chip supports PWM output to control a vibration motor.


<img src="assets/52xB/sf32lb52X-B-VIB.png" width="80%" align="center" />  

<div align="center"> Vibration Motor Circuit Diagram </div>


### Audio Interface

The chip's audio-related interfaces are shown in Table 4-16. The audio interface signals have the following characteristics:
1.	Supports one single-ended ADC input for connecting an external analog MIC. A DC-blocking capacitor with a capacitance of at least 2.2uF must be added in series, and the analog MIC power supply should be connected to the chip's MIC_BIAS power output pin;
2.	Supports one differential DAC output for connecting an external analog audio PA. The DAC output traces should be routed as differential traces with proper ground shielding. Also note: trace capacitance < 10pF, length < 2cm.

<div align="center"> Audio Signal Connection Method </div>

```{table}

|Audio signal |Pin   |Detailed description |
|:---|:---|:---|
|BIAS |MIC_BIAS |Microphone power supply       |
|AU_ADC1P |ADCP |Single-ended analog MIC input  |
|AU_DAC1P |DACP |Differential analog output P    |
|AU_DAC1N |DACN |Differential analog output N    |
```

The recommended circuit for an analog MEMS MIC is shown in {numref}`Figure {number} <sf32lb52X-B-MEMS-MIC>`, and the recommended single-ended circuit for an analog ECM MIC is shown in {numref}`Figure {number} <sf32lb52X-B-ECM-MIC>`. MEMS_MIC_ADC_IN and ECM_MIC_ADC_IN are connected to the ADCP input pin of SF32LB52X.


<img src="assets/52xB/sf32lb52X-B-MEMS-MIC.png" width="80%" align="center" />  

<div align="center"> Analog MEMS MIC Single-Ended Input Circuit Diagram </div>


<img src="assets/52xB/sf32lb52X-B-ECM-MIC.png" width="80%" align="center" />  

<div align="center"> Analog ECM Single-Ended Input Circuit Diagram </div>


The recommended circuit for analog audio output is shown in {numref}`Figure {number} <sf32lb52X-B-DAC-PA>`. Note that the differential low-pass filter inside the dashed box should be placed close to the chip.


<img src="assets/52xB/sf32lb52X-B-DAC-PA.png" width="80%" align="center" />  

<div align="center"> Analog Audio PA Circuit Diagram </div>



### Sensors

The chip supports sensors such as heart rate, accelerometer, and geomagnetic sensors. For the sensor power supply, select a load switch with a relatively low Iq to control power switching.

### UART and I2C Pin Settings

The chip supports mapping UART and I2C functions to any pin. All PA interfaces can be mapped as UART or I2C function pins.

### GPTIM Pin Settings

The chip supports mapping the GPTIM function to any pin. All PA interfaces can be mapped as GPTIM function pins.

### Debug and Flashing Interface

The chip supports the DBG_UART interface for flashing and debugging, and connects to a PC through a UART-to-USB dongle board with a 3.3 V interface. The chip can output debug information through DBG_UART. For details, refer to Table `{number} <sf32lb52x-B-P-JDI-LCD-table>`.

<div align="center"> Debug Port Connection Method </div>

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
