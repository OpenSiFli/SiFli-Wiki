# DSI Screen Parameter Configuration

For basic knowledge about MIPI, please refer to the following articles. The basics of MIPI DSI will not be detailed here.
- [MIPI Primer — DSI Command Mode vs Video Mode:](https://blog.csdn.net/justlxy/article/details/115453751)
- [MIPI DSI-2 Protocol Analysis](https://blog.csdn.net/sinat_43629962/article/details/122998924)

## Preparations Before Configuration
Before configuring the DSI parameters, users need to have a detailed understanding of their screen module's parameters. Please refer to the following list to ensure that you have the necessary information before proceeding with the configuration.
- Number of DSI interface Data Lanes, color format, and maximum frequency
- DSI interface operating mode, Command mode/Video mode, and the different configuration procedures required for each mode.
- Screen resolution and refresh rate
- For Command mode, confirm the screen TE mechanism, whether it is provided through the DSI protocol or through a separate pin.

After preparing the above information, you can configure the screen parameters according to the DSI interface operating mode.
- [Command Mode Parameter Configuration](#Command_mode_conf)
- [Video Mode Parameter Configuration](#Video_mode_conf)


(Command_mode_conf)=
## Command Mode Parameter Configuration
The main configurable parameters for DSI in Command mode include:
- freq  
DSI clock frequency
- color_mode  
Color format, which can be configured as RGB888 or RGB565
- AutomaticClockLaneControl  
Clock automatic control, enabling this will put the clock lane into a low-power state when idle, thus reducing interface power consumption.
- NumberOfLanes  
Number of DSI Data Lanes, up to 2 Data Lanes are supported
- TearingEffectSource  
Configure the source of DSI TE
- TEAcknowledgeRequest  
Enable TE functionality by configuring this
- vsyn_delay_us  
Delay for TE functionality trigger, this function is only effective when TE is enabled, and it configures the delay between the arrival of the TE signal and the actual sending of screen data

The following source code covers all configurations for DSI Command mode. The configurations mentioned above need to be adjusted according to the screen requirements. Other configurations are also described but are not recommended to be changed.
```c
static LCDC_InitTypeDef lcdc_int_cfg_dsi =
{
    .lcd_itf = LCDC_INTF_DSI, /* Select DSI interface */
    .freq = DSI_FREQ_480Mbps, /* Select DSI interface frequency, here 480M is chosen */
    .color_mode = LCDC_PIXEL_FORMAT_RGB888,  /* DBI output color format, should match with .cfg.dsi.CmdCfg.ColorCoding */

    .cfg = {

        .dsi = {

            .Init = {
/* Clock lane clock automatic control, enable this to automatically put the clock lane into lp mode to save power, default is disabled, enable if you need to control interface power consumption. */
                .AutomaticClockLaneControl = DSI_AUTO_CLK_LANE_CTRL_ENABLE,
                .NumberOfLanes = DSI_ONE_DATA_LANE,/* Number of DSI Data Lanes */
/*
 Clock divider ratio in lp mode, no need to change.
 escape clk  = dsi_phy_clk / 2(DDR) / 8 / TXEscapeCkdiv
*/                
                .TXEscapeCkdiv = 0x4,
            },
```

.CmdCfg = {
                .VirtualChannelID      = 0,/* channel ID, no need to change */
                .CommandSize           = 0xFFFF, /* this value is currently not in use, ignore it */
/* Configure TE source as external or internal */                
                .TearingEffectSource   = DSI_TE_EXTERNAL, /* DSI link TE */
                .TEAcknowledgeRequest  = DSI_TE_ACKNOWLEDGE_ENABLE,  /* Enable TE */
/* DSI input & output color format, this configuration will be removed later as it duplicates previous settings */
                .ColorCoding           = DSI_RGB888,//DSI input & output color format
            },
/* These registers are related to the DSI physical layer configuration, and it is not recommended for users to modify them */
            .PhyTimings = {
                .ClockLaneHS2LPTime = 35,/* clock lane switching from HS to LP mode requires this number of clock cycles */
                .ClockLaneLP2HSTime = 35, /* clock lane switching from LP to HS mode requires this number of clock cycles */
                .DataLaneHS2LPTime = 35,/* data lane switching from HS to LP mode requires this number of clock cycles */
                .DataLaneLP2HSTime = 35, /* data lane switching from LP to HS mode requires this number of clock cycles */
                .DataLaneMaxReadTime = 0,/* the maximum number of clock cycles required for a single read operation, this value is not used as read operations do not occur during transmission in the current usage scenario */
                .StopWaitTime = 0, /* the minimum wait time in stop mode before sending an HS mode switch request */
            },
/* HostTimeouts configuration mainly involves timeout errors, generally used to detect abnormal situations for easier debugging in the future, users do not need to modify these settings */
            .HostTimeouts = {
                .TimeoutCkdiv = 1,/* the clock division ratio for timeout, timeout debugging is currently not enabled, so this setting is not effective */
                .HighSpeedTransmissionTimeout = 0,
                .LowPowerReceptionTimeout = 0,
                .HighSpeedReadTimeout = 0,
                .LowPowerReadTimeout = 0,
                .HighSpeedWriteTimeout = 0,
                //.HighSpeedWritePrespMode = DSI_HS_PM_DISABLE,
                .LowPowerWriteTimeout = 0,
                .BTATimeout = 0,
            },

```c
/*  LPCmd This section defines the register settings for command mode, specifying the transmission modes for various types of commands. LP mode has a slower transmission speed but can be captured by logic analyzers, while high-speed mode has a faster transmission speed but cannot be detected by common instruments. It is recommended to set the commands for the generic interface to low speed. For DCS commands, except for longwrite, all others can be set to low speed, which facilitates waveform viewing through a logic analyzer. This section allows user modifications, but it is not highly recommended to change it. */
            .LPCmd = {
                .LPGenShortWriteNoP    = DSI_LP_GSW0P_ENABLE,/*  generic interface shortwrite command with no parameters, enable for low speed, disable for high speed */
                .LPGenShortWriteOneP   = DSI_LP_GSW1P_ENABLE,/*  generic interface shortwrite command with one parameter, enable for low speed, disable for high speed */
                .LPGenShortWriteTwoP   = DSI_LP_GSW2P_ENABLE,/*  generic interface shortwrite command with two parameters, enable for low speed, disable for high speed */
                .LPGenShortReadNoP     = DSI_LP_GSR0P_ENABLE,/*  generic interface shortread command with no parameters, enable for low speed, disable for high speed */
                .LPGenShortReadOneP    = DSI_LP_GSR1P_ENABLE,/*  generic interface shortread command with one parameter, enable for low speed, disable for high speed */
                .LPGenShortReadTwoP    = DSI_LP_GSR2P_ENABLE,/*  generic interface shortread command with two parameters, enable for low speed, disable for high speed */
                .LPGenLongWrite        = DSI_LP_GLW_ENABLE, /* generic interface longwrite command, enable for low speed, disable for high speed */
                .LPDcsShortWriteNoP    = DSI_LP_DSW0P_ENABLE,/*  DCS interface shortwrite command with no parameters, enable for low speed, disable for high speed */
                .LPDcsShortWriteOneP   = DSI_LP_DSW1P_ENABLE, /*  DCS interface shortwrite command with one parameter, enable for low speed, disable for high speed */
                .LPDcsShortReadNoP     = DSI_LP_DSR0P_ENABLE, /* DCS interface shortread command with no parameters, enable for low speed, disable for high speed */
                .LPDcsLongWrite        = DSI_LP_DLW_DISABLE, /*  DCS interface longwrite command, enable for low speed, disable for high speed */
                .LPMaxReadPacket       = DSI_LP_MRDP_ENABLE, /* set the maximum read packet size command mode, enable for low speed, disable for high speed */
                .AcknowledgeRequest    = DSI_ACKNOWLEDGE_DISABLE, // disable LCD error reports, enabling this allows the screen to send acknowledgment packets, mainly used for debugging, generally disable in normal scenarios.
            },


            .vsyn_delay_us = 0,/*  This configuration is meaningful only when TEAcknowledgeRequest is enabled, used to configure the delay in microseconds after the TE signal is high before sending data to the screen */
        },
    },
};
#endif /* BSP_LCDC_USING_DSI */
```
***

(Video_mode_conf)=
## Video Mode Configuration Parameters