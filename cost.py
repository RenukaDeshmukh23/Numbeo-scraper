# -*- coding: utf-8 -*-
import scrapy
import pyperclip,sys

country=pyperclip.paste()

class CostSpider(scrapy.Spider):
    name = 'cost'
    allowed_domains = ['numbeo.com/cost-of-living/']
    start_urls = ['https://www.numbeo.com/cost-of-living/in/'+country+'?displayCurrency=USD']

    def parse(self, response):
        for table in response.xpath('//*[@class="data_wide_table new_bar_table"]//tr'):
            head=table.xpath('.//th[1]/text()').extract_first()
            name= table.xpath('.//td[1]/text()').extract_first()
            price= table.xpath('.//td[2]//text()').extract_first()
            range=table.xpath('.//td[3]//span//text()').extract()

            yield {'Heading':head,
                    'Name':name,
                    'Price':price,
                    'Range':range}
