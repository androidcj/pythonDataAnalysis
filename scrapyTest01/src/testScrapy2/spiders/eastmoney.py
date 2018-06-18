# -*- coding: utf-8 -*-
import scrapy


class EastmoneySpider(scrapy.Spider):
    name = "eastmoney1"
    allowed_domains = ["http://www.eastmoney.com/"]
    start_urls = (
        'http://www.eastmoney.com//',
    )

    def parse(self, response):
        filepath ="E:/python/page.html"
        with open(filepath,'w') as f_obj:
            f_obj.write(response.body)
