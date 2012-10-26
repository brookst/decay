#!/usr/bin/env python
# -*- coding: utf-8 -*- #

SITENAME = u"DECAY"
SITEURL = 'http://decay.skoorb.net'
TWITTER_USERNAME = u"decayfilm"
AUTHOR = u"Decay"
SHOW_FEEDS = True   # Set whether to show feeds on the main page

THEME = "decay"

TIMEZONE = 'Europe/London'
DEFAULT_LANG = 'en'

DEFAULT_PAGINATION = 5
WEBASSETS = True
TYPOGRIFY = True
RELATIVE_URLS = False
DISPLAY_PAGES_ON_MENU = True
MENUITEMS = (('Decay', '//decayfilm.com'),)
#PAGE_DIR = '/pages/'
#PAGE_URL = '/pages/{slug}.html'
#PAGE_SAVE_AS = '/pages/{slug}.html'
#PAGE_LANG_URL = '/pages/{slug}-{lang}.html'
#PAGE_LANG_SAVE_AS = '/pages/{slug}-{lang}.html'

ARTICLE_URL = '/{date:%Y}/{slug}.html'
ARTICLE_SAVE_AS = '/{date:%Y}/{slug}.html'
ARTICLE_LANG_URL = '/{date:%Y}/{slug}-{lang}.html'
ARTICLE_LANG_SAVE_AS = '/{date:%Y}/{slug}-{lang}.html'
FEED_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'
STATIC_PATHS = ['images','files']

# Social widget
SOCIAL = (('Facebook', 'http://www.facebook.com/decayfilm'),
          ('Twitter', 'http://www.twitter.com/decayfilm'),)

