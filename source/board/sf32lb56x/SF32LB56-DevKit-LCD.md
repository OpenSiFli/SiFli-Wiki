# SF32LB56-DevKit-LCD开发板使用指南


## 开发板概述


SF32LB56-DevKit-LCD是一款基于SF32LB56xV系列芯片模组的开发板，主要用于开发基于`MIPI-DPI`/`SPI`/`DSPI`/`QSPI`或`MIPI-DBI(MCU/8080)`接口显示屏的各种应用。

开发板同时搭载模拟MIC输入，模拟音频输出，SDIO接口，USB-C接口，支持TF卡等，为开发者提供丰富的硬件接口资源，可以用于开发各种接口外设的驱动，帮助开发者简化硬件开发过程和缩短产品的上市时间。

SF32LB56_DevKit-LCD的外形如图1，图2所示。

<img src="assets/SF32LB56x-DevKit-LCD_Front_Look.png" width="30%" align="center" />

<div align="center"> 图1 SF32LB56_DevKit-LCD开发板实物正面照 </div>  <br> <br> <br> 


<img src="assets/SF32LB56x_DevKit-LCD_Back_Look.png" width="30%" align="center" /> 

<div align="center"> 图2 SF32LB56_DevKit-LCD开发板实物背面照 </div>  <br> <br> <br> 


### 特性列表
该开发板具有以下特性：
1.	模组：板载基于SF32LB56xV芯片的SF32LB56-MOD-A128R12N1模组，模组配置如下：
    - 标配SF32LB566VCB36芯片，内置合封配置为：
        - 8MB OPI-PSRAM，接口频率144MHz（正式发布可能会改变）
        - 4MB OPI-PSRAM，接口频率144MHz（正式发布可能会改变）
    - 1Gb QSPI-Nand Flash，接口频率72MHz，STR模式（正式发布可能会改变）
    - 48MHz晶体
    - 32.768KHz晶体
    - 板载天线，或IPEX天线座，通过0欧电阻选择，默认为板载天线
    - 射频匹配网络及其它阻容感器件
2.	专用屏幕接口
    - MIPI-DPI，支持正点原子40pin线序FPC连接器
    - SPI/DSPI/QSPI，支持DDR模式QSPI，通过40pin排针引出
    - 8bit MCU/8080，通过40pin排针引出
     - 支持I2C接口的触摸屏
3.	音频
    - 支持模拟MIC输入
    - 模拟音频输出，板载Class-D音频PA
4.	USB
    - Type C接口，支持板载USB转串口芯片，实现程序下载和软件DEBUG，可供电
    - Type C接口，支持USB2.0 FS，可供电
5.	SD卡
    - 支持采用SDIO接口的TF卡，板载Micro SD卡插槽


### 功能框图

<img src="assets/SF32LB56x_DevKit-LCD_Block_Diagram.png" width="80%" align="center" /> 

<div align="center"> 图3 开发板功能框图 </div>  <br> <br> <br> 


### 组件介绍

SF32LB56-DevKit-LCD开发板的主板是整个套件的核心，该主板集成了SF32LB56-MOD-A128R12N1模组，并提供MIPI-DPI（RGB-24bit）的LCD连接座

<img src="assets/56KIT-LCD-T-Notes.png" width="80%" align="center" /> 

<div align="center"> 图3 SF32LB56-DevKit-LCD Board - 正面（点击放大） </div>  <br> <br> <br> 

<img src="assets/56KIT-LCD-B-Notes.png" width="80%" align="center" /> 

<div align="center"> 图4 SF32LB56-DevKit-LCD Board - 背面（点击放大） </div>  <br> <br> <br> 


## 应用程序开发

本节主要介绍硬件和软件的设置方法，以及烧录固件至开发板以及开发应用程序的说明。

### 必备硬件

- 1 x SF32LB56-DevKit-LCD（含SF32LB56-MOD-A128R12N1模组）
- 1 x 屏幕模组
- 1 x USB2.0数据线（标准A型转Type-C型）
- 1 x SWD调试器
- 1 x电脑（Windows、Linux或macOS）

```{note}

1. 如果需要既通过UART调试，也要使用USB接口，需要两根USB2.0数据线；
2. 请确保使用适当的USB数据线，部分数据线仅可用于充电，无法用于数据传输和程序烧录。

```
### 可选硬件

- 1 x 扬声器
- 1 x TF Card
- 1 x 450mAh锂电池

### 硬件设置

准备好开发板，加载第一个示例应用程序：

1.	连接屏幕模组至相应的LCD连接器接口；
2.	打开思澈的SifliTrace工具软件，选择正确的COM口；
3.	插入USB数据线，分别连接PC与开发板的USB to UART端口；
4.	屏幕亮起，可以用手指与触摸屏进行交互。

硬件设置完成，接下来可以进行软件设置。


### 软件设置

SF32LB56-DevKit-LCD的开发板，如何快速设置开发环境，请参考软件相关文档。 

## 硬件参考

本节提供关于开发板硬件的更多信息。

### GPIO分配列表

下表为 SF32LB56-MOD-A128R12N1 模组管脚的 GPIO 分配列表，用于控制开发板的特定组件或功能。

<div align="center"> SF32LB56-MOD-A128R12N1 GPIO分配 </div>

```{table}
:align: center
|管脚|	管脚名称           	   |   功能  |
|:--|:-----------------------|:-----------|
|1  | GND   | 接地                     |
|2  | PB_22 | 触摸屏复位信号             |
|3  | PA_47 | MIPI-DPI(RGB) DE，LCD接口信号 |
|4  | PA_42 | MIPI-DPI(RGB) VSYNC，LCD接口信号 |
|5  | PA_44 | MIPI-DPI(RGB) HSYNC，LCD接口信号 |
|6  | PB_17 | UART4_TXD, BOOTROM默认打印口及小核软件调试接口 |
|7  | PB_16 | UART4_RXD, BOOTROM默认打印口及小核软件调试接口 |
|8  | PA_45 | MIPI-DPI(RGB) CLK，LCD接口信号 |
|9  | PA_46 | MIPI-DPI(RGB) B7，LCD接口信号 |
|10 | PA_18 | USB_DM                  |
|11 | PA_17 | USB_DP                  |
|12 | PA_40 | MIPI-DPI(RGB) B6，MCU 8080 DIO0，QSPI DIO2，E-Paper SDI，LCD接口信号 |
|13 | PA_39 | MIPI-DPI(RGB) B5，MCU 8080 DC，QSPI DIO1，E-Paper DC，LCD接口信号 |
|14 | PB_32 | HOME和长按复位按键        |
|15 | PA_51 | 触摸屏中断INT             |
|16 | PA_41 | MIPI-DPI(RGB) B4，MCU 8080 DIO1，QSPI DIO3，LCD接口信号 |
|17 | PA_43 | MIPI-DPI(RGB) B3，LCD接口信号 |
|18 | PA_38 | MIPI-DPI(RGB) B2，MCU 8080 RD，QSPI DIO0，LCD接口信号 |
|19 | PA_37 | MIPI-DPI(RGB) B1，MCU 8080 WR，QSPI CLK，E-Paper CLK，LCD接口信号 |
|20 | PA_36 | MIPI-DPI(RGB) B0，MCU 8080 CS，QSPI CS，E-Paper CS，LCD接口信号 |
|21 | PA_35 | MIPI-DPI(RGB) G7，LCD接口信号 |
|22 | PA_31 | MIPI-DPI(RGB) G6，MCU 8080 DIO5，LCD接口信号 |
|23 | PA_29 | MIPI-DPI(RGB) G5，MCU 8080 DIO3，LCD接口信号 |
|24 | PA_34 | MIPI-DPI(RGB) G4，MCU 8080 DIO7，LCD接口信号 |
|25 | BOOT_MODE | BOOT_MODE信号，=1下载模式；=0用户程序模式  |
|26 | VDD   | 主电源输入，2.97~3.63V     |
|27 | VDDSIP| 合封存储器电源输入，1.71~1.92V  |
|28 | GND   | 接地                     |
|29 | VDDIO | GPIO电源输入，1.71~3.63V  |
|30 | PA_01 | 触摸屏I2C_SCL            |
|31 | PA_02 | 触摸屏I2C_SDA            |
|32 | PA_03 | UART1_TXD,大核调试串口    |
|33 | PA_04 | UART1_RXD,大核调试串口    |
|34 | PA_15 | SD1_DIO1，SD卡接口信号    |
|35 | PA_22 | SD1_DIO0，SD卡接口信号    |
|36 | PA_27 | SD1_CMD， SD卡接口信号    |
|37 | PA_26 | SD1_CLK， SD卡接口信号    |
|38 | PA_20 | SD1_DIO3，SD卡接口信号    |
|39 | PA_12 | SD1_DIO2，SD卡接口信号    |
|40 | PA_33 | MIPI-DPI(RGB) G3，MCU 8080 TE，QSPI TE，E-Paper BUSY，LCD接口信号 |
|41 | PA_32 | MIPI-DPI(RGB) G2，MCU 8080 DIO6，LCD接口信号 |
|42 | GND   | 接地                     |
|43 | AU_DAC1P_OUT | 模拟音频输出信号    |
|44 | AU_DAC1N_OUT | 模拟音频输出信号    |
|45 | GND   | 接地                     |
|46 | MIC_BIAS | MIC偏置电压            |
|47 | MIC_ADC_IN | MIC输入信号          |
|48 | PA_50 | RSTB，LCD接口信号         |
|49 | PA_30 | MIPI-DPI(RGB) G1，MCU 8080 DIO4，LCD接口信号 |
|50 | PA_28 | MIPI-DPI(RGB) G0，MCU 8080 DIO2，LCD接口信号 |
|51 | PA_25 | MIPI-DPI(RGB) R7，LCD接口信号 |
|52 | PA_23 | MIPI-DPI(RGB) R6，LCD接口信号 |
|53 | PA_21 | MIPI-DPI(RGB) R5，LCD接口信号 |
|54 | PA_19 | MIPI-DPI(RGB) R4，LCD接口信号 |
|55 | PA_24 | MIPI-DPI(RGB) R3，LCD接口信号 |
|56 | PA_16 | MIPI-DPI(RGB) R2，LCD接口信号 |
|57 | PA_13 | MIPI-DPI(RGB) R1，LCD接口信号 |
|58 | PA_14 | MIPI-DPI(RGB) R0，LCD接口信号 |
|59 | PB_23 | BL PWM，LCD接口信号      |
|60 | GND   | 接地                    |
|61 | PB_12 | VBUS_DET，USB插拔检测    |
|62 | PB_11 | GPIO LED控制信号         |
|63 | PB_09 | RGBLED的GPIO控制信号     |
|64 | PB_08 | GPIO                   |
|65 | PB_35 | KEY，功能按键            |
|66 | PA_76 | SD卡座的插入检测接口信号   |
|67 | PA_06 | MPI3_CS，SD2_DIO2，I2S1_MCLK，模组内部Nor Flash接口信号，模组内部支持Nor Flash时，外部不可用 |
|68 | PA_07 | MPI3_DIO1，SD2_DIO3，I2S1_SDI，模组内部Nor Flash接口信号，模组内部支持Nor Flash时，外部不可用 |
|69 | PA_08 | MPI3_DIO2，SD2_CLK，I2S1_SDO，模组内部Nor Flash接口信号，模组内部支持Nor Flash时，外部不可用 |
|70 | PA_09 | MPI3_DIO0，SD2_CMD，I2S1_BCK，模组内部Nor Flash接口信号，模组内部支持Nor Flash时，外部不可用 |
|71 | PA_10 | MPI3_CLK，SD2_DIO0，I2S1_LRCK，模组内部Nor Flash接口信号，模组内部支持Nor Flash时，外部不可用 |
|72 | PA_11 | MPI3_DIO3，SD2_DIO1，模组内部Nor Flash接口信号，模组内部支持Nor Flash时，外部不可用 |
|73 | GND | 接地                      |
|74 | GND | 接地                      |
|76 | GND | 接地                      |
|77 | GND | 接地                      |
|78 | GND | 接地                      |
|79 | PB_13 | SWDIO，SWD接口信号       |
|80 | PB_15 | SWCLK，SWD接口信号       |
|81 | PB_18 | SPI3_CS， RGB屏SPI接口，WIFI的GPIO接口信号  |
|82 | PB_19 | SPI3_CLK，RGB屏SPI接口，WIFI的GPIO接口信号  |
|83 | PB_20 | SPI3_DI， 用作音频功放的GPIO使能信号         |
|84 | PB_21 | SPI3_DO， RGB屏SPI接口，WIFI的GPIO接口信号  |
|85 | PA_69 | SPI2_DI， I2S1_SDI， PDM1_CLK， 用作WIFI的SPI接口信号   |
|86 | PA_64 | SPI2_DO， I2S1_SDO， PDM1_DAT， 用作WIFI的SPI接口信号   |
|87 | PA_73 | SPI2_CLK，I2S1_BCK， PDM2_CLK， 用作WIFI的SPI接口信号   |
|88 | PA_71 | SPI2_CS， I2S1_LRCK，PDM2_DAT， 用作WIFI的SPI接口信号   |
|89 | PA_65 | GPIO，I2S1_MCLK         |
```

### 40P排针接口定义


<img src="assets/SF32LB56x_DevKit-40p-define.svg" width="100%" align="center" /> 

<div align="center"> 图5 开发板40p排针接口定义（点击放大） </div>  <br> <br> <br> 


### 40p RGB线序FPC接口定义

**兼容正点原子40pin线序FPC接口**

<div align="center"> RGB-FPC-J0100 信号定义 </div>

```{table}
:align: center
|管脚|	管脚名称           	   |   功能  |
|:--|:-----------------------|:-----------|
|1   | 5V       | 5V电源输出                 
|2   | 5V       | 5V电源输出   
|3   | R0       | PA_14，LCDC1_DPI_R0  &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp;  
|4   | R1       | PA_13，LCDC1_DPI_R1        
|5   | R2       | PA_16，LCDC1_DPI_R2    
|6   | R3       | PA_24，LCDC1_DPI_R3    
|7   | R4       | PA_19，LCDC1_DPI_R4    
|8   | R5       | PA_21，LCDC1_DPI_R5    
|9   | R6       | PA_23，LCDC1_DPI_R6    
|10  | R7       | PA_25，LCDC1_DPI_R7    
|11  | GND      | 接地  
|12  | G0       | PA_28，LCDC1_DPI_G0 
|13  | G1       | PA_30，LCDC1_DPI_G1                
|14  | G2       | PA_32，LCDC1_DPI_G2         
|15  | G3       | PA_33，LCDC1_DPI_G3       
|16  | G4       | PA_34，LCDC1_DPI_G4                 
|17  | G5       | PA_29，LCDC1_DPI_G5       
|18  | G6       | PA_31，LCDC1_DPI_G6    
|19  | G7       | PA_35，LCDC1_DPI_G7    
|20  | GND      | 接地      
|21  | B0       | PA_36，LCDC1_DPI_B0       
|22  | B1       | PA_37，LCDC1_DPI_B1       
|23  | B2       | PA_38，LCDC1_DPI_B2       
|24  | B3       | PA_43，LCDC1_DPI_B3       
|25  | B4       | PA_41，LCDC1_DPI_B4       
|26  | B5       | PA_39，LCDC1_DPI_B5       
|27  | B6       | PA_40，LCDC1_DPI_B6       
|28  | B7       | PA_46，LCDC1_DPI_B7       
|29  | GND      | 接地       
|30  | CLK      | PA_45，LCDC1_DPI_CLK        
|31  | HSYNC    | PA_44，LCDC1_DPI_HSYNC       
|32  | VSYNC    | PA_42，LCDC1_DPI_VSYNC       
|33  | DE       | PA_47，LCDC1_DPI_DE       
|34  | BL       | PB_23，BL_PWM       
|35  | CTP_RST  | PB_22       
|36  | CTP_SDA  | PA_02，I2C4_SDA       
|37  | NC       | -       
|38  | CTP_SCL  | PA_01，I2C4_SCL       
|39  | CTP_INT  | PA_51       
|40  | RESET    | PA_50            
```

### 供电说明

SF32LB56-DevKit-LCD开发板通过USB Type-C接口供电，板上2个USB Type-C接口都可以给板子供电，下载和调试时，请用 USB-to-UART 端口。

### 烧录测试固件

#### 固件烧录工具 Impeller 下载
通过USB-to-UART端口连上USB线，打开思澈科技的程序下载工具，选取相应的COM口和程序。
1.  下载模式
- 插上Mode跳线帽，上电，开机后进入下载模式，就可以完成程序的下载。
2.  软件开发模式
- 去掉Mode跳线帽，上电，开机后进入串口log打印模式，便进入软件调试模式。

**具体请参考&emsp;[固件烧录工具 Impeller](/tools/烧录工具)**

#### Jlink SWD工具下载和调试

如下面两图所示，用杜邦线把对应的IO连接起来。

<img src="assets/56KIT-JLINK.png" width="80%" align="center" /> 

<div align="center"> 图6 SF32LB56-DevKit-LCD SWD调试接线图 </div>  <br> <br> <br> 



## 样品获取

零售样品与小批量可直接在[淘宝](https://sifli.taobao.com/)购买，批量客户可发邮件到sales@sifli.com或淘宝找客服获取销售联系方式。
参与开源可以免费申请样品，可加入QQ群674699679进行交流。

## 相关文档

- [SF32LB56x芯片技术规格书](https://wiki.sifli.com/silicon/index.html)
- [SF32LB56x用户手册](https://wiki.sifli.com/silicon/index.html)
- [SF32LB56-MOD技术规格书](https://wiki.sifli.com/silicon/index.html)
- [SF32LB56-MOD设计图纸](https://downloads.sifli.com/hardware/files/documentation/SF32LB56-MOD-V1.2.0.zip)
- [SF32LB56-DevKit-LCD设计图纸](https://downloads.sifli.com/hardware/files/documentation/SF32LB56-DevKit-LCD_V1.1.0.zip)

