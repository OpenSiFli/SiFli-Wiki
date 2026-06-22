## 基本介绍

本文的主要目的是帮助开发人员完成基于SF32LB52X系列芯片的手表方案开发。本文重点介绍方案开发过程中的硬件设计相关注意事项，尽可能的减少开发人员工作量，缩短产品的上市周期。

SF32LB52X是一系列用于超低功耗人工智能物联网（AIoT）场景下的高集成度、高性能MCU芯片。芯片采用了基于Arm Cortex-M33 STAR-MC1处理器的大小核架构，集成高性能2D/2.5D图形引擎，人工智能神经网络加速器，双模蓝牙5.3，以及音频CODEC，可广泛用于腕带类可穿戴电子设备、智能移动终端、智能家居等各种应用场景。

:::{attention}
SF32LB52X是SF32LB52系列的**常规供电版本，供电电压为2.97~3.63V，不支持充电**，具体包含如下型号：\
SF32LB52BU36，合封1MB QSPI-NOR Flash \
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


<div align="center"> 封装信息表 </div>

```{table}

|封装名称|尺寸|管脚间距|
|:--|:-|:-|
|QFN68L | 7x7x0.85 mm | 0.35 mm |
```


<img src="assets/52xB/sf32lb52X-B-package-layout.png" width="80%" align="center" />  

<div align="center"> SF32LB52X QFN68L 管脚分布 </div>



## 典型应用方案

下图是典型的SF32LB52A/52D运动手表组成框图，主要功能有显示、存储、传感器、震动马达和音频输入和输出。

<img src="assets/52xB/sf32lb52X-B-watch-app-diagram-52X.png" width="80%" align="center" />  

<div align="center"> SF32LB52B/52E运动手表组成框图 </div>


:::{Note} 
   - 大小核双CPU架构，同时兼顾高性能和低功耗设计要求
   - 片内集成充电管理和PMU模块
   - 支持QSPI接口的TFT或AMOLED显示屏，最高支持512*512分辨率
   - 支持PWM背光控制
   - 支持外接QSPI Nor/Nand Flash和SD Nand Flash存储芯片
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
