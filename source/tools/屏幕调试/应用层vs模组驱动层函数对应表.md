# Application Layer vs. Module Driver Layer Function Correspondence Table
The following table shows the operations at the application layer (here, the application layer refers to the calls made at the rt_device layer) and the corresponding events that occur at the underlying driver layer:

## Screen Application Layer Operations and Corresponding Lower-Level Function Calls
### Screen Open Call Flow
Application layer function call:
```c
rt_device_open(lcd_device, RT_DEVICE_OFLAG_RDWR); // Open the screen
```

| Order | Driver Layer Function Call | Function in File Path | Description |
| ----------- | ----------- | ----------- | ----------- |
| 1 | BSP_LCD_PowerUp(void);  | bsp_lcd_tp.c | Power up the screen |
| 2 | LCD_Init(hlcdc) | nv3051f1.c | Screen driver initialization function |
| 3 | LCD_ReadID(hlcdc) | nv3051f1.c | Screen presence detection (once at startup) |


### Screen Close Call Flow
Application layer function call:
```c
rt_device_close(lcd_device); // Close the screen
```

| Order | Driver Layer Function Call | Function in File Path | Description |
| ----------- | ----------- | ----------- | ----------- |
| 1 | LCD_DisplayOff(hlcdc) | nv3051f1.c | Turn off the LCD |
| 2 | LCD_SetBrightness(hlcdc, br) | nv3051f1.c | Set the backlight brightness to 0 |
| 3 | BSP_LCD_PowerDown(void);  | bsp_lcd_tp.c | Power down the screen |


### Set Screen Data Reception Area
Application layer function call:
```c
rt_graphix_ops(lcd_device)->set_window(0,0,239,319); // Set the reception area with start coordinates {0,0} and dimensions 240x320
```

| Order | Driver Layer Function Call | Function in File Path | Description |
| ----------- | ----------- | ----------- | ----------- |
| 1 | LCD_SetRegion(hlcdc, Xpos0, Ypos0, Xpos1, Ypos1) | nv3051f1.c | Set the screen reception area |


### Push Framebuffer to Screen
Application layer function call:
```c
uint8_t framebuffer[240*320];
rt_graphix_ops(lcd_device)->draw_rect_async((const char *)&frambuffer, 0,0,239,319); // Push the Framebuffer with start coordinates {0,0} and dimensions 240x320 to the screen
```

| Order | Driver Layer Function Call | Function in File Path | Description |
| ----------- | ----------- | ----------- | ----------- |
| 1 | LCD_WriteMultiplePixels(hlcdc, const uint8_t *RGBCode, Xpos0, Ypos0, Xpos1, Ypos1) | nv3051f1.c | Push the Framebuffer to the screen |


### Set Screen Brightness
Application layer function call:
```c
uint8_t brightness = 100;// Backlight brightness percentage value
rt_device_control(lcd_device, RTGRAPHIC_CTRL_SET_BRIGHTNESS, &brightness); // Set the backlight brightness
```

| Order | Driver Layer Function Call | Function in File Path | Description |
| ----------- | ----------- | ----------- | ----------- |
| 1 | LCD_SetBrightness(hlcdc, br) | nv3051f1.c | Set the backlight brightness |
| 2 | LCD_DisplayOn(hlcdc) | nv3051f1.c | Turn on the LCD screen |


### Combined Screen Refresh Operations
The combined refresh function includes: setting the screen data reception area and pushing the Framebuffer to the screen
Application layer function call:
```c
lcd_flush_info_t flush_info = {
    .cmpr_rate = 0,
    .color_format = RTGRAPHIC_PIXEL_FORMAT_RGB565,
    .pixel = framebuffer,
    .window = {100,100,200,200},
    .pixel_area = {0,0,240,240},
};
err = rt_device_control(p_lcd_dev, SF_GRAPHIC_CTRL_LCDC_FLUSH, &flush_info);
```

| Order | Driver Layer Function Call | Function in File Path | Description |
| ----------- | ----------- | ----------- | ----------- |
| 1 | Automatically set the compression rate and color format of the Framebuffer | drv_lcd.c | Automatically completed by the driver framework |
| 2 | LCD_SetRegion(hlcdc, Xpos0, Ypos0, Xpos1, Ypos1) | nv3051f1.c | Set the screen reception area |
| 3 | LCD_WriteMultiplePixels(hlcdc, const uint8_t *RGBCode, Xpos0, Ypos0, Xpos1, Ypos1) | nv3051f1.c | Push the Framebuffer to the screen |


<br>
<br>
<br>
<br>


## TP Application Layer Operations and Corresponding Lower-Level Function Calls
### Open TP Device
```c
rt_device_open(touch_device, RT_DEVICE_FLAG_RDONLY); // Open the TP device
```
| Order | Driver Layer Function Call | Function in File Path | Description |
| ----------- | ----------- | ----------- | ----------- |
| 1 | BSP_TP_PowerUp | bsp_lcd_tp.c | Power up the touch screen |
| 2 | rt_bool_t probe(void) | gt911.c | Touch presence detection (only once) |
| 3 | rt_err_t init(void) | gt911.c | Touch initialization |

### Close TP Device
```c
rt_device_close(touch_device); // Close TP device
```
| Order | Driver Layer Function Call | Function in File Path | Description |
| ----------- | ----------- | ----------- | ----------- |
| 1 | rt_err_t deinit(void) | gt911.c | Touch deinitialization |
| 2 | BSP_TP_PowerUp | bsp_lcd_tp.c | Touch power up |

### Read TP Data Points
```c
struct touch_message touch_data;
rt_device_read(touch_device, 0, &touch_data, 1); // Read TP data points
```

| Order | Driver Layer Function Call | Function in File Path | Description |
| ----------- | ----------- | ----------- | ----------- |
| 1 | rt_err_t read_point(touch_msg_t p_msg) | gt911.c | Touch read data points |