# SF32LB52-DevKit-LCD转接板制作指南

本文指导如何给SF32LB52-DevKit-LCD开发板做配套转接板，用来调试第三方显示屏，WiFi模组等。

## QSPI-LCD接口转接板

QSPI-LCD转接板可以从22pin的FPC座子转接，也可以从40pin的双排针转接。

### 22pin FPC转接方式


```{figure} assets/52Kit-22p-FPC-pin-define.png

:scale: 60%
:name: sf32lb5x-lcd-board-back
SF32LB52-DevKit-LCD板22p FPC座信号定义
```

```{table} SF32LB52-DevKit-LCD-22P分配

:name: SF32LB52-DevKit-LCD-22P-LIST

|管脚|	管脚名称           	   |   功能  |
|:--|:-----------------------|:-----------|
|1  | LEDK    | LCD屏背光二极管阴极                     
|2  | LEDA    | LCD屏背光二极管阳极    
|3  | PA_07   | MIPI-DBI(8080) B0，QSPI D2，LCD接口信号 
|4  | PA_08   | MIPI-DBI(8080) B1，QSPI D3，LCD接口信号 
|5  | PA_37   | MIPI-DBI(8080) B2，LCD接口信号 
|6  | PB_39   | MIPI-DBI(8080) B3，LCD接口信号 
|7  | PB_40   | MIPI-DBI(8080) B4，LCD接口信号 
|8  | PA_41   | MIPI-DBI(8080) B5，LCD接口信号  
|9  | PA_42   | MIPI-DBI(8080) B6，LCD接口信号 
|10 | PA_43   | MIPI-DBI(8080) B7，LCD接口信号                 
|11 | PA_02   | MIPI-DBI(8080) TE，QSPI TE，LCD接口信号                   
|12 | PA_00   | LCD Reset，LCD接口信号 
|13 | PA_04   | MIPI-DBI(8080) WRx，QSPI CLK，SPI CLK，LCD接口信号 
|14 | PB_05   | MIPI-DBI(8080) RDx，QSPI D0，SPI SDI，LCD接口信号         
|15 | PA_03   | MIPI-DBI(8080) CSx，QSPI CS，SPI CS，LCD接口信号             
|16 | PA_06   | MIPI-DBI(8080) DCx，QSPI D1，SPI DC，LCD接口信号 
|17 | VDD_3V3 | 3.3V电源输出 
|18 | PA_31   | 触摸屏INT中断信号
|19 | PA_33   | 触摸屏I2C_SDA信号 
|20 | PA_30   | 触摸屏I2C_SCL信号 
|21 | PA_09   | 触摸屏RTN复位信号 
|22 | GND     | 接地                         

```
SF32LB52-DevKit-LCD开发板的22pin FPC座子，支持MIPI-DBI(8080)和SPI(3/4wire,2/4data)接口，可以通过软件配置IO的MUX来适配数据格式。

```{figure} assets/52Kit-LED-driver.png

:scale: 50%
:name: sf32lb5x-lcd-board-back1
SF32LB52-DevKit-LCD板22p FPC座LED driver电路
```

SF32LB52-DevKit-LCD开发板提供一路LED驱动，默认驱动电流40mA，可以根据LCD显示屏的LED电路结构和电流要求，更改R0110的阻值来调整LED的驱动电流。

```{important}
1. 转接板通过FPC排线和SF32LB52-DevKit-LCD开发板相连，设计时注意转接板上的FPC线序，需要和开发板上的信号定义做交叉。
2. FPC接插件接口中VDD_3V3电源可以给转接板上的屏幕驱动和触摸驱动供电。
3. 开发板的IO是3.3V电平，如果LCD转接板上的驱动芯片的IO电平是1.8V，请使用Level shift芯片来转换电平。
4. 如果转接板需要5V电源，请使用40p 双排针来做转接接口。
5. 开发板上显示接口已经串了电阻，转接板上无需再串电阻。
```

### 40pin 双排针转接方式

```{figure} assets/52Kit-2x20p-pin-define.png

:scale: 60%
:name: sf32lb5x-lcd-board-back2
SF32LB52-DevKit-LCD板40pin 双排针信号定义
```
```{table} SF32LB56-DevKit-LCD-40P信号定义

:name: SF32LB56-DevKit-LCD-40P-LIST

|管脚|	管脚名称           	   |   功能  |
|:--|:-----------------------|:-----------|
|1   | 3V3      | 3v3 power                 
|2   | 5V       | 5v power   
|3   | IO2      | PA_42或PA_14   
|4   | 5V       | 5v power        
|5   | IO3      | PA_41或PA_12     
|6   | GND      | 接地    
|7   | IO4      | PA_43或PA_13    
|8   | IO14     | PA_27   
|9   | GND      | 接地    
|10  | IO15     | PA_20     
|11  | IO17     | PA_08，**MIPI-DBI(8080) B1，QSPI D3，LCD接口信号**   
|12  | IO18     | PA_05，**MIPI-DBI(8080) RDx，QSPI D0，SPI SDI，LCD接口信号** 
|13  | IO27     | PA_40或PA_17  &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp;               
|14  | GND      | 接地         
|15  | IO22     | PA_39或PA_16         
|16  | IO23     | PA_37或PA_15                  
|17  | 3V3      | 3v3 power       
|18  | IO24     | PA_38    
|19  | IO10     | PA_24    
|20  | GND      | 接地      
|21  | IO9      | PA_25       
|22  | IO25     | PA_07，**MIPI-DBI(8080) B0，QSPI D2，LCD接口信号**       
|23  | IO11     | PA_28       
|24  | IO8      | PA_29       
|25  | GND      | 接地       
|26  | IO7      | PA_31，**触摸屏INT中断信号**       
|27  | IO0      | PA_30，**触摸屏I2C_SCL信号**       
|28  | IO1      | PA_22       
|29  | IO5      | PA_23       
|30  | GND      | 接地      
|31  | IO6      | PA_33，**触摸屏I2C_SDA信号**       
|32  | IO12     | PA_00，**LCD Reset，LCD接口信号**       
|33  | IO13     | PA_01，**BL PWM，LCD接口信号**       
|34  | GND      | 接地       
|35  | IO19     | PA06，**MIPI-DBI(8080) DCx，QSPI D1，SPI DC，LCD接口信号**        
|36  | IO16     | PA02，**MIPI-DBI(8080) TE，QSPI TE，LCD接口信号**        
|37  | IO26     | PA09，**触摸屏RTN复位信号**      
|38  | IO20     | PA04，**MIPI-DBI(8080) WRx，QSPI CLK，SPI CLK，LCD接口信号**      
|39  | GND      | 接地       
|40  | IO21     | PA03，**MIPI-DBI(8080) CSx，QSPI CS，SPI CS，LCD接口信号**            

```
```{important}
1. 转接板通过40p双排针和SF32LB52-DevKit-LCD开发板相连，转接板是扣在开发板上面的。
2. 40p双排针接口中3V3和5V电源可以给转接板上的屏幕驱动和触摸驱动供电。
3. 开发板的IO是3.3V电平，如果LCD转接板上的驱动芯片的IO电平是1.8V，请使用Level shift芯片来转换电平。
4. 需要转接板上集成显示屏背光电路。
5. 开发板上显示接口已经串了电阻，转接板上无需再串电阻。
```
## MIPI-DBI(8080)接口转接板

参考QSPI-LCD接口转接板章节

## EDP墨水屏接口转接板


## WiFi模组转接板


