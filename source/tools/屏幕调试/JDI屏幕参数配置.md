# JDI屏幕参数配置
JDI屏幕有2种接口：并口(JDI_PARALLEL)和串口(JDI_SERIAL)。


## 并口(JDI_PARALLEL)
目前并口的比较常见，他一般需要LCDC和一个LP-PWM配合:

1. LP-PWM (Low power PWM 低功耗PWM, 支持系统睡眠时输出PWM波形）用于输出刷新时钟 XFRP/FRP/VCOM, 在58x之后一个LP-PWM可以控制2个pin脚输出相反的波形
1. LCDC(LCD Controller)则用于输出像素数据和其他控制信号


### 参数配置讲解

```c
static LCDC_InitTypeDef lcdc_int_cfg =
{
    .lcd_itf = LCDC_INTF_JDI_PARALLEL,
    .freq = 746268, //HCK frequency

    /* 
        Useless parameter for JDI PARALLEL interface, 
        used to pass the format checking here. 
    */ 
    .color_mode = LCDC_PIXEL_FORMAT_RGB565, 

    .cfg = {
        .jdi = {
            .bank_col_head = 0, //Vertical Blanking pixles at the head
            .valid_columns = THE_LCD_PIXEL_WIDTH, //Vertical valid pixles
            .bank_col_tail = 4, //Vertical Blanking pixles at the tail

            .bank_row_head = 0, //Horizontal Blanking rows at the head
            .valid_rows = THE_LCD_PIXEL_HEIGHT, //Horizontal valid rows
            .bank_row_tail = 4, //Horizontal Blanking rows at the tail

            /* 
                ENB will be active during column [32~95]
            */
            .enb_start_col = 32, 
            .enb_end_col = 95,
        },
    },

};
```




### 刷新时钟
在[LCD_DisplayOn](lcd-cb-func-LCD-DisplayOn)和[LCD_DisplayOff](lcd-cb-func-LCD-DisplayOff)函数内部，通过一个外部定义的rt_device名称（`JDI_FRP_LPPWM_INTERFACE_NAME`）来启动和关闭PWM设备的输出，目的是开关FRP/XFRP/VCOM的输出。

PWM的时钟频率通过接口`rt_pwm_set`设置，如下代码中是60Hz,50%占空比的输出设置：
```c

/**
  * @brief  Enables the Display.
  * @param  None
  * @retval None
  */
static void LCD_DisplayOn(LCDC_HandleTypeDef *hlcdc)
{
    /* Display On, enable the FRP&XFRP output */
#ifdef JDI_FRP_LPPWM_INTERFACE_NAME
    struct rt_device_pwm *device = (struct rt_device_pwm *)rt_device_find(JDI_FRP_LPPWM_INTERFACE_NAME);
    if (!device)
    {
        LOG_E("Can not find FRP LPPWM device:%s", JDI_FRP_LPPWM_INTERFACE_NAME);
    }
    else
    {
        if (0 == (device->parent.open_flag & RT_DEVICE_OFLAG_OPEN))
        {
            rt_device_open((struct rt_device *)device, RT_DEVICE_OFLAG_RDWR);
            rt_pwm_set(device, 1, 16 * 1000 * 1000, 8 * 1000 * 1000); // Set period to 16ms, pulse to 8ms
            rt_pwm_enable(device, 1); //Enable PWM output
        }
    }
#endif
}

/**
  * @brief  Disables the Display.
  * @param  None
  * @retval None
  */
static void LCD_DisplayOff(LCDC_HandleTypeDef *hlcdc)
{
    /* Display Off, disable the FRP&XFRP output */
#ifdef JDI_FRP_LPPWM_INTERFACE_NAME
    struct rt_device_pwm *device = (struct rt_device_pwm *)rt_device_find(JDI_FRP_LPPWM_INTERFACE_NAME);
    if (!device)
    {
        LOG_E("Can not find FRP LPPWM device:%s", JDI_FRP_LPPWM_INTERFACE_NAME);
    }
    else
    {
        if (device->parent.open_flag & RT_DEVICE_OFLAG_OPEN)
        {
            rt_pwm_disable(device, 1); //Disable PWM output
            rt_device_close((struct rt_device *)device);
        }
    }
#endif
}
```

## 串口(JDI_SERIAL)
串口的JDI目前我们没有测试过，虽然硬件上是支持的。 