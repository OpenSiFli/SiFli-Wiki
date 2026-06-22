# 3 flash调试常见问题
## 3.1 SF32LB551的Flash3调试Nand Flash流程?
SF32LB551 Flash3连接在QSPI3，调试Nand flash注意点：<br> 
1，确保打开QSPI Controller 3 Enable，并设置好内存大小，
下图为128MB（1G bit/）
<br>![alt text](./assets/flash/flash001.png)<br>  
2，由于QSPI3会占用PA49和PA51,因此hcpu的log必须得改成segger输出，具体方法参考 2.2.1 。<br> 
3, 查看QSPI3用到的PA44，PA45，PA47，PA49，PA51，PA55模式设置如下，确认其他地方没有使用这些Pin，确认方法，在Hcpu的shell平台分别用：pin status 44 命令查看各个pin状态是否设置正确。
<br>![alt text](./assets/flash/flash002.png)<br>    
4，打开宏#define DRV_SPI_FLASH_TEST，支持spi_flas读写flash的测试shell命令。<br> 
5，用如下命令测试Flash读写是否正确。<br> 
具体命令参考函数int cmd_spi_flash(int argc, char *argv[])<br> 
```
spi_flash -id 0 2 /*显示flash3的ID，读操作发生在开机初始化，需要上电抓波形 */
spi_flash -read 0 2048 2 /*从flash3 十进制0的地址，读取2048个byte数据*/
spi_flash -read 4096 4096 2 /*从flash3 十进制4096的地址，读取4096个byte数据*/
spi_flash -write 4096 4096 0 2 /*从flash3 十进制地址4096，写4096个byte数据*/<
spi_flash -erase 0x20000 0x20000 2 /*从flash3 十六进制0x20000的地址，擦除0x20000个byte数据，注意只能按块擦除，地址和大小只能0x20000倍数 */<br> 
```
**注意：**<br> 
当今的NAND Flash读/写需要按照一个page，但是必须以block大小擦除，见下图：  
<br>![alt text](./assets/flash/flash003.png)<br>      
每个page有2176个单元，所以每个page就是2048Byte + 128Byte（SA）。<br> 
每个Block有64个page组成，所以每个Block容量为2048x64=131,072（0x20000），即为131,072Byte + 8KByte （SA）<br> 
6，新的flash由于不在nand_cmd_id_pool列表中，采用spi_flash -id 0 2命令去读flash3的id，会返回0xff，<br> 
注意：如果逻辑分析仪抓读ID的时序，需要在上电的时候抓，读ID操作在上电的时候，<br> spi_flash -id 0 2命令只是打印出上电初始化时读到的ID。<br> 
7，把spi_flash -id 0 2命令读回的ID，读回值如下：<br> 
```
 msh >spi_flash -id 0 2
 spi_flash -id 0 2
 rt_flash_read_id_addr: 0x68000000,id:2,value:7fa5a1
 ```
新jlink的elf 驱动，uart3里面在下载0x68000000地址时，目前有添加打印ID的log，<br> 如下图：
<br>![alt text](./assets/flash/flash004.png)<br>   
根据命令方式在nand_table.c中nand_cmd_id_pool列表中添加进对应的组别，如下图：
<br>![alt text](./assets/flash/flash005.png)<br>   
{0xa1, 0xa5, 0x7f, 0, 0x8000000}, //FM25LS01_RDID<br> 
如果命令跟type2的命令一样，就能读写正常，通常修改nand_table.c文件<br> nand_cmd_id_pool和nand_cmd_table_list后，就能进行读擦写操作了。<br> 
8，如果4个Type中，逻辑分析仪抓取的时序跟调试的Nand Flash的几组type时序都不相一致，就需要另外定义一个Type来发时序。<br> 

## 3.2 SF32LB555 Lcpu挂载 Flash4流程
以A3芯片的\watch\sifli\project\ec-lb555_lcpu工程支持挂载flash4为例，参考如下附件差分包，相关修改差分都已经加上：<br> 
需要将\middleware\sifli_lib\lib下面的相关rom lib（A3芯片为sifli_rom_a3.lib，其他版本A0\A1\A2为sifli_rom.lib）文件里面flash相关函数拿掉，不要用rom里面的函数，采用代码中的函数，客户手中的rom lib文件可能版本不一，需要重点检查里面的FLASH相关函数。<br> 
修改\middleware\system下面的bf0_pm_a0.c文件<br> 
修改\rtos\rtthread\bsp\sifli\drivers下面的drv_spi_flash.c文件<br> 
修改\watch\sifli\project\ec-lb555_lcpu\linker_scripts下面的<br> link_lcpu_ram.sct分区文件，将一些算法放进flash4中<br> 
修改\watch\sifli\project\ec-lb555_lcpu的menuconfig，打开QSPI FLASH4支持<br> 
修改\watch\sifli\project\ec-lb555_lcpu下面的postbuild.bat文件，增加新的编译文件bin<br> 
修改\watch\sifli\project\ec-lb555_lcpu下面的SConstruct文件，增加新的编译文件bin<br> 
PS：编译的时候需要将ec-lb555_lcpu下的build手动删除掉，如果之前已经存在了bin<br> 文件，可能会出现编译不过的情况，编译成功之后请检查<br> \watch\sifli\project\ec-lb555_lcpu\build\watch_l.bin下是否增加了ER_IROM2文件：<br> 
<br>![alt text](./assets/flash/flash006.png)<br>   

## 3.3 读Flash内SN/MAC接口
SN和MAC在产线下载版本时写入到设备中，以TLV格式保存，
TLV 是一种常用的数据编码格式，它由标签（Type）、长度（Length）和值（Value）三部分组成，即按照ID+LEN+DATA排放。<br>
数据格式可以参考章节：
[5.6 55X查看芯片工厂校准区OTP/Flash数据方法](../tools/sifli.md#5655X查看芯片工厂校准区OTP)

type |length| value
:--|:--|:--
1byte| 1byte| <=256byte

SN的type编号为：FACTORY_CFG_ID_SN,对应值为2。<br>
value组成：描述符+序号(8byte) 如：sifli_00000001<br>
获取sn示例代码：<br>
```c
{
int res = 0;
char sn[300] = {0};
res = rt_flash_config_read(FACTORY_CFG_ID_SN, (uint8_t) *)&sn[0], 256);
} 
rt_flash_config_read(FACTORY_CFG_ID_SN, (uint8_t *)mac, sizeof(mac));
//获取MAC地址方法
rt_flash_config_read(FACTORY_CFG_ID_MAC, (uint8_t *)&mac[0], 6);
```
<a name="34Flash下载驱动对应关系"></a>
## 3.4 Flash下载驱动对应关系

**Uart下载驱动文件** <br>
Uart下载驱动文件为*.bin文件，如下：<br>
ram_patch_52X.bin --对应52X内部或者外挂Nor Flash的驱动<br>
ram_patch_52X_NAND.bin  --对应52X外部Nand Flash/串口波特率低于6M时用的驱动<br>
ram_patch_52X_NAND_6M.bin --对应52X外部Nand Flash/串口波特率等于6M时用的驱动<br>
ram_patch_52X_NAND_8M.bin --对应52X外部Nand Flash/串口波特率等于8M时用的驱动<br>
ram_patch_52X_NAND_NOBBM.bin -- 对应52X外部Nand Flash不用BBM（不建立坏块管理区Bad Block Manage）的驱动<br>
ram_patch_52X_SD.bin --对应sdio接口的sd-nand/sd-emmc的下载驱动<br>
- IImpeller下载选择和bin的对应关系见`Impeller.ini`内配置
```ini
[UART_DRIVER]
SF32LB55X=ram_patch.bin
SF32LB55X_SD=ram_patch_SD.bin
SF32LB56X=ram_patch_56X.bin
SF32LB56X_NAND=ram_patch_56X_NAND.bin
SF32LB56X_SD=ram_patch_56X_SD.bin
SF32LB52X=ram_patch_52X.bin
SF32LB52X_NAND=ram_patch_52X_NAND.bin
SF32LB52X_SD=ram_patch_52X_SD.bin
SF32LB58X_NAND=ram_patch_58X_NAND.bin
SF32LB58X=ram_patch_58X.bin
SF32LB58X_SD=ram_patch_58X_SD.bin

[UART_DRIVER_8M]
SF32LB56X_NAND=ram_patch_56X_NAND_8M.bin
SF32LB52X_NAND=ram_patch_52X_NAND_8M.bin
SF32LB58X_NAND=ram_patch_58X_NAND_8M.bin
```
**Jlink下载驱动文件** <br>
Jlink下载驱动文件为*.elf文件<br>
位于Jlink的安装目录`C:\Program Files\SEGGER\JLink\Devices\SiFli`或`C:\Users\yourname\AppData\Roaming\SEGGER\JLinkDevices\Devices\SiFli`，打开`cmd.exe`命令行窗口，输入`jlink.exe`，即为Windows系统变量配置用到的Jlink，Impeller用的为该默认Jlink版本
- Jlink烧录驱动对应关系见配置文件`JLinkDevices.xml`<br>
```xml
  <Device>
    <ChipInfo Vendor="SiFli" Name="SF32LB52X_NOR" Core="JLINK_CORE_CORTEX_M33" WorkRAMAddr="0x20000000" WorkRAMSize="0x60000" />
    <FlashBankInfo Name="Internal Flash1" BaseAddr="0x10000000" MaxSize="0x8000000"  Loader="Devices/SiFli/SF32LB52X_INT_FLASH1.elf" LoaderType="FLASH_ALGO_TYPE_OPEN" AlwaysPresent="1"/>
    <FlashBankInfo Name="External Flash2" BaseAddr="0x12000000" MaxSize="0x8000000" Loader="Devices/SiFli/SF32LB52X_EXT_FLASH2.elf" LoaderType="FLASH_ALGO_TYPE_OPEN" AlwaysPresent="1"/>
  </Device>
 
  <Device>
    <ChipInfo Vendor="SiFli" Name="SF32LB52X_NAND" Core="JLINK_CORE_CORTEX_M33" WorkRAMAddr="0x20000000" WorkRAMSize="0x80000" />
    <FlashBankInfo Name="External Nand2" BaseAddr="0x62000000" MaxSize="0x3e000000" Loader="Devices/SiFli/SF32LB52X_EXT_NAND2.elf" LoaderType="FLASH_ALGO_TYPE_OPEN" AlwaysPresent="1"/>
  </Device>
```
**uart_download.bat下载驱动**<br>
在SDK中运行批处理文件`uart_download.bat`时，用的下载Flash驱动为`
\tools\uart_download\ImgDownUart.exe`文件，该串口驱动是集成在`ImgDownUart.exe`中，目前的版本驱动是没有飞离出来，烧录驱动没法自行修改