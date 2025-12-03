# SF32LB52-DevKit-LCD开发板使用指南




## 开发板概述


SF32LB52-DevKit-LCD是一款基于SF32LB52x系列芯片模组的开发板，主要用于开发基于`SPI`/`DSPI`/`QSPI`或`MCU/8080`接口显示屏的各种应用。

开发板同时搭载模拟MIC输入，模拟音频输出，SDIO接口，USB-C接口，支持TF卡等，为开发者提供丰富的硬件接口资源，可以用于开发各种接口外设的驱动，帮助开发者简化硬件开发过程和缩短产品的上市时间。

SF32LB52_DevKit-LCD的外形如{numref}`图 {number} <SF32LB52x_DevKit-LCD_Front_Look>`、{numref}`图 {number} <SF32LB52x_DevKit-LCD_Back_Look>`所示。

```{figure} assets/SF32LB52x-DevKit-LCD_Front_Look.png

:scale: 20%
:name: SF32LB52x_DevKit-LCD_Front_Look
SF32LB52x_DevKit-LCD开发板实物正面照
```

```{figure} assets/SF32LB52x_DevKit-LCD_Back_Look.png

:scale: 20%
:name: SF32LB52x_DevKit-LCD_Back_Look
SF32LB52x_DevKit-LCD开发板实物背面照
```
### 特性列表
该开发板具有以下特性：
1.	模组：板载基于SF32LB52x芯片的SF32LB52x-MOD-N16R8模组，模组配置如下：
    - 标配SF32LB525UC6芯片，内置合封配置为：
        - 8MB OPI-PSRAM，接口频率144MHz（正式发布可能会改变）
    - 128Mb QSPI-NOR Flash，接口频率72MHz，STR模式（正式发布可能会改变）
    - 48MHz晶体
    - 32.768KHz晶体
    - 板载天线，或IPEX天线座，通过0欧电阻选择，默认为板载天线
    - 射频匹配网络及其它阻容感器件
2.	专用屏幕接口
    - SPI/DSPI/QSPI，支持DDR模式QSPI，通过22pin FPC和40pin排针引出
    - 8bit MCU/8080，通过22pin FPC和40pin排针引出
     - 支持I2C接口的触摸屏
3.	音频
    - 支持模拟MIC输入
    - 模拟音频输出，板载Class-D音频PA
4.	USB
    - Type C接口，支持板载USB转串口芯片，实现程序下载和软件DEBUG，可供电
    - Type C接口，支持USB2.0 FS，可供电
5.	SD卡
    - 支持采用SPI接口的TF卡，板载Micro SD卡插槽


### 功能框图

```{figure} assets/SF32LB52x_DevKit-LCD_Block_Diagram.png

:scale: 110%
开发板功能框图
```
### 组件介绍

SF32LB52-DevKit-LCD开发板的主板是整个套件的核心，该主板集成了SF32LB52-MOD-N16R8模组，并提供QSPI和MUC8的LCD连接座

```{figure} assets/52KIT-LCD-T-Notes.png

:scale: 70%
SF32LB52-DevKit-LCD Board - 正面（点击放大）
```

```{figure} assets/52KIT-LCD-B-Notes.png

:scale: 70%
SF32LB52-DevKit-LCD Board - 背面（点击放大）
```


## 应用程序开发

本节主要介绍硬件和软件的设置方法，以及烧录固件至开发板以及开发应用程序的说明。

### 必备硬件

- 1 x SF32LB52-DevKit-LCD（含SF32-LB52X-MOD模组）
- 1 x LCD模组
- 1 x USB2.0数据线（标准A型转Type-C型）
- 1 x电脑（Windows、Linux或macOS）

```{note}

1. 如果需要既通过UART调试，也要使用USB接口，需要两根USB2.0数据线；
2. 请确保使用适当的USB数据线，部分数据线仅可用于充电，无法用于数据传输和程序烧录。

```
### 可选硬件

- 1 x扬声器
- 1 x TF Card
- 1 x 大于450mAh锂电池

### 硬件设置

准备好开发板，加载第一个示例应用程序：

1.	连接屏幕模组至相应的LCD连接器接口；
2.	打开思澈的SifliTrace工具软件，选择正确的COM口；
3.	插入USB数据线，分别连接PC与开发板的USB to UART端口；
4.	LCD屏幕亮起，可以用手指与触摸屏进行交互。

硬件设置完成，接下来可以进行软件设置。


### 软件设置

SF32LB52-DevKit-LCD的开发板，如何快速设置开发环境，请参考软件相关文档。 

## 硬件参考

本节提供关于开发板硬件的更多信息。

### GPIO分配列表

下表为 SF32LB52-MOD-N16R8 模组管脚的 GPIO 分配列表，用于控制开发板的特定组件或功能。

```{table} SF32LB52-MOD-N16R8 GPIO分配

:name: SF32LB52-MOD-N16R8-GPIO-LIST

|管脚|	管脚名称           	   |   功能  |
|:--|:-----------------------|:-----------|
|1 | GND   | 接地                     |
|2 | PA_44 | VBUS_DET，充电器插入检测   |
|3 | PA_43 | MCU 8080 DB7，LCD接口信号 |
|4 | PA_42 | MCU 8080 DB6，LCD接口信号 |
|5 | PA_23 | XTAL32K_XO，默认NC       |
|6 | PA_22 | XTAL32K_XI，默认NC       |
|7 | PA_41 | MCU 8080 DB5，LCD接口信号 |
|8 | PA_40 | MCU 8080 DB4，LCD接口信号 |
|9 | PA_39 | MCU 8080 DB3，LCD接口信号 |
|10 | PA_38 | GPIO                    |
|11 | PA_37 | MCU 8080 DB2，LCD接口信号 |
|12 | PA_36 | USB_DM                  |
|13 | PA_35 | USB_DP                  |
|14 | PA_34 | HOME和长按复位按键        |
|15 | PA_33 | 触摸屏I2C_SDA            |
|16 | PA_32 | RGB LED                 |
|17 | VDD33_VOUT2/AVDD33 | SF32LB-MOD-1模组时3.3V电源输出（默认无输出，需要软件配置后才有输出），SF32LB-MOD-A/B时3.3V电源输入  |
|18 | PA_24 | SPI1_DIO，SD卡接口信号    |
|19 | PA_25 | SPI1_DI，SD卡接口信号     |
|20 | PA_26 | SD卡_CD信号，LED          |
|21 | PA_27 | UART_TXD                |
|22 | PA_28 | SPI1_CLK，SD卡接口信号    |
|23 | PA_29 | SPI1_CS，SD卡接口信号     |
|24 | PA_30 | 触摸屏I2C_SCL            |
|25 | PA_31 | 触摸屏中断INT             |
|26 | GND | 接地                       |
|27 | VBAT  | SF32LB-MOD-1模组时3.2~4.7V电源输入，SF32LB-MOD-A/B时3.3V电源输入     |
|28 | PA_20 | UART_RXD                |
|29 | PA_19 | DB_UART_TXD, 程序下载及软件调试接口 |
|30 | PA_18 | DB_UART_RXD, 程序下载及软件调试接口 |
|31 | PA_11 | KEY，功能按键             |
|32 | PA_10 | AU_PA_EN，音频功放控制信号 |
|33 | AU_DAC1P_OUT | 模拟音频输出信号    |
|34 | AU_DAC1N_OUT | 模拟音频输出信号    |
|35 | GND | 接地                       |
|36 | MIC_BIAS | MIC偏置电压            |
|37 | MIC_ADC_IN | MIC输入信号          |
|38 | PA_09 | 触摸屏中断RST             |
|39 | PA_08 | MCU 8080 DB1，QSPI D3，LCD接口信号 |
|40 | PA_07 | MCU 8080 DB0，QSPI D2，LCD接口信号 |
|41 | PA_06 | MCU 8080 DC，QSPI D1，E-Paper DC，LCD接口信号 |
|42 | PA_05 | MCU 8080 RD，QSPI D0，E-Paper SDI，LCD接口信号 |
|43 | PA_04 | MCU 8080 WR，QSPI CLK，E-Paper SCLK，LCD接口信号 |
|44 | PA_03 | MCU 8080 CS，QSPI CS，E-Paper CS，LCD接口信号 |
|45 | PA_02 | MCU 8080 TE，QSPI TE，E-Paper BUSY，LCD接口信号 |
|46 | PA_01 | BL PWM，LCD接口信号      |
|47 | PA_00 | RSTB，LCD接口信号        |
|48 | GND | 接地                      |
|49 | GND | 接地                      |
|50 | GND | 接地                      |
|51 | GND | 接地                      |
|52 | GND | 接地                      |
|53 | GND | 接地                      |
|54 | GND | 接地                      |
|55 | GND | 接地                      |
|56 | GND | 接地                      |
|57 | GND | 接地                      |
|58 | GND | 接地                      |
|58 | GND | 接地                      |
|60 | GND | 接地                      |
|61 | VBATS | 电池电压检测输入          |
|62 | PA_21 | GPIO，只有SF32LB52-MOD-A/B上才有此信号        |
|63 | PA_15 | MPI2_D0，SD1_CMD        |
|64 | PA_16 | MPI2_CLK，SD1_D0        |
|65 | PA_17 | MPI2_D3，SD1_D1         |
|66 | PA_14 | MPI2_D2，SD1_CLK        |
|67 | PA_13 | MPI2_D1，SD1_D3         |
|68 | PA_12 | MPI2_CS，SD1_D2         |

```

```{important}
1. SF32LB52-DevKit-LCD适配SF32LB-MOD-1，SF32LB-MOD-A和SF32LB-MOD-B共三种模组。
2. 模组17管脚VDD33_VOUT2/AVDD33，SF32LB-MOD-1模组时3.3V电源输出（默认无输出，需要软件配置后才有输出），SF32LB-MOD-A/B时3.3V电源输入。
3. 模组27管脚VBAT，SF32LB-MOD-1模组时3.2~4.7V电源输入，SF32LB-MOD-A/B时3.3V电源输入。
4. SF32LB-MOD-1模组的VBAT电源的开机阈值设置为3.58V，关机阈值设置为3.48V。非电池类供电应用，推荐VBAT供3.8V电压。
5. 模组62管脚PA21只有SF32LB52-MOD-A/B支持，SF32LB-MOD-1为NC。
6. 模组62~68管脚默认为模组内部连接Nor Flash，开发板无法使用；若要使用SDIO接口，请选择无flash版本的模组。
```

### 40P排针接口定义

```{figure} assets/SF32LB52x_DevKit-40p-define.png

:scale: 10%
:name: SF32LB52x_DevKit-40p-define
开发板40p排针接口定义（点击放大）
```
### 22p QSPI线序FPC接口定义


```{table} QSPI-FPC-J0102 信号定义
:name: QSPI-FPC-J0102-GPIO-LIST

|管脚|	管脚名称           	   |   功能  |
|:--|:-----------------------|:-----------|
|1  | LEDK    | LCD屏背光二极管阴极                     
|2  | LEDA    | LCD屏背光二极管阳极    
|3  | PA_07   | MIPI-DBI(8080) B0，QSPI D2，LCD接口信号 
|4  | PA_08   | MIPI-DBI(8080) B1，QSPI D3，LCD接口信号 
|5  | PA_37   | MIPI-DBI(8080) B2，LCD接口信号 
|6  | PA_39   | MIPI-DBI(8080) B3，LCD接口信号 
|7  | PA_40   | MIPI-DBI(8080) B4，LCD接口信号 
|8  | PA_41   | MIPI-DBI(8080) B5，LCD接口信号  
|9  | PA_42   | MIPI-DBI(8080) B6，LCD接口信号 
|10 | PA_43   | MIPI-DBI(8080) B7，LCD接口信号                 
|11 | PA_02   | MIPI-DBI(8080) TE，QSPI TE，LCD接口信号                   
|12 | PA_00   | LCD Reset，LCD接口信号 
|13 | PA_04   | MIPI-DBI(8080) WRx，QSPI CLK，SPI CLK，LCD接口信号 
|14 | PA_05   | MIPI-DBI(8080) RDx，QSPI D0，SPI SDI，LCD接口信号         
|15 | PA_03   | MIPI-DBI(8080) CSx，QSPI CS，SPI CS，LCD接口信号             
|16 | PA_06   | MIPI-DBI(8080) DCx，QSPI D1，SPI DC，LCD接口信号 
|17 | VDD_3V3 | 3.3V电源输出 
|18 | PA_31   | 触摸屏INT中断信号
|19 | PA_33   | 触摸屏I2C_SDA信号 
|20 | PA_30   | 触摸屏I2C_SCL信号 
|21 | PA_09   | 触摸屏RTN复位信号 
|22 | GND     | 接地      

```

### 供电说明

SF32LB52-DevKit-LCD开发板有2种供电方式：USB Type-C和电池供电。

1.  板上2个USB Type-C接口都可以给板子供电，下载和调试时，请用 USB-to-UART 端口。
2.  可以电池单独供电，便于脱离电脑独立运行。

### 硬件设置选项

通过USB-to-UART端口连上USB线，打开思澈科技的程序下载工具，选取相应的COM口和程序。
1.  下载模式
- 勾选BOOT项，上电，开机后进入下载模式，就可以完成程序的下载。
2.  软件开发模式
- 去掉BOOT项，上电，开机后进入串口log打印模式，便进入软件调试模式。

**具体请参考&emsp;[固件烧录工具 Impeller](烧录工具)**

### 充电及电池选型

SF32LB52-DevKit-LCD开发板集成了ETA9640P 线性充电芯片，最大支持1A充电电流，默认设置为450mA恒流电流。

电池推荐选取450mAh~500mAh单芯聚合物锂电池，电池接口为2.0mm HDR母座，极性请参考开发板上电池座丝印。

### LCD显示屏接口

SF32LB52-DevKit-LCD开发板支持QSPI接口LCD屏，接插件为22p-0.5pitch FPC，上翻下接触。
信号线序请参考上文定义，线序不同需要做转接板测试，请参考《SF32LB52-DevKit-LCD转接板制作指南》。
* 已支持屏型号：[TFT-H043A28WQISTKN22_V0-3](鑫洪泰)

### 音频接口

SF32LB52-DevKit-LCD开发板集成MEMS MIC和音频功放芯片。
* 支持板上mic的音频信号输入。
* 支持外接喇叭（最大支持3W/4欧姆），喇叭接插件规格（2.0mm 间距 HDR母座）。

## 样品获取

零售样品与小批量可直接在[淘宝](https://sifli.taobao.com/)购买，批量客户可发邮件到sales@sifli.com或淘宝找客服获取销售联系方式。
参与开源可以免费申请样品，可加入QQ群674699679进行交流。

## 相关文档

- [SF32LB52x芯片技术规格书](https://wiki.sifli.com/silicon/index.html)
- [SF32LB52x用户手册](https://wiki.sifli.com/silicon/index.html)
- [SF32LB52-MOD-1技术规格书](https://wiki.sifli.com/silicon/index.html)
- [SF32LB52-MOD-1设计图纸](https://downloads.sifli.com/hardware/files/documentation/SF32LB52-MOD-1-V1.0.0.zip?)
- [SF32LB52-DevKit-LCD设计图纸](https://downloads.sifli.com/hardware/files/documentation/SF32LB52-DevKit-LCD_V1.2.0.zip?)
- [SF32LB52-DevKit-LCD转接板制作指南](SF32LB52-DevKit-LCD-Adapter)



## 开发板版本信息：

* V1.2.0：采用SF32LB52-MOD-1/A/B模组，即将推出SF32LB52-MOD-1(SF32LB525UC6)
```{table} 
|序号 | V1.2.0更新内容 |
|:-- |:------ |
|1 | 修改SD卡拔插检查信号输入管脚，改用PA26，和外部Flash2 片选，GPIO LED共用一个IO。   
```
* V1.1.0：采用SF32LB52-MOD-A/B模组，目前实物有(-A:SF32LB52BU36和-B:SF32LB52EUB6)
```{table} 
|序号 | V1.1.0更新内容 |
|:-- |:------ |
|1 | 更新充电芯片原理图库，解决充电芯片5V输出不对的问题。   
|2 | 去掉MOS管VBUS和VBAT切换电路，后级电路全部由充电芯片的5V输出供电，解决VBUS和VBAT切换不正常问题。 
|3 | 调整音频PA的放大倍数。
|4 | 解决Reset按键异常的问题。 
|5 | 去掉RGBLED电路里的电平转换部分，该电路不满足RGBLED的时序。
|6 | 升级了模组的管脚定义，新增2个IO，解决-1模组和-A/B模组兼容问题。
|7 | 更新电源部分，-A/B的AVDD改为LDO供电，解决原DCDC输出纹波大导致RF灵敏度问题。
|8 | 增加对双flash的支持。
|9 | 增加SD卡的插拔检查功能，只有-A/B支持该功能。
|10 | 增加SDIO WiFi功能选项，只有-A支持该功能。
|11 | 修改定位孔类型，天线背面PCB挖槽。
|12 | 修改了VBUS输入的EOS保护器件接入位置点。
```
* V1.0.0：采用SF32LB52-MOD模组，当前版本
