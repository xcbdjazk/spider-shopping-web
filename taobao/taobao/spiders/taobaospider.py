# -*- coding: utf-8 -*-
import scrapy
import json
from taobao.items import TaobaoItem

class TaobaospiderSpider(scrapy.Spider):
    name = 'taobaospider'
    allowed_domains = ['tce.taobao.com']
    start_urls = ['https://tce.taobao.com/api/mget.htm?tce_sid=1584548&tce_vid=0,1,1,0,0&tid=,,,,&tab=,,,,&topic=,,,,&count=,,,,&env=online,online,online,online,online']
    '''https: // tce.taobao.com / api / mget.htm?tce_sid = 1584548 & tce_vid = 0, 1, 1, 0, 0 & tid =, , , , & tab =, , , , & topic =, , , , & count =, , , , & env = online, online, online, online, online'''

    def parse(self, response):
        # response.body.decode(response.encoding)
        # response.encoding = 'utf-8'

        data=json.loads(response.body)
        # print( type(date),len())
        data=data['result']['1584548']['result']
        i=1
        for ecah in data:
            shops=ecah['shops']
            for product in shops:
                itme=TaobaoItem()
                itme['sname']=product['item_title']
                # a=itme['sname'].
                # print(a,type(a))
                itme['price']=product['item_current_price']
                itme['url_link']=product['item_url']
                itme['img_path']=product['item_pic']
                itme['spider_id'] = i
                yield itme
            i+=1