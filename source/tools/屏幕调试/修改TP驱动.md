# Modify Screen TP Driver


(modify_tp_c_file)=
## Modify the Copied TP Driver File
### Modify the Registered Semaphore Name
```c
static int rt_tp_device_init(void)
{
    ...
    driver.isr_sem = rt_sem_create("gt911", 0, RT_IPC_FLAG_FIFO); // Modify this semaphore name to gt911
    rt_touch_drivers_register(&driver);
    return 0;
}
```

### Modify the Communication Interface in the Probe Function
The probe function generally does the following:

1. Open the communication interface (e.g., I2C), configure the interface frequency, timeout, etc.
2. Read a specific register to check if the TP is present (e.g., a status register of the TP) and return the status. (If multi-TP driver compatibility is not required, you can directly return RT_EOK (TP is present))

### Modify the Init Function
The initialization function of the driver mainly does the following:

1. Reset the TP
2. Configure the TP interrupt GPIO trigger conditions and register the interrupt callback handler

**It is recommended to use the following interfaces, do not use rt_pin_xxx interfaces:**
 - rt_touch_irq_pin_attach(PIN_IRQ_MODE_FALLING, irq_handler, NULL);  TP interrupt registration
 - rt_touch_irq_pin_enable(v)      Enable and disable interrupts


### Modify the Interrupt Callback Function
The interrupt callback generally does not need to be modified, and the handling is usually:

1. Disable the GPIO interrupt
1. Release the semaphore (trigger the upper layer to call read_point to read the data)


### Modify the Read TP Data Callback Function
The implementation of the read TP data function is generally:

1. Read the TP data through the communication interface (e.g., I2C)
1. Re-enable the TP interrupt after reading (trigger the next read)
1. Store and return the data, **Note: The return value should not always be RT_EOK, otherwise it will result in an infinite loop. If the touch data read is complete, return RT_EEMPTY.**

```c
static rt_err_t read_point(touch_msg_t p_msg)
{
    gt911_piont_t i2c_result;

    i2c_read_(0x8150, 6, &i2c_result); // Read TP data via I2C
    
    rt_touch_irq_pin_enable(1); // Enable TP interrupt

    /* Return TP data to p_msg */
    p_msg->event = i2c_result.status ? TOUCH_EVENT_DOWN : TOUCH_EVENT_UP;
    p_msg->x = i2c_result.x;
    p_msg->y = i2c_result.y;

    return RT_EEMPTY; // RT_EEMPTY - indicates that the data has been read.
}
```