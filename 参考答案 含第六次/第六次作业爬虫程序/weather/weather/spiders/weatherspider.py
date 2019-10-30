# -*- coding: utf-8 -*-
import scrapy
from weather.items import WeatherItem
import pandas as pd

class WeatherspiderSpider(scrapy.Spider):
    name = 'weatherspider'
    #allowed_domains = ['example.com']
    base_url = 'https://lishi.tianqi.com/'
    start_urls = [base_url]
    #cities  = ['beijing','shanghai','tianjin','chongqin','zhengzhou']
    cities = ['beijing']
    Dates = pd.date_range(start='1/2014',end='9/2019', freq='M')

    def parse(self, response):
        URLs = []
        for city in self.cities:
            for date in self.Dates:
                url = self.base_url + city+'/'+date.strftime("%Y%m")+'.html'
                URLs.append(url)
        for url in URLs:
            yield scrapy.Request(url,callback = self.parse_data,meta={"city":city,'source':url})

    def parse_data(self,response):
        node_list = response.xpath('//div[@class="tqtongji2"]/ul')
        n0 = node_list.pop(0)
        for node in node_list:
            #print (node)
            item = WeatherItem()
            item['date'] = node.xpath('./li[1]/a/text()').extract_first()
            item['windDirec'] = node.xpath('./li[5]/text()').extract_first()
            item['windLevel'] = node.xpath('./li[6]/text()').extract_first()
            item['source'] = response.meta['source']
            yield item
