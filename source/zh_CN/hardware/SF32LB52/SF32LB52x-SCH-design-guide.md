#### 处理器BUCK电感选择要求

**功率电感关键参数**
:::{important}
L(电感值) = 4.7uH ± 20%，DCR(直流阻抗) ≦ 0.4 ohm，Isat(饱和电流) ≧ 450mA。
:::
#### 如何降低待机功耗

为了满足手表产品的长续航要求，建议硬件设计上利用负载开关对各个功能模块进行动态电源管理；如果是常开的模块或通路，选择合适的器件以降低静态电流。

设计时要注意控制电源开关的GPIO管脚的硬件默认状态，同时增加M级阻值的上下拉电阻，保证负载开关默认关闭。

电源器件选型上，LDO和Load Switch 芯片要选择静态电流Iq和关断电流Istb都小的器件，特别是常开的电源芯片一定要关注下Iq参数。

### 处理器工作模式及唤醒源

<div align="center"> CPU Mode Table </div>

```{table}

|工作模式|CPU |外设  |SRAM |IO   |LPTIM |唤醒源 |唤醒时间 |
|:--|:-------|:----|:----|:----|:---- |:---- |:----   |
|Active |Run |Run |可访问 |可翻转 |Run |- |- |
|Sleep |Stop |Run |可访问 |可翻转 |Run |任意中断 |<0.5us |
|DeepSleep |Stop |Stop |不可访问，全保留 |电平保持 |Run |RTC，唤醒IO，GPIO，LPTIM，蓝牙 |250us |
|Standby |Reset |Reset |不可访问，全保留 |电平保持 |Run |RTC，唤醒IO，LPTIM，蓝牙 |1ms |
|Hibernate |Reset |Reset |不可访问，不保留 |高阻 |Reset |RTC，唤醒IO |>2ms |
```

<div align="center"> Interrupt wake up source Table </div>

```{table}

|中断源|管脚   |详细描述  |
|:--|:-------|:--------|
|LWKUP_PIN0 |PA24 |中断信号0 |
|LWKUP_PIN1 |PA25 |中断信号1 |
|LWKUP_PIN2 |PA26 |中断信号2 |
|LWKUP_PIN3 |PA27 |中断信号3 |
|LWKUP_PIN10 |PA34 |中断信号10 |
|LWKUP_PIN11 |PA35 |中断信号11 |
|LWKUP_PIN12 |PA36 |中断信号12 |
|LWKUP_PIN13 |PA37 |中断信号13 |
|LWKUP_PIN14 |PA38 |中断信号14 |
|LWKUP_PIN15 |PA39 |中断信号15 |
|LWKUP_PIN16 |PA40 |中断信号16 |
|LWKUP_PIN17 |PA41 |中断信号17 |
|LWKUP_PIN18 |PA42 |中断信号18 |
|LWKUP_PIN19 |PA43 |中断信号19 |
|LWKUP_PIN20 |PA44 |中断信号20 |

```

### 时钟
芯片需要外部提供2个时钟源，48MHz主晶体和32.768KHz RTC晶体，晶体的具体规格要求和选型如下：

:::{important}

<div align="center"> 晶体规格要求 </div>

```{table}

|晶体|晶体规格要求   |详细描述  |
|:--|:-------|:--------|
|48MHz |CL≦12pF（推荐值7pF）△F/F0≦±10ppmESR≦30 ohms（推荐值22ohms）|晶振功耗和CL,ESR相关,CL和ESR越小功耗越低，为了最佳功耗性能，建议采用推荐值CL≦7pF，ESR≦22 ohms.晶体旁边预留并联匹配电容,当CL<9pF时，无需焊接电容|
|32.768KHz |CL≦12.5pF（推荐值7pF）△F/F0≦±20ppm ESR≦80k ohms（推荐值38Kohms）|晶振功耗和CL,ESR相关,CL和ESR越小功耗越低，为了最佳功耗性能，建议采用推荐值CL≦9pF，ESR≦40K ohms.晶体旁边预留并联匹配电容,当CL<12.5pF时，无需焊接电容|
```

<div align="center"> 推荐晶体列表 </div>

```{table}

|型号|厂家   |参数  |
|:---|:-------|:--------|
|E1SB48E001G00E  |Hosonic     |F0 = 48.000000MHz，△F/F0 = -6 ~ 8 ppm，CL = 8.8 pF，ESR = 22 ohms Max TOPR = -30 ~ 85℃，Package =（2016 公制）|
|ETST00327000LE  |Hosonic     |F0 = 32.768KHz，△F/F0 = -20 ~ 20 ppm，CL = 7 pF，ESR = 70K ohms Max TOPR = -40 ~ 85℃，Package =（3215 公制）|
|SX20Y048000B31T-8.8  |TKD    |F0 = 48.000000MHz，△F/F0 = -10 ~ 10 ppm，CL = 8.8 pF，ESR = 40 ohms Max TOPR = -20 ~ 75℃，Package =（2016 公制）|
|SF32K32768D71T01  |TKD       |F0 = 32.768KHz，△F/F0 = -20 ~ 20 ppm，CL = 7 pF，ESR = 70K ohms Max TOPR = -40 ~ 85℃，Package =（3215 公制）|
```
:::

### 射频

射频走线要求为50ohms特征阻抗。如果天线是匹配好的，射频上无需再增加额外器件。设计时建议预留π型匹配网络用来杂散滤波或天线匹配。

<img src="assets/52xB/sf32lb52X-B-rf-diagram.png" width="80%" align="center" />  

<div align="center"> 射频电路图 </div>



### 显示

芯片支持3-Line SPI、4-Line SPI、Dual data SPI、Quad data SPI和串行JDI 接口。支持16.7M-colors（RGB888）、262K-colors（RGB666）、65K-colors（RGB565）和 8-color（RGB111）Color depth模式。最高支持512RGBx512分辨率。

#### SPI/QSPI显示接口

芯片支持 3/4-wire SPI和Quad-SPI 接口来连接LCD显示屏，各信号描述如下表所示。

<div align="center"> SPI/QSPI 信号连接方式 </div>

```{table}

|spi信号|管脚   |详细描述  |
|:--|:-------|:--------|
|CSx |PA03 |使能信号 |
|WRx_SCL |PA04 |时钟信号 |
|DCx |PA06 |4-wire SPI 模式下的数据/命令信号Quad-SPI 模式下的数据1  |
|SDI_RDx |PA05 |3/4-wire SPI 模式下的数据输入信号Quad-SPI 模式下的数据0  |
|SDO |PA05 |3/4-wire SPI 模式下的数据输出信号请和SDI_RDX短接到一起 |
|D[0] |PA07 |Quad-SPI 模式下的数据2 |
|D[1] |PA08 |Quad-SPI 模式下的数据3 |
|RESET |PA00 |复位显示屏信号 |
|TE |PA02 |Tearing effect to MCU frame signal |
```

#### JDI显示接口

芯片支持并行JDI接口来连接LCD显示屏，如下表所示。

<div align="center"> 并行JDI屏信号连接方式 </div>

```{table}

|spi信号|管脚   |详细描述  |
|:--|:-------|:--------|
|CSx |PA03 |使能信号 |
|WRx_SCL |PA04 |时钟信号 |
|DCx |PA06 |4-wire SPI 模式下的数据/命令信号Quad-SPI 模式下的数据1  |
|SDI_RDx |PA05 |3/4-wire SPI 模式下的数据输入信号Quad-SPI 模式下的数据0  |
|SDO |PA05 |3/4-wire SPI 模式下的数据输出信号请和SDI_RDX短接到一起 |
|D[0] |PA07 |Quad-SPI 模式下的数据2 |
|D[1] |PA08 |Quad-SPI 模式下的数据3 |
|RESET |PA00 |复位显示屏信号 |
|TE |PA02 |Tearing effect to MCU frame signal |
```

#### 触摸和背光接口

芯片支持I2C格式的触摸屏控制接口和触摸状态中断输入，同时支持1路PWM信号来控制背光电源的使能和亮度，如下表所示。

<div align="center"> 触摸和背光控制连接方式 </div>

```{table}

|spi信号|管脚   |详细描述  |
|:--|:-------|:--------|
|CSx |PA03 |使能信号 |
|WRx_SCL |PA04 |时钟信号 |
|DCx |PA06 |4-wire SPI 模式下的数据/命令信号Quad-SPI 模式下的数据1  |
|SDI_RDx |PA05 |3/4-wire SPI 模式下的数据输入信号Quad-SPI 模式下的数据0  |
|SDO |PA05 |3/4-wire SPI 模式下的数据输出信号请和SDI_RDX短接到一起 |
|D[0] |PA07 |Quad-SPI 模式下的数据2 |
|D[1] |PA08 |Quad-SPI 模式下的数据3 |
|RESET |PA00 |复位显示屏信号 |
|TE |PA02 |Tearing effect to MCU frame signal |
```

### 存储
#### 存储器连接接口描述
芯片支持外挂SPI Nor Flash、SPI NAND Flash、SD NAND Flash和eMMC 四种存储介质。

<div align="center"> SPI Nor/Nand Flash信号连接 </div>

```{table}

|spi信号|管脚   |详细描述  |
|:--|:-------|:--------|
|CSx |PA03 |使能信号 |
|WRx_SCL |PA04 |时钟信号 |
|DCx |PA06 |4-wire SPI 模式下的数据/命令信号Quad-SPI 模式下的数据1  |
|SDI_RDx |PA05 |3/4-wire SPI 模式下的数据输入信号Quad-SPI 模式下的数据0  |
|SDO |PA05 |3/4-wire SPI 模式下的数据输出信号请和SDI_RDX短接到一起 |
|D[0] |PA07 |Quad-SPI 模式下的数据2 |
|D[1] |PA08 |Quad-SPI 模式下的数据3 |
|RESET |PA00 |复位显示屏信号 |
|TE |PA02 |Tearing effect to MCU frame signal |
```

<div align="center"> SD Nand Flash和eMMC信号连接 </div>

```{table}

|spi信号|管脚   |详细描述  |
|:--|:-------|:--------|
|CSx |PA03 |使能信号 |
|WRx_SCL |PA04 |时钟信号 |
|DCx |PA06 |4-wire SPI 模式下的数据/命令信号Quad-SPI 模式下的数据1  |
|SDI_RDx |PA05 |3/4-wire SPI 模式下的数据输入信号Quad-SPI 模式下的数据0  |
|SDO |PA05 |3/4-wire SPI 模式下的数据输出信号请和SDI_RDX短接到一起 |
|D[0] |PA07 |Quad-SPI 模式下的数据2 |
|D[1] |PA08 |Quad-SPI 模式下的数据3 |
|RESET |PA00 |复位显示屏信号 |
|TE |PA02 |Tearing effect to MCU frame signal |
```


#### 启动设置

芯片支持内部合封Spi Nor Flash、外挂Spi Nor Flash、外挂Spi Nand Flash、外挂SD Nand Flash和外挂eMMC启动。其中：
- SF32LB52AUx6 内部合封有flash，默认从内部合封flash启动
- SF32LB52D/F/HUx6 内部合封psram，必须从外挂的存储介质启动


<div align="center"> 启动选项设置 </div>

```{table}

|Bootstrap[1] (PA13) |Bootstrap[0] (PA17)    |Boot From ext memory  |
|:----:|:----:|:---|
|L |L |Spi Nor Flash  |
|L |H |Spi Nand Flash |
|H |L |SD Nand Flash  |
|H |H |eMMC           |
```

#### 启动存储介质电源控制
芯片支持对启动存储介质的电源开关控制，以降低关机功耗。电源开关的使能管脚必须使用PA21来控制，开关的使能电平要求是[高打开，低关闭]。

:::{important}
- SF32LB52AUx6 内部合封有flash，请给VDD_SIP加电源开关。
- SF32LB52D/F/HUx6 内部合封psram，如果PVDD=3.3V，且VDD_SIP使用内部LDO供电，VDD_SIP可以不加电源开关；如果PVDD=1.8V，VDD_SIP要加电源开关。
- 外供存储介质的电源独立于VDD_SIP，单独增加电源开关。
- **所有和启动有关的存储器的电源开关的使能脚必须用PA21控制。**
:::

### 按键
#### 开关机按键
芯片的PA34支持长按复位功能，可以设计成按键，实现开关机+长按复位功能。PA34的长按复位功能要求高电平有效，所以设计成默认下拉为低，按键按下后电平为高，如{numref}`图 {number} <sf32lb52X-B-PWKEY>`所示。

<img src="assets/52xB/sf32lb52X-B-PWKEY.png" width="80%" align="center" />  

<div align="center"> 开关机按键电路图 </div>


#### 普通GPIO按键

#### 机械旋钮按键


### 振动马达

芯片支持PWM输出来控制振动马达。


<img src="assets/52xB/sf32lb52X-B-VIB.png" width="80%" align="center" />  

<div align="center"> 振动马达电路图 </div>


### 音频接口

芯片的音频相关接口，如表4-16所示，音频接口信号有以下特点：
1.	支持一路单端ADC输入，外接模拟MIC，中间需要加容值至少2.2uF的隔直电容，模拟MIC的电源接芯片MIC_BIAS电源输出脚；
2.	支持一路差分DAC输出，外接模拟音频PA， DAC输出的走线，按照差分线走线，做好包地屏蔽处理，还需要注意：Trace Capacitor < 10pF, Length < 2cm。

<div align="center"> 音频信号连接方式 </div>

```{table}

|音频信号 |管脚   |详细描述 |
|:---|:---|:---|
|BIAS |MIC_BIAS |麦克风电源       |
|AU_ADC1P |ADCP |单端模拟MIC输入  |
|AU_DAC1P |DACP |差分模拟输出P    |
|AU_DAC1N |DACN |差分模拟输出N    |
```

模拟MEMS MIC推荐电路如{numref}`图 {number} <sf32lb52X-B-MEMS-MIC>`所示，模拟ECM MIC 单端推荐电路如{numref}`图 {number} <sf32lb52X-B-ECM-MIC>`所示，其中MEMS_MIC_ADC_IN和ECM_MIC_ADC_IN连接到SF32LB52X的ADCP输入管脚。


<img src="assets/52xB/sf32lb52X-B-MEMS-MIC.png" width="80%" align="center" />  

<div align="center"> 模拟MEMS MIC单端输入电路图 </div>


<img src="assets/52xB/sf32lb52X-B-ECM-MIC.png" width="80%" align="center" />  

<div align="center"> 模拟ECM单端输入电路图 </div>


模拟音频输出推荐电路如{numref}`图 {number} <sf32lb52X-B-DAC-PA>`所示，注意虚线框内的差分低通滤波器要靠近芯片端放置。


<img src="assets/52xB/sf32lb52X-B-DAC-PA.png" width="80%" align="center" />  

<div align="center"> 模拟音频PA电路图 </div>



### 传感器

芯片支持心率、加速度和地磁等传感器。传感器的供电电源，选择Iq比较小的Load Switch来进行电源的开关控制。

### UART和I2C管脚设置

芯片支持任意管脚UART和I2C功能映射，所有的PA接口都可以映射成UART或I2C功能管脚。

### GPTIM管脚设置

芯片支持任意管脚GPTIM功能映射，所有的PA接口都可以映射成GPTIM功能管脚。

### 调试和下载接口

芯片支持DBG_UART接口用于下载和调试，通过3.3V接口的UART转USB Dongle板接PC机。芯片可以通过DBG_UART进行调试信息输出，具体请参考表`{number} <sf32lb52x-B-P-JDI-LCD-table>`

<div align="center"> 调试口连接方式 </div>

```{table}

|DBG信号 |管脚   |详细描述 |
|:---|:---|:---|
|DBG_UART_RXD |PA18 |Debug UART 接收 |
|DBG_UART_TXD |PA19 |Debug UART 发送 |
```

### 产线烧录和晶体校准

思澈科技提供脱机下载器来完成产线程序的烧录和晶体校准，硬件设计时，请注意至少预留测试点：PVDD、GND、AVDD33、DB_UART_RXD、DB_UART_RXD，PA01。

详细的烧录和晶体校准见“**_脱机下载器使用指南.pdf”文档，包含在开发资料包中。



### 原理图和PCB图纸检查列表

见“**_Schematic checklist_**.xlsx”和“**_PCB checklist_**.xlsx”文档，包含在开发资料包中。
