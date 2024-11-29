# pelicanconf.py

THEME = "notmyidea"  # You can choose your theme or use "notmyidea" theme
PLUGIN_PATHS = ['plugins']
PLUGINS = ['render_math']

# General settings
AUTHOR = 'Your Name'
SITENAME = 'My Machine Learning Blog'
SITEURL = ''  # Set to your GitHub Pages URL in production (e.g., https://yourusername.github.io/your-repository-name)
TIMEZONE = 'America/New_York'  # Or use your own timezone

# Content settings
DEFAULT_LANG = 'en'

# Enable Markdown extensions (including tables)
MARKDOWN = {
    'extensions': ['codehilite', 'extra', 'md_in_html', 'admonition', 'tables']
}

# MathJax (optional, for LaTeX rendering)
MATHJAX_URL = 'https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js'

# Other settings (optional)
DEFAULT_PAGINATION = 10