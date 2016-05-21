#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import sys, os
sys.path.insert(0, os.path.realpath('./plugins'))

AUTHOR = 'Jake Howard'
SITENAME = 'TheOrangeOne'
SITEURL = 'http://theorangeone.net'

PATH = 'content'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
import social
SOCIAL = social.generate()


DEFAULT_PAGINATION = False
DELETE_OUTPUT_DIRECTORY = True


PAGE_PATHS = ["pages"]
PAGE_SAVE_AS = "{slug}/index.html"
PAGE_URL = "{slug}"

THEME = "theme"
THEME_STATIC_DIR = "static"
THEME_STATIC_PATHS = ['static/build']
STATIC_PATHS = ["assets", "assets/favicon.ico"]
EXTRA_PATH_METADATA = {
    "assets/favicon.ico": {"path": "favicon.ico"}
}

ARTICLE_PATHS = ["articles"]
ARTICLE_SAVE_AS = "blog/{slug}/index.html"
ARTICLE_URL = "/blog/{slug}/"

TAG_URL = "blog/tag/{slug}/"
TAG_SAVE_AS = "blog/tag/{slug}/index.html"

TAGS_URL = "blog/tags/"
TAGS_SAVE_AS = "blog/tags/index.html"

AUTHOR_URL = "/blog/author/{slug}/"
AUTHOR_SAVE_AS = "blog/author/{slug}/index.html"

AUTHORS_URL = "/blog/authors/"
AUTHORS_SAVE_AS = "blog/authors/index.html"

ARCHIVES_URL = "blog/archive/"
ARCHIVES_SAVE_AS = "blog/archive/index.html"

CATEGORY_SAVE_AS = False
CATEGORIES_SAVE_AS = False

PLUGIN_PATHS = ["pelican_plugins"]
PLUGINS = ['sitemap']

SITEMAP = {
    'format': 'xml'
}


# Extra context
