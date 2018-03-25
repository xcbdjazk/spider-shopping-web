# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
# import json

class TaobaoPipeline(object):
    def __init__(self):
        import sys
        reload(sys)
        sys.setdefaultencoding('utf-8')
        self.conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123', db='shopping',charset='utf8')
        # 创建游标
        self.cursor = self.conn.cursor()
        # dele = 'truncate table index_spider_porduct'
        # self.cursor.execute(dele)
        # self.conn.commit()

    def process_item(self, item, spider):
        item =dict(item)
        sname = item['sname'].encode('utf-8')
        price = item['price'].encode('utf-8')
        url_link = item['url_link'].encode('utf-8')
        img_path = item['img_path'].encode('utf-8')
        spider_id=item['spider_id']
        # print(item)
        sql="INSERT INTO index_spider_porduct(sname,price,url_link,img_path,spider_id) VALUES ('%s','%s','%s','%s','%s');"%(sname,price,url_link,img_path,spider_id)
        self.cursor.execute(sql)
        # 提交到数据库执行
        self.conn.commit()
        return item
    def close_spider(self, spider):
        self.conn.close()

