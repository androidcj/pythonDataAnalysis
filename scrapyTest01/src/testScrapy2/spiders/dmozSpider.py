# -*- coding: utf-8 -*-
import scrapy
from testScrapy2.items import Testscrapy2Item



class DmozSpider(scrapy.Spider):
    name = "dmoz_spider"
    allowed_domains = ["dmoz.org/"]
    start_urls = (
        'http://www.dmoz.org/',
    )

    def parse(self, response):
        aside_nodes = response.xpath('//aside')   #表示根节点下的 aside标签   根节点一般为<html>
        for aside_node in aside_nodes:
            item = Testscrapy2Item()
            top_cat = aside_node.xpath('.//h2//a//text()').extract()   #返回当前节点下 的 h2 节点下 a 节点下的文本
            sub_cat = aside_node.xpath('.//h3//a//text()').extract()   #返回当前节点下 的 h3 节点下 a 节点下的文本
            item['top_cat'] = top_cat
            item['sub_cat'] = sub_cat
            yield item
            
        