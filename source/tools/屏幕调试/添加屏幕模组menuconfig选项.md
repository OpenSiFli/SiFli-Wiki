
(add_lcd_menuconfig)=
# 为新的屏幕模组添加menuconfig选项
屏幕模组的menuconfig选项是集合了屏驱IC、背光IC、触控IC的一个综合菜单选项，它指定了这个模组使用了哪个屏幕IC, 哪个触控IC, 使用什么类型的背光，同时指定了模组的液晶玻璃的分辨率、DPI、外形等信息。添加后就可以在工程里面[使用这个新的menuconfig菜单选项](./使用新的屏幕模组.md)。

总共分为以下几个步骤：
1. 打开Kconfig_lcd文件
2. 添加屏幕模组选项
3. 配置屏幕模组液晶的分辨率、DPI

## 1 打开SDK\customer\boards\Kconfig_lcd文件
## 2 添加屏幕模组选项
- 新的屏幕模组的宏一般形式是`LCD_USING_AAA_BBB_CCC`形式, AAA是模组的生产厂家，BBB是模组的型号，CCC是模组的编号出厂日期等，这些信息在模组厂提供的屏幕模组信息里面有。
- 屏幕模组的名称，尽量写上尺寸，接口类型，模组厂家，模组编号，分辨率，等信息
```
        config LCD_USING_TFT_AH034A01ZJINV4C30            <<<<<<新的屏幕模组的宏,不能跟其他的有重名
            bool "3.4 round DSI Video TFT LCD(800x800)"   <<<<<<屏幕模组的名称,在menuconfig中显示的名称
            select TSC_USING_GT911 if BSP_USING_TOUCHD    <<<<<<<模组使用的TP的IC宏
            select LCD_USING_NV3051F1                     <<<<<<模组使用的屏驱IC宏
            select BL_USING_AW9364                        <<<<<<可选项，选择背光驱动 见注3 
            select BSP_USING_ROUND_TYPE_LCD               <<<<<<可选项，建议圆形屏幕添加,方形屏幕可删除这行
            select BSP_LCDC_USING_DSI_VIDEO               <<<<<<见注1
            depends on BSP_SUPPORT_DSI_VIDEO              <<<<<<可选项,见注2
```

**注1**: 
指定该屏幕使用什么接口类型，支持以下选项：
| 宏定义 | 屏驱接口类型 |
| :---- | :----|
| BSP_LCDC_USING_SPI_NODCX_1DATA | 3SPI 1DATA(代表3线SPI，使用1根数据线，下同) |
| BSP_LCDC_USING_SPI_NODCX_2DATA | 3SPI 2DATA  |
| BSP_LCDC_USING_SPI_DCX_1DATA   | 4SPI 1DATA  |
| BSP_LCDC_USING_SPI_DCX_2DATA   | 4SPI 2DATA  |
| BSP_LCDC_USING_QADSPI          | 4SPI 4DATA，目前比较常用的QSPI接口  |
| BSP_LCDC_USING_DDR_QADSPI      | 4SPI 4DATA DDR（QSPI的接口基础上，使用双沿通信）  |
| BSP_LCDC_USING_DBI             |  DBI |
| BSP_LCDC_USING_DSI             |  DSI Command |
| BSP_LCDC_USING_DSI_VIDEO       |  DSI Video |
| BSP_LCDC_USING_DPI             |  DPI(RGB) |
| BSP_LCDC_USING_JDI_PARALLEL    |  JDI 并口 |

**注2**: 
可选项，根据当前开发板是否支持该类型的接口，来决定是否显示该menuconfig选项。
支持的选项如下（其他接口默认都支持，可以不设置）：
| 宏定义 | 屏驱接口类型 |
| :---- | :----|
| BSP_SUPPORT_DSI             |  DSI Command |
| BSP_SUPPORT_DSI_VIDEO       |  DSI Video |
| BSP_SUPPORT_DPI             |  DPI(RGB) |

(lcd_menuconfig_select_backlight_type)=
**注3**: 
可选项，背光驱动仅针对配有背光的屏幕模组，如AMOLED屏幕不需要背光，则可以不设置
支持的选项如下：
| 宏定义 | 屏驱接口类型 |
| :---- | :----|
| BL_USING_AW9364             |  使用AW9364背光芯片 |
| LCD_USING_PWM_AS_BACKLIGHT  |  直接使用芯片的PWM驱动背光 |




## 3 配置屏幕模组液晶的分辨率、DPI
- 分辨率在模组手册里面比较容易找到
- DPI（Dot Per Inch, 有的叫PPI - Pixel Per Inch)的值可能需要自己根据屏幕的物理大小和分辨率计算一下。但是这个值不会影响点亮屏幕, 一般在UI层才会用到这个值。
```py
    config LCD_HOR_RES_MAX
        int
        default 368 if LCD_USING_ED_LB55DSI17801
        default 368 if LCD_USING_ED_LB55DSI17801_QADSPI
        ...
	    default 800 if LCD_USING_TFT_AH034A01ZJINV4C30  <<<<<<新增项,前面的数字代表水平分辨率是800

    config LCD_VER_RES_MAX
        int
        default 448 if LCD_USING_ED_LB55DSI17801
        default 448 if LCD_USING_ED_LB55DSI17801_QADSPI
        ...
        default 800 if LCD_USING_TFT_AH034A01ZJINV4C30   <<<<<<新增项,前面的数字代表垂直分辨率是800

config LCD_DPI
        int
        default 315 if LCD_USING_ED_LB55DSI17801
        default 315 if LCD_USING_ED_LB55DSI17801_QADSPI
        ...
        default 235 if LCD_USING_TFT_AH034A01ZJINV4C30  <<<<<<新增项,前面的数字代表DPI值是235

```

<br>
<br>
<br>
<br>