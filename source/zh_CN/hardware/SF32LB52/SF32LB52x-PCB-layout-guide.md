## PCB设计指导

### PCB封装设计

SF32LB52X系列芯片的QFN68L封装尺寸：7mmX7mmx0.85mm；管脚数：68；PIN 间距：0.35mm。 详细尺寸如图5-1所示。

<img src="assets/52xB/sf32lb52X-B-QFN68L-POD.png" width="80%" align="center" />  

<div align="center"> 图5-1 QFN68L封装尺寸图 </div>


<img src="assets/52xB/sf32lb52X-B-QFN68L-SHAPE.png" width="80%" align="center" />  

<div align="center"> 图5-2 QFN68L封装形状图 </div>


<img src="assets/52xB/sf32lb52X-B-QFN68L-REF.png" width="80%" align="center" />  

<div align="center"> 图5-3 QFN68L封装PCB焊盘设计参考图 </div>



### PCB叠层设计

SF32LB52X系列芯片支持单双面布局，器件可以放到单面，也可以把电容等放到芯片的背面。PCB支持PTH通孔设计，推荐采用4层PTH，推荐参考叠层结构如图5-4所示。

<img src="assets/52xB/sf32lb52X-B-PCB-STACK.png" width="80%" align="center" />  

<div align="center"> 图5-4 参考叠层结构图 </div>



### PCB通用设计规则

PTH 板PCB通用设计规则如图5-5所示。

<img src="assets/52xB/sf32lb52X-B-PCB-RULE.png" width="80%" align="center" />  

<div align="center"> 图5-5 通用设计规则 </div>



### PCB走线扇出

QFN封装信号扇出，所有管脚全部通过表层扇出，如图5-6所示。

<img src="assets/52xB/sf32lb52X-B-PCB-FANOUT.png" width="80%" align="center" />  

<div align="center"> 如图5-6 表层扇出参考图 </div>



### 时钟接口走线

晶体需摆放在屏蔽罩里面，离PCB板框间距大于1mm,尽量远离发热大的器件，如PA，Charge，PMU等电路器件，距离最好大于5mm以上，避免影响晶体频偏，晶体电路禁布区间距大于0.25mm避免有其它金属和器件，如图5-7所示。

<img src="assets/52xB/sf32lb52X-B-PCB-CRYSTAL.png" width="80%" align="center" />  

<div align="center"> 图5-7 晶体布局图 </div>


48MHz晶体走线建议走表层，长度要求控制在3-10mm区间，线宽0.1mm，必须立体包地处理，并且远离VBAT、DC/DC及高速信号线。48MHz晶体区域下方表层及临层做禁空处理，禁止其它走线从其区域走，如图5-8，5-9，5-10所示。

<img src="assets/52xB/sf32lb52X-B-PCB-48M-SCH.png" width="80%" align="center" />  

<div align="center"> 图5-8 48MHz晶体原理图 </div>


<img src="assets/52xB/sf32lb52X-B-PCB-48M-MOD.png" width="80%" align="center" />  

<div align="center"> 图5-9 48MHz晶体走线模型 </div>


<img src="assets/52xB/sf32lb52X-B-PCB-48M-ROUTE-REF.png" width="80%" align="center" />  

<div align="center"> 图5-10 48MHz晶体走线参考 </div>


32.768KHz晶体走线建议走表层，长度控制≤10mm，线宽0.1mm。32K_XI/32_XO平行走线间距≥0.15mm，必须立体包地处理。晶体区域下方表层及临层做禁空处理，禁止其它走线从其区域走，如图5-11，5-12，5-13所示。

<img src="assets/52xB/sf32lb52X-B-PCB-32K-SCH.png" width="80%" align="center" />  

<div align="center"> 图5-11 32.768KHz晶体原理图 </div>


<img src="assets/52xB/sf32lb52X-B-PCB-32K-MOD.png" width="80%" align="center" />  

<div align="center"> 图5-12 32.768KHz晶体走线模型 </div>


<img src="assets/52xB/sf32lb52X-B-PCB-32K-ROUTE-REF.png" width="80%" align="center" />  

<div align="center"> 图5-13 32.768KHz晶体走线参考 </div>



### 射频接口走线

射频匹配电路要尽量靠近芯片端放置，不要靠近天线端。AVDD_BRF射频电源其滤波电容尽量靠近芯片管脚放置，电容接地管脚打孔直接接主地。RF信号的π型网络的原理图和PCB分别如图5-14，5-15所示。

<img src="assets/52xB/sf32lb52X-B-SCH-RF.png" width="80%" align="center" />  

<div align="center"> 图5-14 π型网络以及电源电路原理图 </div>


<img src="assets/52xB/sf32lb52X-B-PCB-RF.png" width="80%" align="center" />  

<div align="center"> 图5-15 π型网络以及电源PCB布局 </div>



射频走线建议走表层，避免打孔穿层影响RF性能，线宽最好大于10mil，需要立体包地处理，避免走锐角和直角。射频线做50欧阻抗控制，两边多打屏蔽地孔，如图5-16, 5-17所示。

<img src="assets/52xB/sf32lb52X-B-SCH-RF-2.png" width="80%" align="center" />  

<div align="center"> 图5-16 RF信号电路原理图 </div>


<img src="assets/52xB/sf32lb52X-B-PCB-RF-ROUTE.png" width="80%" align="center" />  

<div align="center"> 图5-17 RF信号PCB走线图 </div>



### 音频接口走线
AVDD33_AUD是音频的供电管脚，其滤波电容靠近对应管脚放置，这样滤波电容的接地脚可以良好地连接到PCB的主地。MIC_BIAS是给麦克风外设供电的电源输出管脚，其对应滤波电容靠近对应管脚放置。同样AUD_VREF管脚的滤波电容也靠近管脚放置，如图5-18a，5-18b所示。

<img src="assets/52xB/sf32lb52X-B-SCH-AUDIO-PWR.png" width="80%" align="center" />  

<div align="center"> 图5-18a 音频相关电源滤波电路 </div>


<img src="assets/52xB/sf32lb52X-B-PCB-AUDIO-PWR.png" width="80%" align="center" />  

<div align="center"> 图5-18b 音频相关电源滤波电路PCB参考走线 </div>



模拟信号输入ADCP管脚，对应电路器件尽量靠近芯片管脚放置，走线线长尽量短，做立体包地处理，远离其它强干扰信号，如图5-19a，5-19b所示。

<img src="assets/52xB/sf32lb52X-B-SCH-AUDIO-ADC.png" width="80%" align="center" />  

<div align="center"> 图5-19a 模拟音频输入原理图 </div>


<img src="assets/52xB/sf32lb52X-B-PCB-AUDIO-ADC.png" width="80%" align="center" />  

<div align="center"> 图5-19b 模拟音频输入PCB设计 </div>



模拟信号输出DACP/DACN管脚，对应电路器件尽量靠近芯片管脚放置，每一路P/N需要按照差分线形式走线，走线线长尽量短，寄生电容小于10pf，需做立体包地处理，远离其它强干扰信号，如图5-20a，5-20b所示。

<img src="assets/52xB/sf32lb52X-B-SCH-AUDIO-DAC.png" width="80%" align="center" />  

<div align="center"> 图5-20a 模拟音频输出原理图 </div>


<img src="assets/52xB/sf32lb52X-B-PCB-AUDIO-DAC.png" width="80%" align="center" />  

<div align="center"> 图5-20b 模拟音频输出PCB设计 </div>



### USB接口走线

USB走线PA35(USB DP)/PA36(USB_DN) 必须先过ESD器件管脚，然后再到芯片端，要保证ESD器件接地管脚能良好连接主地。走线需按照差分线形式走，并做90欧差分阻抗控制，且做立体包处理，如图5-21a，5-21b所示。


<img src="assets/52xB/sf32lb52X-B-SCH-USB.png" width="80%" align="center" />  

<div align="center"> 5-21a USB信号原理图 </div>


<img src="assets/52xB/sf32lb52X-B-PCB-USB.png" width="80%" align="center" />  

<div align="center"> 5-21b USB信号PCB设计 </div>


图5-22a为USB信号的元件布局参考图，图5-22b为PCB走线模型。


<img src="assets/52xB/sf32lb52X-B-PCB-USB-LAYOUT.png" width="80%" align="center" />  

<div align="center"> 图5-22a USB信号器件布局参考 </div>


<img src="assets/52xB/sf32lb52X-B-PCB-USB-ROUTE.png" width="80%" align="center" />  

<div align="center"> 图5-22b USB信号走线模型 </div>



### SDIO接口走线
SDIO信号走线尽量一起走，避免分开走，整个走线长度≤50mm, 组内长度控制≤6mm。SDIO接口时钟信号需立体包地处理，DATA和CMD信号也需要包地处理，如图5-23a，5-23b所示。

<img src="assets/52xB/sf32lb52X-B-SCH-SDIO.png" width="80%" align="center" />  

<div align="center"> 图5-23a SDIO接口电路图 </div>


<img src="assets/52xB/sf32lb52X-B-PCB-SDIO.png" width="80%" align="center" />  

<div align="center"> 图5-23b SDIO PCB走线模型 </div>



### DCDC电路走线
DC-DC电路功率电感和滤波电容必须靠近芯片的管脚放置。BUCK_LX走线尽量短且粗，保证整个DC-DC电路回路电感小；BUCK_FB管脚反馈线不能太细，必须大于0.25mm。所有的DC-DC输出滤波电容接地脚多打过孔连接到主地平面。功率电感区域表层禁止铺铜，临层必须为完整的参考地，避免其它线从电感区域里走线，如图5-24a，5-24b所示。

<img src="assets/52xB/sf32lb52X-B-SCH-DCDC.png" width="80%" align="center" />  

<div align="center"> 图5-24a DC-DC关键器件电路图 </div>


<img src="assets/52xB/sf32lb52X-B-PCB-DCDC.png" width="80%" align="center" />  

<div align="center"> 图5-24b DC-DC关键器件PCB布局图 </div>



### 电源供电走线

PVDD为芯片内置PMU模块电源输入脚，对应的电容必须靠近管脚放置，走线尽量的粗，不能低于0.4mm，如图5-25所示。

<!-- 这里的内容需要A3和B3做区别处理 -->
<img src="assets/52xB/sf32lb52X-B-PCB-PMU.png" width="80%" align="center" />  

<div align="center"> 图5-25 PVDD电源走线图 </div>



AVDD33、VDDIOA、VDD_SIP、AVDD33_AUD和AVDD_BRF等管脚滤波电容靠近对应的管脚放置，其走线宽必须满足输入电流要求，走线尽量短粗，从而减少电源纹波提高系统稳定性。

<!-- A3版本需要增加充电部分内容 -->

### 其它接口走线

管脚配置为GPADC 管脚信号，必须要求立体包地处理，远离其它干扰信号，如电池电量电路，温度检查电路等。

### EMI&ESD
- 避免屏蔽罩外面表层长距离走线，特别是时钟、电源等干扰信号尽量走内层，禁止走表层。
- ESD保护器件必须靠近连接器对应管脚放置，信号走线先过ESD保护器件管脚，避免信号分叉，没过ESD保护管脚。
- ESD器件接地脚必须保证过孔连接主地，保证地焊盘走线短且粗，减少阻抗提高ESD器件性能。
