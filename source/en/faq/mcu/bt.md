# 11 Bluetooth
## 11.1 Disabling BLE Advertising and Modifying the BLE Advertising Interval
Remove the call to: ble_app_advertising_start(); from the ble_peripheral_task function.<br>
As shown in the figure below:
<br>![alt text](./assets/bt/bt001.png)<br>  
Modify the ble advertising interval:<br>
In the ble_app_advertising_start function,
<br>![alt text](./assets/bt/bt002.png)<br>  
para.config.mode_config.conn_config.interval = 0x30; //0x30*0.625=30ms, advertise once every 30ms<br>
0x30 is decimal 48 * 0.625=30ms, advertise once every 30ms.<br>
If you want to change it to advertise once every 500ms, change it to 800.<br>
