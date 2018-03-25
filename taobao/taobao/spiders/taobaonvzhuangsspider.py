# -*- coding: utf-8 -*-
import scrapy
import json
from taobao.items import TaobaoItem
from selenium import webdriver

class TaobaonvzhuangsspiderSpider(scrapy.Spider):
    name = 'taobaonvzhuangsspider'
    allowed_domains = ['tce.taobao.com']
    start_urls = ['https://tce.taobao.com/api/mget.htm?tce_sid=1114134,1911961,2246347,2246468,1911959,1911898,1114192']

    def parse(self, response):
        content=json.loads(response.text)
        i=4
        for key,values in content['result'].items():
            result=values['result']
            for lists in result:
                item=TaobaoItem()
                item['sname']=lists['item_title']
                item['price']=lists['item_current_price']
                item['url_link']=lists['item_url']
                item['img_path']=lists['item_pic']
                item['spider_id']=i
                yield  item
            i +=1