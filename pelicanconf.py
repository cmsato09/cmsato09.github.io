#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'cmsato09'
SITENAME = 'Novice Programmer Journey from Zero'
SITETITLE = SITENAME
SITESUBTITLE = 'beginning a programming blog'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'US/Pacific'

DEFAULT_LANG = 'en'

SITELOGO = '/icons/rook_clipart.png'
THEME = 'Flex'
DISPLAY_PAGES_ON_MENU = False
USE_FOLDER_AS_CATEGORY = True
MAIN_MENU = True

PATH = 'content'
STATIC_PATHS = ['icons','images']
ARTICLE_PATHS = ['articles']
ARTICLE_SAVE_AS = 'articles/{date:%Y}/{date:%Y-%m-%d}-{slug}.html'
PAGE_PATHS = ['pages']


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

MENUITEMS = (('Archives', '/archives.html'),
            ('Categories', '/categories.html'),
	    ('Tags', '/tags.html'),)

DEFAULT_PAGINATION = 20

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
DELETE_OUTPUT_DIRECTORY = False