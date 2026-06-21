# 11 蓝牙
## 11.1 ble广播关闭和ble广播时间修改
ble_peripheral_task函数中去掉: ble_app_advertising_start();调用，<br>
如下图:
<br>![alt text](./assets/bt/bt001.png)<br>  
ble广播时间修改:<br>
ble_app_advertising_start函数中，
<br>![alt text](./assets/bt/bt002.png)<br>  
para.config.mode_config.conn_config.interval = 0x30; //0x30*0.625=30ms广播一次<br>
0x30为十进制48 * 0.625=30ms广播一次.<br>
如果要修改为500ms广播一次， 修改为800，<br>
