# SF32LB52X-硬件设计指南

:::{attention}
本文档适配后缀为字母`B、E、G、J`的芯片，使用3.3V电源供电；后缀为字母`D`的芯片，使用1.8V电源供电。

对于后缀为数字`0、3、5、7`的芯片，属于SF32LB52x系列,使用锂电池供电，支持USB充电。应该参照[硬件设计指南](/hardware/SF32LB520-3-5-7-HW-Application)
:::

## 基本介绍

本文的主要目的是帮助开发人员完成基于SF32LB52X系列芯片的手表方案开发。本文重点介绍方案开发过程中的硬件设计相关注意事项，尽可能的减少开发人员工作量，缩短产品的上市周期。

SF32LB52X是一系列用于超低功耗人工智能物联网（AIoT）场景下的高集成度、高性能MCU芯片。芯片采用了基于Arm Cortex-M33 STAR-MC1处理器的大小核架构，集成高性能2D/2.5D图形引擎，人工智能神经网络加速器，双模蓝牙5.3，以及音频CODEC，可广泛用于腕带类可穿戴电子设备、智能移动终端、智能家居等各种应用场景。

:::{attention}
SF32LB52X是SF32LB52系列的**常规供电版本，供电电压为2.97~3.63V(除52D外，52D为1.71~1.98V)，不支持充电**，具体包含如下型号：\
SF32LB52BU36，合封1MB QSPI-NOR Flash \
SF32LB52DUB6，合封4MB OPI-PSRAM \
SF32LB52EUB6，合封4MB OPI-PSRAM \
SF32LB52GUC6，合封8MB OPI-PSRAM \
SF32LB52JUD6，合封16MB OPI-PSRAM
:::

处理器外设资源如下：

- 45x GPIO
- 3x UART
- 4x I2C
- 2x GPTIM
- 2x SPI
- 1x I2S音频接口
- 1x SDIO 存储接口
- 1x PDM音频接口
- 1x 差分模拟音频输出
- 1x 单端模拟音频输入
- 支持单/双/四数据线SPI显示接口，支持串行JDI模式显示接口
- 支持带GRAM和不带GRAM的两种显示屏
- 支持UART下载和软件调试


## 封装


<div align="center"> 表2-1 封装信息表 </div>

```{table}
:align: center
|封装名称|尺寸|管脚间距|
|:--|:-|:-|
|QFN68L | 7x7x0.85 mm | 0.35 mm |
```


<img src="assets/52xB/sf32lb52X-B-package-layout.png" width="80%" align="center" />  

<div align="center"> 图2-1 QFN68L管脚分布 </div>  <br> <br> <br>



## 典型应用方案

下图是典型的SF32LB52X运动手表组成框图，主要功能有显示、存储、传感器、震动马达和音频输入和输出。

<!-- 这里的图片有问题，需要替换为B3版本的框图 -->
<img src="assets/52xB/sf32lb52X-B-watch-app-diagram-52X.png" width="80%" align="center" />  

<div align="center"> 图3-1 运动手表组成框图 </div>  <br> <br> <br>


:::{Note} 

   - 大小核双CPU架构，同时兼顾高性能和低功耗设计要求
   - 片内集成PMU模块
   - 支持QSPI接口的TFT或AMOLED显示屏，最高支持512*512分辨率
   - 支持PWM背光控制
   - 支持外接QSPI NOR/NAND Flash和SD NAND Flash存储芯片
   - 支持双模蓝牙5.3
   - 支持模拟音频输入
   - 支持模拟音频输出
   - 支持PWM震动马达控制
   - 支持SPI/I2C接口的加速度/地磁/陀螺仪传感器
   - 支持SPI/I2C接口的心率/血氧/心电图/地磁传感器
   - 支持UART调试打印接口和烧写工具
   - 支持蓝牙HCI调试接口
   - 支持产线一拖多程序烧录
   - 支持产线校准晶体功能
   - 支持OTA在线升级功能
:::



## 原理图设计指导

### 电源

#### 处理器供电要求

<div align="center"> 表4-1 电源供电要求 </div>

```{table}
:align: center
|电源管脚| 最小电压(V) | 典型电压(V) | 最大电压(V) | 最大电流(mA) |   详细描述 |
|:--|:--|:--|:--|:--|:----------------------------------------------------|
|PVDD       |2.97   |3.3        |3.63   |150    |PVDD系统电源输入，接10uF电容 
|BUCK_LX    |-      |1.25       |-      |50     |BUCK输出脚，接4.7uH电感 
|BUCK_FB    |-      |1.25       |-      |50     |BUCK反馈和内部电源输入脚，接电感另一端，且外接4.7uF电容 
|VDD_VOUT1  |-      |1.1        |-      |50     |内部LDO，外接4.7uF电容，内部电源，不给外设供电 
|VDD_VOUT2  |-      |0.9        |-      |20     |内部LDO，外接4.7uF电容，内部电源，不给外设供电 
|VDD_RET    |-      |0.9        |-      |1      |内部LDO，外接0.47uF电容，内部电源，不给外设供电 
|VDD_RTC    |-      |1.1        |-      |1      |内部LDO，外接1uF电容，内部电源，不给外设供电 
|VDDIOA     |1.71   |1.8/3.3    |3.63   |-      |GPIO电源输入，外接1uF电容 
|AVDD33     |2.97   |3.3        |3.63   |100    |3.3V模拟电源输入，外接4.7uF电容 
|AVDD33_AUD |2.97   |3.3        |3.63   |50     |3.3V音频电源输入，外接2.2uF电容  
|VDD_SIP    |1.71   |1.8/3.3    |3.63   |30     |内部LDO，或者外部电源输入{SUP}`(1)` ，外接1uF电容
|AVDD_BRF   |2.97   |3.3        |3.63   |100    |模拟电源输入，外接4.7uF电容 
|MIC_BIAS   |1.4    |-          |2.8    |-      |MIC电源输出，外接1uF电容 
```
:::{note} 
{SUP}`(1)`
* SF32LB52BU36，需要外供1.8V或3.3V
* SF32LB52BU56，需要外供3.3V
* SF32LB52DUB6，需要外供1.8V
* SF32LB52E/G/JUx6，内部LDO直接供电，无需外供
:::
:::{important}
系统使用Hibernate mode时，VDD_SIP供电要关闭，否则合封存储的I/O上会有漏电风险。VDD_SIP的电源控制信号请使用专用的PA21引脚。
:::

#### 处理器BUCK电感选择要求

**功率电感关键参数**
:::{important}
L(电感值) = 4.7uH ± 20%，DCR(直流阻抗) ≦ 0.4 ohm，Isat(饱和电流) ≧ 450mA。
:::

<!-- A3版本要增加电池及充电控制 -->

#### 如何降低待机功耗

为了满足手表产品的长续航要求，建议硬件设计上利用负载开关对各个功能模块进行动态电源管理；如果是常开的模块或通路，选择合适的器件以降低静态电流。

设计时要注意控制电源开关的GPIO管脚的硬件默认状态，同时增加M级阻值的上下拉电阻，保证负载开关默认关闭。

电源器件选型上，LDO和Load Switch 芯片要选择静态电流Iq和关断电流Istb都小的器件，特别是常开的电源芯片一定要关注下Iq参数。



### 处理器工作模式及唤醒源

<div align="center"> 表4-4 CPU Mode Table </div>

```{table}
:align: center
|工作模式|CPU |外设  |SRAM |IO   |LPTIM |唤醒源 |唤醒时间 |
|:--|:-------|:----|:----|:----|:---- |:---- |:----   |
|Active |Run |Run |可访问 |可翻转 |Run |- |- |
|Sleep |Stop |Run |可访问 |可翻转 |Run |任意中断 |<0.5us |
|DeepSleep |Stop |Stop |不可访问，全保留 |电平保持 |Run |RTC，唤醒IO，GPIO，LPTIM，蓝牙 |250us |
|Standby |Reset |Reset |不可访问，全保留 |电平保持 |Run |RTC，唤醒IO，LPTIM，蓝牙 |1ms |
|Hibernate |Reset |Reset |不可访问，不保留 |高阻 |Reset |RTC，唤醒IO |>2ms |
```

如表4-5所示，全系列芯片支持15个Standby和Hibernate模式下可唤醒中断源。

<div align="center">表4-5 Interrupt wake up source Table </div>

```{table}
:align: center
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

<div align="center"> 表4-6 晶体规格要求 </div>

```{table}
:align: center
|晶体|晶体规格要求   |详细描述  |
|:--|:-------|:--------|
|48MHz |7pF≦CL≦12pF（推荐值8.8pF） △F/F0≦±10ppm ESR≦30 ohms（推荐值22ohms）|晶振功耗和CL,ESR相关,CL和ESR越小功耗越低，为了最佳功耗性能，建议采用CL和ESR在要求范围内相对较小值的物料。晶体旁边预留并联匹配电容,当CL<12pF时，无需焊接电容|
|32.768KHz |CL≦12.5pF（推荐值7pF）△F/F0≦±20ppm ESR≦80k ohms（推荐值38Kohms）|晶振功耗和CL,ESR相关,CL和ESR越小功耗越低，为了最佳功耗性能，建议采用CL和ESR在要求范围内相对较小值的物料。晶体旁边预留并联匹配电容,当CL<12.5pF时，无需焊接电容|
```

<div align="center"> 表4-7 推荐晶体列表 </div>

```{table}
:align: center
|型号|厂家   |参数  |
|:---|:-------|:--------|
|E1SB48E001G00E  |Hosonic     |F0 = 48.000000MHz，△F/F0 = -6 ~ 8 ppm，CL = 8.8 pF，ESR = 22 ohms Max TOPR = -30 ~ 85℃，Package =（2016 公制）|
|ETST00327000LE  |Hosonic     |F0 = 32.768KHz，△F/F0 = -20 ~ 20 ppm，CL = 7 pF，ESR = 70K ohms Max TOPR = -40 ~ 85℃，Package =（3215 公制）|
|SX20Y048000B31T-8.8  |TKD    |F0 = 48.000000MHz，△F/F0 = -10 ~ 10 ppm，CL = 8.8 pF，ESR = 40 ohms Max TOPR = -20 ~ 75℃，Package =（2016 公制）|
|SF32K32768D71T01  |TKD       |F0 = 32.768KHz，△F/F0 = -20 ~ 20 ppm，CL = 7 pF，ESR = 70K ohms Max TOPR = -40 ~ 85℃，Package =（3215 公制）|
```
:::

详细的物料认证信息，请参考：
[SIFLI-MCU-AVL-认证表](index)

### 射频

射频走线要求为50ohms特征阻抗。如果天线是匹配好的，射频上无需再增加额外器件。设计时建议预留π型匹配网络用来杂散滤波或天线匹配。

<img src="assets/52xB/sf32lb52X-B-rf-diagram.png" width="80%" align="center" />  

<div align="center"> 图4-7 射频电路图 </div>   <br>  <br>  <br>



### 显示

芯片支持3-Line SPI、4-Line SPI、Dual data SPI、Quad data SPI和串行JDI 接口。支持16.7M-colors（RGB888）、262K-colors（RGB666）、65K-colors（RGB565）和 8-color（RGB111）Color depth模式。最高支持512RGBx512分辨率。

<div align="center"> 表4-8 LCD driver支持列表 </div>

```{table}
:align: center
| 型号   | 厂家  | 分辨率  | 类型   | 接口 |
| :-- | :-- | :-- | :-- | :-- |
| RM69090  | Raydium    | 368*448 | Amoled | 3-Line SPI，4-Line  SPI，Dual data SPI，  Quad data SPI，MIPI-DSI |
| RM69330  | Raydium    | 454*454 | Amoled | 3-Line SPI，4-Line  SPI，Dual data SPI，  Quad data SPI，8-bits  8080-Series MCU ，MIPI-DSI |
| ILI8688E | ILITEK     | 368*448 | Amoled | Quad data SPI，MIPI-DSI                                      |
| SH8601A  | 晟合技术   | 454*454 | Amoled | 3-Line SPI，4-Line  SPI，Dual data SPI，  Quad data SPI，8-bits  8080-Series MCU ，MIPI-DSI |
| SPD2012  | Solomon    | 356*400 | TFT    | Quad data SPI                                                |
| GC9C01   | Galaxycore | 360*360 | TFT    | Quad data SPI                                                |
| GC9B71   | Galaxycore | 320*380 | TFT    | Quad data SPI                                                |
| ST77903  | Sitronix   | 400*400 | TFT    | Quad data SPI                                                |
| ICNA3311 | Chipone    | 454*454 | Amoled | Quad data SPI                                                |
| FT2308   | FocalTech  | 410*494 | Amoled | Quad data SPI                                                |
```


#### SPI/QSPI显示接口

芯片支持 3/4-wire SPI和Quad-SPI 接口来连接LCD显示屏，各信号描述如下表所示。

<div align="center"> 表4-9 SPI/QSPI 信号连接方式 </div>

```{table}
:align: center
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

<div align="center"> 表4-10 并行JDI屏信号连接方式 </div>

```{table}
:align: center

| JDI信号  | I/O  | 详细描述   |
|:--|:-------|:--------|
| JDI_VCK  | PA39 | Shift clock for the vertical driver                  |
| JDI_VST  | PA08 | Start signal for the vertical driver                 |
| JDI_XRST | PA40 | Reset signal for the horizontal and  vertical driver |
| JDI_HCK  | PA41 | Shift  clock for the horizontal driver               |
| JDI_HST  | PA06 | Start signal for the horizontal driver               |
| JDI_ENB  | PA07 | Write enable signal for the pixel memory             |
| JDI_R1   | PA05 | Red image data (odd pixels)                          |
| JDI_R2   | PA42 | Red image data (even pixels)                         |
| JDI_G1   | PA04 | Green image data (odd pixels)                        |
| JDI_G2   | PA43 | Green image data (even pixels)                       |
| JDI_B1   | PA03 | Blue image data (odd pixels)                         |
| JDI_B2   | PA02 | Blue image data (even pixels)                        |
```

#### EPD显示接口

芯片支持8bit 并口EPD显示屏接口，如下表所示。

```{table}
:align: center

| EDP信号  | I/O  | 详细描述   |
|:--|:-------|:--------|
| CLK          | PA04 | Clock source driver                    |
| CKV/CPV      | GPIO | Clock gate driver                      |
| SPH          | PA06 | Start pulse source driver              |
| SPV/STV      | GPIO | Start pulse gate driver                |
| LE           | GPIO | Latch enable source driver             |
| OE           | GPIO | Output enable source driver            |
| D0           | PA07 | Data signal source driver bit0         |
| D1           | PA08 | Data signal source driver bit1         |
| D2           | PA37 | Data signal source driver bit2         |
| D3           | PA39 | Data signal source driver bit3         |
| D4           | PA40 | Data signal source driver bit4         |
| D5           | PA41 | Data signal source driver bit5         |
| D6           | PA42 | Data signal source driver bit6         |
| D7           | PA43 | Data signal source driver bit7         |
| GMODE        | GPIO | Output mode selection gate driver      |
| VPOS         | TPS  | Positive power supply source driver    |
| VNEG         | TPS  | Negative power supply source driver    |
| VGH          | TPS  | Positive power supply gate driver      |
| VGL          | TPS  | Negative power supply gate driver      |
| VCOM         | TPS  | Common connection                      |
| TPS_WAKEUP   | GPIO | TPS pmic wake up                       |
| TPS_PWRUP    | GPIO | TPS pmic power up                      |
| TPS_SDA      | I2C  | TPS pmic I2C sda                       |
| TPS_SCL      | I2C  | TPS pmic I2C scl                       |
| TPS_PWRCOM   | GPIO | TPS pmic VCOM_CTRL,vcom enable         |
| TPS_GOOD     | GPIO | TPS pmic power good output             |

```
:::{note}

上表中，I/O列里
- 标记'PA**'的是必须这样分配IO
- 标记GPIO是可以任意分配IO
- 标记TPS是指TPS pmic芯片输出到屏的IO
- 标记I2C是指需要分配I2C功能的IO

:::


#### 触摸和背光接口

芯片支持I2C格式的触摸屏控制接口和触摸状态中断输入，同时支持1路PWM信号来控制背光电源的使能和亮度，如下表所示。

<div align="center"> 表4-11 触摸和背光控制连接方式 </div>

```{table}
:align: center
| 触摸屏和背光信号 | 管脚 | 详细描述                   |
| ---------------- | ---- | -------------------------- |
| Interrupt        | PA43 | 触摸状态中断信号（可唤醒） |
| I2C1_SCL         | PA42 | 触摸屏I2C的时钟信号        |
| I2C1_SDA         | PA41 | 触摸屏I2C的数据信号        |
| BL_PWM           | PA01 | 背光PWM控制信号            |
| Reset            | PA44 | 触摸复位信号               |
```

### 存储
#### 存储器连接接口描述
芯片支持外挂SPI NOR Flash、SPI NAND Flash、SD NAND Flash和eMMC 四种存储介质。

<div align="center"> 表4-12 SPI NOR/NAND Flash信号连接 </div>

```{table}
:align: center
| Flash 信号 | I/O信号 | 详细描述                                    |
| ---------- | ------- | ------------------------------------------- |
| CS#        | PA12    | Chip select, active low.                    |
| SO         | PA13    | Data Input (Data Input Output 1)            |
| WP#        | PA14    | Write Protect Output (Data Input Output  2) |
| SI         | PA15    | Data Output (Data Input Output 0)           |
| SCLK       | PA16    | Serial Clock Output                         |
| Hold#      | PA17    | Data Output (Data Input Output 3)           |
```


<div align="center"> 表4-13 SD NAND Flash和eMMC信号连接 </div>

```{table}
:align: center
| Flash 信号 | I/O信号 | 详细描述 |
| ---------- | ------- | -------- |
| SD2_CMD    | PA15    | 命令信号 |
| SD2_D1     | PA17    | 数据1    |
| SD2_D0     | PA16    | 数据0    |
| SD2_CLK    | PA14    | 时钟信号 |
| SD2_D2     | PA12    | 数据2    |
| SD2_D3     | PA13    | 数据3    |
```
:::{important}
- NOR Flash: 外部不用加上拉电阻
- Nand Flash: PA17(Hold#)加上拉电阻
- SD Nand Flash: PA13(D3)和PA15(CMD)加上拉电阻
- eMMC: PA17(D1)、PA13(D3)和PA15(CMD)加上拉电阻
- 上拉电阻推荐7.5K
:::

#### 启动设置

芯片支持内部合封Spi NOR Flash、外挂Spi NOR Flash、外挂Spi NAND Flash、外挂SD NAND Flash和外挂eMMC启动。其中：
- SF32LB52AUx6 内部合封有flash，默认从内部合封flash启动
- SF32LB52D/F/HUx6 内部合封PSRAM，必须从外挂的存储介质启动


<!-- 这里的图片需要修改，A3和B3要不同的版本 -->

<img src="assets/52xB/sf32lb52X-B-Bootstrap.png" width="80%" align="center" />  

<div align="center"> 图4-8 Bootstrap管脚推荐电路图 </div>  <br> <br> <br>

<!-- eMMC只有B3支持，A3要删除 -->
<div align="center"> 表4-14 启动选项设置 </div>

```{table}
:align: center
|Bootstrap[1] (PA13) |Bootstrap[0] (PA17)    |Boot From ext memory  |
| ------------ | ------------ | -------------- |
| L            | L            | SPI NOR Flash  |
| L            | H            | SPI NAND Flash |
| H            | X            | SD NAND Flash  |
| H            | H            | eMMC           |
```

#### 启动存储介质电源控制
芯片支持对启动存储介质的电源开关控制，以降低关机功耗。电源开关的使能管脚必须使用PA21来控制，开关的使能电平要求是[高打开，低关闭]。

:::{important}
- SF32LB52AUx6 内部合封有flash，请给VDD_SIP加电源开关。
- SF32LB52D/F/HUx6 内部合封PSRAM，如果PVDD=3.3V，且VDD_SIP使用内部LDO供电，VDD_SIP可以不加电源开关；如果PVDD=1.8V，VDD_SIP要加电源开关。
- 外供存储介质的电源独立于VDD_SIP，单独增加电源开关。
<!-- eMMC只有B3支持，A3要删除 -->
- eMMC芯片有VCC和VCCQ两种电源域，方式1：可以2个电源一起做控制，关机功耗低，但eMMC在sleep时恢复慢，CPU平均功耗高；方式2：可以单独控制VCC，VCCQ常供不断电，关机功耗比方式1高，但eMMC在sleep时恢复快，CPU平均功耗比方式1低。
- **所有和启动有关的存储器的电源开关的使能脚必须用PA21控制。**
- MPI外接32MB及以上容量的NOR Flash时，Flash必须用PA21控制可以断电，使得Flash在MCU重启或进入Hibernate时可以退出4BYTE Mode，否则ROM会认不出Flash。外接16MB及以下容量的NOR Flash时，Flash可以常供电。
- 参考设计中，PA13和PA17都预留了上拉电阻位置，根据存储介质类型选择上拉电阻，电阻推荐7.5K。
:::

### 按键
#### 开关机按键
芯片的PA34支持长按复位功能，可以设计成按键，实现开关机+长按复位功能。PA34的长按复位功能要求高电平有效，所以设计成默认下拉为低，按键按下后电平为高，如{numref}`图 {number} <sf32lb52X-B-PWKEY>`所示。

<img src="assets/52xB/sf32lb52X-B-PWKEY.png" width="80%" align="center" />  

<div align="center">图4-9 开关机按键电路图 </div>   <br>  <br>  <br>


#### 机械旋钮按键

<img src="assets/52xB/sf32lb52X-B-XNKEY.png" width="80%" align="center" />  

<div align="center">图4-10 开关机按键电路图 </div>   <br>  <br>  <br>

### 振动马达

芯片支持PWM输出来控制振动马达。

<!-- 这里的内容需要A3和B3做区别处理 -->
<img src="assets/52xB/sf32lb52X-B-VIB.png" width="80%" align="center" />  

<div align="center"> 图4-11 振动马达电路图 </div>  <br> <br> <br>


### 音频接口

芯片的音频相关接口，如表4-15所示，音频接口信号有以下特点：
1.	支持一路单端ADC输入，外接模拟MIC，中间需要加容值至少2.2uF的隔直电容，模拟MIC的电源接芯片MIC_BIAS电源输出脚；
2.	支持一路差分DAC输出，外接模拟音频PA， DAC输出的走线，按照差分线走线，做好包地屏蔽处理，还需要注意：Trace Capacitor < 10pF, Length < 2cm。

<div align="center"> 表4-15 音频信号连接方式 </div>

```{table}
:align: center
|音频信号 |管脚   |详细描述 |
|:---|:---|:---|
|BIAS |MIC_BIAS |麦克风电源       |
|AU_ADC1P |ADCP |单端模拟MIC输入  |
|AU_DAC1P |DACP |差分模拟输出P    |
|AU_DAC1N |DACN |差分模拟输出N    |
```

模拟MEMS MIC推荐电路如图4-12所示，模拟ECM MIC 单端推荐电路如图4-13所示，其中MEMS_MIC_ADC_IN和ECM_MIC_ADC_IN连接到SF32LB52x的ADCP输入管脚。


<img src="assets/52xB/sf32lb52X-B-MEMS-MIC.png" width="80%" align="center" />  

<div align="center"> 图4-12 模拟MEMS MIC单端输入电路图 </div>   <br>  <br>  <br>


<img src="assets/52xB/sf32lb52X-B-ECM-MIC.png" width="80%" align="center" />  

<div align="center"> 图4-13 模拟ECM单端输入电路图 </div>   <br>  <br>  <br>


模拟音频输出推荐电路如图4-14 所示，注意虚线框内的差分低通滤波器要靠近芯片端放置。


<img src="assets/52xB/sf32lb52X-B-DAC-PA.png" width="80%" align="center" />  

<div align="center"> 图4-14 模拟音频PA电路图 </div>   <br>  <br>  <br>



### 传感器

芯片支持心率、加速度和地磁等传感器。传感器的供电电源，选择Iq比较小的Load Switch来进行电源的开关控制。

### UART和I2C管脚设置

芯片支持任意管脚UART和I2C功能映射，所有的PA接口都可以映射成UART或I2C功能管脚。

### GPTIM管脚设置

芯片支持任意管脚GPTIM功能映射，所有的PA接口都可以映射成GPTIM功能管脚。

### 调试和下载接口

芯片支持DBG_UART接口用于下载和调试，通过3.3V接口的UART转USB Dongle板接PC机。

<div align="center">表4-16 调试口连接方式 </div>

```{table}
:align: center
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


## PCB设计指导

### PCB封装设计

SF32LB52X系列芯片的QFN68L封装尺寸：7mmX7mmx0.85mm；管脚数：68；PIN 间距：0.35mm。 详细尺寸如图5-1所示。

<img src="assets/52xB/sf32lb52X-B-QFN68L-POD.png" width="80%" align="center" />  

<div align="center"> 图5-1 QFN68L封装尺寸图 </div>   <br>  <br>  <br>


<img src="assets/52xB/sf32lb52X-B-QFN68L-SHAPE.png" width="80%" align="center" />  

<div align="center"> 图5-2 QFN68L封装形状图 </div>   <br>  <br>  <br>


<img src="assets/52xB/sf32lb52X-B-QFN68L-REF.png" width="80%" align="center" />  

<div align="center"> 图5-3 QFN68L封装PCB焊盘设计参考图 </div>   <br>  <br>  <br>



### PCB叠层设计

SF32LB52X系列芯片支持单双面布局，器件可以放到单面，也可以把电容等放到芯片的背面。PCB支持PTH通孔设计，推荐采用4层PTH，推荐参考叠层结构如图5-4所示。

<img src="assets/52xB/sf32lb52X-B-PCB-STACK.png" width="80%" align="center" />  

<div align="center"> 图5-4 参考叠层结构图 </div>   <br>  <br>  <br>



### PCB通用设计规则

PTH 板PCB通用设计规则如图5-5所示。

<img src="assets/52xB/sf32lb52X-B-PCB-RULE.png" width="80%" align="center" />  

<div align="center"> 图5-5 通用设计规则 </div>   <br>  <br>  <br>



### PCB走线扇出

QFN封装信号扇出，所有管脚全部通过表层扇出，如图5-6所示。

<img src="assets/52xB/sf32lb52X-B-PCB-FANOUT.png" width="80%" align="center" />  

<div align="center"> 如图5-6 表层扇出参考图 </div>   <br>  <br>  <br>



### 时钟接口走线

晶体需摆放在屏蔽罩里面，离PCB板框间距大于1mm,尽量远离发热大的器件，如PA，Charge，PMU等电路器件，距离最好大于5mm以上，避免影响晶体频偏，晶体电路禁布区间距大于0.25mm避免有其它金属和器件，如图5-7所示。

<img src="assets/52xB/sf32lb52X-B-PCB-CRYSTAL.png" width="80%" align="center" />  

<div align="center"> 图5-7 晶体布局图 </div>   <br>  <br>  <br>


48MHz晶体走线建议走表层，长度要求控制在3-10mm区间，线宽0.1mm，必须立体包地处理，并且远离VBAT、DC/DC及高速信号线。48MHz晶体区域下方表层及临层做禁空处理，禁止其它走线从其区域走，如图5-8，5-9，5-10所示。

<img src="assets/52xB/sf32lb52X-B-PCB-48M-SCH.png" width="80%" align="center" />  

<div align="center"> 图5-8 48MHz晶体原理图 </div>   <br>  <br>  <br>


<img src="assets/52xB/sf32lb52X-B-PCB-48M-MOD.png" width="80%" align="center" />  

<div align="center"> 图5-9 48MHz晶体走线模型 </div>   <br>  <br>  <br>


<img src="assets/52xB/sf32lb52X-B-PCB-48M-ROUTE-REF.png" width="80%" align="center" />  

<div align="center"> 图5-10 48MHz晶体走线参考 </div>   <br>  <br>  <br>


32.768KHz晶体走线建议走表层，长度控制≤10mm，线宽0.1mm。32K_XI/32_XO平行走线间距≥0.15mm，必须立体包地处理。晶体区域下方表层及临层做禁空处理，禁止其它走线从其区域走，如图5-11，5-12，5-13所示。

<img src="assets/52xB/sf32lb52X-B-PCB-32K-SCH.png" width="80%" align="center" />  

<div align="center"> 图5-11 32.768KHz晶体原理图 </div>   <br>  <br>  <br>


<img src="assets/52xB/sf32lb52X-B-PCB-32K-MOD.png" width="80%" align="center" />  

<div align="center"> 图5-12 32.768KHz晶体走线模型 </div>   <br>  <br>  <br>


<img src="assets/52xB/sf32lb52X-B-PCB-32K-ROUTE-REF.png" width="80%" align="center" />  

<div align="center"> 图5-13 32.768KHz晶体走线参考 </div>   <br>  <br>  <br>



### 射频接口走线

射频匹配电路要尽量靠近芯片端放置，不要靠近天线端。AVDD_BRF射频电源其滤波电容尽量靠近芯片管脚放置，电容接地管脚打孔直接接主地。RF信号的π型网络的原理图和PCB分别如图5-14，5-15所示。

<img src="assets/52xB/sf32lb52X-B-SCH-RF.png" width="80%" align="center" />  

<div align="center"> 图5-14 π型网络以及电源电路原理图 </div>   <br>  <br>  <br>


<img src="assets/52xB/sf32lb52X-B-PCB-RF.png" width="80%" align="center" />  

<div align="center"> 图5-15 π型网络以及电源PCB布局 </div>   <br>  <br>  <br>



射频走线建议走表层，避免打孔穿层影响RF性能，线宽最好大于10mil，需要立体包地处理，避免走锐角和直角。射频线做50欧阻抗控制，两边多打屏蔽地孔，如图5-16, 5-17所示。

<img src="assets/52xB/sf32lb52X-B-SCH-RF-2.png" width="80%" align="center" />  

<div align="center"> 图5-16 RF信号电路原理图 </div>   <br>  <br>  <br>


<img src="assets/52xB/sf32lb52X-B-PCB-RF-ROUTE.png" width="80%" align="center" />  

<div align="center"> 图5-17 RF信号PCB走线图 </div>   <br>  <br>  <br>



### 音频接口走线
AVDD33_AUD是音频的供电管脚，其滤波电容靠近对应管脚放置，这样滤波电容的接地脚可以良好地连接到PCB的主地。MIC_BIAS是给麦克风外设供电的电源输出管脚，其对应滤波电容靠近对应管脚放置。同样AUD_VREF管脚的滤波电容也靠近管脚放置，如图5-18a，5-18b所示。

<img src="assets/52xB/sf32lb52X-B-SCH-AUDIO-PWR.png" width="80%" align="center" />  

<div align="center"> 图5-18a 音频相关电源滤波电路 </div>   <br>  <br>  <br>


<img src="assets/52xB/sf32lb52X-B-PCB-AUDIO-PWR.png" width="80%" align="center" />  

<div align="center"> 图5-18b 音频相关电源滤波电路PCB参考走线 </div>   <br>  <br>  <br>



模拟信号输入ADCP管脚，对应电路器件尽量靠近芯片管脚放置，走线线长尽量短，做立体包地处理，远离其它强干扰信号，如图5-19a，5-19b所示。

<img src="assets/52xB/sf32lb52X-B-SCH-AUDIO-ADC.png" width="80%" align="center" />  

<div align="center"> 图5-19a 模拟音频输入原理图 </div>   <br>  <br>  <br>


<img src="assets/52xB/sf32lb52X-B-PCB-AUDIO-ADC.png" width="80%" align="center" />  

<div align="center"> 图5-19b 模拟音频输入PCB设计 </div>   <br>  <br>  <br>



模拟信号输出DACP/DACN管脚，对应电路器件尽量靠近芯片管脚放置，每一路P/N需要按照差分线形式走线，走线线长尽量短，寄生电容小于10pf，需做立体包地处理，远离其它强干扰信号，如图5-20a，5-20b所示。

<img src="assets/52xB/sf32lb52X-B-SCH-AUDIO-DAC.png" width="80%" align="center" />  

<div align="center"> 图5-20a 模拟音频输出原理图 </div>   <br>  <br>  <br>


<img src="assets/52xB/sf32lb52X-B-PCB-AUDIO-DAC.png" width="80%" align="center" />  

<div align="center"> 图5-20b 模拟音频输出PCB设计 </div>   <br>  <br>  <br>



### USB接口走线

USB走线PA35(USB DP)/PA36(USB_DN) 必须先过ESD器件管脚，然后再到芯片端，要保证ESD器件接地管脚能良好连接主地。走线需按照差分线形式走，并做90欧差分阻抗控制，且做立体包处理，如图5-21a，5-21b所示。


<img src="assets/52xB/sf32lb52X-B-SCH-USB.png" width="80%" align="center" />  

<div align="center"> 5-21a USB信号原理图 </div>   <br>  <br>  <br>


<img src="assets/52xB/sf32lb52X-B-PCB-USB.png" width="80%" align="center" />  

<div align="center"> 5-21b USB信号PCB设计 </div>   <br>  <br>  <br>


图5-22a为USB信号的元件布局参考图，图5-22b为PCB走线模型。


<img src="assets/52xB/sf32lb52X-B-PCB-USB-LAYOUT.png" width="80%" align="center" />  

<div align="center"> 图5-22a USB信号器件布局参考 </div>   <br>  <br>  <br>


<img src="assets/52xB/sf32lb52X-B-PCB-USB-ROUTE.png" width="80%" align="center" />  

<div align="center"> 图5-22b USB信号走线模型 </div>   <br>  <br>  <br>



### SDIO接口走线
SDIO信号走线尽量一起走，避免分开走，整个走线长度≤50mm, 组内长度控制≤6mm。SDIO接口时钟信号需立体包地处理，DATA和CMD信号也需要包地处理，如图5-23a，5-23b所示。

<img src="assets/52xB/sf32lb52X-B-SCH-SDIO.png" width="80%" align="center" />  

<div align="center"> 图5-23a SDIO接口电路图 </div>   <br>  <br>  <br>


<img src="assets/52xB/sf32lb52X-B-PCB-SDIO.png" width="80%" align="center" />  

<div align="center"> 图5-23b SDIO PCB走线模型 </div>   <br>  <br>  <br>



### DCDC电路走线
DC-DC电路功率电感和滤波电容必须靠近芯片的管脚放置。BUCK_LX走线尽量短且粗，保证整个DC-DC电路回路电感小；BUCK_FB管脚反馈线不能太细，必须大于0.25mm。所有的DC-DC输出滤波电容接地脚多打过孔连接到主地平面。功率电感区域表层禁止铺铜，临层必须为完整的参考地，避免其它线从电感区域里走线，如图5-24a，5-24b所示。

<img src="assets/52xB/sf32lb52X-B-SCH-DCDC.png" width="80%" align="center" />  

<div align="center"> 图5-24a DC-DC关键器件电路图 </div>   <br>  <br>  <br>


<img src="assets/52xB/sf32lb52X-B-PCB-DCDC.png" width="80%" align="center" />  

<div align="center"> 图5-24b DC-DC关键器件PCB布局图 </div>   <br>  <br>  <br>



### 电源供电走线

PVDD为芯片内置PMU模块电源输入脚，对应的电容必须靠近管脚放置，走线尽量的粗，不能低于0.4mm，如图5-25所示。

<!-- 这里的内容需要A3和B3做区别处理 -->
<img src="assets/52xB/sf32lb52X-B-PCB-PMU.png" width="80%" align="center" />  

<div align="center"> 图5-25 PVDD电源走线图 </div>  <br> <br> <br>



AVDD33、VDDIOA、VDD_SIP、AVDD33_AUD和AVDD_BRF等管脚滤波电容靠近对应的管脚放置，其走线宽必须满足输入电流要求，走线尽量短粗，从而减少电源纹波提高系统稳定性。

<!-- A3版本需要增加充电部分内容 -->

### 其它接口走线

管脚配置为GPADC 管脚信号，必须要求立体包地处理，远离其它干扰信号，如电池电量电路，温度检查电路等。

### EMI&ESD
- 避免屏蔽罩外面表层长距离走线，特别是时钟、电源等干扰信号尽量走内层，禁止走表层。
- ESD保护器件必须靠近连接器对应管脚放置，信号走线先过ESD保护器件管脚，避免信号分叉，没过ESD保护管脚。
- ESD器件接地脚必须保证过孔连接主地，保证地焊盘走线短且粗，减少阻抗提高ESD器件性能。
- 
### 其它

USB 充电线测试点必须放置在TVS 管前面，电池座TVS 管 放置在平台前面 其走线必须保证先过TVS 然后再到芯片端，如图5-27所示。

<img src="assets/52xA/sf32LB52x-A-SCH-PMU-TVS.png" width="80%" align="center" />  

<div align="center"> 图5-27 电源TVS布局参考 </div>   <br>  <br>  <br>

<img src="assets/52xA/sf32LB52x-A-SCH-PMU-EOS.png" width="80%" align="center" />  

<div align="center"> 图5-28 TVS走线参考 </div>   <br>  <br>  <br>

TVS 管接地脚尽量避免走长线再连接到地，如图5-28所示。

## 相关文档

- [SF32LB52x芯片技术规格书](https://downloads.sifli.com/silicon/DS0052-SF32LB52x-%E8%8A%AF%E7%89%87%E6%8A%80%E6%9C%AF%E8%A7%84%E6%A0%BC%E4%B9%A6%20V2p4.pdf?)
- [SF32LB52x用户手册](https://downloads.sifli.com/silicon/UM0052-SF32LB52x-%E7%94%A8%E6%88%B7%E6%89%8B%E5%86%8C%20V0p3.pdf?)
- [SF32LB52-硬件参考设计包](https://downloads.sifli.com/hardware/files/documentation/SF32LB52-%E7%A1%AC%E4%BB%B6%E5%8F%82%E8%80%83%E8%AE%BE%E8%AE%A1-20250619.zip?)


## 修订历史

```{table}
:align: left
:name: sf32lb52x-B-history

|版本 |日期   |发布说明 |
|:---|:---|:---|
|0.0.1 |10/2024 |初始版本 |

```
