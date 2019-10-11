# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class YsuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass
    # 标题
    title = scrapy.Field()
    # 时间
    time = scrapy.Field()
    # 地址
    url = scrapy.Field()
    # 内容
    content = scrapy.Field()
    # 摘要
    abstract = scrapy.Field()
    # 作者
    author = scrapy.Field()
    # 图片地址
    image_urls = scrapy.Field()
    # 图片路径
    image_paths = scrapy.Field()
    # html
    html = scrapy.Field()
    # 格式化html
    format = scrapy.Field()
    # 时间发生时间
    event_time = scrapy.Field()