# 测量结果汇总

表格中 Sniff 模式和 Scan 的电流值为该模式的增量电流，Sleep 为睡眠电流，实际的平均电流等于增量电流与睡眠电流之和，例如 Sniff 模式下，500ms 间隔，attemp=4，10dBm 的发射功率，平均电流为 23+16.6=39.6uA

## BT 功耗

| 模式 | 条件 | 电源电压 3.3V @TXpower=0dBm | 电源电压 3.3V @TXpower=4dBm | 电源电压 3.3V @TXpower=10dBm | 电源电压 3.3V @TXpower=13dBm | 单位 |
|------|------|---------------------------|----------------------------|-----------------------------|-----------------------------|------|
| ∆BT Sniff Mode | 500ms (attempt=4) | 18.6 | 23.4 | 23 | 40.9 | uA |
| ∆Both Scan | Inquiry Scan and Page Scan | 52.6 | 52.6 | 52.6 | 52.6 | uA |
| Sleep | 16.6 | 16.6 | 16.6 | 16.6 | 16.6 | uA |
1. Inquiry Scan 每 2.56s 接收 16.87ms，Page Scan 每 1.28s 接收 16.87ms。
2. bt 500ms sniff@TXpower10dBm：=23+16.6=39.6uA