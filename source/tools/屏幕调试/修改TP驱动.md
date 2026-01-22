# 修改屏幕TP驱动


(modify_tp_c_file)=
## 修改复制的TP驱动文件
### 修改注册的信号量名称
```c
static int rt_tp_device_init(void)
{
    ...
    driver.isr_sem = rt_sem_create("gt911", 0, RT_IPC_FLAG_FIFO); //修改这个信号量名称为gt911
    rt_touch_drivers_register(&driver);
    return 0;
}
```

### 修改probe函数里面的通信接口
Probe函数一般做几件事情：

1. 打开通信接口（比如I2C），配置接口频率、超时时间等
2. 读取某个寄存器，根据TP是否在位（比如TP的某个状态寄存器）返回状态。（如果不需要做多TP驱动兼容，可直接返回RT_EOK(TP在位）)

### 修改Init函数
驱动的初始化函数里面主要做：

1. 复位TP
2. 配置TP中断GPIO的触发条件，注册中断回调处理函数

**建议使用下列接口,不要使用rt_pin_xxx接口：**
 - rt_touch_irq_pin_attach(PIN_IRQ_MODE_FALLING, irq_handler, NULL);  TP中断注册
 - rt_touch_irq_pin_enable(v)      中断使能和去使能


### 修改中断回调函数
中断回调一般不需要修改，处理一般都是：

1. 关掉GPIO中断使能
1. 释放信号量（触发上层调用read_point读取数据）


### 修改读TP数据回调函数
读TP数据函数的实现一般是：

1. 通过通信接口（比如I2C)读取TP的数据
1. 读取完毕后使能TP中断（触发下一次读取）
1. 将数据转存并返回，**注意：返回值不能始终返回RT_EOK, 否则会陷入死循环。如果读取触控数据结束，请返回RT_EEMPTY。**

```c
static rt_err_t read_point(touch_msg_t p_msg)
{
    gt911_piont_t i2c_result;

    i2c_read_(0x8150, 6, &i2c_result); //通过I2C  读取TP数据
    
    rt_touch_irq_pin_enable(1); //使能TP中断

    /*返回TP数据到p_msg*/
    p_msg->event = i2c_result.status ? TOUCH_EVENT_DOWN : TOUCH_EVENT_UP;
    p_msg->x = i2c_result.x;
    p_msg->y = i2c_result.y;

    return RT_EEMPTY; //RT_EEMPTY - 代表数据已经读完。
}
```


