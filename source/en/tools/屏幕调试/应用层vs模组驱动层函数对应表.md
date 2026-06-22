# Mapping table between application-layer functions and module driver-layer functions
The following table shows what happens in the underlying driver for various application-layer operations (here, the application layer refers to calls at the rt_device layer):

## Application-layer display operations and corresponding underlying function calls
### Call flow for turning on the display
Application-layer call function:
```c
rt_device_open(lcd_device, RT_DEVICE_OFLAG_RDWR); //打开屏幕
```

| Sequence |  Driver-layer call function | Function file path | Description |
| ----------- | ----------- | ----------- | ----------- |
| 1 | BSP_LCD_PowerUp(void);  | bsp_lcd_tp.c | Display power-on |
| 2 | LCD_Init(hlcdc) | nv3051f1.c | Display driver initialization function |
| 3 | LCD_ReadID(hlcdc) | nv3051f1.c | Display presence detection (checked once at boot) |


### Call flow for turning off the display
Application-layer call function:
```c
rt_device_close(lcd_device); //关闭屏幕
```

| Sequence |  Driver-layer call function | Function file path | Description |
| ----------- | ----------- | ----------- | ----------- |
| 1 | LCD_DisplayOff(hlcdc) | nv3051f1.c | Turn off the LCD. |
| 2 | LCD_SetBrightness(hlcdc, br) | nv3051f1.c | Set the backlight brightness to 0. |
| 3 | BSP_LCD_PowerDown(void);  | bsp_lcd_tp.c | Display power-off |


### Set the display data receiving area.
Application-layer call function:
```c
rt_graphix_ops(lcd_device)->set_window(0,0,239,319); //设置起始坐标为{0,0}，高宽为240x320的接收区域
```

| Sequence |  Driver-layer call function | Function file path | Description |
| ----------- | ----------- | ----------- | ----------- |
| 1 | LCD_SetRegion(hlcdc, Xpos0, Ypos0, Xpos1, Ypos1) | nv3051f1.c | Set the display receiving area. |

### Push the framebuffer to the display.
Application-layer call function:
```c
uint8_t framebuffer[240*320];
rt_graphix_ops(lcd_device)->draw_rect_async((const char *)&frambuffer, 0,0,239,319); //推送起始坐标为{0,0}，高宽为240x320的Framebuffer到屏幕
```

| Sequence |  Driver-layer call function | Function file path | Description |
| ----------- | ----------- | ----------- | ----------- |
| 1 | LCD_WriteMultiplePixels(hlcdc, const uint8_t *RGBCode, Xpos0, Ypos0, Xpos1, Ypos1) | nv3051f1.c | Push the framebuffer to the display. |


### Set display brightness.
Application-layer call function:
```c
uint8_t brightness = 100;//背光亮度百分比值
rt_device_control(lcd_device, RTGRAPHIC_CTRL_SET_BRIGHTNESS, &brightness); //Set backlight brightness
```

| Sequence |  Driver-layer call function | Function file path | Description |
| ----------- | ----------- | ----------- | ----------- |
| 1 | LCD_SetBrightness(hlcdc, br) | nv3051f1.c | Set backlight brightness |
| 2 | LCD_DisplayOn(hlcdc) | nv3051f1.c | Turn on the LCD display. |


### Combined screen refresh operation
The combined refresh function includes: Set the display data receiving area.&Push the framebuffer to the display.
Application-layer call function:
```c
lcd_flush_info_t flush_info = {
    .cmpr_rate = 0,
    .color_format = RTGRAPHIC_PIXEL_FORMAT_RGB565,
    .pixel = framebuffer,
    .window = {100,100,200,200}，
    .pixel_area = {0,0,240,240},
};
err = rt_device_control(p_lcd_dev, SF_GRAPHIC_CTRL_LCDC_FLUSH, &flush_info);
```

| Sequence |  Driver-layer call function | Function file path | Description |
| ----------- | ----------- | ----------- | ----------- |
| 1 | Automatically set the framebuffer compression ratio and color format. | drv_lcd.c | Automatically completed by the driver framework. |
| 2 | LCD_SetRegion(hlcdc, Xpos0, Ypos0, Xpos1, Ypos1) | nv3051f1.c | Set the display receiving area. |
| 3 | LCD_WriteMultiplePixels(hlcdc, const uint8_t *RGBCode, Xpos0, Ypos0, Xpos1, Ypos1) | nv3051f1.c | Push the framebuffer to the display. |


<br>
<br>
<br>
<br>


## Application-layer TP operations and corresponding underlying function calls
### Open the TP device.
```c
rt_device_open(touch_device, RT_DEVICE_FLAG_RDONLY); //Open the TP device.
```
| Sequence |  Driver-layer call function | Function file path | Description |
| ----------- | ----------- | ----------- | ----------- |
| 1 |  BSP_TP_PowerUp | bsp_lcd_tp.c | Touch power-on |
| 2 | rt_bool_t probe(void) | gt911.c | Touch presence detection (performed only once) |
| 3 |  rt_err_t init(void) | gt911.c | Touch initialization |

### Close the TP device.
```c
rt_device_close(touch_device); //Close the TP device.
```
| Sequence |  Driver-layer call function | Function file path | Description |
| ----------- | ----------- | ----------- | ----------- |
| 1 |  rt_err_t deinit(void) | gt911.c | Touch deinitialization |
| 2 |  BSP_TP_PowerUp | bsp_lcd_tp.c | Touch power-on |

### Read TP data points.
```c
struct touch_message touch_data;
rt_device_read(touch_device, 0, &touch_data, 1); //Read TP data points.
```

| Sequence |  Driver-layer call function | Function file path | Description |
| ----------- | ----------- | ----------- | ----------- |
| 1 |   rt_err_t read_point(touch_msg_t p_msg) | gt911.c | Touch read data points |
