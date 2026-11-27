# SF32LB57-DevKit-Core-3p3开发板使用指南

## 开发板版本信息：

* *-N1-V1.0.0：配置SF32LB57ZUN3N6芯片（内部合封1MB NOR Flash）
* *-N16-V1.0.0：配置SF32LB57ZUN7N6芯片（内部合封16MB NOR Flash）

## 1. 开发板概述

SF32LB57-DevKit-Core-3p3是基于思澈科技SF32LB57ZUN3N6或SF32LB57ZUN7N6芯片的开发板，尺寸为30.88mm*68mm。板边排针采用蛇形孔设计，可免焊接插接使用。开发板支持GPIO、UART、I2C、SPI、LCD、I2S、GPADC、PWM和模拟音频输入输出。

```{image} assets/SF32LB57-DevKit-Core-3p3-Front_look.png
:width: 20%
:align: center
```

<div align="center"> 开发板实物正面照 </div>  <br>  <br>  <br>

```{image} assets/SF32LB57-DevKit-Core-3p3-Back_look.png
:width: 20%
:align: center
```

<div align="center"> 开发板实物背面照 </div>  <br>  <br>  <br>

## 2. 特性列表

该开发板具有以下特性：

1. 板型：
    - -N1：板载SF32LB57ZUN3N6芯片，配置如下：

        - 合封配置为：
            - 1MB NOR Flash，接口频率72MHz

    - -N16：板载SF32LB57ZUN7N6芯片，配置如下：

        - 合封配置为：
            - 16MB NOR Flash
2. 晶体
    - 48MHz晶体
    - 32.768KHz晶体
3. 天线
    - 板载PCBA天线
    - 板子I-PEX天线座
4. GPIO
    - 支持37个GPIO
5. UART-I2C-GPTIM
    - 3x UART
    - 4x I2C
    - 2x GPTIM
    - 57系列GPIO采用矩阵路由，通用外设信号可按芯片Pinmux配置分配到GPIO；具体复用以HKB知识库《SF32LB57 引脚复用矩阵》为准
6. SPI
    - 2x SPI
7. GPADC
    - 6x GPADC
8. 显示
    - FPC16P，0.5mm间距接插件扩展显示
    - SPI/DSPI/Quad SPI，支持DDR模式QSPI显示接口
    - 支持I2C接口的触摸屏
    - 通过16p排线，支持**1.85inch AMOLED Module**显示屏
9. 音频
    - 支持音频ADC输入，可以接模拟麦克风或硅麦克风
    - 支持PDM数字麦克风输入
    - 模拟音频输出，需要外接Class-AB/D音频PA来驱动喇叭
10. USB
    - Type C-UART接口，板载CH343P串口芯片，实现程序下载和软件DEBUG，可供电
    - USB接口，支持USB2.0 FS，通过排针引出
11. 按键
    - 1x 功能按键
    - 1x 开关机按键，支持长按10s复位功能
12. LED灯
    - 1x WS2812B-2020-V6 RGB LED，由PA32控制
13. 电源
    - 通过USB Type-C接口供电
    - 板载VBUS 5V转3.3V的LDO芯片（ETA5055V330DS2F）
    - CH343P的RTS#信号用于MCU复位控制
    - 支持跳线配置1.8V或3.3V给MCU供电
    - 支持通过跳线选择外部存储器类型，并可串接电流表测试电源电流
    - 支持单MCU功耗测试，最小系统功耗测试，整板功耗测试

## 3. 管脚定义

```{image} assets/SF32LB57-DevKit-Core-3p3-T-pinout.svg
:width: 100%
:align: center
```

<div align="center"> 开发板Pinout（点击放大） </div>  <br>  <br>  <br>

### 管脚详细描述

下表为 SF32LB57-DevKit-Core-3p3 开发板管脚的详细描述。

表中列出的专用复用功能依据HKB知识库《SF32LB57 引脚复用矩阵》。SF32LB57采用矩阵路由，UART、I2C、SPI、CAN、定时器、PWM、I2S、PDM、LCDC和DCMI等矩阵信号可路由到GPIO；各引脚的专用复用及模拟/唤醒功能见下表和HKB Pinmux。

<div align="center"> LEFT PIN（J1）管脚描述表 </div>

```{table}
:align: center
:width: 100%
:widths: 10 16 64 10
:class: devkit-pin-table

|管脚|管脚名称|复位默认及复用功能|上下拉|
|:--|:-----------------------|:-----------|------|
|1  | GND   | 接地                     |  |
|2  | PA_44 | **PA44**、SWDIO（HKB Pinmux）                         | PD |
|3  | PA_43 | **PA43**、SWCLK（HKB Pinmux）                         | PD |
|4  | PA_42 | **PA42**、SD1_DIO1、WKUP_PIN                          | PU |
|5  | PA_41 | **PA41**、SD1_DIO0、WKUP_PIN                          | PU |
|6  | PA_40 | **PA40**、SPI2_CS、SD1_CMD、WKUP_PIN                  | PU |
|7  | PA_39 | **PA39**、SPI2_CLK、SD1_CLK、WKUP_PIN                 | PU |
|8  | PA_38 | **PA38**、SPI2_DI、SD1_DIO3、WKUP_PIN、GPADC_CH10     | PD |
|9  | PA_37 | **PA37**、SPI2_DIO、SD1_DIO2、WKUP_PIN、GPADC_CH9     | PD |
|10 | PA_36 | **PA36**、USB_DM、WKUP_PIN、GPADC_CH8                 | PD |
|11 | PA_35 | **PA35**、USB_DP、WKUP_PIN、GPADC_CH7                 | PD |
|12 | PA_31 | **PA31**、SD2_CMD、GPADC_CH3                          | PD |
|13 | PA_30 | **PA30**、SD2_CLK、GPADC_CH2、EFUSE_PWR               | PD |
|14 | PA_29 | **PA29**、SPI1_CS、SD2_DIO3、GPADC_CH1                | PD |
|15 | PA_28 | **PA28**、SPI1_CLK、SD2_DIO2、GPADC_CH0               | PD |
|16 | GND   | 接地                     |  |
|17 | 3.3V  | 3.3V电源，USB Type-C不插时，可以当做3.3V输入；当USB Type-C插入时，可以当做3.3V输出 |  |
|18 | PA_27 | **PA27**、SD1_DIO1、SD2_DIO1、RTC_CLK、LPTIM2_OUT、LPTIM2_OUTB | PU |
|19 | PA_26 | **PA26**、SD1_DIO0、SD2_DIO0、RTC_CLK、LPTIM2_OUT、LPTIM2_OUTB | PU |
|20 | PA_25 | **PA25**、SPI1_DI、SD1_CMD、SD2_CMD、RTC_CLK、LPTIM2_OUT、LPTIM2_OUTB、XTAL32K_EXT | PD |
|21 | PA_24 | **PA24**、SPI1_DIO、SD1_CLK、SD2_CLK、RTC_CLK、LPTIM2_OUT、LPTIM2_OUTB | PD |
|22 | PA_34 | **PA34**、WKUP_PIN、GPADC_CH6、电源键长按复位                | PD |
|23 | PA_33 | **PA33**、SD2_DIO1、WKUP_PIN、GPADC_CH5                | PD |
|24 | PA_32 | **PA32**、SD2_DIO0、GPADC_CH4、WS2812B数据              | PD |
```

<div align="center"> RIGHT PIN（J2）管脚描述表 </div>

```{table}
:align: center
:width: 100%
:widths: 10 16 64 10
:class: devkit-pin-table

|管脚|管脚名称|复位默认及复用功能|上下拉|
|:--|:-----------------------|:-----------|------|
|1  | GND   | 接地                     |  |
|2  | PA_00 | **PA00**、LCDC1_SPI_RSTB、SD2_DIO2                    | PD |
|3  | PA_01 | **PA01**、SD2_DIO3                                    | PD |
|4  | PA_02 | **PA02**、LCDC1_SPI_TE、SD2_CLK                       | PD |
|5  | PA_03 | **PA03**、LCDC1_SPI_CS、SD2_CMD                       | PU |
|6  | PA_04 | **PA04**、LCDC1_SPI_CLK、SD2_DIO0                     | PD |
|7  | PA_05 | **PA05**、LCDC1_SPI_DIO0、SD2_DIO1                    | PD |
|8  | PA_06 | **PA06**、LCDC1_SPI_DIO1、SD1_DIO2                    | PD |
|9  | PA_07 | **PA07**、LCDC1_SPI_DIO2、SD1_DIO3                    | PD |
|10 | PA_08 | **PA08**、LCDC1_SPI_DIO3、SD1_CLK                     | PD |
|11 | PA_09 | **PA09**、SD1_CMD、ADC1N、TP_INT                      | PD |
|12 | MIC_ADC  | MIC_ADC_IN输入信号           |  |
|13 | MIC_BIAS | MIC偏置电压           |  |
|14 | DACP  | 模拟音频输出信号          |  |
|15 | DACN  | 模拟音频输出信号          |  |
|16 | GND   | 接地                    |  |
|17 | 1.8V  | 1.8V电源，USB Type-C不插时，可以当做1.8V输入；当USB Type-C插入时，可以当做1.8V输出 |  |
|18 | PA_10 | **PA10**、SD1_DIO0、ADC2P、TP_RST                     | PD |
|19 | PA_11 | **PA11**、MPI3_CS2、SD1_DIO1、ADC2N、TP_SDA           | PU |
|20 | PA_20 | **PA20**、SWO、TP_SCL                                | PD |
|21 | PA_21 | **PA21**（通用GPIO）                                 | PD |
|22 | PA_18 | **USART1_RXD**（调试串口）、SWCLK（HKB Pinmux）        | PU |
|23 | PA_19 | **USART1_TXD**（调试串口）、SWDIO（HKB Pinmux）        | PU |
|24 | 5V    | 5V电源，USB Type-C不插时，可以当做5V输入；当USB Type-C插入时，可以当做5V输出 |  |
```

### 16p QSPI线序FPC接口定义

<div align="center"> 16p FPC接口信号定义 </div>

```{table}
:align: center
:width: 100%
:widths: 10 16 64 10
:class: devkit-pin-table

|管脚|管脚名称|复位默认及复用功能|上下拉|
|:--|:-----------------------|:-----------|------|
|1  | GND    | 接地                        |      |
|2  | PA_00 | **PA00**、LCDC1_SPI_RSTB、SD2_DIO2   | PD   |
|3  | PA_01 | **PA01**、SD2_DIO3    | PD   |
|4  | PA_02 | **PA02**、LCDC1_SPI_TE、SD2_CLK   | PD   |
|5  | PA_03 | **PA03**、LCDC1_SPI_CS、SD2_CMD    | PU   |
|6  | PA_04 | **PA04**、LCDC1_SPI_CLK、SD2_DIO0   | PD   |
|7  | PA_05 | **PA05**、LCDC1_SPI_DIO0、SD2_DIO1    | PD   |
|8  | PA_06 | **PA06**、LCDC1_SPI_DIO1、SD1_DIO2   | PD   |
|9  | PA_07 | **PA07**、LCDC1_SPI_DIO2、SD1_DIO3    | PD   |
|10 | PA_08 | **PA08**、LCDC1_SPI_DIO3、SD1_CLK    | PD   |
|11 | 3.3V  | 3.3V电源输出                  |      |
|12 | GND    | 接地                        |      |
|13 | PA_09 | **PA09**、SD1_CMD、ADC1N、TP_INT    | PD   |
|14 | PA_11 | **PA11**、MPI3_CS2、SD1_DIO1、ADC2N    | PU   |
|15 | PA_20 | **PA20**、SWO、TP_SCL    | PD   |
|16 | PA_10 | **PA10**、SD1_DIO0、ADC2P、TP_RST    | PD   |
```

## 4. 功能介绍

### 供电说明

开发板支持以下3种供电方式：

- USB Type-C接口供电（默认）
- 5V和GND排针供电
- 3.3V和GND排针供电

调试过程中优先推荐的供电方式：Type-C USB接口供电。

### LED控制

开发板板载1颗可寻址RGB LED，数据输入连接PA32，使用WS2812协议控制。

<div align="center"> LED灯信号控制表 </div>

```{table}
:align: center
:width: 100%
:widths: 20 20 60
:class: devkit-simple-table

|LED编号|对应GPIO|描述|
|:--|:-----------------------|:-----------|
|WS2812B RGB LED| PA32 | WS2812单线数据输入 |
```

### 外置Flash

芯片已合封NOR Flash。原理图另外提供外置存储器焊接位和启动配置跳线，可按设计选择以下存储器类型，实际是否焊接以具体板卡物料为准：

- SPI NOR Flash，WSON8-8x6mm或WSON8-6x5mm
- SPI NAND Flash，WSON8-8x6mm
- SD NAND Flash，WSON8-8x6mm
- eMMC

<div align="center"> Flash信号定义 </div>

```{table}
:align: center
:width: 100%
:widths: 10 16 64 10
:class: devkit-pin-table

|管脚|管脚名称|复位默认及复用功能|上下拉|
|:--|:-----------------------|:-----------|------|
|1  | PA_12 | **PA12**、MPI3_CS、SD1_DIO2    | PU   |
|2  | PA_13 | **PA13**、MPI3_DIO1、SD1_DIO3    | PD   |
|3  | PA_14 | **PA14**、MPI3_DIO2、SD1_CLK   | PD   |
|4  | PA_15 | **PA15**、MPI3_DIO0、SD1_CMD   | PD   |
|5  | PA_16 | **PA16**、MPI3_CLK、SD1_DIO0    | PD   |
|6  | PA_17 | **PA17**、MPI3_DIO3、SD1_DIO1    | PD   |
```

<div align="center"> 板型和Flash信息对应表 </div>

```{table}
:align: center
:width: 100%
:widths: 42 28 30
:class: devkit-model-table

|开发板型号|MCU合封规格|板载规格|
|:--|:-----------------------|:-----------|
|SF32LB57-DevKit-Core-3p3-N1      | SF32LB57ZUN3N6，1MB SPI NOR Flash  | 无    |
|SF32LB57-DevKit-Core-3p3-N16     | SF32LB57ZUN7N6，16MB SPI NOR Flash | 无    |

```

### 按键

开发板板载2个按键，需要软件自定义功能，其中KEY1支持硬件长按10秒复位功能，开发者可参考下表进行对应管脚的控制。

<div align="center"> 按键信号控制表 </div>

```{table}
:align: center
:width: 100%
:widths: 20 20 60
:class: devkit-simple-table

|按键编号|对应GPIO|描述|
|:--|:-----------------------|:-----------|
|KEY1  | PA34    | 高电平有效，支持长按10秒复位 |
|KEY2  | PA33    | 高电平有效                |
```

### 下载和调试

通过USB-to-UART端口连上USB线，打开思澈科技的程序下载工具，选取相应的COM口和程序。

1. 下载模式
    - 勾选BOOT项，上电，开机后进入下载模式，就可以完成程序的下载。
2. 软件开发模式
    - 去掉BOOT项，上电，开机后进入串口log打印模式，便进入软件调试模式。
3. 开发板复位
    - 通过上位机工具控制CH343P的RTS#管脚来复位MCU。

**具体请参考&emsp;[固件烧录工具 Impeller](../../tools/烧录工具)**

### LCD显示屏接口

开发板支持QSPI接口LCD屏，接插件为立式16p-0.5pitch FPC，上翻下接触。
信号线序请参考上文定义。线序不同需要使用转接排线或转接板。

通过FPC-16p排线可以直接接**1.85inch AMOLED Module**屏。

```{image} assets/57-FPC-16P-Adapter.png
:width: 80%
:align: center
```

<div align="center"> FPC转接排线 </div>  <br>  <br>  <br>

### 音频扩展

开发板需要外挂麦克风和差分音频功放。

- [参考驻极体麦克风板](https://item.taobao.com/item.htm?id=891546819215&pisk=g3ttX5NYqXciCTxOKdu3mg2lmpDkD2vNvCJ7msfglBdphC1GiNsbdM6A3l1f5K6fDBOmQ1vj_IKAOG_2SsfGMip2wFhoq0vwQiSSZbmk_owrJgP_f1Ncdk6RDONxuxqpQiSjZbmoqdJwNSry3l6fdvBG3tsfGl1IpT6lcl_bfyNCT6sbfO__Ry6fhSZ1GIwIAtX8crZf5D_CnTIfGI6jpp1Fhi1j9jlAOR10DUgQANrLBEqbcHBORwv11a7-n97T3dfac9-NB05WC6Ebm14gj8ppIfEyKG-MwTAiAldJhL8fJnFIws-pdhTXL5hAXpAw2Gt-6lXhv1Q5d3M0z6xdsItORYqRoMtlPGTn8fbcXts1zek4SsTXe3IMsXrfsUpB9ax3tujWzBKAPgsr_3xJmCVlwt4tpna4uN6E_bxHypqU4QWdZAnYur7ELo49mA44uw-Pp_DtWrzV8X5..&spm=a21xtw.29178619.product_shelf.3.34d33772zuSkO1&skuId=5740404937614)
- [参考MEMS麦克风板](https://detail.tmall.com/item.htm?id=814534179060&ns=1&pisk=g53Se-TCQTXSM7adOuA4GovZEnUEB2t27L5IsfeFzMU-hJej6Q2yx3DIcvH048eyZyZKpYHQxQ2UpJME90oW7FloZy4KRd8w7X1wqAH79uIJ9ZF_9IPRFEzkwy4pQd8w7bcu-A0VoWbdDSe0NMFKpuIvk72Y9gUKp-EY65W8JvHpksF3TaILvWIvG7VCJge8prBYaWILpvUpGje09yF-pyhh41NBV8cWwk_r8dRlbJwfJw3bMJDrGUSQ3cNSvRGRYjGxlNq7Bbef8d9YgqwQnVp2cjDr2YPmdF9bWcDjRlUBPOVSDfaYUPLRkzuowcEKWpjKNzwSpkiDCNP7zmZsP0AhHbHaFcUoT19rGkFsrzo2FNetfbnai2JcyJixv4ru-TpQKqGxyDsrmNy1kVsCGlbLGgAXGMjHuIb4G5SWKTq8i7Z2GI6-xObd8iRXGTnu2SV77IOfevf..&priceTId=213e054e17429838198525727ea59a&skuId=5678321102126&spm=a21n57.1.hoverItem.1&utparam=%7B%22aplus_abtest%22%3A%22730abba11fa183522caa7f9e2e59074c%22%7D&xxc=ad_ztc)
- [参考音频功放板](https://item.taobao.com/item.htm?id=12602258834&pisk=g0_-U1DKS-2uuY_Ji_rm-FD4yzVGJofPMT5s-pvoAtBAOT9kKBTBGjOptDiCOpYdp9BpEHwyrwBvzZjo-L2yJ66MWR2gSPfPaF8QIRD0Vn9v5CJINvAShrTH9SVDsp5Pae8QIR4gS_kKdDDKAB9QMrOBteOBRHNYlBpjPBgWOxNv3KgWN3tWhrOkwQiCd3tjcBRHO0gIRKOX3BTBd9TQMs92OfrQpKGWK2I_ccEC086nR2_vwntcNLGv-ZOJCdCSx2gIYQKJC_94QNZ2_n1evwlEJnf5b9R1FYwpLZCfPG6_n0v5XBCGvOUs8IS5eZtdoWzNMUIAkUb7Lc5cMLt9oiq4EHYReGJwVoyVChCGjU7_HV9dVTWebw2ZzL1C_NSMWzHwwi19kgyOSNQhEAv9t0FARDoeVIyzIZjt6G1omIpgwynEYnPq-0Q3ZDoe0NRvI7E-YD-43&spm=a21xtw.29178619.product_shelf.2.654a20dbhEwOYd)

### PCB元件位置查询

<a href="../../_static/SF32LB57-DevKit-Core-3p3-辅助焊接.html">SF32LB57-DevKit-Core-3p3-PCB</a>

## 5. 样品获取

零售样品与小批量可直接在[淘宝](https://sifli.taobao.com/)购买，批量客户可发邮件到sales@sifli.com或淘宝找客服获取销售联系方式。
参与开源可以免费申请样品，可加入QQ群674699679进行交流。

## 6. 相关文档

- [SF32LB57X芯片技术规格书](https://downloads.sifli.com/docs/Datasheet/%E5%B8%B8%E4%BE%9B%E7%94%B5/DS5702-SF32LB57X-%E8%8A%AF%E7%89%87%E6%8A%80%E6%9C%AF%E8%A7%84%E6%A0%BC%E4%B9%A6%20V0p2p3.pdf)
- [SF32LB57X用户手册](https://downloads.sifli.com/docs/Datasheet/%E9%94%82%E7%94%B5/UM5701-SF32LB57x-%E7%94%A8%E6%88%B7%E6%89%8B%E5%86%8C%20V0p1p1.pdf)
- [SF32LB57-DevKit-Core-3p3设计图纸](https://downloads.sifli.com/hardware/files/documentation/SF32LB57-DevKit-Core-3p3-V100_2026-10-25.zip)
- [SF32LB57-DevKit-LCD转接板制作指南](SF-DevKit-LCM-Adapter)
- [硬件知识库-查询信息和原理图审图](https://github.com/OpenSiFli/SiFli-HKB)