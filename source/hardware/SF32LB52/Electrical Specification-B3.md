#### Processor Power Supply Requirements

<div align="center"> Power Supply Requirements </div>

```{table}

| Power Pin | Minimum Voltage(V) | Typical Voltage(V) | Maximum Voltage(V) | Maximum Current(mA) | Detailed Description |
|:--|:--|:--|:--|:--|:----------------------------------------------------|
| PVDD       | 2.97   | 3.3        | 3.63   | 150    | PVDD system power input, connect a 10uF capacitor |
| BUCK_LX    | -      | 1.25       | -      | 50     | BUCK output pin, connect a 4.7uH inductor |
| BUCK_FB    | -      | 1.25       | -      | 50     | BUCK feedback and internal power input pin, connect to the other end of the inductor, and an external 4.7uF capacitor |
| VDD_VOUT1  | -      | 1.1        | -      | 50     | Internal LDO, connect an external 4.7uF capacitor |
| VDD_VOUT2  | -      | 0.9        | -      | 20     | Internal LDO, connect an external 4.7uF capacitor |
| VDD_RET    | -      | 0.9        | -      | 1      | Internal LDO, connect an external 0.47uF capacitor |
| VDD_RTC    | -      | 1.1        | -      | 1      | Internal LDO, connect an external 1uF capacitor |
| VDDIOA     | 1.71   | 1.8/3.3    | 3.63   | -      | GPIO power input, connect an external 1uF capacitor |
| AVDD33     | 2.97   | 3.3        | 3.63   | 100    | 3.3V analog power input, connect an external 4.7uF capacitor |
| AVDD33_AUD | 2.97   | 3.3        | 3.63   | 50     | 3.3V audio power input, connect an external 2.2uF capacitor |
| VDD_SIP    | 1.71   | 1.8/3.3    | 3.63   | 30     | Internal LDO or external power input{SUP}`(1)` , connect an external 1uF capacitor |
| AVDD_BRF   | 2.97   | 3.3        | 3.63   | 100    | Analog power input, connect an external 4.7uF capacitor |
| MIC_BIAS   | 1.4    | -          | 2.8    | -      | MIC power output, connect an external 1uF capacitor |
```
:::{note}
{SUP}`(1)`
* SF32LB52BU36, requires external 1.8V or 3.3V
* SF32LB52BU56, requires external 3.3V
* SF32LB52E/G/JUx6, when PVDD=1.8V, the internal LDO cannot be used and requires external 1.8V; when PVDD=3.3V, the internal LDO directly supplies power, no external supply is needed
:::
:::{important}
When the system is in Hibernate mode, the VDD_SIP power supply must be turned off to avoid leakage current on the I/O of the integrated storage. The power control signal for VDD_SIP should use the dedicated PA21 pin.
:::