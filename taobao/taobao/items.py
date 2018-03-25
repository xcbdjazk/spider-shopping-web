# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TaobaoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    sname=scrapy.Field()
    price=scrapy.Field()
    url_link=scrapy.Field()
    img_path=scrapy.Field()
    spider_id=scrapy.Field()
