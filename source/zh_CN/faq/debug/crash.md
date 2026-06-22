# 4 死机现场保存方法
## 4.1 死机现场保存到FLASH内
1. menuconfig配置<br>
 `(Top) → RTOS → RT-Thread Components → Utilities → Enable save assert context in flash. ` 
<br>![alt text](./assets/crash/crash001.png)<br>

2. 空间分配(文件系统)<br>
在flash_map excel表中配置死机保存所用的空间及分区，以文件方式保存直接SIZE/分区/子目录即可(仅供参考，flash_map excel表，目前仅solution方案支持)，可以自行创建文件存储。
<br>![alt text](./assets/crash/crash002.png)<br>
在flash_map excel表中配置死机保存所用的空间及分区，可以采用共享buffer的方式，在分区里面填写共享buffer的分区名字，地址/SIZE/分区类型使用下图公式自动获取
<br>![alt text](./assets/crash/crash008.png)<br>

3. 数据导出<br>
终端死机后，会保存数据到配置的位置，在重启后可以用手机APP`SiFli_BLE`导出，SiFli APP的安装包apk和源码可以通过github下载：<br>
[SiFli APP Demo Release](https://github.com/OpenSiFli/SiFli_OTA_APP/releases/tag/1.0.10)<br>
[SiFli_OTA_APP Demo](https://github.com/OpenSiFli/SiFli_OTA_APP)

步骤如下：
<br>![alt text](./assets/crash/crash003.png)![alt text](./assets/crash/crash004.png)![alt text](./assets/crash/crash005.png)![alt text](./assets/crash/crash006.png)![alt text](./assets/crash/crash007.png)<br>

4. 数据解析<br>
导出的文件用如下工具解析，即可直接用trace32工具进行死机现场分析
<br>![alt text](./assets/crash/crash010.png)<br>
<br>![alt text](./assets/crash/crash009.png)<br>
分析方法可以参照章节：<br>
[6.2 用Trace32恢复Hcpu死机现场](../tools/trace32.md#Mark_用Trace32恢复Hcpu死机现场)