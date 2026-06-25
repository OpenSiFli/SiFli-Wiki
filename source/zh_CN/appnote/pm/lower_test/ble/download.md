# 例程编译与烧写
## 编译
如果使用已编译好的 image 文件，可以直接跳到烧录部分进行烧录开始测试。

进入example\pm\bt\project\hcpu目录，执行
```
scons --board=sf32lb52-core_n16r16 -j8 
```
编译生成HCPU的image文件(不需要单独编译LCPU 的工程，编译 HCPU 时会自动编译 LCPU 并打包 LCPU 的 bin 到 HCPU 的镜像中)，编译生成的 image 文件保存在 build 目录下。

![](assert/image3.png)


## 烧写镜像
在命令行编译的目录下执行 
```
build_sf32lb52-core_n16r16_hcpu\uart_download.bat 
```
烧写 build 目录下编译生成的镜像文件。

## 改变发射功率
工程默认配置的发射功率是0dbm，可以使用`ble_tx_pwr_save x`命令修改发射功率，x是需要修改的发射功率大小，例如改变发射功率为10dbm：`ble_tx_pwr_save 10` 。改完后会自动重启生效。