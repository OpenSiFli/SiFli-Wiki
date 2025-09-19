# 11 Bluetooth
## 11.1 BLE Advertising Disable and BLE Advertising Interval Modification
Remove the call to `ble_app_advertising_start();` in the `ble_peripheral_task` function, as shown in the following figure:
<br>![alt text](./assets/bt/bt001.png)<br>  
To modify the BLE advertising interval:
<br>![alt text](./assets/bt/bt002.png)<br>  
In the `ble_app_advertising_start` function,
<br>para.config.mode_config.conn_config.interval = 0x30; // 0x30 * 0.625 = 30ms advertising interval<br>
0x30 is 48 in decimal * 0.625 = 30ms advertising interval.<br>
To change the interval to 500ms, modify it to 800,<br>