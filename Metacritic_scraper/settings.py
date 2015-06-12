# -*- coding: utf-8 -*-

# Scrapy settings for Metacritic_scraper project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'Metacritic_scraper'

SPIDER_MODULES = ['Metacritic_scraper.spiders']
NEWSPIDER_MODULE = 'Metacritic_scraper.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'Metacritic_scraper (+http://www.yourdomain.com)'

#ITEM_PIPELINES = ['Metacritic_scraper.pipelines.MongoDBPipeline', ]

#MONGODB_SERVER = "localhost"
#MONGODB_PORT = 27017
#MONGODB_DB = "metacriticDB"
#MONGODB_COLLECTION = "musicBlogs"