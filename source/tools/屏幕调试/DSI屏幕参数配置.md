# DSI屏幕参数配置

相关mipi的基础知识可以参考下面文章，这里不再对MIPI DSI基础知识进行详述。
- [MIPI扫盲——DSI Command Mode vs Video Mode：](https://blog.csdn.net/justlxy/article/details/115453751)
- [MIPI DSI-2 协议解析](https://blog.csdn.net/sinat_43629962/article/details/122998924)

## 配置参数前的准备
在配置DSI的参数前，用户需要对自己屏幕模组的参数指标有比较详细的认知，请参考以下列表，确认在配置前已经了解相关的信息。
- DSI接口Data Lane数量，色彩格式，最高频率
- DSI接口工作模式，Command模式/Video模式，不同模式需要参考不同的配置流程。
- 屏幕分辨率，刷新率
- 对于Command模式，确认屏幕TE的机制，是通过DSI协议，还是通过单独的引脚提供TE信号。  

在准备好以上信息后，就可以根据DSI接口工作模式进行屏幕参数配置。
- [Command模式参数配置](#Command_mode_conf)
- [Video模式参数配置](#Video_mode_conf)


(Command_mode_conf)=
## Command模式参数配置
Command模式下DSI相关可配置的参数主要有：
- freq  
DSI时钟频率
- color_mode  
色彩格式，可以配置RGB888或者RGB565
- AutomaticClockLaneControl  
Clock自动控制，使能后，clock lane在空闲时会进入低功耗状态，这样可以降低接口功耗。
- NumberOfLanes  
DSI Data Lane数量，最高可以支持2 Data Lane
- TearingEffectSource  
配置DSI的TE来源
- TEAcknowledgeRequest  
配置Enable使能TE功能
- vsyn_delay_us  
TE功能触发送数的延迟，该功能只有在TE使能时才有效，配置表示TE信号来之后，到正式发送屏幕数据之间的延迟

如下的源码中，涵盖了DSI Command模式的所有配置，上述提到的配置是需要根据屏幕要求进行更改的，其他配置，也有对应描述，但是不建议进行更改。
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

## Video模式参数配置

Video模式下大部分参数与command模式相同，主要增加了`VidCfg`的配置以及关闭了TE配置，相同部分不再赘述，下面的代码只列出了Video模式下和Command模式有差异的部分，其他地方都用`...`省略：

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

    1. Video模式下在执行`HAL_LCDC_Init`之后会保持command模式，用于配置屏驱IC, 当通过`HAL_LCDC_SendLayerData(_IT)`接口启动刷屏后，才会切换到Video模式

    2. Video模式下对应DPI的PCLK频率的公式大概是这样的:`DSI_CLK = PCLK * bpp / NumOfDsiLane`.  例如屏幕要求DPI频率大于28MHz, 使用16bit位深, 2个DSI数据线, 那么至少需要DSI的频率是 28*16/2=224MHz

:::