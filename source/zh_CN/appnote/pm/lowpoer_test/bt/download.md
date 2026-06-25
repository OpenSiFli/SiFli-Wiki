# 例程编译与烧录
## 编译
进入example\pm\bt\project\hcpu目录，执行 
```
scons --board=sf32lb52-core_n16r16 -j8
```
编译生成HCPU的image文件，编译生成的 image文件保存在 build目录下。
![](assert/image3.png)


## 烧写镜像
在命令行编译的目录下执行 
```
build_sf32lb52-core_n16r16_hcpu\uart_download.bat
```
烧写 build目录下编译生成的镜像文件。

## 改变发射功率
工程默认配置的发射功率是0dbm，可以使用`ble_tx_pwr_save x`命令修改发射功率，x是需要修改的发射功率大小，例如改变发射功率为10dbm：`ble_tx_pwr_save 10` 。改完后会自动重启生效。