# SF32LB58x Hardware Self-Check Guide

:::{attention}
This document is intended for the hardware design self-check of the SF32LB58x series chips. After completing the hardware design, please check item by item against this document to ensure the hardware design meets specification requirements.
Before reading, please make sure you have completed:
[Hardware Design Guide](/hardware/SF32LB58x-HW-Application)&nbsp;&nbsp;
[Hardware Design Self-Check List](<https://downloads.sifli.com/hardware/files/documentation/SF32LB58x%20Schematic%26PCB%20checklist_V1.0_20260121.xlsx>)
:::

## Basic Introduction

This document is the hardware self-check guide for the SF32LB58x series chips, applicable to chips in the BGA256 package.

This document targets SF32LB58x hardware whose prototype has been completed and boards have been returned. The focus is not to re-check the design scheme, but to confirm whether the board is capable of stable operation during power-up, download, communication, and use, through measured test points, an oscilloscope, a multimeter, and a serial port.

:::{important}
**The SF32LB58x uses an external power supply method:**

- **Power input**: Connect a 1.71V ~ 3.6V external power source to the PVDD1/PVDD2 pins
- **Charging method**: There is no on-chip charging management module; an external charging management chip (such as the SF30147C PMIC chip) is required
- **Lithium battery voltage detection**: The VBAT voltage is detected via the GPADC pin, requiring a resistor divider

:::{note}
The SF32LB58x (BGA256 package) supports dual BUCK outputs (BUCK1 and BUCK2) and requires two external 4.7uH inductors.
It is recommended to use the SF30147C PMIC chip to provide a complete power management solution.
:::

### Recommended Tools

- Multimeter: for measuring supply voltages, test point voltages, and short circuits
- Oscilloscope: for observing clock waveforms, ripple, and power-up transients
- USB cable and serial port tools
- Backup power supply or replaceable battery

### Test Conditions

- Before powering up the board, confirm there is no obvious short circuit, no reversed polarity, no solder whiskers or bridging
- Before testing, confirm the test points have been provided and are accessible
- Perform static measurements first, then dynamic power-up and communication tests

## 1. Pre-Power-On Checks

Perform visual inspection and simple electrical checks first to avoid chasing obvious problems after power-up.

- Check whether key components are missing, installed in reverse, cold-soldered, or obviously shorted
- Confirm the orientations of the power input connector and charging port are correct
- Confirm key test points (PVDD1, PVDD2, BUCK1_LX, BUCK1_FB, BUCK2_LX, BUCK2_FB, etc.) have been provided and are measurable
- Confirm the reset, download, and debug pins are not mistakenly pulled low or high by peripherals

## 2. Power Supply and Power-Up Self-Check

After power-up, first confirm that the main power supply is normal, then check whether the internal LDO/PMU outputs meet expectations. It is recommended to measure in the order of "input → intermediate nodes → load end".

### 2.1 Power Supply Voltage Check Table

| Test Point | Before Power-Up/No Load | Normal Operation | Description |
| :------------------ | :-------------- | :------------- | :----------------------------------------------------------- |
| PVDD1               | 0V              | 1.71V ~ 3.6V   | PVDD1 power supply input, requires external 10uF+0.1uF capacitors                        |
| PVDD2               | 0V              | 1.71V ~ 3.6V   | PVDD2 power supply input, requires external 10uF+0.1uF capacitors                        |
| BUCK1_LX / BUCK1_FB | 0V or approx. 1.25V   | approx. 1.25V       | On-chip DC-DC1 output/feedback, requires an external 4.7uH inductor and 4.7uF+0.1uF capacitors     |
| BUCK2_LX / BUCK2_FB | 0V or approx. 0.9V    | approx. 0.9V        | On-chip DC-DC2 output/feedback, requires an external 4.7uH inductor and 4.7uF+0.1uF capacitors     |
| LDO_VOUT1           | 0V              | approx. 1.1V        | On-chip LDO output, requires an external 4.7uF capacitor                              |
| VDD_RET             | 0V              | approx. 0.9V        | On-chip RET LDO output, requires an external 0.47uF capacitor                         |
| VDD_RTC             | 0V              | approx. 1.1V        | On-chip RTC LDO output, requires an external 0.1uF capacitor                          |
| AVDD_BRF            | 0V              | 1.71V ~ 3.3V   | RF power supply input, requires an external 1uF capacitor                                 |
| AVDD18_DSI          | 0V              | 1.71V ~ 2.5V   | MIPI DSI power supply input, requires an external 4.7uF capacitor; leave floating if unused               |
| AVDD33_ANA          | 0V              | 3.15V ~ 3.45V  | Analog power supply + RF PA power supply input, requires an external 1uF capacitor                      |
| AVDD33_AUD          | 0V              | 3.15V ~ 3.45V  | Analog audio power supply input, requires an external 4.7uF capacitor                           |
| AVDD33_USB          | 0V              | 3.15V ~ 3.45V  | USB power supply input, requires an external 1uF capacitor                                  |
| MIC_BIAS            | 0V              | 1.4V ~ 2.8V    | Microphone bias power supply output, requires an external 1uF capacitor                           |
| VDDIOA              | 0V              | 1.71V ~ 3.45V  | PA12-PA93 I/O power supply input, requires an external 1uF capacitor                        |
| VDDIOA2             | 0V              | 1.71V ~ 3.45V  | PA0-PA11 I/O power supply input, requires an external 1uF capacitor                         |
| VDDIOB              | 0V              | 1.71V ~ 3.45V  | PB I/O power supply input, requires an external 1uF capacitor                               |
| VDDIOSA             | 0V              | 1.71V ~ 1.98V  | SIPA power supply input, requires an external 1uF capacitor                                 |
| VDDIOSB             | 0V              | 1.71V ~ 1.98V  | SIPB power supply input, requires an external 1uF capacitor                                 |
| VDDIOSC             | 0V              | 1.71V ~ 1.98V  | SIPC power supply input, requires an external 1uF capacitor                                 |
| GPADC_VREFP         | 0V              | -              | GPADC reference voltage input, only connect an external capacitor, no external supply needed                   |
| AUD_VREF            | 0V              | Refer to the chip datasheet | Audio reference voltage output (generated inside the chip); externally only connect a filter capacitor          |

### 2.2 Power Supply Self-Check Points

- If PVDD1/PVDD2 have no voltage, first check the power input connector, protection components, and power path
- If BUCK1/BUCK2 is abnormal, suspect problems with DCDC-related components, the inductor, or the feedback network
- If LDO_VOUT1 has no voltage, first confirm whether the chip has powered up normally
- The VDDIOA/VDDIOA2/VDDIOB voltage range is 1.71V ~ 3.45V, and the VDDIOSA/VDDIOSB/VDDIOSC voltage range is 1.71V ~ 1.98V; please verify against the configuration used to confirm the expected voltage
- **Lithium battery voltage detection**: The VBAT voltage is detected via the GPADC pin, requiring a resistor divider
- **Charging function**: An external charging management chip (such as SF30147C) is required; ensure the trickle charging current of the charging IC is large enough (at least 40mA) to avoid being unable to charge an over-discharged battery

### 2.4 Flash Memory Power Supply Check

SF32LB58x supports external Flash memory, including SPI Nor/NAND Flash, SD NAND Flash, and eMMC.

| Memory Type | Power Supply | Power Switch Required | Control Pin | Description |
| :------- | :------- | :--------------- | :------- | :--- |
| External SPI Nor Flash | VDDIOA2 (1.8V or 3.3V) | Not required | - | Direct power supply, no power switch needed |
| External SPI Nand Flash | VDDIOA2 (1.8V or 3.3V) | Required | PA43 | High level turns on, low level turns off |
| External SD Nand Flash | VDDIOA2 (3.3V) | Required | PA43 | High level turns on, low level turns off; SD NAND only supports 3.3V |
| External eMMC | VDDIOA2 (1.8V) | Required | PA43 | A 1.8V interface level is recommended |

:::{important}
**Flash power supply check points:**
1. **VDDIOA2 voltage**: Power supply for the SD1 interface, supporting 1.8V and 3.3V; a 1.8V interface level is recommended for SPI NAND FLASH and EMMC, while SD NAND FLASH only supports 3.3V
2. **PA43 control signal**: The power control pin of the external Flash **must** be controlled by PA43; high level turns on, low level turns off
3. **Hibernate mode**: When using Hibernate mode, the Flash power supply must be turned off; otherwise there is a leakage current risk
4. **Large-capacity Flash**: When an external ≥32MB SPI Nor Flash is used, PA43 must be used to cut off power so that the Flash exits 4BYTE Mode
5. **Dual SDIO**: The 58x supports two SDIO interfaces; SD1 connects to EMMC or SD NAND, and SD2 connects to an SD card or WIFI chip
:::

### 2.3 Power Ripple and Power-Up Sequence

- Use an oscilloscope to observe whether the main power supply and analog power supply show obvious droops or spikes at the moment of power-up
- Observe whether the power-up sequence shows reset jitter, supply hysteresis, or momentary short circuits
- If the board crashes or restarts immediately after power-up, first check the power ripple, reset release sequence, and load switch

## 3. Clock and Reset Self-Check

### 3.1 48MHz Main Clock

- Use an oscilloscope to observe whether stable oscillation exists at the nodes corresponding to the 48MHz crystal
- If there is no waveform, first check the crystal, load capacitors, bypass network, and corresponding test points
- If a waveform exists but the frequency deviates significantly, first check the crystal model, matching capacitors, and component mounting quality

### 3.2 32.768kHz RTC Clock

- Use an oscilloscope or frequency counter to confirm whether the 32.768kHz clock is stably present
- An abnormal RTC clock causes abnormal low-power wake-up, timing, and certain peripheral functions
- If the 48MHz clock is normal but the 32K clock is abnormal, first check the RTC crystal and its matching network

### 3.3 Reset Detection

:::{important}
The hardware reset of the SF32LB58x chip is implemented through the RSTN pin, and **the reset button must be long-pressed to trigger a reset**. RSTN is designed as active-low — default pull-up to high, and pulled low after the button is pressed. This is the same as the common active-low reset design.
:::

- After power-up, confirm the RSTN reset pin defaults to high level (not pressed), and the chip runs normally after the main power supply is stable
- **Long-press** the reset button (hold for about 10 seconds) and confirm the board can trigger a hardware reset and restart
- If there is no response after a long press, first check: whether RSTN is correctly connected to the button circuit, whether the reset button works, and whether the main power supply is stable
- If the device restarts repeatedly on its own, the reset circuit design may be wrong; please check the pull-up/pull-down configuration against the reset circuit diagram in the hardware design guide

## 4. Download and Debug Self-Check

### 4.1 UART

- Confirm UART TX/RX/GND are accessible and the serial tool can connect normally
- If boot messages/log output can be seen after power-up, the serial link is basically normal
- If there is no serial output, first check whether TX/RX are reversed, occupied by peripherals, or missing pull-up/pull-down or level conversion

### 4.2 Serial Communication Verification

:::{important}
**Even if there is no user program in the chip, the SF32LB58x automatically outputs boot logs containing the string "SFBL" through DBG_UART after power-up.** This is inherent behavior of the chip's internal ROM and can be used to verify that the serial communication link works properly.
:::

After connecting the serial tool (baud rate 1000000), power up and observe the serial output:

- If you can see output containing **"SFBL"**, the serial communication link is normal (TX/RX connected correctly, levels matched, baud rate correct), even if no program has been flashed into the chip yet
- If you see no output at all, troubleshoot in order:

  - Confirm whether TX/RX are reversed
  - Confirm whether the serial tool level matches the chip IO level (1.8V or 3.3V)
  - Confirm the baud rate is set to 1000000
  - Confirm the DBG_UART pins are not occupied or shorted by peripherals
  - Confirm the chip power supply is normal and the chip has powered up normally

## 5. Common Fault Correspondence

| Symptom | Priority Check Items |
| :--------------------- | :-------------------------------------------------------- |
| No voltage at all after power-up | Power input connector, main power path, protection components |
| PVDD normal but internal power abnormal | BUCK, feedback network, PMU output, inductor |
| No SFBL output on serial port | Whether TX/RX are reversed, level matching, baud rate 1000000, whether the power supply is normal |
| No response to long-press reset | RSTN button circuit (active-low), pull-up/pull-down configuration, whether the power supply is stable |
| No clock waveform | Crystal, matching network, corresponding test points, soldering quality |
| Device restarts repeatedly | Whether the VSYS voltage waveform is correct, power ripple |
| SWD not recognized | SWCLK/SWDIO connection, power supply, debug tool configuration |
| USB function abnormal | AVDD33_USB power supply, USB DP/DM traces, ESD protection components |
| Lithium battery cannot be charged | Charging management chip (SF30147C), trickle charging current, battery connection |
| GPADC detects VBAT abnormally | Divider resistor configuration, GPADC reference voltage, battery voltage range |
| Flash not recognized | VDDIOA2 power supply, PA43 control signal, Flash soldering quality |
| Program cannot be downloaded to Flash | PA43 control signal, Flash power switch, 4BYTE Mode exit |
| eMMC/SD Nand not recognized | VDDIOA2 voltage (SD Nand requires 3.3V), PA43 control signal |
