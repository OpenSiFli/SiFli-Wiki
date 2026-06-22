#### Processor Power Supply Requirements

<div align="center"> Power Supply Requirements </div>

```{table}

|Power Pin| Minimum Voltage (V) | Typical Voltage (V) | Maximum Voltage (V) | Maximum Current (mA) |   Detailed Description |
|:--|:--|:--|:--|:--|:----------------------------------------------------|
|PVDD       |2.97   |3.3        |3.63   |150    |PVDD system power input, connected to a 10uF capacitor 
|BUCK_LX    |-      |1.25       |-      |50     |BUCK output pin, connected to a 4.7uH inductor 
|BUCK_FB    |-      |1.25       |-      |50     |BUCK feedback and internal power input pin, connected to the other end of the inductor and externally connected to a 4.7uF capacitor 
|VDD_VOUT1  |-      |1.1        |-      |50     |Internal LDO, externally connected to a 4.7uF capacitor 
|VDD_VOUT2  |-      |0.9        |-      |20     |Internal LDO, externally connected to a 4.7uF capacitor 
|VDD_RET    |-      |0.9        |-      |1      |Internal LDO, externally connected to a 0.47uF capacitor 
|VDD_RTC    |-      |1.1        |-      |1      |Internal LDO, externally connected to a 1uF capacitor 
|VDDIOA     |1.71   |1.8/3.3    |3.63   |-      |GPIO power input, externally connected to a 1uF capacitor 
|AVDD33     |2.97   |3.3        |3.63   |100    |3.3V analog power input, externally connected to a 4.7uF capacitor 
|AVDD33_AUD |2.97   |3.3        |3.63   |50     |3.3V audio power input, externally connected to a 2.2uF capacitor  
|VDD_SIP    |1.71   |1.8/3.3    |3.63   |30     |Internal LDO, or external power input{SUP}`(1)` , externally connected to a 1uF capacitor
|AVDD_BRF   |2.97   |3.3        |3.63   |100    |Analog power input, externally connected to a 4.7uF capacitor
|GPADC_VREF |-      |-          |-      |-      |GPADC reference voltage input; only externally connected to a 4.7uF capacitor, no external power supply required
|AUD_VREF   |-      |-          |-      |-      |Audio reference voltage input; only externally connected to a 1.0uF capacitor, no external power supply required
|MIC_BIAS   |1.4    |-          |2.8    |-      |MIC power output, externally connected to a 1uF capacitor 
```
:::{note}
{SUP}`(1)`
* SF32LB52BU36 requires an external 1.8V or 3.3V supply
* SF32LB52BU56 requires an external 3.3V supply
* SF32LB52E/G/JUx6: when PVDD=1.8V, the internal LDO cannot be used and an external 1.8V supply is required; when PVDD=3.3V, the internal LDO supplies power directly and no external supply is required
:::
:::{important}
When the system uses Hibernate mode, the VDD_SIP supply must be turned off; otherwise, there is a risk of leakage on the I/O of the co-packaged memory. Use the dedicated PA21 pin for the VDD_SIP power control signal.
:::
