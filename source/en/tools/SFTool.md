# sftool

A command-line utility for SiFli SoC serial tools.

## Overview

sftool is an open-source tool designed for SiFli SoC families. It interacts with chips through a serial interface and supports multiple operations, including writing data to flash and resetting the chip.

## Features

- Supports SF32 series chips
- Supports multiple storage types: NOR flash, NAND flash, and SD cards
- Configurable serial port parameters
- Reliable flash write capability with verification and compression support
- Flexible reset options
- Customizable number of connection attempts

## Installation


### Download Prebuilt Packages

You can download the latest prebuilt sftool from GitHub Releases. The package naming convention is sftool-v{version}-{target}.zip/tar.xz. Select the archive that matches your system architecture.

[GitHub Release](https://github.com/OpenSiFli/sftool/releases)

URL: https://github.com/OpenSiFli/sftool/releases



### Install with Cargo

```bash
cargo install --git https://github.com/OpenSiFli/sftool
```

### Build from Source

```bash
# 克隆仓库
git clone https://github.com/OpenSiFli/sftool.git
cd sftool

# 使用Cargo编译
cargo build --release

# 编译后的二进制文件位于
# ./target/release/sftool
```

## Usage

### Basic Command Format

```bash
sftool [选项] 命令 [命令选项]
```

### Global Options

- `-c, --chip <CHIP>`: Target chip type (currently supports SF32LB52)
- `-m, --memory <MEMORY>`: Memory type [nor, nand, sd] (default: nor)
- `-p, --port <PORT>`: Serial port device path
- `-b, --baud <BAUD>`: Serial baud rate used for flash/write and read operations (default: 1000000)
- `--before <OPERATION>`: Operation before connecting to the chip [no_reset, soft_reset] (default: no_reset)
- `--after <OPERATION>`: Operation after the tool finishes [no_reset, soft_reset] (default: soft_reset)
- `--connect-attempts <ATTEMPTS>`: Number of connection attempts. A negative value or 0 means unlimited attempts (default: 7)
- `--compat` : Compatibility mode. Enable this option if timeout errors occur frequently or verification fails after download.

### Flash Write Command

```bash
# Linux/Mac
sftool -c SF32LB52 -p /dev/ttyUSB0 write_flash [选项] <文件@地址>...
# Windows
sftool -c SF32LB52 -p COM9 write_flash [选项] <文件@地址>...
```

#### Flash Write Options

- `--verify`: Verify the flash data that was just written
- `-u, --no-compress`: Disable data compression during transfer
- `-e, --erase-all`: Erase all flash regions before programming, not only the written region
- `<file@address>`: Binary file and its target address. If the file format contains address information, the @address part is optional

### Examples

Linux/Mac:

```bash
# 写入单个文件到闪存
sftool -c SF32LB52 -p /dev/ttyUSB0 write_flash app.bin@0x12020000

# 写入多个文件到不同地址
sftool -c SF32LB52 -p /dev/ttyUSB0 write_flash bootloader.bin@0x12010000 app.bin@0x12020000 ftab.bin@0x12000000

# 写入并验证
sftool -c SF32LB52 -p /dev/ttyUSB0 write_flash --verify app.bin@0x12020000

# 写入前擦除所有闪存
sftool -c SF32LB52 -p /dev/ttyUSB0 write_flash -e app.bin@0x12020000
```

Windows:

```bash
# 写入多个文件到不同地址
sftool -c SF32LB52 -p /dev/ttyUSB0 write_flash bootloader.bin@0x1000 app.bin@0x12010000 ftab.bin@0x12000000
# 其它同上
```

## Library Usage

sftool also provides a reusable Rust library, `sftool-lib`, which can be integrated into other Rust projects:

```rust
use sftool_lib::{SifliTool, SifliToolBase, WriteFlashParams};

fn main() {
    let mut tool = SifliTool::new(
        SifliToolBase {
            port_name: "/dev/ttyUSB0".to_string(),
            chip: "sf32lb52".to_string(),
            memory_type: "nor".to_string(),
            quiet: false,
        },
        Some(WriteFlashParams {
            file_path: vec!["app.bin@0x10000".to_string()],
            verify: true,
            no_compress: false,
            erase_all: false,
        }),
    );
    
    if let Err(e) = tool.write_flash() {
        eprintln!("Error: {:?}", e);
    }
}
```

## Contributing

Issues and Pull Requests are welcome!

## Project Links

- [GitHub Repository](https://github.com/OpenSiFli/sftool)
- [Documentation](https://docs.rs/sftool)
