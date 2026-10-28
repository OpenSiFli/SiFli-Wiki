# bin2bmp 工具

## 工具简介

`bin2bmp` 是一个把**显存原始二进制数据**直接还原为 **BMP 图片**的调试小工具，常用于以下场景：

* 屏幕显示异常时，直接查看 LVGL 实际写入 framebuffer 的内容，确认问题出在 **LVGL 渲染** 还是 **LCD 驱动/屏本身**
* 没有截屏接口的板子上，把当前屏幕内容"抓"出来作为图片保存
* 验证双 buffer 切换、部分刷新（partial refresh）等逻辑是否符合预期

工具位于 SDK 的 `tools/bin2bmp/` 目录下，包含三个文件：

| 文件 | 作用 |
| --- | --- |
| `bmp.py` | BMP 图片生成与像素格式转换的核心库 |
| `bin2bmp.py` | **离线**方式：把已有的 `.bin` 文件转换为 BMP |
| `jlinkbin2bmp.py` | **在线**方式：通过 J-Link 直接从板子内存 dump framebuffer，再转 BMP |

## 工作原理

整个流程可以理解为"内存 → bin 文件 → BMP 图片"两步：

```
┌──────────┐   J-Link/SWD   ┌────────────┐   bin2bmp   ┌─────────┐
│  板子内存  │ ────────────▶ │  xxx.bin   │ ──────────▶ │ xxx.bmp │
│ framebuffer│   (savebin)   │ (原始数据)  │  (像素解码)  │ (图片)   │
└──────────┘                └────────────┘             └─────────┘
```

* `jlinkbin2bmp.py` 一键完成上面两步：先调用 `JLink.exe` 的 `savebin` 命令把指定地址的内存保存为 `.bin`，再调用 `bmp.py` 把 `.bin` 解码成 `.bmp` 并自动打开
* `bin2bmp.py` 只做第二步，用于已经手上已经有 `.bin` 文件的情况（比如之前 dump 下来的、或别人发过来的）

## 支持的颜色格式

工具支持 framebuffer 中常见的像素格式，**必须与当前工程实际使用的格式一致**，否则解出来的图会是杂色条纹。

| 格式 | 位深 (bit) | 每像素字节数 | 说明 |
| --- | --- | --- | --- |
| `a8` | 8 | 1 | 8 位 alpha，单色（默认红色）加透明度 |
| `a4` | 4 | 0.5 | 4 位 alpha，2 像素/字节 |
| `a2` | 2 | 0.25 | 2 位 alpha，4 像素/字节 |
| `rgb332` | 8 | 1 | R3G3B2 |
| `rgb565` | 16 | 2 | R5G6B5 |
| `bgr565` | 16 | 2 | B5G6R5 |
| `argb8565` | 24 | 3 | A8 + R5G6B5 |
| `rgb888` | 24 | 3 | R8G8B8 |
| `argb8888` | 32 | 4 | A8R8G8B8 |
| `rgba8888` | 32 | 4 | R8G8B8A8 |
| `yuyv` | 16 | 2 | YUV 4:2:2 packed (Y0 U Y1 V) |
| `uyvy` | 16 | 2 | YUV 4:2:2 packed (U Y0 V Y1) |

## 使用准备

1. **Python 3**：直接 `python xxx.py` 即可运行，无需安装额外依赖（只用标准库）
2. **J-Link**：使用 `jlinkbin2bmp.py` 时需要安装 [SEGGER J-Link](https://www.segger.com/downloads/jlink/) 并保证 `JLink.exe` 在 PATH 中
3. **板子已通过 SWD 连接 J-Link**，并且固件处于运行状态

下面以 SDK 自带的 `example/multimedia/lvgl/watch` 例程（板型 `sf32lb58-lcd_a128r32n1`，屏幕 390×450，RGB888）为例，完整走一遍流程。

## 方式一（推荐）：jlinkbin2bmp.py 在线 dump

这是最常用的方式，一条命令搞定，dump 完成后会自动打开生成的 BMP。

### 步骤 1：从 map 文件找到 framebuffer 地址

编译完成后，在工程的 build 目录下会生成 `main.map`，里面记录了所有全局/静态变量的链接地址。framebuffer 变量命名规则如下：

| 变量名 | 位置 | 用途 |
| --- | --- | --- |
| `buf1_1`, `buf1_2` | L1 SRAM（0x2000xxxx） | LVGL **部分刷新**用的绘制 buffer，高度由 `LV_FB_LINE_NUM` 决定，**不是全屏** |
| `buf2_1`, `buf2_2` | L2 PSRAM（0x62xxxxxx） | **全屏** framebuffer，用于 RAMLESS 屏或 `BSP_USING_LCD_FRAMEBUFFER` 模式 |

> **想看"屏幕上完整的画面"，应该 dump `buf2_1` / `buf2_2`；`buf1_x` 只是 LVGL 的绘制 staging buffer，只能看到当前正在刷新的几行。**

在 watch 例程的 `main.map` 中搜索 `frambuf` 关键字，可以看到：

```text
 .bss.l1_non_ret_bss_frambuf
                0x2000ef50    0x3ed78 .../middleware/lvgl/lv_drivers/lv_lcd.o
 ...
 .bss.l2_non_ret_bss_anim_frambuf
                0x62000000   0x101148 .../middleware/lvgl/app_mem.o
 *fill*         0x62101148       0x38
 .bss.l2_non_ret_bss_frambuf
                0x62101180   0x101164 .../middleware/lvgl/lv_drivers/lv_lcd.o
```

解读：

* **buf2_1 起始地址 = `0x62101180`**（l2_non_ret_bss_frambuf 段的起始地址就是 buf2_1）
* 段总大小 0x101164 = 1053028 字节 ≈ 2 个 390×450×3 的全屏 buffer 加对齐填充
* buf2_2 紧跟在 buf2_1 之后（64 字节对齐），偏移 = `ALIGN(390*450*3, 64)` = 0x808C0，因此 **buf2_2 = `0x62101180 + 0x808C0` = `0x62181A40`**

```{note}
不同工程、不同屏幕分辨率、不同颜色格式，地址都不一样。**每次重新编译后地址都可能变化**，请以当前 build 目录下最新的 `main.map` 为准。
```

### 步骤 2：确认颜色格式和分辨率

打开 build 目录下的 `.config` 文件，搜索以下关键字：

```text
CONFIG_LCD_HOR_RES_MAX=390          # 屏幕水平分辨率
CONFIG_LCD_VER_RES_MAX=450          # 屏幕垂直分辨率
CONFIG_LV_COLOR_DEPTH_24=y          # 24bit = RGB888，每像素 3 字节
# CONFIG_LV_COLOR_DEPTH_16 is not set
```

| LV_COLOR_DEPTH | 对应 jlinkbin2bmp 颜色格式参数 |
| --- | --- |
| 16 | `rgb565` |
| 24 | `rgb888` |
| 32 | `argb8888` |

本例：分辨率 390×450，颜色格式 `rgb888`。

### 步骤 3：执行 dump 命令

进入 SDK 的 `tools/bin2bmp/` 目录，执行：

```bash
cd tools/bin2bmp
python jlinkbin2bmp.py "-if SWD -speed 12000" rgb888 390 450 62101180
```

参数说明：

| 参数 | 含义 |
| --- | --- |
| 第 1 个参数 | 传给 J-Link 的连接参数，本地 USB 连接用 `"-if SWD -speed 12000"`；如果走 UsartServer 远程转发，用 `"-ip 127.0.0.1:19025 -if SWD -speed 1000"` |
| 第 2 个参数 | 颜色格式（小写） |
| 第 3 / 4 个参数 | 宽 / 高（像素） |
| 第 5 个参数 | framebuffer 起始地址（**十六进制，不带 `0x` 前缀也可以**） |

执行过程会输出 J-Link 的连接日志，最后 `Reading 526500 bytes from addr 0x62101180 into file...O.K.` 表示 dump 成功，随后脚本会自动调用系统默认图片查看器打开生成的 BMP。

### 步骤 4：查看结果

下面两张图就是跑 `example/multimedia/lvgl/watch` 例程的板子，依次 dump `buf2_1` 和 `buf2_2` 拿到的结果——正是手表 demo 的主菜单界面：

```{figure} assets/bin2bmp_buf2_1.png
:scale: 60%

buf2_1（地址 0x62101180）内容：手表主菜单
```

```{figure} assets/bin2bmp_buf2_2.png
:scale: 60%

buf2_2（地址 0x62181A40）内容：与 buf2_1 一致（静态画面时双 buffer 内容相同）
```

```{note}
静态画面下两个 buffer 内容一致；动画/滑动过程中两个 buffer 会一新一旧交替，这是正常现象，正好可以用这个工具观察双 buffer 切换时机。
```

## 方式二：bin2bmp.py 离线转换

如果手上已经有 dump 好的 `.bin` 文件（比如之前保存的、或同事发过来的），直接用 `bin2bmp.py` 转换：

```bash
python bin2bmp.py hcpu_ram.bin rgb565 454 454 2000
```

参数说明：

| 参数 | 含义 |
| --- | --- |
| 第 1 个参数 | bin 文件路径 |
| 第 2 个参数 | 颜色格式 |
| 第 3 / 4 个参数 | 宽 / 高（像素） |
| 第 5 个参数（可选） | **偏移量**（十六进制字符串，如 `2000` 表示从文件 0x2000 偏移处开始解析；不填默认为 0） |

生成的 BMP 文件名格式为 `<bin文件名>_offset0x<偏移>_<宽>x<高>_<格式>.bmp`，会自动用系统默认看图工具打开。

## 常见问题

### 解出来全是杂色条纹

* **颜色格式填错**：例如实际是 RGB565 却填了 rgb888，每像素字节数对不上，整个画面会错乱。请回到 `.config` 确认 `LV_COLOR_DEPTH`
* **分辨率填错**：宽高任意一个不对都会出现斜条纹。请确认 `.config` 中的 `LCD_HOR_RES_MAX` / `LCD_VER_RES_MAX`

### 图像整体左右/上下偏移

* **地址没对准 buffer 起始地址**：检查 map 文件中的地址是否抄错；如果 dump 的是 buf2_2，要确认是否算上了 64 字节对齐的填充

### 解出来全黑 / 全白 / 全 0

* 该 buffer 当前没有被使用。比如工程配置为单 buffer（`LV_FB_ONE_NOT_SCREEN_SIZE`），`buf1_2` 就不存在；或双 buffer 中当前只有一块在被刷新
* 屏幕当前确实显示纯黑/纯白画面（比如息屏、启动 logo 阶段）

### 图像上下颠倒

BMP 文件本身按"底向上"存储像素，工具已经做了翻转处理。如果仍然颠倒，多半是把部分 buffer 的高度填错了，请检查 `LV_FB_LINE_NUM` 与实际使用方式。

### J-Link 连接失败

* 检查 SWD 连线、板子是否上电
* 检查是否有其他程序（Ozone、J-Flash、Keil 调试器等）占用了 J-Link
* 远程场景下确认 UsartServer 已启动并监听对应端口

## 提示与技巧

* **想看动画中间帧**：在动画播放过程中执行 dump，buf2_1 和 buf2_2 的内容会不一样，分别代表"正在显示的"和"正在绘制的"那一帧
* **想看部分刷新区域**：dump `buf1_1`（高度为 `LV_FB_LINE_NUM` 行），可以看到 LVGL 当前正在合成的那一段画面
* **批量保存分析**：`jlinkbin2bmp.py` 每次都会生成 `<地址>_<宽>x<高>_<格式>.bmp`，文件名自带参数，方便归档对比

## 相关工具

* [SFTool](SFTool.md) —— 烧录与串口日志
* [UsartServer](index.md) —— UART 转 J-Link 远程调试（56x/52x 平台）
* [图形转换工具](图形转换工具.md) —— 离线图片/视频资源转换
