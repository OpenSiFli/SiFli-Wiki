# Modify the screen TP driver


(modify_tp_c_file)=
## Modify the copied TP driver file
### Modify the registered semaphore name
```c
static int rt_tp_device_init(void)
{
    ...
    driver.isr_sem = rt_sem_create("gt911", 0, RT_IPC_FLAG_FIFO); //修改这个信号量名称为gt911
    rt_touch_drivers_register(&driver);
    return 0;
}
```

### Modify the communication interface in the probe function
The Probe function generally performs several tasks:

1. Open the communication interface (such as I2C), and configure the interface frequency, timeout, and so on
2. Read a register and return the status according to whether the TP is present (for example, a TP status register). If compatibility with multiple TP drivers is not required, you can directly return RT_EOK (TP present))

### Modify the Init function
The driver initialization function mainly does the following:

1. Reset TP
2. Configure the trigger condition of the TP interrupt GPIO, and register the interrupt callback handler

**It is recommended to use the following interfaces and not use rt_pin_xxx interfaces:**
 - rt_touch_irq_pin_attach(PIN_IRQ_MODE_FALLING, irq_handler, NULL);  TP interrupt registration
 - rt_touch_irq_pin_enable(v)      Interrupt enable and disable


### Modify the interrupt callback function
The interrupt callback generally does not need to be modified. It usually performs the following:

1. Disable the GPIO interrupt
1. Release the semaphore (triggering the upper layer to call read_point to read data)


### Modify the callback function for reading TP data
The implementation of the TP data read function is generally:

1. Read TP data through the communication interface (such as I2C)
1. After reading is complete, enable the TP interrupt (to trigger the next read)
1. Transfer and return the data. **Note: the return value must not always be RT_EOK, otherwise it will fall into an infinite loop. If touch data reading is complete, return RT_EEMPTY.**

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
