# 15 I2S相关
## 15.1 MCLK输出频率翻倍
1，PLL的49.152M分频比SPCLK_DIV从8变为4，MCLK从6.144M提高到12.288M<br>
```c
#ifdef DOUBLE_MCLK    
    __HAL_I2S_SET_SPCLK_DIV(hi2s, 4);   // set to 12.288M to i2s (49.152M/4=12.288M)  PLL 
#else
    __HAL_I2S_SET_SPCLK_DIV(hi2s, 8);   // set to 6.144M to i2s   PLL
#endif
```
2，对应的bclk duty还有lrck duty都提高一倍，这样保证MCLK翻倍后，其他时钟频率保持不变
如下，对应结构体中CLK_DIV_T的如下值都提高一倍<br>
```c
uint16_t  lr_clk_duty_high;   /*!<  LRCK duty cycle high   */
uint16_t  lr_clk_duty_low;    /*!<  RX LRCK duty cycle low   */
uint16_t  blck_duty;          /*!<  bit clock duty cycle   */
```
原{48000, 64, 64,  2},修改为{48000, 128, 128,  4},其他采样率配置也一样修改<br>
```c
#ifdef DOUBLE_MCLK
static CLK_DIV_T  txrx_clk_div[9]  = {{48000, 128, 128,  4}, {44100, 128, 128,  4}, {32000, 192, 192,  6}, {24000, 256, 256, 8}, {22050, 256, 256,  8},
    {16000, 384, 384, 12}, {12000, 512, 512, 16}, {11025, 512, 512, 16}, { 8000, 768, 768, 24}
};
#else
static CLK_DIV_T  txrx_clk_div[9]  = {{48000, 64, 64,  2}, {44100, 64, 64,  2}, {32000, 96, 96,  3}, {24000, 128, 128, 4}, {22050, 128, 128,  4},
    {16000, 192, 192, 6}, {12000, 256, 256, 8}, {11025, 256, 256, 8}, { 8000, 384, 384, 12}
};
```

