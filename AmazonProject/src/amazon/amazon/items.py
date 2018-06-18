# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazonItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    rank_number = scrapy.Field()
    book_name = scrapy.Field()
    author = scrapy.Field()
    star_rank = scrapy.Field()
    book_type = scrapy.Field()
    price = scrapy.Field()
    
    