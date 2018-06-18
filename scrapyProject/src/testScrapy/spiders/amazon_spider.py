# -*- coding: utf-8 -*-
import scrapy


class AmazonSpider(scrapy.Spider):
    name = "amazon_spider"
    allowed_domains = ["https://www.amazon.cn/%E5%9B%BE%E4%B9%A6/b/ref=topnav_storetab_b?ie=UTF8"]
    start_urls = (
        'https://www.amazon.cn/%E5%9B%BE%E4%B9%A6/b/ref=topnav_storetab_b?ie=UTF8&node=658390051',
    )

    def parse(self, response):
        filepath ="./page.html"
        with open(filepath,'w') as f_obj:
            f_obj.write(response.body)
        
       
