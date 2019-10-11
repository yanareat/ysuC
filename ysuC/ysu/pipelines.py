# -*- coding: utf-8 -*-

# python连接mongodb数据库
# import pymongo
# from ysu.settings import mongoHost,mongoPort,mongoDBname,mongoDBcollection

# 导入json
import json
# 导入框架
import scrapy
# ImagesPipeline
from scrapy.pipelines.images import ImagesPipeline
# 导入mysql
import pymysql

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

# # ysuItem存数据库
# class YsuPipeline(object):
#     def __init__(self):
#         host=mongoHost
#         port=mongoPort
#         dbname=mongoDBname
#         sheetname=mongoDBcollection
#         client=pymongo.MongoClient(host=host,port=port)
#         mydb=client[dbname]
#         self.post=mydb[sheetname]
#
#     def process_item(self, item, spider):
#         data = dict(item)
#         self.post.insert(data)
#         return item
#

# 转化数组到json
def arr2Json(items):
    cons = {}
    for i in range(len(items)):
        cons[i] = items[i]
    return json.dumps(cons, ensure_ascii=False)

# 图片下载
class YsuImagesPipeline(ImagesPipeline):
    # 得到图片请求
    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            yield scrapy.Request(item['url'][0:item['url'].rfind('/') + 1] + image_url, meta={'item': image_url})
    # 设置文件名
    def file_path(self, request, response=None, info=None):
        return request.meta['item']
    # 下载完成图片
    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if image_paths:
            item['image_paths'] = image_paths
        return item

# 存实体对象到mysql
class YsuMysqlPipeline(object):
    # 初始化
    def __init__(self):
        dbparams = {
            'host': '39.106.1.127',
            'port': 3306,
            'user': 'evan',
            'password': '222430',
            'database': 'ysu',
            'charset': 'utf8'
        }
        self.conn = pymysql.connect(**dbparams)
        self.cursor = self.conn.cursor()
        self._sql = None
    # 储存过程
    def process_item(self, item, spider):
        item['content']=arr2Json(item['content'])
        prou=item['url'][0:item['url'].rfind('/') + 1]
        for i in range(len(item['image_urls'])):
            item['image_urls'][i] = prou + item['image_urls'][i]
        for i in range(len(item['image_paths'])):
            item['image_paths'][i] = item['image_paths'][i].replace("../../","http://39.106.1.127:8080/")
        item['image_urls'] = arr2Json(item['image_urls'])
        item['image_paths']=arr2Json(item['image_paths'])

        self.cursor.execute(self.sql, (item['url'], item['title'], item['event_time'],item['abstract'],item['time'], item['author'], item['content'],item['html'],item['format'],item['image_urls'],item['image_paths']))
        self.conn.commit()
        return item

    @property
    def sql(self):
        if not self._sql:
            self._sql = """
                insert into ysu_news(Id,Url,Title,Time,Abstract,AddTime,Author,Content,Original,Html,ImageUrls,ImagePaths) values(null,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                """
            return self._sql
        return self._sql