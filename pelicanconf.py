#!/usr/bin/env python
# -*- coding: utf-8 -*- #

SITENAME = u"DECAY"
SITEURL = 'http://decay.skoorb.net'
TWITTER_USERNAME = u"decayfilm"
AUTHOR = u"Decay"
SHOW_FEEDS = True   # Set whether to show feeds on the main page
YOUTUBE_ID = "luNueXoAw3I"

THEME = "decay"

TIMEZONE = 'Europe/London'
DEFAULT_LANG = 'en'

DEFAULT_PAGINATION = 4
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

FILES_TO_COPY = (
        ('extra/.htaccess', '.htaccess'),
        ('extra/humans.txt', 'humans.txt'),
        ('extra/robots.txt', 'robots.txt'),
        )

# Social widget
SOCIAL = (('Facebook', 'http://www.facebook.com/decayfilm'),
          ('Twitter', 'http://www.twitter.com/decayfilm'),)

# Custom filters
from datetime import date

RUN_DATE = date.today()
def in_future(articles):
    """Filter to return list of only future articles"""
    now = RUN_DATE.isoformat()
    return [article for article in articles if article.date.isoformat() > now]

def in_past(articles):
    """Filter to return list of only past articles"""
    now = RUN_DATE.isoformat()
    return [article for article in articles if article.date.isoformat() <= now]

JINJA_FILTERS = {'in_future': in_future, 'in_past': in_past}
