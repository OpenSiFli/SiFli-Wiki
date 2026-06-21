# Configuration file for the Sphinx documentation builder.

project = 'SiFli-Wiki'
copyright = '2025, SiFli'
author = 'SiFli'
release = 'v1.0'

extensions = [
    "sphinx_design",
    "myst_parser",
    "sphinx_copybutton",
    "sphinx_sitemap",
]

templates_path = ['../_templates']
language = 'zh_CN'
exclude_patterns = []

html_theme = 'shibuya'
numfig = True
html_copy_source = False
html_show_sourcelink = False
html_static_path = ['../_static']
html_logo = '../_static/logo_white.png'
html_favicon = '../_static/logo_favicon.png'

html_css_files = [
    'custom.css',
    'lightbox.css',
]
html_js_files = [
    'js/baidu.js',
    'js/custom.js',
    'js/lightbox.js',
]
html_theme_options = {
    "accent_color": "blue",
    "announcement": """
        <div style="text-align: center">
            思澈 Solution 全面开放：一套产品级方案，加速从原型到量产
            <a href='https://docs.sifli.com/projects/solution/0.introduction/index.html'>Solution文档</a>.
        </div>
    """,
    "github_url": "https://github.com/OpenSiFli",
    "nav_links": [

        {"title": "入门指南", "url": "docs/index"},
        {"title": "API文档", "url": "https://docs.sifli.com/projects/sdk/latest/sf32lb52x/index.html", "external": True},
        {"title": "Solution文档", "url": "https://docs.sifli.com/projects/solution/0.introduction/index.html", "external": True},
        {"title": "关于我们", "url": "about/index"},
    ],
}

myst_enable_extensions = [
    "amsmath",
    "attrs_inline",
    "attrs_block",
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist",
]
myst_fence_as_directive = ["mermaid"]

html_baseurl = 'https://wiki.sifli.com/'
sitemap_url_scheme = "{link}"
sitemap_filename = 'sitemap.xml'
sitemap_locales = []

html_context = {
    "languages": [
        ("English", "/en/%s.html", "en"),
        ("中文", "/%s.html", "zh"),
    ],
    "source_type": "github",
    "source_user": "OpenSiFli",
    "source_repo": "SiFli-Wiki",
    "source_version": "main",
    "source_docs_path": '/source/zh_CN/',
}


def setup(app):
    app.tags.add("html_en" if app.config.language == "en" else "html_zh")
