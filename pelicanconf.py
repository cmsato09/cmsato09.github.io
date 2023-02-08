#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'cmsato09'
SITENAME = 'Rookie Coding ~ Journey as a Novice Programmer'
SITETITLE = SITENAME
SITESUBTITLE = 'The start of a programming blog'
# SITEURL = 'https://cmsato09.github.io'

# comment out above siteurl and uncomment the other siteurl below when testing locally
SITEURL = 'http://localhost:8000'

PATH = 'content'

TIMEZONE = 'US/Pacific'

DEFAULT_LANG = 'en'

SITELOGO = '/images/rook_clipart.png'
THEME = 'Flex'
DISPLAY_PAGES_ON_MENU = True
#USE_FOLDER_AS_CATEGORY = True
MAIN_MENU = True

PATH = 'content'
STATIC_PATHS = ['icons','images',]
ARTICLE_PATHS = ['articles']
ARTICLE_SAVE_AS = 'articles/{date:%Y}/{slug}.html'
ARTICLE_URL = ARTICLE_SAVE_AS
PAGE_PATHS = ['pages']
RELATIVE_URLS = False

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Python Developer Mindset', 'https://pybit.es/catalogue/the-pdm-program/'),
         )

# Social widget
SOCIAL = (('github', 'https://github.com/cmsato09'),
          ('linkedin', 'https://www.linkedin.com/in/christopher-m-sato/'),)

MENUITEMS = (
        ('Archives', '/archives.html'),
        ('Categories', '/categories.html'),
	('Tags', '/tags.html'),
        )

DEFAULT_PAGINATION = 20

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
DELETE_OUTPUT_DIRECTORY = False