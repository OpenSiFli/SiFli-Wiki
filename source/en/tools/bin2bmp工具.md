# bin2bmp Tool

## Tool Overview

`bin2bmp` is a small debugging utility that converts raw framebuffer binary data back into BMP images. Common use cases include:

* When the screen display is abnormal, directly inspect what LVGL actually wrote into the framebuffer — to decide whether the problem lies in **LVGL rendering** or **the LCD driver / panel itself**
* Capture the current screen content as an image on boards that do not have a dedicated screenshot interface
* Verify dual-buffer switching, partial refresh, and other display logic

The tool lives under `tools/bin2bmp/` in the SDK and consists of three files:

| File | Purpose |
| --- | --- |
| `bmp.py` | Core library for BMP generation and pixel format conversion |
| `bin2bmp.py` | **Offline** mode: convert an existing `.bin` file into a BMP |
| `jlinkbin2bmp.py` | **Online** mode: dump the framebuffer directly from the board via J-Link, then convert to BMP |

## How It Works

The whole flow is a two-step pipeline: "memory → bin file → BMP image":

```
┌────────────┐   J-Link/SWD   ┌────────────┐   bin2bmp    ┌─────────┐
│ Board RAM   │ ────────────▶ │  xxx.bin   │ ──────────▶ │ xxx.bmp │
│ framebuffer │   (savebin)   │ (raw data) │  (decode)    │ (image) │
└────────────┘               └────────────┘              └─────────┘
```

* `jlinkbin2bmp.py` does both steps in one shot: it first invokes `JLink.exe`'s `savebin` command to dump a memory range into a `.bin` file, then calls `bmp.py` to decode that `.bin` into a `.bmp` and opens it automatically.
* `bin2bmp.py` only does the second step — useful when you already have a `.bin` file on hand (a previous dump, or one shared by a colleague).

## Supported Pixel Formats

The tool supports the pixel formats commonly found in framebuffers. **The format argument must match the project's actual configuration**, otherwise the decoded image will look like scrambled color stripes.

| Format | Bit depth | Bytes/pixel | Description |
| --- | --- | --- | --- |
| `a8` | 8 | 1 | 8-bit alpha, monochrome (default red) + transparency |
| `a4` | 4 | 0.5 | 4-bit alpha, 2 pixels per byte |
| `a2` | 2 | 0.25 | 2-bit alpha, 4 pixels per byte |
| `rgb332` | 8 | 1 | R3G3B2 |
| `rgb565` | 16 | 2 | R5G6B5 |
| `bgr565` | 16 | 2 | B5G6R5 |
| `argb8565` | 24 | 3 | A8 + R5G6B5 |
| `rgb888` | 24 | 3 | R8G8B8 |
| `argb8888` | 32 | 4 | A8R8G8B8 |
| `rgba8888` | 32 | 4 | R8G8B8A8 |
| `yuyv` | 16 | 2 | YUV 4:2:2 packed (Y0 U Y1 V) |
| `uyvy` | 16 | 2 | YUV 4:2:2 packed (U Y0 V Y1) |

## Prerequisites

1. **Python 3**: run `python xxx.py` directly — no third-party packages required (uses only the standard library).
2. **J-Link**: when using `jlinkbin2bmp.py`, install [SEGGER J-Link](https://www.segger.com/downloads/jlink/) and make sure `JLink.exe` is on your PATH.
3. **The board is connected to J-Link via SWD and the firmware is running.**

Below we walk through a complete example using the `example/multimedia/lvgl/watch` sample from the SDK (board `sf32lb58-lcd_a128r32n1`, screen 390×450, RGB888).

## Method 1 (Recommended): jlinkbin2bmp.py — Online Dump

This is the most common workflow. One command does everything and opens the resulting BMP automatically.

### Step 1: Find the framebuffer address in main.map

After a successful build, `main.map` is generated in the build directory. It contains the link addresses of all global and static variables. The framebuffer variables follow a predictable naming pattern:

| Variable | Location | Purpose |
| --- | --- | --- |
| `buf1_1`, `buf1_2` | L1 SRAM (0x2000xxxx) | LVGL **partial refresh** drawing buffers. Height = `LV_FB_LINE_NUM` lines — **not full screen size**. |
| `buf2_1`, `buf2_2` | L2 PSRAM (0x62xxxxxx) | **Full-screen** framebuffers, used in RAMLESS LCD mode or when `BSP_USING_LCD_FRAMEBUFFER` is enabled. |

> **If you want to see what is actually on the screen, dump `buf2_1` / `buf2_2`. `buf1_x` is just LVGL's staging buffer — it only holds a few rows of the current refresh region.**

Search for the keyword `frambuf` in the watch sample's `main.map`:

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

Reading this:

* **buf2_1 starts at `0x62101180`** — that is the start of the `l2_non_ret_bss_frambuf` section.
* Section size 0x101164 = 1,053,028 bytes ≈ two 390×450×3 full-screen buffers plus alignment padding.
* buf2_2 immediately follows buf2_1 (64-byte aligned). Offset = `ALIGN(390*450*3, 64)` = 0x808C0, therefore **buf2_2 = `0x62101180 + 0x808C0` = `0x62181A40`**.

```{note}
Different projects, screen resolutions, and color depths produce different addresses. **Addresses can also change between builds** — always use the latest `main.map` from your current build directory.
```

### Step 2: Confirm color format and resolution

Open the `.config` file in the build directory and search for:

```text
CONFIG_LCD_HOR_RES_MAX=390          # horizontal resolution
CONFIG_LCD_VER_RES_MAX=450          # vertical resolution
CONFIG_LV_COLOR_DEPTH_24=y          # 24-bit = RGB888, 3 bytes per pixel
# CONFIG_LV_COLOR_DEPTH_16 is not set
```

| LV_COLOR_DEPTH | Corresponding jlinkbin2bmp format argument |
| --- | --- |
| 16 | `rgb565` |
| 24 | `rgb888` |
| 32 | `argb8888` |

For this example: resolution 390×450, color format `rgb888`.

### Step 3: Run the dump command

From the SDK root:

```bash
cd tools/bin2bmp
python jlinkbin2bmp.py "-if SWD -speed 12000" rgb888 390 450 62101180
```

Argument breakdown:

| # | Meaning |
| --- | --- |
| 1 | Connection parameters passed to J-Link. For direct USB use `"-if SWD -speed 12000"`; for remote access via UsartServer use `"-ip 127.0.0.1:19025 -if SWD -speed 1000"`. |
| 2 | Pixel format (lowercase). |
| 3 / 4 | Width / height in pixels. |
| 5 | Framebuffer start address in hex (the `0x` prefix is optional). |

You will see J-Link connection logs. The line `Reading 526500 bytes from addr 0x62101180 into file...O.K.` confirms a successful dump, and the script then opens the generated BMP with your system's default image viewer.

### Step 4: Inspect the result

The two images below are actual dumps from the `example/multimedia/lvgl/watch` sample running on the board — they show the watch main-menu UI:

```{figure} assets/bin2bmp_buf2_1.png
:scale: 60%

buf2_1 (address 0x62101180): watch main menu
```

```{figure} assets/bin2bmp_buf2_2.png
:scale: 60%

buf2_2 (address 0x62181A40): identical to buf2_1 (static frame, both buffers are in sync)
```

```{note}
When the frame is static, both buffers have the same content. During animations or scrolling they alternate between an "old" and a "new" frame, which is exactly how you can observe the dual-buffer swap timing with this tool.
```

## Method 2: bin2bmp.py — Offline Conversion

Use `bin2bmp.py` when you already have a `.bin` file on hand (saved previously, or received from a colleague):

```bash
python bin2bmp.py hcpu_ram.bin rgb565 454 454 2000
```

Argument breakdown:

| # | Meaning |
| --- | --- |
| 1 | Path to the bin file. |
| 2 | Pixel format. |
| 3 / 4 | Width / height in pixels. |
| 5 (optional) | **Offset** in hex (e.g. `2000` means start parsing from byte 0x2000 inside the file; default is 0). |

The output BMP is named `<bin_filename>_offset0x<offset>_<width>x<height>_<format>.bmp` and opens with the system's default image viewer.

## FAQ

### The decoded image is full of color stripes

* **Wrong pixel format.** For example, RGB565 misinterpreted as RGB888 throws off every pixel boundary. Go back to `.config` and double-check `LV_COLOR_DEPTH`.
* **Wrong resolution.** Either dimension being incorrect produces diagonal stripes. Confirm `LCD_HOR_RES_MAX` / `LCD_VER_RES_MAX` in `.config`.

### The whole image is shifted left/right or up/down

* **The address does not point at the true buffer start.** Re-read `main.map`. If you are dumping `buf2_2`, make sure you accounted for the 64-byte alignment padding that follows buf2_1.

### The decoded image is all black / all white / all zeros

* That particular buffer is not currently in use. For example, a single-buffer configuration (`LV_FB_ONE_NOT_SCREEN_SIZE`) means `buf1_2` does not exist, or one of the dual buffers may just not be the one actively being refreshed.
* The screen genuinely shows a pure black/white frame (e.g. during boot logo or blanking).

### The image is upside down

BMP files store pixels bottom-up, and the tool already handles the flip. If it still looks inverted, the height argument is most likely wrong — check whether you are reading a partial buffer (`LV_FB_LINE_NUM`) or a full-screen buffer.

### J-Link connection fails

* Check the SWD wiring and that the board is powered.
* Verify no other program (Ozone, J-Flash, Keil debugger, etc.) is holding the J-Link.
* For remote access, confirm UsartServer is running and listening on the expected port.

## Tips and Tricks

* **Capture intermediate animation frames.** Run the dump while an animation is playing — `buf2_1` and `buf2_2` will differ, showing the "currently displayed" and "currently being drawn" frames respectively.
* **Inspect partial refresh regions.** Dump `buf1_1` (height = `LV_FB_LINE_NUM` rows) to see the slice LVGL is currently composing.
* **Batch dumps for comparison.** `jlinkbin2bmp.py` always names the file with `<address>_<width>x<height>_<format>.bmp`, so archives are self-documenting.

## Related Tools

* [SFTool](SFTool.md) — flashing and serial log tool
* [UsartServer](index.md) — UART-to-J-Link relay for remote debugging (56x/52x platforms)
* [Graphics Conversion Tool](图形转换工具.md) — offline image and video asset conversion
