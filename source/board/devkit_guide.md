# 开发板型号指南

## 开发板编号规则 SF32LB5x-DevKit-Xxxx-AaaaBbbbCccc

### 主类别 *SF32LB5x-DevKit*

- SF：芯片系列
    - SiFli，公司logo
- 32：芯片系列
    - 32：32-bit MCU系列
- LB：系列属性
    - LB：Low-power Bluetooth MCU
    - VB：采用RISC-V处理器的Bluetooth MCU
- 5：处理器系列
    - 5：基于32-bit Arm Cortex-M33 Star-MC1处理器，或类似算力的RISC-V处理器
    - 0：基于32-bit Arm Cortex-M0+处理器
- x：高中低定位
    - 8：5x系列旗舰产品
    - 6/5：5x系列中端产品
    - 2：5x系列性价比产品

### 子类别 *Xxxx*
- 3p3：不支持锂电池供电，常规3.3V供电系列
- Vbat：支持锂电池供电系列
- y: 52模组专用子类别
    - 1：支持锂电池供电系列，板载SF32LB525UC6/SF32LB527UD6芯片
    - A：不支持锂电池供电，常规3.3V供电系列，板载SF32LB52BU36/SF32LB52BU36芯片,合封FLASH
    - B：不支持锂电池供电，常规3.3V供电系列，板载SF32LB52DUB6/SF32LB52JUD6芯片,合封PSRAM

### 配置类别 *AaaaBbbbCccc*
- Aaaa：可变Flash容量
    - N16：16MB QSPI-NOR Flash
    - A128：128MB SPI-Nand Flash
    - D128：128MB SD-Nand Flash
    - E4：  4GB eMMC
- Bbbb：PSRAM容量
    - R4：4MB OPI-PSRAM
    - R8：8MB OPI-PSRAM
    - R12：4MB+8MB OPI-PSRAM
    - R16：16MB OPI/HPI-PSRAM
    - R32：16+16MB HPI-PSRAM
    - R64：32+32MB HPI-PSRAM
- Cccc：常备Flash容量
    - N1：1MB QSPI-NOR Flash
    - N4：4MB QSPI-NOR Flash


## SF32LB52-DevKit-Nano

开发板代码| 芯片代码 | 可变Flash容量 | PSRAM容量 | 常备Flash | 环境温度 | 开发板尺寸（mm）
:- | :-|:-|:-|:-|:-|:-
SF32LB52-DevKit-Nano-N4      | SF32LB52BU56 | None            | None           | 4MB QSPI-NOR | -40~85C | 51*20.32
SF32LB52-DevKit-Nano-N16R16  | SF32LB52JUD6 | 16MB QSPI-NOR   | 16MB OPI-PSRAM | None         | -40~85C | 51*20.32
SF32LB52-DevKit-Nano-A128R16 | SF32LB52JUD6 | 128MB QSPI-NAND | 16MB OPI-PSRAM | None         | -40~85C | 51*20.32

## SF32LB52-DevKit-Core

开发板代码| 芯片代码 | 可变Flash容量 | PSRAM容量 | 常备Flash | 环境温度 | 开发板尺寸（mm）
:- | :-|:-|:-|:-|:-|:-
SF32LB52-DevKit-Core-3p3-N4      | SF32LB52BU56 | None            | None           | 4MB QSPI-NOR | -40~85C | 68*31
SF32LB52-DevKit-Core-3p3-N16R16  | SF32LB52JUD6 | 16MB QSPI-NOR   | 16MB OPI-PSRAM | None         | -40~85C | 68*31
SF32LB52-DevKit-Wlan-Core-3p3-N16R16  | SF32LB52JUD6 | 16MB QSPI-NOR   | 16MB OPI-PSRAM | None         | -40~85C | 82*62


## SF32LB52-DevKit-LCD

* 用于适配SF32LB52-MOD-1、SF32LB52-MOD-A和SF32LB52-MOD-B系列模组
* 主推型号:SF32LB52-DevKit-LCD-1
* 开发板供电：USB-Type-C或锂离子电池供电
* 支持充电功能，推荐450mAh单芯聚合物锂电池，标称电压3.7V，充满电压4.2V
* 板载CH343P芯片，支持1路USB转UART调试口
* 板载1x开关按键、1x功能按键和1x复位按键
* 板载SPI，DSPI，QSPI和8080接口的显示接口，采用22p，0.5mm间距FPC转接座
* 板载40p，2x20p双排针信号转接接口
* 板载1路MEMS MIC
* 板载1路音频功放，支持1路SPK(最大支持3W/4欧姆)接入
* 板载1xRGBLED，1xCharger LED，1xGPIO控制LED和1x上电指示LED
* 板载SPI接口的TF卡座
* SF32LB52-DevKit-LCD-A可外挂NOR Flash，或外挂SDIO外设，包括WiFi、SD-NAND、或eMMC（4线模式）


开发板代码| 模组代码 | Flash容量 | PSRAM容量 | 环境温度 | 开发板尺寸（mm）
:- | :-|:-|:-|:-|:-
SF32LB52-DevKit-LCD-1-N16R8   | SF32LB52-MOD-1-N16R8   | 16MB QSPI-NOR   | 8MB OPI-PSRAM  | -40~85C | 65*38
SF32LB52-DevKit-LCD-1-A128R16 | SF32LB52-MOD-1-A128R16 | 128MB QSPI-NAND | 16MB OPI-PSRAM | -40~85C | 65*38
<!-- SF32LB52-DevKit-LCD-A-N1      | SF32LB52-MOD-A-N1      | 1MB QSPI-NOR    | n/a            | -40~85C | 65*38 -->
<!-- SF32LB52-DevKit-LCD-B-N16R4   | SF32LB52-MOD-B-N16R4   | 16MB QSPI-NOR   | 4MB OPI-PSRAM  | -40~85C | 65*38 -->



## SF32LB56-DevKit-LCD

* 用于适配SF32LB56-MOD系列模组
* 开发板供电：USB-Type-C
* 板载CH343K芯片，支持2路USB转UART调试口
* 板载SWD接口，4p-2.54mm间距单排针
* 支持Mode启动模式跳线
* 板载1x开关按键、1x功能按键和1x复位按键
* 板载MIPI-DPI(RGB-24bit)显示接口，采用40p，0.5mm间距FPC转接座，兼容正点原子RGB接口线序
* 板载40p，2x20p双排针信号转接接口
* 板载1路MEMS MIC
* 板载1路音频功放，支持1路SPK(最大支持3W/4欧姆)接入
* 板载1xRGBLED，1xGPIO控制LED和1x上电指示LED
* 板载SDIO接口的TF卡座


开发板代码| 模组代码 | Flash容量 | PSRAM容量 | 常备Flash | 环境温度 | 开发板尺寸（mm）
:-| :-|:-|:-|:-|:-|:-
SF32LB56-DevKit-LCD-N16R12N1  | SF32LB56-MOD-N16R12N1  | 16MB QSPI-NOR   | 4+8MB OPI-PSRAM | 1MB QSPI-NOR | -40~85C | 65*38
SF32LB56-DevKit-LCD-A128R12N1 | SF32LB56-MOD-A128R12N1 | 128MB QSPI-NAND | 4+8MB OPI-PSRAM | 1MB QSPI-NOR | -40~85C | 65*38

## SF32LB58-DevKit-LCD

* 用于适配SF32LB58-MOD系列模组
* 开发板供电：USB-Type-C
* 板载CH343K芯片，支持2路USB转UART调试口
* 板载SWD接口，包含在40p双排针中
* 支持Mode启动模式跳线
* 板载1x开关按键、1x功能按键和1x复位按键
* 板载MIPI-DSI(2lane)显示接口，采用30p，0.5mm间距FPC转接座
* 板载MIPI-DPI(RGB-24bit)显示接口，采用40p，0.5mm间距FPC转接座，兼容正点原子RGB接口线序
* 板载双40p，2x20p双排针信号转接接口
* 板载1路MEMS MIC
* 支持2路音频ADC输入，包含在40p双排针中
* 板载2路音频功放输出，支持2路SPK(最大支持3W/4欧姆)接入，包含在40p双排针中
* 板载1x RGBLED，2x GPIO控制LED和1x上电指示LED
* 板载SDIO接口的TF卡座


开发板代码| 模组代码 | Flash容量 | PSRAM容量 | 常备Flash容量 | 环境温度 | 开发板尺寸（mm）
:-| :-|:-|:-|:-|:-|:-
SF32LB58-DevKit-LCD-N16R32N1  | SF32LB58-MOD-N16R32N1  | 16MB QSPI-NOR   | 16+16MB HPI-PSRAM | 1MB QSPI-NOR | -40~85C | 65*50
SF32LB58-DevKit-LCD-A128R32N1 | SF32LB58-MOD-A128R32N1 | 128MB QSPI-NAND | 16+16MB HPI-PSRAM | 1MB QSPI-NOR | -40~85C | 65*50


## SF32-OED-6'-EDP

* 用于适配SF32LB52-MOD-1模组
* 开发板供电：锂离子电池供电
* 支持充电功能，USB-Type-C充电口。推荐1500mAh单芯聚合物锂电池，标称电压3.7V，充满电压4.2V
* 板载CH340N芯片，支持1路USB转UART调试口
* 板载3个GPADC按键
* 板载x8 EDP显示接口，采用34p，0.5mm间距FPC转接座
* 板载触摸屏接口，采用8p，0.5mm间距FPC转接座
* 板载1路MEMS MIC
* 板载1路音频功放，支持1路SPK(最大支持3W/4欧姆)接入
* 板载6轴（加速度和陀螺仪）IMU和温湿度传感器
* 板载SPI接口的TF卡座


开发板代码| 模组代码 | Flash容量 | PSRAM容量 | 环境温度 | 开发板尺寸（mm）
:- | :-|:-|:-|:-|:-
SF32-OED-6'-EDP-N16R8   | SF32LB52-MOD-1-N16R8   | 16MB QSPI-NOR   | 8MB OPI-PSRAM  | -40~85C | 106*64
SF32-OED-6'-EDP-A128R16 | SF32LB52-MOD-1-A128R16 | 128MB QSPI-NAND | 16MB OPI-PSRAM | -40~85C | 106*64

