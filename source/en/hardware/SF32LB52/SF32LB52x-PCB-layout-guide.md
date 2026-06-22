## PCB Design Guidelines

### PCB Footprint Design

The QFN68L package dimensions of the SF32LB52X series chips are: 7 mm x 7 mm x 0.85 mm; number of pins: 68; pin pitch: 0.35 mm. Detailed dimensions are shown in Figure 5-1.

<img src="assets/52xB/sf32lb52X-B-QFN68L-POD.png" width="80%" align="center" />  

<div align="center"> Figure 5-1 QFN68L Package Dimensions </div>


<img src="assets/52xB/sf32lb52X-B-QFN68L-SHAPE.png" width="80%" align="center" />  

<div align="center"> Figure 5-2 QFN68L Package Outline </div>


<img src="assets/52xB/sf32lb52X-B-QFN68L-REF.png" width="80%" align="center" />  

<div align="center"> Figure 5-3 QFN68L Package PCB Pad Design Reference </div>



### PCB Stackup Design

The SF32LB52X series chips support single-sided and double-sided layouts. Components can be placed on one side, or capacitors and other components can be placed on the back side of the chip. The PCB supports a PTH through-hole design. A 4-layer PTH design is recommended, and the recommended reference stack-up structure is shown in Figure 5-4.

<img src="assets/52xB/sf32lb52X-B-PCB-STACK.png" width="80%" align="center" />  

<div align="center"> Figure 5-4 Reference Stack-up Structure </div>



### General PCB Design Rules

The general PCB design rules for a PTH board are shown in Figure 5-5.

<img src="assets/52xB/sf32lb52X-B-PCB-RULE.png" width="80%" align="center" />  

<div align="center"> Figure 5-5 General Design Rules </div>



### PCB Trace Fanout

For QFN package signal fanout, all pins are fanned out through the top layer, as shown in Figure 5-6.

<img src="assets/52xB/sf32lb52X-B-PCB-FANOUT.png" width="80%" align="center" />  

<div align="center"> Figure 5-6 Top-Layer Fanout Reference </div>



### Clock Interface Routing

The crystal must be placed inside the shielding can, with a clearance of more than 1 mm from the PCB outline. Keep it as far away as possible from components that generate significant heat, such as PA, Charge, PMU, and other circuit components. The distance should preferably be greater than 5 mm to avoid affecting the crystal frequency offset. The crystal circuit keep-out area should have a clearance greater than 0.25 mm to avoid other metals and components, as shown in Figure 5-7.

<img src="assets/52xB/sf32lb52X-B-PCB-CRYSTAL.png" width="80%" align="center" />  

<div align="center"> Figure 5-7 Crystal Layout </div>


It is recommended to route the 48 MHz crystal traces on the top layer, with the length controlled within the range of 3–10 mm and the trace width 0.1 mm. Three-dimensional ground shielding is required, and the traces must be kept away from VBAT, DC/DC, and high-speed signal lines. No plane voids or copper cutouts are allowed on the top layer under the 48 MHz crystal area or on adjacent layers. Other traces are prohibited from passing through this area, as shown in Figures 5-8, 5-9, and 5-10.

<img src="assets/52xB/sf32lb52X-B-PCB-48M-SCH.png" width="80%" align="center" />  

<div align="center"> Figure 5-8 48MHz Crystal Schematic </div>


<img src="assets/52xB/sf32lb52X-B-PCB-48M-MOD.png" width="80%" align="center" />  

<div align="center"> Figure 5-9 48MHz Crystal Routing Model </div>


<img src="assets/52xB/sf32lb52X-B-PCB-48M-ROUTE-REF.png" width="80%" align="center" />  

<div align="center"> Figure 5-10 48MHz Crystal Routing Reference </div>


It is recommended to route the 32.768 kHz crystal traces on the top layer, with the length controlled to ≤10 mm and a trace width of 0.1 mm. The spacing between the parallel 32K_XI/32_XO traces must be ≥0.15 mm, and three-dimensional ground shielding is required. No plane voids or copper cutouts are allowed on the top layer under the crystal area or on adjacent layers, and no other traces are allowed to pass through this area, as shown in Figures 5-11, 5-12, and 5-13.

<img src="assets/52xB/sf32lb52X-B-PCB-32K-SCH.png" width="80%" align="center" />  

<div align="center"> Figure 5-11 32.768KHz Crystal Schematic </div>


<img src="assets/52xB/sf32lb52X-B-PCB-32K-MOD.png" width="80%" align="center" />  

<div align="center"> Figure 5-12 32.768KHz Crystal Routing Model </div>


<img src="assets/52xB/sf32lb52X-B-PCB-32K-ROUTE-REF.png" width="80%" align="center" />  

<div align="center"> Figure 5-13 32.768KHz Crystal Routing Reference </div>



### RF Interface Routing

The RF matching circuit should be placed as close as possible to the chip side, not near the antenna side. The filter capacitor for the AVDD_BRF RF power supply should be placed as close as possible to the chip pin, and the capacitor ground pin should be connected directly to the main ground through a via. The schematic and PCB layout of the π-type network for the RF signal are shown in Figures 5-14 and 5-15, respectively.

<img src="assets/52xB/sf32lb52X-B-SCH-RF.png" width="80%" align="center" />  

<div align="center"> Figure 5-14 π-Type Network and Power Circuit Schematic </div>


<img src="assets/52xB/sf32lb52X-B-PCB-RF.png" width="80%" align="center" />  

<div align="center"> Figure 5-15 π-Type Network and Power PCB Layout </div>



It is recommended to route RF traces on the top layer to avoid vias and layer transitions that may affect RF performance. The trace width should preferably be greater than 10 mil. Three-dimensional ground shielding is required, and acute-angle and right-angle routing should be avoided. RF traces should be controlled to 50 Ω impedance, with plenty of shielding ground vias placed on both sides, as shown in Figures 5-16 and 5-17.

<img src="assets/52xB/sf32lb52X-B-SCH-RF-2.png" width="80%" align="center" />  

<div align="center"> Figure 5-16 RF Signal Circuit Schematic </div>


<img src="assets/52xB/sf32lb52X-B-PCB-RF-ROUTE.png" width="80%" align="center" />  

<div align="center"> Figure 5-17 RF Signal PCB Routing Diagram </div>



### Audio Interface Routing
AVDD33_AUD is the audio power supply pin, and its filter capacitor should be placed close to the corresponding pin so that the ground pin of the filter capacitor has a solid connection to the PCB main ground. MIC_BIAS is the power output pin that supplies power to the microphone peripheral, and its corresponding filter capacitor should be placed close to the corresponding pin. Similarly, the filter capacitor for the AUD_VREF pin should also be placed close to the pin, as shown in Figures 5-18a and 5-18b.

<img src="assets/52xB/sf32lb52X-B-SCH-AUDIO-PWR.png" width="80%" align="center" />  

<div align="center"> Figure 5-18a Audio-Related Power Filtering Circuit </div>


<img src="assets/52xB/sf32lb52X-B-PCB-AUDIO-PWR.png" width="80%" align="center" />  

<div align="center"> Figure 5-18b PCB Reference Routing for the Audio-Related Power Filtering Circuit </div>



For the analog signal input ADCP pin, place the corresponding circuit components as close as possible to the chip pin, keep the trace length as short as possible, apply three-dimensional ground shielding, and keep it away from other strong interference signals, as shown in Figures 5-19a and 5-19b.

<img src="assets/52xB/sf32lb52X-B-SCH-AUDIO-ADC.png" width="80%" align="center" />  

<div align="center"> Figure 5-19a Analog Audio Input Schematic </div>


<img src="assets/52xB/sf32lb52X-B-PCB-AUDIO-ADC.png" width="80%" align="center" />  

<div align="center"> Figure 5-19b Analog Audio Input PCB Design </div>



For the analog signal output DACP/DACN pins, place the corresponding circuit components as close as possible to the chip pins. Each P/N pair must be routed as differential traces, with trace lengths kept as short as possible and parasitic capacitance less than 10 pF. Three-dimensional ground shielding is required, and the traces should be kept away from other strong interference signals, as shown in Figures 5-20a and 5-20b.

<img src="assets/52xB/sf32lb52X-B-SCH-AUDIO-DAC.png" width="80%" align="center" />  

<div align="center"> Figure 5-20a Analog Audio Output Schematic </div>


<img src="assets/52xB/sf32lb52X-B-PCB-AUDIO-DAC.png" width="80%" align="center" />  

<div align="center"> Figure 5-20b Analog Audio Output PCB Design </div>



### USB Interface Routing

The USB traces PA35(USB DP)/PA36(USB_DN) must first pass through the ESD device pins and then go to the chip side. Ensure that the ESD device ground pins are properly connected to the main ground. The traces must be routed as differential traces with 90-ohm differential impedance control, and three-dimensional ground shielding must be applied, as shown in Figures 5-21a and 5-21b.


<img src="assets/52xB/sf32lb52X-B-SCH-USB.png" width="80%" align="center" />  

<div align="center"> 5-21a USB Signal Schematic </div>


<img src="assets/52xB/sf32lb52X-B-PCB-USB.png" width="80%" align="center" />  

<div align="center"> 5-21b USB Signal PCB Design </div>


Figure 5-22a is a reference diagram for the component layout of USB signals, and Figure 5-22b is the PCB routing model.


<img src="assets/52xB/sf32lb52X-B-PCB-USB-LAYOUT.png" width="80%" align="center" />  

<div align="center"> Figure 5-22a USB Signal Component Placement Reference </div>


<img src="assets/52xB/sf32lb52X-B-PCB-USB-ROUTE.png" width="80%" align="center" />  

<div align="center"> Figure 5-22b USB Signal Routing Model </div>



### SDIO Interface Routing
SDIO signal traces should be routed together as much as possible and should not be routed separately. The total trace length should be ≤50 mm, and the length matching within the group should be controlled to ≤6 mm. The clock signal of the SDIO interface requires three-dimensional ground shielding, and the DATA and CMD signals also require ground shielding, as shown in Figures 5-23a and 5-23b.

<img src="assets/52xB/sf32lb52X-B-SCH-SDIO.png" width="80%" align="center" />  

<div align="center"> Figure 5-23a SDIO Interface Circuit Diagram </div>


<img src="assets/52xB/sf32lb52X-B-PCB-SDIO.png" width="80%" align="center" />  

<div align="center"> Figure 5-23b SDIO PCB Routing Model </div>



### DCDC Circuit Routing
The power inductor and filter capacitors of the DC-DC circuit must be placed close to the chip pins. The BUCK_LX trace should be as short and wide as possible to ensure low loop inductance for the entire DC-DC circuit. The feedback trace for the BUCK_FB pin must not be too narrow and must be greater than 0.25 mm. The ground pins of all DC-DC output filter capacitors should be connected to the main ground plane with multiple vias. Copper pouring is prohibited on the top layer in the power inductor area, and the adjacent layer must be a complete reference ground. Avoid routing other traces through the inductor area, as shown in Figures 5-24a and 5-24b.

<img src="assets/52xB/sf32lb52X-B-SCH-DCDC.png" width="80%" align="center" />  

<div align="center"> Figure 5-24a DC-DC Key Component Circuit Diagram </div>


<img src="assets/52xB/sf32lb52X-B-PCB-DCDC.png" width="80%" align="center" />  

<div align="center"> Figure 5-24b DC-DC Key Component PCB Layout </div>



### Power Supply Routing

PVDD is the power input pin for the chip's built-in PMU module. The corresponding capacitor must be placed close to the pin, and the trace should be as wide as possible and must not be less than 0.4 mm, as shown in Figure 5-25.

<!-- This content needs separate handling for A3 and B3. -->
<img src="assets/52xB/sf32lb52X-B-PCB-PMU.png" width="80%" align="center" />  

<div align="center"> Figure 5-25 PVDD Power Routing Diagram </div>



The filter capacitors for pins such as AVDD33, VDDIOA, VDD_SIP, AVDD33_AUD, and AVDD_BRF should be placed close to the corresponding pins. Their trace widths must meet the input current requirements, and the traces should be as short and wide as possible to reduce power supply ripple and improve system stability.

<!-- The A3 version needs additional charging-section content. -->

### Other Interface Routing

When a pin is configured as a GPADC signal pin, three-dimensional ground shielding is required, and it must be kept away from other interfering signals, such as the battery level circuit and temperature check circuit.

### EMI&ESD
- Avoid long-distance routing on the outer layer outside the shielding can. In particular, interfering signals such as clocks and power should be routed on inner layers as much as possible and must not be routed on the outer layer.
- ESD protection devices must be placed close to the corresponding connector pins. Signal traces should first pass through the ESD protection device pins to avoid signal branches that bypass the ESD protection pins.
- The ground pins of ESD devices must be connected to the main ground through vias. Ensure that the ground pad traces are short and wide to reduce impedance and improve ESD device performance.
