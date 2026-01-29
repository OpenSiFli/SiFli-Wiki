// 自动语言检测和跳转
(function() {
    console.log('=== 语言自动跳转脚本开始执行 ===');
    
    // 检查是否已经处理过语言跳转（避免无限重定向）
    var hasRedirected = sessionStorage.getItem('languageRedirected');
    console.log('是否已处理过跳转:', hasRedirected);
    
    if (hasRedirected) {
        console.log('已处理过语言跳转，跳过自动切换');
        return;
    }

    // 获取浏览器语言
    var browserLang = navigator.language || navigator.userLanguage;
    var langCode = browserLang.toLowerCase().split('-')[0]; // 获取主语言代码，如 'zh', 'en'
    console.log('浏览器语言:', browserLang, '-> 语言代码:', langCode);
    
    // 获取当前页面路径
    var currentPath = window.location.pathname;
    var currentHost = window.location.hostname;
    console.log('当前路径:', currentPath);
    console.log('当前域名:', currentHost);
    
    // 判断当前是否在英文版 (/en/ 路径)
    var isEnglishPage = currentPath.startsWith('/en/');
    console.log('当前是否为英文页面:', isEnglishPage);
    
    // 如果浏览器语言是中文，但当前在英文页面
    if ((langCode === 'zh' || langCode === 'cn') && isEnglishPage) {
        // 构建中文页面URL（移除 /en/ 前缀）
        var chinesePath = currentPath.replace(/^\/en/, '');
        console.log('检测到中文浏览器 + 英文页面，准备跳转到:', chinesePath);
        // 标记已处理过跳转
        sessionStorage.setItem('languageRedirected', 'true');
        window.location.href = chinesePath;
        return;
    }
    
    // 如果浏览器语言是英文，但当前在中文页面
    if (langCode === 'en' && !isEnglishPage && currentPath !== '/') {
        // 构建英文页面URL（添加 /en/ 前缀）
        var englishPath = '/en' + currentPath;
        console.log('检测到英文浏览器 + 中文页面，准备跳转到:', englishPath);
        // 标记已处理过跳转
        sessionStorage.setItem('languageRedirected', 'true');
        window.location.href = englishPath;
        return;
    }
    
    // 如果到达这里，说明语言匹配或是首页，标记为已处理
    console.log('语言已匹配或首页，无需跳转');
    sessionStorage.setItem('languageRedirected', 'true');
    console.log('=== 语言自动跳转脚本执行完成 ===');
})();

document.addEventListener('DOMContentLoaded', function() {
    var links = document.querySelectorAll('a');
    var currentHost = window.location.hostname;

    links.forEach(function(link) {
        var href = link.href;
        try {
            var linkUrl = new URL(href);
            // 检查是否为外部链接
            if (linkUrl.hostname !== currentHost && (href.startsWith('http:') || href.startsWith('https:'))) {
                link.setAttribute('target', '_blank');
                link.setAttribute('rel', 'noopener noreferrer');
            }
        } catch(e) {
            // 处理无效URL
        }
    });
    
    // 用户手动切换语言时，清除自动跳转标记
    var languageLinks = document.querySelectorAll('a[href*="/en/"], a[href^="/"][href$=".html"]');
    languageLinks.forEach(function(link) {
        link.addEventListener('click', function() {
            sessionStorage.removeItem('languageRedirected');
        });
    });
});
