## PCB Design Guidelines

### PCB Package Design

The QFN68L package dimensions for the SF32LB52X series chips are: 7mm x 7mm x 0.85mm; number of pins: 68; pin pitch: 0.35mm. The detailed dimensions are shown in Figure 5-1.

<img src="assets/52xB/sf32lb52X-B-QFN68L-POD.png" width="80%" align="center" />  

<div align="center"> Figure 5-1 QFN68L Package Dimensions </div>


<img src="assets/52xB/sf32lb52X-B-QFN68L-SHAPE.png" width="80%" align="center" />  

<div align="center"> Figure 5-2 QFN68L Package Shape </div>


<img src="assets/52xB/sf32lb52X-B-QFN68L-REF.png" width="80%" align="center" />  

<div align="center"> Figure 5-3 QFN68L Package PCB Pad Design Reference </div>



### PCB Stackup Design

The SF32LB52X series chips support single and double-sided layouts. Components can be placed on a single side, or capacitors and other components can be placed on the backside of the chip. The PCB supports PTH (Plated Through Hole) design, and a 4-layer PTH is recommended. The recommended stackup structure is shown in Figure 5-4.

<img src="assets/52xB/sf32lb52X-B-PCB-STACK.png" width="80%" align="center" />  

<div align="center"> Figure 5-4 Reference Stackup Structure </div>



### General PCB Design Rules

General design rules for PTH boards are shown in Figure 5-5.

<img src="assets/52xB/sf32lb52X-B-PCB-RULE.png" width="80%" align="center" />  

<div align="center"> Figure 5-5 General Design Rules </div>



### PCB Trace Fanout

For QFN package signal fanout, all pins should be fanned out on the surface layer, as shown in Figure 5-6.

<img src="assets/52xB/sf32lb52X-B-PCB-FANOUT.png" width="80%" align="center" />  

<div align="center"> Figure 5-6 Surface Layer Fanout Reference </div>



### Clock Interface Traces

The crystal should be placed inside the shield, with a distance greater than 1mm from the PCB edge. It should be placed as far as possible from heat-generating components such as PA, Charge, and PMU circuits, with a recommended distance of more than 5mm to avoid affecting the crystal frequency. The crystal circuit should have a clearance of more than 0.25mm to avoid other metals and components, as shown in Figure 5-7.

<img src="assets/52xB/sf32lb52X-B-PCB-CRYSTAL.png" width="80%" align="center" />  

<div align="center"> Figure 5-7 Crystal Layout </div>

For the 48MHz crystal, it is recommended to route the traces on the surface layer, with a length controlled between 3-10mm and a line width of 0.1mm. The traces must be surrounded by a ground plane and should be kept away from VBAT, DC/DC, and high-speed signal lines. The area below the 48MHz crystal on the surface layer and adjacent layers should be kept clear of other traces, as shown in Figures 5-8, 5-9, and 5-10.

<img src="assets/52xB/sf32lb52X-B-PCB-48M-SCH.png" width="80%" align="center" />  

<div align="center"> Figure 5-8 48MHz Crystal Schematic </div>


<img src="assets/52xB/sf32lb52X-B-PCB-48M-MOD.png" width="80%" align="center" />  

<div align="center"> Figure 5-9 48MHz Crystal Trace Model </div>


<img src="assets/52xB/sf32lb52X-B-PCB-48M-ROUTE-REF.png" width="80%" align="center" />  

<div align="center"> Figure 5-10 48MHz Crystal Trace Reference </div>

For the 32.768KHz crystal, it is recommended to route the traces on the surface layer, with a length controlled to ≤10mm and a line width of 0.1mm. The parallel trace spacing between 32K_XI and 32K_XO should be ≥0.15mm, and the traces must be surrounded by a ground plane. The area below the 32.768KHz crystal on the surface layer and adjacent layers should be kept clear of other traces, as shown in Figures 5-11, 5-12, and 5-13.

<img src="assets/52xB/sf32lb52X-B-PCB-32K-SCH.png" width="80%" align="center" />  

<div align="center"> Figure 5-11 32.768KHz Crystal Schematic </div>


<img src="assets/52xB/sf32lb52X-B-PCB-32K-MOD.png" width="80%" align="center" />  

<div align="center"> Figure 5-12 32.768KHz Crystal Trace Model </div>


<img src="assets/52xB/sf32lb52X-B-PCB-32K-ROUTE-REF.png" width="80%" align="center" />  

<div align="center"> Figure 5-13 32.768KHz Crystal Trace Reference </div>



### RF Interface Traces

The RF matching circuit should be placed as close as possible to the chip end, not near the antenna end. The filter capacitors for the AVDD_BRF RF power supply should be placed as close as possible to the chip pins, with the capacitor ground pins connected directly to the main ground. The schematics and PCB layout for the π-network and power circuit are shown in Figures 5-14 and 5-15.

<img src="assets/52xB/sf32lb52X-B-SCH-RF.png" width="80%" align="center" />  

<div align="center"> Figure 5-14 π-Network and Power Circuit Schematic </div>


<img src="assets/52xB/sf32lb52X-B-PCB-RF.png" width="80%" align="center" />  

<div align="center"> Figure 5-15 π-Network and Power PCB Layout </div>

For RF traces, it is recommended to route them on the surface layer to avoid vias that can affect RF performance. The line width should be greater than 10mil, and the traces should be surrounded by a ground plane to avoid sharp and right angles. The RF traces should be impedance-controlled to 50 ohms, with additional ground vias on both sides, as shown in Figures 5-16 and 5-17.

<img src="assets/52xB/sf32lb52X-B-SCH-RF-2.png" width="80%" align="center" />  

<div align="center"> Figure 5-16 RF Signal Circuit Schematic </div>

<img src="assets/52xB/sf32lb52X-B-PCB-RF-ROUTE.png" width="80%" align="center" />  

<div align="center"> Figure 5-17 RF Signal PCB Routing </div>



### Audio Interface Routing
AVDD33_AUD is the power supply pin for audio, and its filtering capacitor should be placed close to the corresponding pin so that the ground pin of the filtering capacitor can be well connected to the main ground of the PCB. MIC_BIAS is the power output pin for the microphone peripheral, and its corresponding filtering capacitor should also be placed close to the corresponding pin. Similarly, the filtering capacitor for the AUD_VREF pin should be placed close to the pin, as shown in Figure 5-18a and 5-18b.

<img src="assets/52xB/sf32lb52X-B-SCH-AUDIO-PWR.png" width="80%" align="center" />  

<div align="center"> Figure 5-18a Audio Power Supply Filtering Circuit </div>


<img src="assets/52xB/sf32lb52X-B-PCB-AUDIO-PWR.png" width="80%" align="center" />  

<div align="center"> Figure 5-18b PCB Reference Routing for Audio Power Supply Filtering Circuit </div>



The analog signal input ADCP pin should have the corresponding circuit components placed as close to the chip pin as possible, with the trace length kept as short as possible. The area should be shielded with a ground plane and kept away from other strong interference signals, as shown in Figure 5-19a and 5-19b.

<img src="assets/52xB/sf32lb52X-B-SCH-AUDIO-ADC.png" width="80%" align="center" />  

<div align="center"> Figure 5-19a Analog Audio Input Schematic </div>


<img src="assets/52xB/sf32lb52X-B-PCB-AUDIO-ADC.png" width="80%" align="center" />  

<div align="center"> Figure 5-19b PCB Design for Analog Audio Input </div>



The analog signal output DACP/DACN pins should have the corresponding circuit components placed as close to the chip pin as possible. Each P/N pair should be routed as differential lines with the trace length kept as short as possible, and parasitic capacitance should be less than 10pf. The area should be shielded with a ground plane and kept away from other strong interference signals, as shown in Figure 5-20a and 5-20b.

<img src="assets/52xB/sf32lb52X-B-SCH-AUDIO-DAC.png" width="80%" align="center" />  

<div align="center"> Figure 5-20a Analog Audio Output Schematic </div>


<img src="assets/52xB/sf32lb52X-B-PCB-AUDIO-DAC.png" width="80%" align="center" />  

<div align="center"> Figure 5-20b PCB Design for Analog Audio Output </div>



### USB Interface Routing

The USB traces PA35 (USB DP) / PA36 (USB_DN) must first pass through the ESD device pin and then to the chip end, ensuring that the ground pin of the ESD device is well connected to the main ground. The traces should be routed as differential lines with 90 ohm differential impedance control and shielded with a ground plane, as shown in Figure 5-21a and 5-21b.

<img src="assets/52xB/sf32lb52X-B-SCH-USB.png" width="80%" align="center" />  

<div align="center"> Figure 5-21a USB Signal Schematic </div>


<img src="assets/52xB/sf32lb52X-B-PCB-USB.png" width="80%" align="center" />  

<div align="center"> Figure 5-21b USB Signal PCB Design </div>


Figure 5-22a shows the component placement reference for USB signals, and Figure 5-22b shows the PCB routing model.

<img src="assets/52xB/sf32lb52X-B-PCB-USB-LAYOUT.png" width="80%" align="center" />  

<div align="center"> Figure 5-22a USB Signal Component Placement Reference </div>


<img src="assets/52xB/sf32lb52X-B-PCB-USB-ROUTE.png" width="80%" align="center" />  

<div align="center"> Figure 5-22b USB Signal Routing Model </div>



### SDIO Interface Routing
SDIO signal traces should be routed together as much as possible, avoiding separate routing. The total trace length should be ≤50mm, and the length difference within the group should be controlled to ≤6mm. The SDIO clock signal should be shielded with a ground plane, and the DATA and CMD signals should also be shielded, as shown in Figure 5-23a and 5-23b.

<img src="assets/52xB/sf32lb52X-B-SCH-SDIO.png" width="80%" align="center" />  

<div align="center"> Figure 5-23a SDIO Interface Circuit Diagram </div>


<img src="assets/52xB/sf32lb52X-B-PCB-SDIO.png" width="80%" align="center" />  

<div align="center"> Figure 5-23b SDIO PCB Routing Model </div>



### DCDC Circuit Routing
The power inductor and filtering capacitors of the DC-DC circuit must be placed close to the chip pins. The BUCK_LX trace should be as short and thick as possible to ensure a low inductance loop for the entire DC-DC circuit. The BUCK_FB feedback trace should not be too thin and must be greater than 0.25mm. All DC-DC output filtering capacitors should have multiple vias connecting their ground pins to the main ground plane. The power inductor area should not have copper pour on the top layer, and the adjacent layer must be a complete reference ground to avoid other traces passing through the inductor area, as shown in Figure 5-24a and 5-24b.

<img src="assets/52xB/sf32lb52X-B-SCH-DCDC.png" width="80%" align="center" />  

<div align="center"> Figure 5-24a Key Components of DC-DC Circuit Diagram </div>


<img src="assets/52xB/sf32lb52X-B-PCB-DCDC.png" width="80%" align="center" />  

<div align="center"> Figure 5-24b PCB Layout for Key Components of DC-DC Circuit </div>



### Power Supply Routing

PVDD is the power input pin for the built-in PMU module of the chip. The corresponding capacitors must be placed close to the pin, and the trace should be as thick as possible, not less than 0.4mm, as shown in Figure 5-25.

<!-- The content here needs to be handled differently for A3 and B3 -->
<img src="assets/52xB/sf32lb52X-B-PCB-PMU.png" width="80%" align="center" />

<div align="center"> Figure 5-25 PVDD Power Trace Diagram </div>



The filtering capacitors for the AVDD33, VDDIOA, VDD_SIP, AVDD33_AUD, and AVDD_BRF pins should be placed close to the corresponding pins. The trace width must meet the input current requirements, and the traces should be as short and wide as possible to reduce power ripple and improve system stability.

<!-- A3 version needs to add charging content -->

### Other Interface Traces

When the pins are configured as GPADC signal pins, they must be surrounded by a ground plane to minimize interference from other signals, such as the battery level circuit and temperature check circuit.

### EMI & ESD
- Avoid long traces on the outer layer of the shield, especially for clock and power signals, which should be routed on inner layers and not on the outer layer.
- ESD protection devices must be placed close to the corresponding connector pins. The signal traces should pass through the ESD protection device pins first to avoid signal branching before passing through the ESD protection pins.
- The ground pins of the ESD protection devices must be connected to the main ground via vias, ensuring that the ground plane traces are short and wide to reduce impedance and improve the performance of the ESD protection devices.