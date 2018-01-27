# -*- coding: utf-8 -*-
import scrapy


class Tencent1Spider(scrapy.Spider):
    name = 'tencent1'
    allowed_domains = ['tencent.com']
    start_urls = ['http://tencent.com/']

    def parse(self, response):
        pass
