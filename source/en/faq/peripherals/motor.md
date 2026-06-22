# 4 Common Motor Debugging Issues
## 4.1 Configuration for GPIO-Emulated Motor Vibration
Considering that the motor may be driven by any IO pin, the solution code implements GPIO-based motor driving code.<br>
Macro after menuconfig configuration in rtconfig.h:<br>
```c
#define MOTOR_ENABLED 1 //启动马达
/* MOTOR_USE_PWM is not set */
#define MOTOR_PERIOD 200  //马达震动周期
#define MOTOR_POWER_IO -1 //马达开电，没有开电控制配置为-1
#define MOTOR_SW_CONTRL 1 //使能软件控制马达
#define MOTOR_CTRL_IO 121  // 配置为121-96 =PB25为马达驱动口
```
You can use the following test code to test the motor function:<br>
finsh serial command: motor set 1 8 4<br>
Parameters: 1 means start motor, 8 means vibrate 8 times, and 4 means 40% duty cycle.<br>
The actual drive waveform is shown below:<br>
<br>![alt text](./assets/motor/motor001.png)<br>   
```c
#ifdef RT_USING_FINSH
int motor(int argc, char **argv)
{
char i;
 if (argc > 1)
 {
 if (strcmp("on", argv[1]) == 0)
 {
	 rt_kprintf("motor on!\n");
	 app_start_motor();
 	 app_set_motor_level(MOTOR_TEN_LEVEL);
 }
 else if (strcmp("off", argv[1]) == 0)
 {
	 rt_kprintf("motor off!\n"); 
	 app_stop_motor();
 }
 else if (strcmp("set", argv[1]) == 0)
 {
 	uint32_t mode = strtoul(argv[2], 0, 16);
	uint32_t time = strtoul(argv[3], 0, 16);
	uint32_t level = strtoul(argv[4], 0, 16);	
	rt_kprintf("turn on mode:%d,time:%d,level:%d\n",mode,time,level);
 	app_set_motor_level(level);	
	app_motor_control(mode,time);
 } 
 else
 {
 	rt_kprintf("command is err!\n");
	rt_kprintf("example:\n motor on\n motor off\n motor set 1 50\n");
 }
 }
 return 0;
}
MSH_CMD_EXPORT(motor, forward motor command); /* 导出到 msh 命令列表中 */
#endif
对应的占空比级别为
const app_motor_grade_t g_motor_level[MOTOR_MAX_LEVEL - 1] =
{
    {MOTOR_PERIOD, MOTOR_PERIOD / 10},
    {MOTOR_PERIOD, (MOTOR_PERIOD / 10) * 2},
    {MOTOR_PERIOD, (MOTOR_PERIOD / 10) * 3},
    {MOTOR_PERIOD, (MOTOR_PERIOD / 10) * 4},
    {MOTOR_PERIOD, (MOTOR_PERIOD / 10) * 5},
    {MOTOR_PERIOD, (MOTOR_PERIOD / 10) * 6},
    {MOTOR_PERIOD, (MOTOR_PERIOD / 10) * 7},
    {MOTOR_PERIOD, (MOTOR_PERIOD / 10) * 8},
    {MOTOR_PERIOD, (MOTOR_PERIOD / 10) * 9},
    {MOTOR_PERIOD, (MOTOR_PERIOD / 10) * 10},
};
```
