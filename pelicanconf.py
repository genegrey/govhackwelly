#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'aimee whitcroft'
SITENAME = u'GovHack Wellington'
SITEURL = ''

PATH = 'content'

PAGE_PATHS = ['pages']

ARTICLE_PATHS = ['articles']

STATIC_PATHS = ['images']

THEME_PATHS = ['themes']
THEME = 'themes/pelican-bootstrap3'

BANNER = 'images/govhackwellingtonbanner.png'
BANNER_SUBTITLE = 'empower.enable.connect || 3-5 July 2015'
BANNER_ALL_PAGES = True
#HEADER_IMAGE = 'images/GovHackFinalTaglineColourStickerStyle.png'

#Plugins
PLUGIN_PATH = 'plugins'

#Tipue search
PLUGINS = ['tipue_search']
DIRECT_TEMPLATES = (('index', 'tags', 'categories', 'authors', 'archives', 'search'))

TIMEZONE = 'Pacific/Auckland'

DEFAULT_LANG = u'en'

PAGE_ORDER_BY = 'sortorder'
# ARTICLE_ORDER_BY = 'xxx'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('GovHack', 'http://www.govhack.org'),
         ('Hack Miramar', 'http://www.hackmiramar.org/'),)

# Social widget
SOCIAL = (('Facebook' , 'https://www.facebook.com/govhackwellington'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

#Tags
TAG_CLOUD_MAX_ITEMS = 10

#Categories
DISPLAY_CATEGORIES_ON_MENU = False

#Authors
SHOW_ARTICLE_AUTHOR = True
SHOW_ARTICLE_CATEGORY = True




