# 15 I2S Related
## 15.1 MCLK Output Frequency Doubling
1. Change the SPCLK_DIV division ratio of PLL's 49.152M from 8 to 4, increasing MCLK from 6.144M to 12.288M<br>
```c
#ifdef DOUBLE_MCLK    
    __HAL_I2S_SET_SPCLK_DIV(hi2s, 4);   // set to 12.288M to i2s (49.152M/4=12.288M)  PLL 
#else
    __HAL_I2S_SET_SPCLK_DIV(hi2s, 8);   // set to 6.144M to i2s   PLL
#endif
```
2. Correspondingly, double the duty cycles of bclk and lrck to ensure that after MCLK is doubled, other clock frequencies remain unchanged.  
As shown below, the following values in the CLK_DIV_T structure are all doubled<br>
```c
uint16_t  lr_clk_duty_high;   /*!<  LRCK duty cycle high   */
uint16_t  lr_clk_duty_low;    /*!<  RX LRCK duty cycle low   */
uint16_t  blck_duty;          /*!<  bit clock duty cycle   */
```
Original {48000, 64, 64,  2}, changed to {48000, 128, 128,  4}, other sample rate configurations are modified similarly<br>
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
