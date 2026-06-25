// 自动语言检测和跳转
(function() {
    var preferredLanguageKey = 'preferredLanguage';
    var autoRedirectKey = 'languageRedirected';
    var currentPath = window.location.pathname;
    var currentSearch = window.location.search || '';
    var currentHash = window.location.hash || '';

    function isRootPath(path) {
        return path === '/' || path === '/index.html';
    }

    function normalizePreferredLanguage(language) {
        if (language === 'en' || language === 'zh-CN') {
            return language;
        }
        return '';
    }

    function getBrowserPreferredLanguage() {
        var browserLang = (navigator.language || navigator.userLanguage || '').toLowerCase();
        return browserLang.split('-')[0] === 'en' ? 'en' : 'zh-CN';
    }

    function pathForLanguage(path, language) {
        if (language === 'en') {
            if (path === '/en' || path.startsWith('/en/')) {
                return path;
            }
            return path === '/' || path === '/index.html' ? '/en/' : '/en' + path;
        }

        if (path === '/en') {
            return '/';
        }
        if (path.startsWith('/en/')) {
            return path.replace(/^\/en/, '') || '/';
        }
        return path;
    }

    function redirectToLanguage(language) {
        var targetPath = pathForLanguage(currentPath, language);
        if (targetPath !== currentPath) {
            window.location.replace(targetPath + currentSearch + currentHash);
            return true;
        }
        return false;
    }

    var preferredLanguage = normalizePreferredLanguage(localStorage.getItem(preferredLanguageKey));

    // 用户已经手动选择过语言时，始终尊重该选择，不再按浏览器语言覆盖。
    if (preferredLanguage) {
        redirectToLanguage(preferredLanguage);
        return;
    }

    // 没有用户偏好时，只在首次访问根路径时根据浏览器语言做一次引导。
    if (!sessionStorage.getItem(autoRedirectKey)) {
        sessionStorage.setItem(autoRedirectKey, 'true');
        if (isRootPath(currentPath)) {
            redirectToLanguage(getBrowserPreferredLanguage());
        }
    }
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
    
    // 用户手动切换语言后保存偏好，后续页面加载时不再被浏览器语言改回去。
    var languageLinks = document.querySelectorAll('.nav-languages-choices a');
    languageLinks.forEach(function(link) {
        link.addEventListener('click', function() {
            try {
                var linkUrl = new URL(link.href);
                var preferredLanguage = linkUrl.pathname === '/en' || linkUrl.pathname.startsWith('/en/') ? 'en' : 'zh-CN';
                localStorage.setItem('preferredLanguage', preferredLanguage);
                sessionStorage.setItem('languageRedirected', 'true');
            } catch(e) {
                // 处理无效URL
            }
        });
    });
});
