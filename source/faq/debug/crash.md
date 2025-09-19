# 4 Methods for Saving Crash Dump
## 4.1 Saving Crash Dump to FLASH
1. menuconfig Configuration<br>
 `(Top) → RTOS → RT-Thread Components → Utilities → Enable save assert context in flash. ` 
<br>![alt text](./assets/crash/crash001.png)<br>

2. Space Allocation (File System)<br>
Configure the space and partition for crash dump in the flash_map excel table. For file-based saving, you can directly specify SIZE/partition/subdirectory (for reference, the flash_map excel table is currently supported only by solution schemes). You can also create your own file storage.
<br>![alt text](./assets/crash/crash002.png)<br>
In the flash_map excel table, configure the space and partition for crash dump. You can use a shared buffer by specifying the partition name of the shared buffer in the partition field. The address/SIZE/partition type can be automatically obtained using the formula shown in the following image.
<br>![alt text](./assets/crash/crash008.png)<br>

3. Data Export<br>
After a terminal crash, the data will be saved to the configured location. After rebooting, you can export the data using the `SiFli_BLE` mobile app. The installation package (apk) and source code for the SiFli app can be downloaded from GitHub:<br>
[SiFli APP Demo Release](https://github.com/OpenSiFli/SiFli_OTA_APP/releases/tag/1.0.10)<br>
[SiFli_OTA_APP Demo](https://github.com/OpenSiFli/SiFli_OTA_APP)

The steps are as follows:
<br>![alt text](./assets/crash/crash003.png)![alt text](./assets/crash/crash004.png)![alt text](./assets/crash/crash005.png)![alt text](./assets/crash/crash006.png)![alt text](./assets/crash/crash007.png)<br>

4. Data Parsing<br>
Use the following tool to parse the exported file, and you can then analyze the crash dump using the trace32 tool.
<br>![alt text](./assets/crash/crash010.png)<br>
<br>![alt text](./assets/crash/crash009.png)<br>
For analysis methods, refer to the section:<br>
[6.2 Using Trace32 to Restore Hcpu Crash Dump](../tools/trace32.md#Mark_Using_Trace32_to_Restore_Hcpu_Crash_Dump)