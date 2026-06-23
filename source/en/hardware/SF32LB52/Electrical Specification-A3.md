#### Processor Power Supply Requirements

```{table} Power Supply Requirements
:name: sf32lb52x-B--POWER

|Power Pin| Minimum Voltage (V) | Typical Voltage (V) | Maximum Voltage (V) | Maximum Current (mA) |   Description |
|:--|:--|:--|:--|:--|:----------------------------------------------------|
|VBUS       |4.5    |5.0    |5.5    |500    |VBUS power input 
|VBAT       |3.5    |-      |4.6    |500    |VBAT power output
|VCC        |3.2    |-      |4.7    |500    |System power input
|VSYS       |-      |3.3    |-      |500    |VSYS power output{sup}`(1)`   
|BUCK_LX    |-      |1.25   |-      |50     |BUCK output pin, connected to an inductor 
|BUCK_FB    |-      |1.25   |-      |50     |BUCK feedback and internal power input pin, connected to the other end of the inductor with an external capacitor 
|VDD_VOUT1  |-      |1.1    |-      |50     |Internal LDO with external capacitor 
|VDD_VOUT2  |-      |0.9    |-      |20     |Internal LDO with external capacitor 
|VDD_RET    |-      |0.9    |-      |1      |Internal LDO with external capacitor 
|VDD_RTC    |-      |1.1    |-      |1      |Internal LDO with external capacitor 
|VDD18_VOUT |-      |1.8    |-      |30     |SIP power{sup}`(2)` 
|VDD33_VOUT1|-      |3.3    |-      |150    |3.3V LDO output 1{sup}`(3)`
|VDD33_VOUT2|-      |3.3    |-      |150    |3.3V LDO output 2
|AVDD33_AUD |2.97   |3.3    |3.63   |50     |3.3V audio power input 
|AVDD_BRF   |2.97   |3.3    |3.63   |100    |RF power input 
|GPADC_VREF |-      |-      |-      |-      |GPADC reference voltage input; connect only an external 4.7uF capacitor, with no external power supply
|AUD_VREF   |-      |-      |-      |-      |Audio reference voltage input; connect only an external 1.0uF capacitor, with no external power supply 
|MIC_BIAS   |1.4    |-      |2.8    |-      |MIC power output 

```
:::{note}

{sup}`(1)` VSYS power supply, powering AVDD_BRF 

{sup}`(2)` VDD18_VOUT power supply \
SF32LB520U36, externally supplied 3.3V power \
SF32LB523UB6, SF32LB525UC6, and SF32LB527UD6 use the internal LDO and do not require an external power supply 

{sup}`(3)` VDD33_VOUT1 power supply \
SF32LB520U36, powering VDD18_VOUT, external Flash, and AVDD33_AUD \
SF32LB523UB6, SF32LB525UC6, and SF32LB527UD6 power the external Flash and AVDD33_AUD

:::
