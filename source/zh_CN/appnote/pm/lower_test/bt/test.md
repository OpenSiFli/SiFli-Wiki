# 测试说明
使用 BT 例程可以测试 Scan 和 Sniff 模式的功耗，系统上电后测试例程自动开启 Scan 和 ADV，使用手机连接蓝牙设备，在 HCPU 的 console 里可以发送命令修改配置，发送的命令都需以回车换行结尾。

PC与调试板使用 USB Type-C线连接后会枚举出两个串口，其中 HCPU使用第二个串口作为 console端口，如下图所示。

![](assert/image1.png)

串口设置参见下图，波特率均设置为 1000000。

![](assert/image2.png)

为便于控制测试条件，使用 PA24作为 HCPU的唤醒 PIN。当唤醒 PIN为低电平时 HCPU无法进入低功耗模式，此时可以通过 console给 HCPU发送命令修改参数，当 PA24悬空或者接高电平（即 3.3V电压，下文如未特别说明，高电平均指 3.3V电压）时，HCPU进入低功耗模式，LCPU则周期性的进出低功耗模式，此时 console无法使用。

测试例程 LCPU的主频为 24MHz，HCPU的低功耗模式为 Deepsleep，LCPU的低功耗模式为 Standby。HCPU使用 btskey命令操作菜单修改配置。
