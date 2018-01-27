# -*- coding: utf-8 -*-
import scrapy
from tencent.items import TencentItem

class TencentSpider(scrapy.Spider):
    name = 'tencent1'
    # 允许的域不需要加协议
    allowed_domains = ['tencent.com']
    # 修改起始的url
    start_urls = ['https://hr.tencent.com/position.php']

    def parse(self, response):
        # 获取职位节点列表
        node_list = response.xpath('//tr[@class="even"]|//tr[@class="odd"]')
        # print(len(node_list))

        # 编列节点列表，从没一个节点中抽取数据
        for node in node_list:
            # item实例化
            item = TencentItem()
            # 抽取数据
            item['name'] = node.xpath('./td[1]/a/text()').extract()[0]
            item['detail_link'] = 'https://hr.tencent.com/' + node.xpath('./td[1]/a/@href').extract()[0]
            # extract_first()提取结果的第一个，如果存在则提取，如果不存在则赋值为None
            item['category'] = node.xpath('./td[2]/text()').extract_first()
            item['number'] = node.xpath('./td[3]/text()').extract()[0]
            item['address'] = node.xpath('./td[4]/text()').extract()[0]
            item['pub_date'] = node.xpath('./td[5]/text()').extract()[0]

            # 返回数据给引擎
            yield item
