# -*- coding: utf-8 -*-
import scrapy
from aqi.items import AqiItem
import pandas as pd


class MyaqiSpider(scrapy.Spider):
    name = 'myaqi'
    allowed_domains = ['www.aqistudy.cn']
    base_url = 'https://www.aqistudy.cn/historydata/'
    start_urls = ['https://www.aqistudy.cn/historydata/daydata.php?city=北京&month=201402']
    cities = ['北京']
    Dates = pd.date_range(start='1/2014', end='9/2019', freq='M')

    def parse(self, response):
        URLs = []
        for city in self.cities:
            for date in self.Dates:
                url = self.base_url + "daydata.php?city=" + city + "&month=" + date.strftime("%Y%m")
                URLs.append(url)
        for url in URLs:
            yield scrapy.Request(url,callback = self.parse_data,meta={"city":city,'source':url})


    def parse_data(self, response):
        node_list = response.xpath('//tbody/tr')
        n0 = node_list.pop(0)

        for node in node_list:
            item = AqiItem()
            item['city'] = '北京'
            item['date'] = node.xpath('./td[1]//text()').get()
            item['AQI'] = node.xpath('./td[2]//text()').get()
            item['qLevel'] = node.xpath('./td[3]//text()').get()
            item['PM25'] = node.xpath('./td[4]//text()').get()
            yield item
