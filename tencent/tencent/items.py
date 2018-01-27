# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentItem(scrapy.Item):
    # define the fields for your item here like:
    # 职位名
    name = scrapy.Field()
    # 详情页面链接
    detail_link = scrapy.Field()
    # 职位类别
    category = scrapy.Field()
    # 人数
    number = scrapy.Field()
    # 地址
    address = scrapy.Field()
    # 发布时间
    pub_date = scrapy.Field()











