#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import sys, os
sys.path.insert(0, os.path.realpath('./plugins'))

# Global core settings
AUTHOR = 'Jake Howard'
SITENAME = 'TheOrangeOne'
SITEURL = 'http://theorangeone.net'
PATH = 'content'
TIMEZONE = 'Europe/London'
DEFAULT_LANG = 'en'
PAGE_PATHS = ["pages"]
THEME = "theme"
THEME_STATIC_DIR = "static"
THEME_STATIC_PATHS = ['static/build']
STATIC_PATHS = ["assets", "assets/favicon.ico"]
EXTRA_PATH_METADATA = {
    "assets/favicon.ico": {"path": "favicon.ico"}
}
USE_FOLDER_AS_CATEGORY = True
DEFAULT_PAGINATION = False
SLUGIFY_SOURCE = 'basename'

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
import links
SOCIAL = links.social()
INDEX_PROJECTS = links.index_projects()

# Disable some pages
TAG_URL = False
TAG_SAVE_AS = False
TAGS_SAVE_AS = False
AUTHORS_URL = False
AUTHORS_SAVE_AS = False
CATEGORIES_SAVE_AS = False
ARCHIVES_URL = False
ARCHIVES_SAVE_AS = False

# Override page URLs
PAGE_SAVE_AS = "{slug}/index.html"
PAGE_URL = "{slug}"
ARTICLE_SAVE_AS = "{category}/{slug}/index.html"
ARTICLE_URL = "{category}/{slug}/"
AUTHOR_URL = "author/{slug}/"
AUTHOR_SAVE_AS = "author/{slug}/index.html"
CATEGORY_SAVE_AS = "{slug}/index.html"
CATEGORY_URL = "{slug}/"

# Add ATOM feed
FEED_ATOM = 'feed.atom'
FEED_DOMAIN = SITEURL

# Setup plugins
PLUGIN_PATHS = ["pelican_plugins"]
PLUGINS = ["sitemap", "filetime_from_git", "pelican-jinja2content"]

SITEMAP = {
    "format": "xml"
}

# Setup markdown extensions
from fontawesome_markdown import FontAwesomeExtension
MD_EXTENSIONS = [FontAwesomeExtension(), 'codehilite(css_class=highlight)', 'extra']

# Setup jinja2 filters
import filters
JINJA_FILTERS = {
    "datetime": filters.format_datetime,
    "raw": filters.html_to_raw,
    "category_find": filters.category_find,
    "limit": filters.limit
}
