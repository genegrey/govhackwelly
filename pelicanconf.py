#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'aimee whitcroft'
SITENAME = u'GovHack Wellington'
SITEURL = ''

PATH = 'content'

PAGE_PATHS = ['pages']

ARTICLE_PATHS = ['articles']

STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

THEME_PATHS = ['themes']
THEME = 'themes/pelican-bootstrap3'

# Logo & banner

BANNER = '/images/plainwhitebanner.png'
BANNER_SUBTITLE = 'bringing order to chaos'
BANNER_ALL_PAGES = True

#SITELOGO = 'images/GovHackFinalNoTaglineColour.png'
SITELOGO_SIZE = 40
HIDE_SITENAME = True

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

SPONSORS = (('Fujitsu', 'http://fujitsu.co.nz', 'http://www.fujitsu.com/au/resources/design/stylesheets/images/css_images/fujitsu/symbolmark.gif'), ('Silverstripe', 'http://silverstripe.com', 'https://scontent.xx.fbcdn.net/hprofile-xta1/v/l/t1.0-1/p50x50/1800250_10150370979104946_1786160472_n.png?oh=7b816ea8eb311d5557994453022962af&oe=55C3A67C'))

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




