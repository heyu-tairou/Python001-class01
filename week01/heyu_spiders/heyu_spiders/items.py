# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class HeyuSpidersItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    mname = scrapy.Field()
    mtype = scrapy.Field()
    mdate = scrapy.Field()
