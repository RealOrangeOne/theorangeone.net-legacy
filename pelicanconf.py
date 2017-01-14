# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import sys, os
sys.path.insert(0, os.path.realpath('./'))

# Global core settings
AUTHOR = "Jake Howard"
SITENAME = "TheOrangeOne"
SITEURL = "https://theorangeone.net"
PATH = 'content'
TIMEZONE = "Europe/London"
DEFAULT_LANG = "en"
PAGE_PATHS = ["pages"]
THEME = "theme"
THEME_STATIC_DIR = "static"
THEME_STATIC_PATHS = ["static/build"]
STATIC_PATHS = ["assets"]
DEFAULT_DATE = 'fs'
WITH_FUTURE_DATES = True
LOAD_CONTENT_CACHE = False
CACHE_CONTENT = False

USE_FOLDER_AS_CATEGORY = True
DEFAULT_PAGINATION = False
SLUGIFY_SOURCE = 'basename'

# Social widget
from plugins import links
ACCOUNTS = links.accounts()
FOOTER_LINKS = links.footer()
INDEX_PROJECTS = links.index_projects()

# Extra config
BUILD_PRODUCTION = 'BUILD_PRODUCTION' in os.environ
from plugins import image_resizer
META_IMAGES = image_resizer.generate()
PIWIK = {
    'url': 'piwik.theorangeone.net',
    'site_id': 1
}

# Disable some pages
TAG_URL = False
TAG_SAVE_AS = False
TAGS_SAVE_AS = False
AUTHORS_URL = False
AUTHORS_SAVE_AS = False
CATEGORIES_SAVE_AS = False
ARCHIVES_URL = False
ARCHIVES_SAVE_AS = False
AUTHOR_URL = False
AUTHOR_SAVE_AS = False

# Override page URLs
PAGE_SAVE_AS = "{slug}/index.html"
PAGE_URL = "{slug}/"
ARTICLE_SAVE_AS = "{category}/{slug}/index.html"
ARTICLE_URL = "{category}/{slug}/"
CATEGORY_SAVE_AS = "{slug}/index.html"
CATEGORY_URL = "{slug}/"

# Add ATOM feed
FEED_ATOM = 'feed.atom'
FEED_DOMAIN = SITEURL

# Setup plugins
PLUGIN_PATHS = ["plugins", "pelican_plugins"]
PLUGINS = [
    'sitemap',
    'pelican-jinja2content',
    'metatags',
    'autopages',
    'screenfetch',
    'post_build',
    'static_build'
]

if BUILD_PRODUCTION:
    PLUGINS.append("minify")  # only minify on production build

SITEMAP = {
    "format": 'xml'
}
CATEGORY_PAGE_PATH = "theme/templates/categories"
MINIFY = {
    'remove_comments': True,
    'remove_optional_attribute_quotes': False,
    'reduce_boolean_attributes': True,
}

# Setup markdown extensions
from fontawesome_markdown import FontAwesomeExtension
from pyembed.markdown import PyEmbedMarkdown
from mkdcomments import CommentsExtension
MARKDOWN = {
    'extensions': [
        FontAwesomeExtension(),
        PyEmbedMarkdown(),
        CommentsExtension(),
        'codehilite(css_class=highlight)',
        'extra'
    ],
    "output_format": "html5"
}
# Setup jinja2 filters
from plugins import filters
JINJA_FILTERS = {
    "datetime": filters.format_datetime,
    "category_find": filters.category_find,
    "limit": filters.limit
}

JINJA_ENVIRONMENT = {
    'trim_blocks': True,
    'lstrip_blocks': True,
    'extensions': [
        'jinja2.ext.with_',
        'plugins.include_with.IncludeWith'
    ]
}
