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
BANNER_SUBTITLE = 'empower.enable.connect || 3-5 July 2015'
BANNER_ALL_PAGES = True

SITELOGO = 'images/GovHackFinalNoTaglineColour.png'
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

SPONSORS = (
    ('HP', 'http://www8.hp.com/nz/en/home.html', 'HP-logo.png'),
    ('Silverstripe', 'http://silverstripe.com', 'silverstripe-logo.png'),
    ('Catalyst', 'http://catalyst.net.nz', 'catalyst-logo.png'),
    ('Uber', 'https://www.uber.com/cities/wellington', 'uber-logo.png'),
    ('Optimal Bi', 'http://optimalbi.com/', 'optimalbi-logo.png'),
    ('Optimal People', 'http://www.optimalpeople.co.nz/', 'optimal-people-logo.png'),
    ('Air New Zealand', 'http://airnz.co.nz', 'AirNZ-logo.jpg'),
    ('IWantMyName', 'http://iwmn.com', 'iwantmyname-logo.png'),
    ('NZ Rise', 'http://nzrise.org.nz', 'nzrise-logo.png'),
    ('Vend', 'https://www.vendhq.com/', 'vend-logo.png'),
    ('MBIE', 'http://mbie.govt.nz', 'mbie-logo.png'),
    ('Fujitsu', 'http://www.fujitsu.com/nz/', 'fujitsu-logo.png'),
    ('Intergraph', 'http://www.intergraph.com/global/nz/', 'intergraph-logo.png'),
    ('Webb Street Brewery', 'https://www.facebook.com/webbstreetbrewery', 'webb-st-brewery-logo.png'),
    ('Propellerhear', 'http://www.propellerhead.co.nz/', 'propellerhead-logo.png'),
    ('Rabid Tech', 'http://rabid.co.nz', 'rabid-logo.png'),
    ('Hack Miramar', 'http://www.hackmiramar.org/', 'hack-miramar-logo.jpg')
    )

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




