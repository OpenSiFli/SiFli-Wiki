// docs/source/_static/chatbot.js
window.difyChatbotConfig = {
    token: 'bfjEKWdbaWBkgcDC',
    baseUrl: 'https://ai.sifli.com'
};

const script = document.createElement('script');
script.src = 'https://ai.sifli.com/embed.min.js';
script.id = 'bfjEKWdbaWBkgcDC';
script.defer = true;
document.body.appendChild(script);

const style = document.createElement('style');
style.textContent = `
    /* 聊天按钮 */
    #dify-chatbot-bubble-button {
        position: fixed !important;
        bottom: 4rem !important;
        right: 1.5rem !important;
        top: unset !important;
        left: unset !important;
        width: 48px !important;
        height: 48px !important;
        background-color: #1C64F2 !important;
        border: 2px solid white;
        border-radius: 50%;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
        z-index: 99999 !important;
        cursor: pointer;
        transition: transform 0.2s ease;
    }

    #dify-chatbot-bubble-button:hover {
        transform: scale(1.1);
    }

    /* 聊天窗口 - 桌面端 */
    #dify-chatbot-bubble-window {
        position: fixed !important;
        bottom: 5rem !important;
        right: 1.5rem !important;
        top: unset !important;
        left: unset !important;
        width: 24rem !important;
        height: 40rem !important;
        max-height: calc(100vh - 6rem) !important;
        border-radius: 12px !important;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2) !important;
        z-index: 99998 !important;
        overflow: hidden;
    }

    /* 移动端适配 */
    @media (max-width: 768px) {
        #dify-chatbot-bubble-button {
            bottom: 1rem !important;
            right: 1rem !important;
            width: 44px !important;
            height: 44px !important;
        }

        #dify-chatbot-bubble-window {
            bottom: 0 !important;
            right: 0 !important;
            width: 100vw !important;
            height: 85vh !important;
            max-height: 85vh !important;
            border-radius: 12px 12px 0 0 !important;
        }
    }

    /* 大尺寸移动设备适配 */
    @media (min-width: 769px) and (max-width: 1024px) {
        #dify-chatbot-bubble-window {
            width: 22rem !important;
            height: 36rem !important;
        }
    }
`;
document.head.appendChild(style);
