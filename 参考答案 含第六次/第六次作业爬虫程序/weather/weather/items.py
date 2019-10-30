# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WeatherItem(scrapy.Item):
    # define the fields for your item here like:
    # 日期
    date = scrapy.Field()
    # 风向
    windDirec = scrapy.Field()
    # 风力
    windLevel = scrapy.Field()
    # 数据源
    source = scrapy.Field()
