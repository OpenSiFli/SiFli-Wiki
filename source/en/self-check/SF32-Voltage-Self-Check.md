# SF32 Hardware Voltage Self-Check Guide

:::{attention}
This document is used by customers to self-verify whether the voltage of each power node is normal when the system crashes or fails to connect to JLink after completing the hardware design. Please perform the checks against the corresponding voltage specifications based on the chip series you are using.
:::

## Preparation Before Checking

### Required Tools

- Multimeter (accuracy ±1%)
- Oscilloscope (optional, for ripple checking)
- Development board or custom test board

### Check Conditions

- The power supply is stable with ripple kept as low as possible
- The chip is in normal operating state (not in sleep mode)

---

## SF32LB52x Series (Lithium Battery-Powered Version)

:::{note}
Applicable models: SF32LB520U36, SF32LB523UB6, SF32LB525UC6, SF32LB527UD6
Power supply: lithium battery powered, supports USB charging
:::

### Power Voltage Check Table

| Check Point | Typical Voltage (V) | Allowed Range (V) | Max Current (mA) | Check Description |
| --------------------- | ----------- | ----------- | ------------ | -------------------------------------- |
| **VBUS**        | 5.0         | 4.6 ~ 5.5   | 500          | USB charging input; check when the charger is plugged in |
| **VBAT**        | -           | 3.2 ~ 4.7   | 500          | Battery voltage; check when powered by battery |
| **VCC**         | -           | 3.2 ~ 4.7   | 500          | System main power supply; close to VBAT when powered by lithium battery |
| **VSYS**        | 3.3         | -           | 500          | RF power supply output |
| **BUCK_LX**     | 1.25        | -           | 50           | DC-DC output, connected to the inductor |
| **BUCK_FB**     | 1.25        | -           | 50           | DC-DC feedback, connected to the other end of the inductor |
| **VDD_VOUT1**   | 1.1         | -           | 50           | Internal LDO1 output (internal power supply, not for peripherals) |
| **VDD_VOUT2**   | 0.9         | -           | 20           | Internal LDO2 output (internal power supply, not for peripherals) |
| **VDD_RET**     | 0.9         | -           | 1            | Internal retention LDO (internal power supply, not for peripherals) |
| **VDD_RTC**     | 1.1         | -           | 1            | RTC power supply (internal power supply, not for peripherals) |
| **VDD18_VOUT**  | 1.8         | -           | 30           | SIP power supply (internal power supply, not for peripherals) |
| **VDD33_VOUT1** | 3.3         | -           | 150          | 3.3V LDO output 1 (output only after software configuration) |
| **VDD33_VOUT2** | 3.3         | -           | 150          | 3.3V LDO output 2 (output only after software configuration) |
| **AVDD33_AUD**  | 3.3         | 2.97 ~ 3.63 | 50           | Audio power supply input |
| **AVDD_BRF**    | 3.3         | 2.97 ~ 3.63 | 100          | RF power supply input |
| **MIC_BIAS**    | -           | 1.4 ~ 2.8   | -            | Microphone power supply output |

### Check Points

:::{important}

1. **VBUS check**: When a USB charger is plugged in, the VBUS voltage should be between 4.6V and 5.5V
2. **Battery voltage**: The VBAT voltage should be between 3.2V and 4.7V, and should not drop below 3.2V at low battery level
3. **DC-DC output**: The BUCK_LX and BUCK_FB voltages should be 1.25V
4. **Internal LDOs**: VDD_VOUT1 = 1.1V and VDD_VOUT2 = 0.9V; abnormalities in these two voltages will prevent the chip from starting up
5. **3.3V outputs**: VDD33_VOUT1/VOUT2 only have output after software configuration; no output by default
   :::

---

## SF32LB52X Series (3.3V/1.8V Powered Version)

:::{note}
Applicable models: SF32LB52BU36, SF32LB52DUB6, SF32LB52EUB6, SF32LB52GUC6, SF32LB52JUD6
Power supply: 3.3V power supply (1.8V for 52D), charging not supported
:::

### Power Voltage Check Table

| Check Point | Typical Voltage (V) | Allowed Range (V) | Max Current (mA) | Check Description |
| -------------------- | ----------- | ----------- | ------------ | -------------------------------------- |
| **PVDD**       | 3.3         | 2.97 ~ 3.63 | 150          | System main power supply input |
| **BUCK_LX**    | 1.25        | -           | 50           | DC-DC output, connected to a 4.7uH inductor |
| **BUCK_FB**    | 1.25        | -           | 50           | DC-DC feedback, connected to the other end of the inductor |
| **VDD_VOUT1**  | 1.1         | -           | 50           | Internal LDO1 output (internal power supply, not for peripherals) |
| **VDD_VOUT2**  | 0.9         | -           | 20           | Internal LDO2 output (internal power supply, not for peripherals) |
| **VDD_RET**    | 0.9         | -           | 1            | Internal retention LDO (internal power supply, not for peripherals) |
| **VDD_RTC**    | 1.1         | -           | 1            | RTC power supply (internal power supply, not for peripherals) |
| **VDDIOA**     | 1.8/3.3     | 1.71 ~ 3.63 | -            | GPIO power supply input |
| **AVDD33**     | 3.3         | 2.97 ~ 3.63 | 100          | 3.3V analog power supply input |
| **AVDD33_AUD** | 3.3         | 2.97 ~ 3.63 | 50           | Audio power supply input |
| **VDD_SIP**    | 1.8/3.3     | 1.71 ~ 3.63 | 30           | SIP power supply (can be powered by internal LDO or external supply) |
| **AVDD_BRF**   | 3.3         | 2.97 ~ 3.63 | 100          | RF power supply input |
| **MIC_BIAS**   | -           | 1.4 ~ 2.8   | -            | Microphone power supply output |

### Check Points

:::{important}

1. **PVDD check**: The main power supply should be between 2.97V and 3.63V; 3.3V is recommended
2. **VDDIOA check**: Depending on the chip model, it may be 1.8V or 3.3V
   - SF32LB52BU36: 1.8V or 3.3V
   - SF32LB52DUB6: 1.8V
   - SF32LB52E/G/J: powered by internal LDO
3. **VDD_SIP check**: Power supply requirements differ depending on the chip model
   - SF32LB52BU36: external 1.8V or 3.3V
   - SF32LB52BU56: external 3.3V
   - SF32LB52DUB6: external 1.8V
   - SF32LB52E/G/J: powered by internal LDO, no external supply needed
4. **Hibernate mode**: When using Hibernate mode, the VDD_SIP power supply must be turned off; otherwise there is a leakage current risk on the I/O of the co-packaged memory
   :::

---

## SF32LB55x Series

:::{note}
Applicable models: SF32LB551 (QFN68L), SF32LB553 (BGA125), SF32LB557 (BGA145/169), etc.
:::

### PMU Power Voltage Check Table

| Check Point | Typical Voltage (V) | Allowed Range (V) | Max Current (mA) | Check Description |
| ------------------------------ | ----------- | ----------- | ------------ | -------------------------------------- |
| **VDD1**                 | 1.8         | 1.71 ~ 3.6  | 50           | Main power supply input 1 (must be powered) |
| **VDD2**                 | 1.8         | 1.71 ~ 3.6  | 50           | Main power supply input 2 (not available on SF32LB551) |
| **BUCK1_VSW/BUCK1_VOUT** | 1.25        | -           | 50           | BUCK1 output, connected to the inductor |
| **BUCK2_VSW/BUCK2_VOUT** | 0.9         | -           | 50           | BUCK2 output, connected to the inductor (not available on SF32LB551) |
| **LDOVCC2_VOUT**         | 0.9         | -           | 50           | LDO mode output (used when BUCK2 is set to LDO mode) |
| **LDO_VOUT1**            | 1.1         | -           | 50           | Internal LDO1 output |
| **LDO_VOUT2**            | 0.9         | -           | 20           | Internal LDO2 output |
| **VDD_RET**              | 0.9         | -           | 1            | Retention LDO output |
| **VDD_RTC**              | 1.1         | -           | 1            | RTC power supply |

### Other Power Voltage Check Table

| Check Point | Typical Voltage (V) | Allowed Range (V) | Max Current (mA) | Check Description |
| ------------------ | ----------- | ----------- | ------------ | ---------------------------- |
| **AVDD_BRF** | 1.8         | 1.71 ~ 3.63 | 30           | RF power supply input |
| **AVDD_DSI** | 1.8         | 1.71 ~ 2.75 | 20           | MIPI DSI power supply input (must be powered) |
| **VDD_SIP**  | 1.8         | 1.71 ~ 1.98 | 30           | Co-packaged memory chip power supply input |
| **AVDD33**   | 3.3         | 3.15 ~ 3.63 | 50           | Analog power supply input |
| **VDDIOA**   | 1.8         | 1.71 ~ 3.63 | -            | PA I/O power supply input |
| **VDDIOB**   | 1.8         | 1.71 ~ 3.63 | -            | PB I/O power supply input |

### Check Points

:::{important}

1. **VDD1/VDD2 check**: The main power supply range is 1.71V~3.6V; 1.8V is recommended. VDD1 and VDD2 must be powered up at the same time
2. **BUCK1 check**: The output should be 1.25V
3. **BUCK2 check**: The output should be 0.9V; not available on SF32LB551
4. **AVDD_DSI**: Must be powered, voltage range 1.71V~2.75V
5. **VDD_SIP**: Voltage range 1.71V~1.98V; do not exceed 1.98V
6. **Package differences**:
   - SF32LB551 (QFN68L): no VDD2, BUCK2_VSW, BUCK2_VOUT, LDOVCC2_VOUT, or AVDD_DSI
   - SF32LB553 (BGA125): no AVDD_DSI
     :::

---

## SF32LB56xU Series (QFN68L Package)

:::{note}
Applicable models: SF32LB56xU series, QFN68L package
:::

### Power Voltage Check Table

| Check Point | Typical Voltage (V) | Allowed Range (V) | Max Current (mA) | Check Description |
| ------------------------- | ----------- | ----------- | ------------ | ---------------------------------- |
| **PVDD**            | 1.8         | 1.7 ~ 3.6   | 100          | System main power supply input |
| **BUCK_LX/BUCK_FB** | 1.25        | -           | 100          | DC-DC output/feedback |
| **LDO1_VOUT**       | 1.1         | -           | 50           | LDO1 output |
| **LDO2_VOUT**       | 0.9         | -           | 20           | LDO2 output |
| **VDD_RET**         | 0.9         | -           | 1            | Retention LDO output |
| **VDD_RTC**         | 1.1         | -           | 1            | RTC power supply |
| **MIC_BIAS**        | -           | 1.4 ~ 2.8   | -            | Microphone power supply output |
| **AVDD33_ANA**      | 3.3         | 3.15 ~ 3.45 | 50           | Analog power supply + RF PA power supply input |
| **AVDD33_AUD**      | 3.3         | 3.15 ~ 3.45 | 50           | Analog audio power supply |
| **VDDIO1**          | 1.8         | 1.71 ~ 1.98 | -            | Power supply input for the co-packaged memory of the internal big core |
| **VDDIO2**          | 1.8/3.3     | 1.71 ~ 3.45 | -            | PA GPIO power supply input |
| **VDDIO3**          | 1.8/3.3     | 1.71 ~ 3.45 | -            | Power supply input for PA5~11 |
| **VDDIO4**          | 1.8/3.3     | 1.71 ~ 3.45 | -            | Power supply input for PB GPIO and the co-packaged Flash of the internal small core |

### SF30147C PMU Power Check Table

| Check Point | Typical Voltage (V) | Allowed Range (V) | Max Current (mA) | Check Description |
| --------------- | ----------- | ----------- | ------------ | ------------------------------ |
| **VBUCK** | 1.8         | 1.8 ~ 1.8   | 500          | PVDD and other 1.8V power inputs of SF32LB56xU |
| **LVSW1** | 1.8         | 1.8 ~ 1.8   | 100          | 1.8V power supply output |
| **LVSW2** | 1.8         | 1.8 ~ 1.8   | 100          | G-SENSOR 1.8V power supply input |
| **LVSW3** | 1.8         | 1.8 ~ 1.8   | 150          | Heart-rate 1.8V power supply input |
| **LVSW4** | 1.8         | 1.8 ~ 1.8   | 150          | LCD 1.8V power supply input |
| **LVSW5** | 1.8         | 1.8 ~ 1.8   | 150          | 1.8V power supply output |
| **LDO1**  | 3.3         | 2.8 ~ 3.3   | 100          | AVDD33_ANA and other 3.3V power inputs |
| **LDO2**  | 3.3         | 2.8 ~ 3.3   | 100          | Motor power supply input |
| **LDO3**  | 3.3         | 2.8 ~ 3.3   | 100          | LCD 3.3V power supply input |
| **LDO4**  | 3.3         | 2.8 ~ 3.3   | 100          | Heart-rate 3.3V power supply input |
| **HVSW1** | -           | 2.8 ~ 5     | 150          | Analog Class-K PA power supply input |
| **HVSW2** | -           | 2.8 ~ 5     | 150          | GPS power supply input |

### Check Points

:::{important}

1. **PVDD check**: The main power supply range is 1.7V~3.6V; 1.8V is recommended
2. **VDDIO1**: Power supply for the co-packaged memory of the internal big core, must be 1.8V (1.71V~1.98V)
3. **VDDIO2/3/4**: GPIO power supplies, can be 1.8V or 3.3V
4. **AVDD33_ANA**: Analog power supply, must be 3.3V (3.15V~3.45V)
   :::

---

## SF32LB56xV Series (BGA Package)

:::{note}
Applicable models: SF32LB56xV series, BGA package
:::

### Power Voltage Check Table

| Check Point | Typical Voltage (V) | Allowed Range (V) | Max Current (mA) | Check Description |
| ------------------------- | ----------- | ----------- | ------------ | ----------------------- |
| **PVDD**            | 1.8         | 1.71 ~ 3.6  | 100          | System main power supply input |
| **BUCK_LX/BUCK_FB** | 1.25        | -           | 100          | DC-DC output/feedback |
| **LDO1_VOUT**       | 1.1         | -           | 50           | LDO1 output |
| **LDO2_VOUT**       | 0.9         | -           | 20           | LDO2 output |
| **VDD_RET**         | 0.9         | -           | 1            | Retention LDO output |
| **VDD_RTC**         | 1.1         | -           | 1            | RTC power supply |
| **MIC_BIAS**        | -           | 1.4 ~ 2.8   | -            | Microphone power supply output |
| **AVDD_BRF**        | 1.8         | 1.71 ~ 3.3  | 1            | RF power supply input |
| **AVDD33_ANA**      | 3.3         | 3.15 ~ 3.45 | 50           | Analog power supply + RF PA power supply input |
| **AVDD33_AUD**      | 3.3         | 3.15 ~ 3.45 | 50           | Analog audio power supply |
| **VDDIOA**          | 1.8/3.3     | 1.71 ~ 3.45 | -            | PA12-PA78 I/O power supply input |
| **VDDIOA2**         | 1.8/3.3     | 1.71 ~ 3.45 | -            | PA0-PA11 I/O power supply input |
| **VDDIOB**          | 1.8/3.3     | 1.71 ~ 3.45 | -            | PB I/O power supply input |
| **VDDIOSA**         | 1.8         | 1.71 ~ 1.98 | -            | SIPA power supply input |
| **VDDIOSB**         | 1.8         | 1.71 ~ 1.98 | -            | SIPB power supply input |
| **VDDIOSC**         | 1.8         | 1.71 ~ 1.98 | -            | SIPC power supply input |

### SF30147C PMU Power Check Table

| Check Point | Typical Voltage (V) | Allowed Range (V) | Max Current (mA) | Check Description |
| --------------- | ----------- | ----------- | ------------ | ------------------------------ |
| **VBUCK** | 1.8         | 1.8 ~ 1.8   | 500          | PVDD and other 1.8V power inputs of SF32LB56xV |
| **LVSW1** | 1.8         | 1.8 ~ 1.8   | 100          | I2S Class-K PA logic power supply input |
| **LVSW2** | 1.8         | 1.8 ~ 1.8   | 100          | G-SENSOR 1.8V power supply input |
| **LVSW3** | 1.8         | 1.8 ~ 1.8   | 150          | Heart-rate 1.8V power supply input |
| **LVSW4** | 1.8         | 1.8 ~ 1.8   | 150          | LCD 1.8V power supply input |
| **LVSW5** | 1.8         | 1.8 ~ 1.8   | 150          | EMMC CORE power supply input |
| **LDO1**  | 3.3         | 2.8 ~ 3.3   | 100          | AVDD33_ANA and other 3.3V power inputs |
| **LDO2**  | 3.3         | 2.8 ~ 3.3   | 100          | EMMC or SD NAND power supply input |
| **LDO3**  | 3.3         | 2.8 ~ 3.3   | 100          | LCD 3.3V power supply input |
| **LDO4**  | 3.3         | 2.8 ~ 3.3   | 100          | Heart-rate 3.3V power supply input |
| **HVSW1** | -           | 2.8 ~ 5     | 150          | Analog Class-K PA power supply input |
| **HVSW2** | -           | 2.8 ~ 5     | 150          | GPS power supply input |

### Check Points

:::{important}

1. **PVDD check**: The main power supply range is 1.71V~3.6V; 1.8V is recommended
2. **VDDIOSA/B/C**: SIP power supplies, must be 1.8V (1.71V~1.98V)
3. **AVDD33_ANA**: Analog power supply, must be 3.3V (3.15V~3.45V)
4. **Package differences**: Compared with the QFN package, the BGA package has additional power pins such as VDDIOA, VDDIOA2, VDDIOB, and VDDIOSA/B/C
   :::

---

## SF32LB58x Series

:::{note}
Applicable models: SF32LB58x series
:::

### SF30147C PMU Power Check Table

| Check Point | Typical Voltage (V) | Allowed Range (V) | Max Current (mA) | Check Description |
| --------------- | ----------- | ----------- | ------------ | -------------------------------- |
| **VBUCK** | 1.8         | 1.8 ~ 1.8   | 500          | PVDD1/PVDD2 and other 1.8V power supplies of SF32LB58x |
| **LVSW1** | 1.8         | 1.8 ~ 1.8   | 100          | I2S Class-K PA logic power supply |
| **LVSW2** | 1.8         | 1.8 ~ 1.8   | 100          | G-SENSOR 1.8V power supply |
| **LVSW3** | 1.8         | 1.8 ~ 1.8   | 150          | Heart-rate 1.8V power supply |
| **LVSW4** | 1.8         | 1.8 ~ 1.8   | 150          | LCD 1.8V power supply |
| **LVSW5** | 1.8         | 1.8 ~ 1.8   | 150          | EMMC CORE power supply |
| **LDO1**  | 3.3         | 2.8 ~ 3.3   | 100          | AVDD33_USB and other 3.3V power supplies |
| **LDO2**  | 3.3         | 2.8 ~ 3.3   | 100          | EMMC or SD NAND power supply |
| **LDO3**  | 3.3         | 2.8 ~ 3.3   | 100          | LCD 3.3V power supply |
| **LDO4**  | 3.3         | 2.8 ~ 3.3   | 100          | Heart-rate 3.3V power supply |
| **HVSW1** | -           | 2.8 ~ 5     | 150          | Analog Class-K PA power supply |
| **HVSW2** | -           | 2.8 ~ 5     | 150          | GPS power supply |

### Other Power Voltage Check Table

| Check Point | Typical Voltage (V) | Allowed Range (V) | Max Current (mA) | Check Description |
| -------------------- | ----------- | ----------- | ------------ | ------------------------------ |
| **AVDD_BRF**   | 1.8         | 1.71 ~ 3.3  | 1            | RF power supply input |
| **AVDD18_DSI** | 1.8         | 1.71 ~ 2.5  | 20           | MIPI DSI power supply input (leave floating if unused) |
| **AVDD33_ANA** | 3.3         | 3.15 ~ 3.45 | 50           | Analog power supply + RF PA power supply input |
| **AVDD33_AUD** | 3.3         | 3.15 ~ 3.45 | 50           | Analog audio power supply input |
| **AVDD33_USB** | 3.3         | 3.15 ~ 3.45 | 50           | USB power supply input |
| **VDDIOA**     | 1.8/3.3     | 1.71 ~ 3.45 | -            | PA12-PA93 I/O power supply input |
| **VDDIOA2**    | 1.8/3.3     | 1.71 ~ 3.45 | -            | PA0-PA11 I/O power supply input |
| **VDDIOB**     | 1.8/3.3     | 1.71 ~ 3.45 | -            | PB I/O power supply input |
| **VDDIOSA**    | 1.8         | 1.71 ~ 1.98 | -            | SIPA power supply input |
| **VDDIOSB**    | 1.8         | 1.71 ~ 1.98 | -            | SIPB power supply input |
| **VDDIOSC**    | 1.8         | 1.71 ~ 1.98 | -            | SIPC power supply input |

### Check Points

:::{important}

1. **VBUCK check**: Must be 1.8V; powers multiple 1.8V power domains
2. **LDO1 check**: Powers 3.3V supplies such as AVDD33_USB, AVDD33_ANA, and AVDD33_AUD
3. **VDDIOSA/B/C**: SIP power supplies, must be 1.8V (1.71V~1.98V)
4. **AVDD18_DSI**: MIPI DSI power supply; can be left floating when unused
   :::

---

## Peripheral Power Check Notes

### Flash Memory Power Supply

:::{important}
The following content is from the "Boot Memory Power Control" chapters of each chip's hardware design guide.
:::

#### SF32LB52x Series (Lithium Battery Version)

| Memory Type | Power Supply | Power Switch Required | Control Pin | Description |
| ---------------------------- | ------------------------- | ---------------- | -------------- | ------------------------------- |
| Internal co-packaged Flash (520Ux6) | VDD33_VOUT1 → VDD18_VOUT | - | - | Set the VDD18_VOUT internal LDO to the off state |
| Internal co-packaged PSRAM (523/5/7Ux6) | Internal LDO | - | - | Just connect an external power source to VDD18_VOUT |
| External SPI Nor Flash | VDD33_VOUT1 | Not required | - | Direct power supply, no power switch needed |
| External SPI Nand Flash | VDD33_VOUT1 | **Required** | **PA21** | High level turns on, low level turns off |
| External SD Nand Flash | VDD33_VOUT1 | **Required** | **PA21** | High level turns on, low level turns off |

Source: [SF32LB52x Hardware Design Guide - Boot Memory Power Control](/hardware/SF32LB520-3-5-7-HW-Application)

#### SF32LB52X Series (3.3V/1.8V Powered Version)

| Memory Type | Power Supply | Power Switch Required | Control Pin | Description |
| --------------------------------------- | ------------------ | ---------------- | -------------- | ---------------------- |
| Internal co-packaged Flash (52AUx6) | VDD_SIP | **Required** | **PA21** | A power switch is mandatory |
| Internal co-packaged PSRAM (52D/F/HUx6, PVDD=3.3V) | VDD_SIP (internal LDO) | Optional | - | Not needed when powered by internal LDO |
| Internal co-packaged PSRAM (52D/F/HUx6, PVDD=1.8V) | VDD_SIP | **Required** | **PA21** | Mandatory when PVDD=1.8V |
| External memory | Independent of VDD_SIP | **Required** | **PA21** | Add a separate power switch |
| External ≥32MB SPI Nor Flash | - | **Required** | **PA21** | Power-off is required to exit 4BYTE Mode |
| External ≤16MB SPI Nor Flash | - | Not required | - | Can be powered continuously |

Source: [SF32LB52X Hardware Design Guide - Boot Memory Power Control](/hardware/SF32LB52B-E-G-J-HW-Application)

#### SF32LB56xU Series

- Flash interface: MPI (SPI Nor/NAND) or SD (SD NAND), physically pin-compatible
- Flash GPIO power supply: **VDDIO3** (PA06~PA11), independent of other GPIO voltage domains
- The VDDIO3 voltage should be set according to the external Flash interface level (1.8V or 3.3V)

Source: [SF32LB56xU Hardware Design Guide - External Memory](/hardware/SF32LB56xU-HW-Application)

#### SF32LB56xV Series

- Flash interface: MPI (SPI Nor/NAND) or SD (SD NAND), physically pin-compatible
- Flash GPIO power supply: **VDDIOA2** (PA06~PA11), independent of other GPIO voltage domains
- Supports eMMC with two power domains: VCC and VCCQ

Source: [SF32LB56xV Hardware Design Guide - External Memory](/hardware/SF32LB56xV-HW-Application)

### Flash Power Check Points

:::{important}

1. **VDD_SIP voltage**: Power supply for co-packaged memory; the range is 1.71~3.63V for the 52X series and 1.71~1.98V for the 56x series
2. **PA21 control signal**: The power switch enable pin of all boot memories **must** be controlled by PA21; high level turns on, low level turns off
3. **Hibernate mode**: When using Hibernate mode, the VDD_SIP power supply must be turned off; otherwise there is a leakage current risk on the I/O of the co-packaged memory
4. **Large-capacity Flash**: When an external ≥32MB SPI Nor Flash is used, PA21 must be used to cut off power so that the Flash exits 4BYTE Mode
5. **VDDIO voltage matching**: VDDIO3 of 56xU and VDDIOA2 of 56xV should be set according to the Flash interface level
   :::

---

## Troubleshooting Common Issues

### Voltage Abnormality Troubleshooting Flow

```
Voltage abnormality
├── Voltage is 0V
│   ├── Check whether the power chip is working
│   ├── Check whether the enable signal is correct
│   └── Check for cold solder joints
├── Voltage too low
│   ├── Check whether the load is too heavy
│   ├── Check the output capability of the power chip
│   └── Check whether the PCB traces are too thin
├── Voltage too high
│   ├── Check whether the feedback resistors are correct
│   └── Check whether the power chip is damaged
└── Large voltage ripple
    ├── Check whether the filter capacitors are soldered
    ├── Check whether the capacitor values are correct
    └── Check whether the PCB layout is reasonable
```

### Key Voltage Quick Reference by Series

| Series | Main Power | DC-DC Output | 3.3V Supply | 1.8V Supply |
| ---------- | ------------------- | ----------------------- | ---------------- | --------------- |
| SF32LB52x  | VBAT/VCC 3.2~4.7V   | BUCK 1.25V              | VDD33_VOUTx 3.3V | VDD18_VOUT 1.8V |
| SF32LB52X  | PVDD 2.97~3.63V     | BUCK 1.25V              | AVDD33 3.3V      | VDD_SIP 1.8V    |
| SF32LB55x  | VDD1/VDD2 1.71~3.6V | BUCK1 1.25V, BUCK2 0.9V | AVDD33 3.3V      | VDD_SIP 1.8V    |
| SF32LB56xU | PVDD 1.7~3.6V       | BUCK 1.25V              | AVDD33_ANA 3.3V  | VDDIO1 1.8V     |
| SF32LB56xV | PVDD 1.71~3.6V      | BUCK 1.25V              | AVDD33_ANA 3.3V  | VDDIOSx 1.8V    |
| SF32LB58x  | VBUCK 1.8V          | BUCK 1.25V              | LDO1 3.3V        | VBUCK 1.8V      |

---

## Revision History

| Version | Date | Release Notes |
| ---- | ---------- | -------------------------------- |
| 1.0  | 2026-07-13 | Initial version, integrating voltage check information for all series |
