# -*- coding: utf-8 -*-

# Scrapy settings for cnproxy project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'cnproxy'

SPIDER_MODULES = ['cnproxy.spiders']
NEWSPIDER_MODULE = 'cnproxy.spiders'

ITEM_PIPELINES = ['cnproxy.pipelines.CnproxyPipeline']

USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.54 Safari/536.5'

COOKIES_ENABLED = False

# DOWNLOAD_DELAY = 3

MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017
MONGODB_DBNAME = 'bilibili'
MONGODB_DOCNAME = 'proxy'

# FEED_URI = u'proxy.csv'
# FEED_FORMAT = 'CSV'
