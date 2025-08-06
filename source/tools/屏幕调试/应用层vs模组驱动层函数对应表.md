# 应用层vs模组驱动层函数对应表
以下表格是各种应用层的操作（这里的应用层是指rt_device层的调用）对应的底层驱动发生的事情：

## 屏幕的应用层操作和对应的底层函数调用
### 打开屏幕调用流程
应用层调用函数：
```c
rt_device_open(lcd_device, RT_DEVICE_OFLAG_RDWR); //打开屏幕
```

| 顺序 |  驱动层调用函数 | 函数在文件路径 | 描述 |
| ----------- | ----------- | ----------- | ----------- |
| 1 | BSP_LCD_PowerUp(void);  | bsp_lcd_tp.c | 屏幕上电 |
| 2 | LCD_Init(hlcdc) | nv3051f1.c | 屏驱初始化函数 |
| 3 | LCD_ReadID(hlcdc) | nv3051f1.c | 屏幕在位检测（开机检测1次） |


### 关闭屏幕调用流程
应用层调用函数：
```c
rt_device_close(lcd_device); //关闭屏幕
```

| 顺序 |  驱动层调用函数 | 函数在文件路径 | 描述 |
| ----------- | ----------- | ----------- | ----------- |
| 1 | LCD_DisplayOff(hlcdc) | nv3051f1.c | 关闭液晶 |
| 2 | LCD_SetBrightness(hlcdc, br) | nv3051f1.c | 设置背光亮度为0 |
| 3 | BSP_LCD_PowerDown(void);  | bsp_lcd_tp.c | 屏幕下电 |


### 设置屏幕数据接收区域
应用层调用函数：
```c
rt_graphix_ops(lcd_device)->set_window(0,0,239,319); //设置起始坐标为{0,0}，高宽为240x320的接收区域
```

| 顺序 |  驱动层调用函数 | 函数在文件路径 | 描述 |
| ----------- | ----------- | ----------- | ----------- |
| 1 | LCD_SetRegion(hlcdc, Xpos0, Ypos0, Xpos1, Ypos1) | nv3051f1.c | 设置屏幕接收区域 |

### 推送Framebuffer到屏幕
应用层调用函数：
```c
uint8_t framebuffer[240*320];
rt_graphix_ops(lcd_device)->draw_rect_async((const char *)&frambuffer, 0,0,239,319); //推送起始坐标为{0,0}，高宽为240x320的Framebuffer到屏幕
```

| 顺序 |  驱动层调用函数 | 函数在文件路径 | 描述 |
| ----------- | ----------- | ----------- | ----------- |
| 1 | LCD_WriteMultiplePixels(hlcdc, const uint8_t *RGBCode, Xpos0, Ypos0, Xpos1, Ypos1) | nv3051f1.c | 推送Framebuffer到屏幕 |


### 设置屏幕亮度
应用层调用函数：
```c
uint8_t brightness = 100;//背光亮度百分比值
rt_device_control(lcd_device, RTGRAPHIC_CTRL_SET_BRIGHTNESS, &brightness); //设置背光亮度
```

| 顺序 |  驱动层调用函数 | 函数在文件路径 | 描述 |
| ----------- | ----------- | ----------- | ----------- |
| 1 | LCD_SetBrightness(hlcdc, br) | nv3051f1.c | 设置背光亮度 |
| 2 | LCD_DisplayOn(hlcdc) | nv3051f1.c | 打开液晶屏幕 |


### 组合刷屏操作
组合刷新函数包括了：设置屏幕数据接收区域&推送Framebuffer到屏幕
应用层调用函数：
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

| 顺序 |  驱动层调用函数 | 函数在文件路径 | 描述 |
| ----------- | ----------- | ----------- | ----------- |
| 1 | 自动设置framebuffer的压缩率和颜色格式 | drv_lcd.c | 驱动框架自动完成 |
| 2 | LCD_SetRegion(hlcdc, Xpos0, Ypos0, Xpos1, Ypos1) | nv3051f1.c | 设置屏幕接收区域 |
| 3 | LCD_WriteMultiplePixels(hlcdc, const uint8_t *RGBCode, Xpos0, Ypos0, Xpos1, Ypos1) | nv3051f1.c | 推送Framebuffer到屏幕 |


<br>
<br>
<br>
<br>


## TP的应用层操作和对应的底层函数调用
### 打开TP设备
```c
rt_device_open(touch_device, RT_DEVICE_FLAG_RDONLY); //打开TP设备
```
| 顺序 |  驱动层调用函数 | 函数在文件路径 | 描述 |
| ----------- | ----------- | ----------- | ----------- |
| 1 |  BSP_TP_PowerUp | bsp_lcd_tp.c | 触控上电 |
| 2 | rt_bool_t probe(void) | gt911.c | 触控在位检测（只做1次） |
| 3 |  rt_err_t init(void) | gt911.c | 触控初始化 |

### 关闭TP设备
```c
rt_device_close(touch_device); //关闭TP设备
```
| 顺序 |  驱动层调用函数 | 函数在文件路径 | 描述 |
| ----------- | ----------- | ----------- | ----------- |
| 1 |  rt_err_t deinit(void) | gt911.c | 触控去初始化 |
| 2 |  BSP_TP_PowerUp | bsp_lcd_tp.c | 触控上电 |

### 读取TP数据点
```c
struct touch_message touch_data;
rt_device_read(touch_device, 0, &touch_data, 1); //读取TP数据点
```

| 顺序 |  驱动层调用函数 | 函数在文件路径 | 描述 |
| ----------- | ----------- | ----------- | ----------- |
| 1 |   rt_err_t read_point(touch_msg_t p_msg) | gt911.c | 触控读取数据点 |
