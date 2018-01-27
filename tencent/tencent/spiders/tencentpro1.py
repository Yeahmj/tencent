# -*- coding: utf-8 -*-
import scrapy
from tencent.items import TencentItemPro

class TencentSpider(scrapy.Spider):
    name = 'tencentpro1'
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
            item = TencentItemPro()
            # 抽取数据
            item['name'] = node.xpath('./td[1]/a/text()').extract()[0]
            item['detail_link'] = 'https://hr.tencent.com/' + node.xpath('./td[1]/a/@href').extract()[0]
            # extract_first()提取结果的第一个，如果存在则提取，如果不存在则赋值为None
            item['category'] = node.xpath('./td[2]/text()').extract_first()
            item['number'] = node.xpath('./td[3]/text()').extract()[0]
            item['address'] = node.xpath('./td[4]/text()').extract()[0]
            item['pub_date'] = node.xpath('./td[5]/text()').extract()[0]


            # 返回数据给引擎
            # yield item

            # 提交详情页面的请求
            yield scrapy.Request(
                item['detail_link'],
                callback=self.parse_detail,
                meta={'meta1':item}
            )

        # 获取下一页链接，并且做成请求发送个引擎
        # 拼接下一页url
        next_url = 'https://hr.tencent.com/' + response.xpath('//*[@id="next"]/@href').extract()[0]
        # 判断是否到达最后一页
        if 'javascript:;' not in next_url:
            # 没有到达最后一页就发送请求，模拟翻页
            yield scrapy.Request(next_url,callback=self.parse)

    def parse_detail(self, response):
        item = response.meta['meta1']
        item['duty'] = ''.join(response.xpath('//tr[3]/td/ul/li/text()').extract())
        item['require'] = ''.join(response.xpath('//tr[4]/td/ul/li/text()').extract())

        yield item


