# DSI screen parameter configuration

For basic MIPI knowledge, refer to the following articles. MIPI DSI basics are not described in detail here.
- [MIPI Basics -- DSI Command Mode vs Video Mode:](https://blog.csdn.net/justlxy/article/details/115453751)
- [MIPI DSI-2 Protocol Analysis](https://blog.csdn.net/sinat_43629962/article/details/122998924)

## Preparation before configuring parameters
Before configuring DSI parameters, you need to understand the parameters and specifications of your screen module in detail. Refer to the following list and confirm that you understand the relevant information before configuration.
- Number of DSI interface Data Lanes, color format, and maximum frequency
- DSI interface operating mode: Command mode or Video mode. Different modes require different configuration flows.
- Screen resolution and refresh rate
- For Command mode, confirm the screen TE mechanism, whether it is provided through the DSI protocol or through a separate pin.  

After preparing the above information, configure the screen parameters according to the DSI interface operating mode.
- [Command mode parameter configuration](#Command_mode_conf)
- [Video mode parameter configuration](#Video_mode_conf)


(Command_mode_conf)=
## Command mode parameter configuration
In Command mode, the configurable DSI-related parameters mainly include:
- freq  
DSI clock frequency
- color_mode  
Color format, which can be configured as RGB888 or RGB565
- AutomaticClockLaneControl  
Clock automatic control. After it is enabled, the clock lane enters a low-power state when idle, reducing interface power consumption.
- NumberOfLanes  
Number of DSI Data Lanes. Up to 2 Data Lanes are supported
- TearingEffectSource  
Configure the TE source of DSI
- TEAcknowledgeRequest  
Configure Enable to enable the TE function
- vsyn_delay_us  
Delay for the TE function to trigger data transmission. This function is valid only when TE is enabled. The configuration indicates the delay between the arrival of the TE signal and the formal transmission of screen data.

The following source code covers all DSI Command mode configurations. The configurations mentioned above need to be changed according to screen requirements. Other configurations also have corresponding descriptions, but changing them is not recommended.
```c
static LCDC_InitTypeDef lcdc_int_cfg_dsi =
{
    .lcd_itf = LCDC_INTF_DSI, /* 选择DSI接口 */
    .freq = DSI_FREQ_480Mbps, /* 选择DSI接口频率，这里选择480M */
    .color_mode = LCDC_PIXEL_FORMAT_RGB888,  /* DBI output color format,   should match with .cfg.dsi.CmdCfg.ColorCoding */

    .cfg = {

        .dsi = {

            .Init = {
/*  clock lane时钟自动控制，enable后，clock lane会自动进入lp模式来节省功耗，默认关闭，如果需要控制接口功耗，再打开。*/
                .AutomaticClockLaneControl = DSI_AUTO_CLK_LANE_CTRL_ENABLE,
                .NumberOfLanes = DSI_ONE_DATA_LANE,/* DSI Data Lane数量 */
/*
 lp模式下的时钟分频比，不用做更改。
 escape clk  = dsi_phy_clk / 2(DDR) / 8 / TXEscapeCkdiv
*/                
                .TXEscapeCkdiv = 0x4,
            },

            .CmdCfg = {
                .VirtualChannelID      = 0,/* channel ID, 不用做更改 */
                .CommandSize           = 0xFFFF, /* 这个值目前没有作用,忽略 */
/* 配置TE源来自外部还是内部 */                
                .TearingEffectSource   = DSI_TE_EXTERNAL, /* DSI link TE */
                .TEAcknowledgeRequest  = DSI_TE_ACKNOWLEDGE_ENABLE,  /* Enable TE */
/* DSI input & output color format，该配置后面会被移除，与之前配置重复 */
                .ColorCoding           = DSI_RGB888,//DSI input & output color format
            },
/* 这部分寄存器都是dsi物理层相关配置，不建议用户进行更改 */
            .PhyTimings = {
                .ClockLaneHS2LPTime = 35,/*  clock lane从hs切换到lp模式需要的时钟周期 */
                .ClockLaneLP2HSTime = 35, /* clock lane从lp切换到hs模式需要的时钟周期 */
                .DataLaneHS2LPTime = 35,/* data lane从hs切换到lp模式需要的时钟周期 */
                .DataLaneLP2HSTime = 35, /* data lane从lp切换到hs模式需要的时钟周期 */
                .DataLaneMaxReadTime = 0,/*  单次读取所需要的最大时钟周期数，因为现有使用状况下，读取不会发生在发数的阶段，所以该值没有被使用。 */
                .StopWaitTime = 0, /* stop模式下，发送hs模式切换请求的最小等待时间 */
            },
/* HostTimeouts 这一部分配置主要设计timeout报错，一般用来检测异常情况，方便以后debug，用户不需要修改 */
            .HostTimeouts = {
                .TimeoutCkdiv = 1,/* timeout的时钟分频比，timeout debug目前没有打开，没有生效 */
                .HighSpeedTransmissionTimeout = 0,
                .LowPowerReceptionTimeout = 0,
                .HighSpeedReadTimeout = 0,
                .LowPowerReadTimeout = 0,
                .HighSpeedWriteTimeout = 0,
                //.HighSpeedWritePrespMode = DSI_HS_PM_DISABLE,
                .LowPowerWriteTimeout = 0,
                .BTATimeout = 0,
            },

/*  LPCmd 这里的寄存器定义了command模式下，各种类型的指令对应的发送模式，LP模式发送速度慢，但是可以被逻分抓到，高速模式发送速度快，但常用仪器无法检测。这里建议对于generic接口的command，设置为低速即可，对于dcs的指令，除了longwrite，其他均可以设置为低速，这样便于通过逻分查看波形。这部分允许用户更改，但不太建议改动。*/
            .LPCmd = {
                .LPGenShortWriteNoP    = DSI_LP_GSW0P_ENABLE,/*  generic接口shortwrite指令无参数发送模式，enable为低速，disable为高速 */
                .LPGenShortWriteOneP   = DSI_LP_GSW1P_ENABLE,/*  generic接口shortwrite指令单参数发送模式，enable为低速，disable为高速 */
                .LPGenShortWriteTwoP   = DSI_LP_GSW2P_ENABLE,/*  generic接口shortwrite指令双参数发送模式，enable为低速，disable为高速 */
                .LPGenShortReadNoP     = DSI_LP_GSR0P_ENABLE,/*  generic接口shortread指令无参数发送模式，enable为低速，disable为高速 */
                .LPGenShortReadOneP    = DSI_LP_GSR1P_ENABLE,/*   generic接口shortread指令单参数发送模式，enable为低速，disable为高速 */
                .LPGenShortReadTwoP    = DSI_LP_GSR2P_ENABLE,/*   generic接口shortread指令双参数发送模式，enable为低速，disable为高速 */
                .LPGenLongWrite        = DSI_LP_GLW_ENABLE, /* generic接口longwrite指令发送模式，enable为低速，disable为高速 */
                .LPDcsShortWriteNoP    = DSI_LP_DSW0P_ENABLE,/* dcs接口shortwrite指令无参数发送模式，enable为低速，disable为高速 */
                .LPDcsShortWriteOneP   = DSI_LP_DSW1P_ENABLE, /*  dcs接口shortwrite指令单参数发送模式，enable为低速，disable为高速 */
                .LPDcsShortReadNoP     = DSI_LP_DSR0P_ENABLE, /* ddcs接口shortread指令无参数发送模式，enable为低速，disable为高速 */
                .LPDcsLongWrite        = DSI_LP_DLW_DISABLE, /*  dcs接口longwrite指令单参数发送模式，enable为低速，disable为高速 */
                .LPMaxReadPacket       = DSI_LP_MRDP_ENABLE, /* 设置最大读取包尺寸指令模式发送模式，enable为低速，disable为高速*/
                .AcknowledgeRequest    = DSI_ACKNOWLEDGE_DISABLE, //disable LCD error reports 使能后允许屏幕端发送应答包，主要用于debug，一般场景下disable即可。
            },


            .vsyn_delay_us = 0,/* 该配置在使能TEAcknowledgeRequest后，才有意义，用于配置TE信号高电平延时多少us后，再给屏送数 */
        },
    },
};
```

---

(Video_mode_conf)=

## Video mode parameter configuration

Most parameters in Video mode are the same as in command mode. The main additions are the `VidCfg` configuration and disabling TE configuration. The same parts are not repeated. The following code lists only the parts that differ between Video mode and Command mode; other parts are omitted with `...`:

```c
static LCDC_InitTypeDef lcdc_int_cfg_dsi =
{
    .lcd_itf = LCDC_INTF_DSI_VIDEO, /* 选择DSI Video接口 */
    
    ...

    .cfg = {

        .dsi = {

            ...

            .CmdCfg = {
                .VirtualChannelID      = 0,/* channel ID, 不用做更改 */
                .CommandSize           = 0xFFFF, /* 这个值目前没有作用,忽略 */
                
                /* Video模式没有TE，需要关闭TE，source选DSI link TE */                
                .TearingEffectSource   = DSI_TE_DSILINK, /* DSI link TE */
                .TEAcknowledgeRequest  = DSI_TE_ACKNOWLEDGE_DISABLE,  /* 关闭 TE */
            },

            ...


            //.vsyn_delay_us = 0,  /* Video模式下该参数无作用，可省略 */


            /*  Video模式特有的参数配置  */
            .VidCfg = {
                .Mode = DSI_VID_MODE_NB_EVENTS, //暂时只支持NoneBurst Event 模式

                .VS_width      = 4,    //Vsync信号里面有几个Hsync信号
                .HS_width      = 15,   //Hsync信号里面有几个DPI的PCLK信号

                .VBP = 16,              //Back Porch的行数
                .VAH = LCD_HOR_RES_MAX,  //有效数据行数
                .VFP = 20,              //Front Porch的行数

                .HBP = 15,              //Back Porch的列数
                .HAW = LCD_VER_RES_MAX, //有效数据的列数
                .HFP = 15,              //Front Porch的列数

                .interrupt_line_num = 1, //默认保持1
            },
        },
    },
};
```

:::{note}

    1. In Video mode, after `HAL_LCDC_Init` is executed, command mode is maintained for configuring the screen driver IC. It switches to Video mode only after screen refresh is started through the `HAL_LCDC_SendLayerData(_IT)` interface

    2. In Video mode, the formula corresponding to the DPI PCLK frequency is roughly as follows: `DSI_CLK = PCLK * bpp / NumOfDsiLane`. For example, if the screen requires the DPI frequency to be greater than 28MHz, uses 16bit color depth, and has 2 DSI data lanes, then the required DSI frequency is at least 28*16/2=224MHz

:::

### Screen debugging sequence for Video mode
1. First confirm that the configuration parameters are correct, such as the DSI frequency and the number of data lanes (58x supports up to 2 lanes). Currently only NoneBurst Event mode is supported.
2. Confirm that the screen initialization commands are correct and that the screen can be lit through the screen self-test command (remember to turn on the backlight)
3. If an image can be displayed but it is corrupted or disordered, consult our FAE.
