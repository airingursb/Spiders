# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider
from scrapy.http import Request
from scrapy.selector import Selector
from cnproxy.items import CnproxyItem

class Cnproxy(CrawlSpider):
    name = "cnproxy"
    redis_key = 'cnproxy:start_urls'
    start_urls = ['http://www.haodailiip.com/guonei']

    url = 'http://www.haodailiip.com/guonei'

    def parse(self, response):
        # print response.body
        selector = Selector(response)
        Proxys = selector.xpath('//table[@class="proxy_table"]')
        for eachProxy in Proxys:
            ip = eachProxy.xpath('tr/td[1]/text()').extract()
            port = eachProxy.xpath('tr/td[2]/text()').extract()
            anonymous = eachProxy.xpath('tr/td[5]/text()').extract()
            for i in range(1, len(ip)):
                item = CnproxyItem()
                item['ip'] = ip[i]
                item['port'] = port[i]
                item['anonymous'] = anonymous[i]
                yield item
        # nextLink = selector.xpath('//span[@class="next"]/link/@href').extract()
        # #第10页是最后一页，没有下一页的链接
        # if nextLink:
        #     nextLink = nextLink[0]
        #     print nextLink
        #     yield Request(self.url + nextLink, callback=self.parse)

