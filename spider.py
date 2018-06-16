# coding:utf-8
import os
import ssl
from urllib import request

import settings
from lxml import etree

from db import DB
from item import UserItem
import random

class QiuBaiSpider():
    def __init__(self):
        ssl._create_default_https_context = ssl._create_unverified_context
        self.db = DB()
        self.opener = request.build_opener(request.ProxyHandler(proxies={'http':random.choice(settings.proxies['http'])}))
        print('爬虫开始走')


    def __del__(self):
        print('感谢有你，我要走了。。。')
        self.db.close()

    def run(self):
        next_url = settings.run_url
        while True:
            html = self.request(next_url)
            next_url = self.parse(html)
            if not next_url:
                break

    def request(self,url):
        req = request.Request(url,headers=settings.headers)
        # resp = request.urlopen(req)
        resp = self.opener.open(req)
        if resp.status == 200:
            print('ok')
            html = resp.read().decode()
            print(html)
            return html

    #网页解析函数
    def parse(self,html):
        et = etree.HTML(html)
        authors = et.xpath(settings.author_path)
        print(authors)
        for author in authors:  #author是Element对象类型
            #print(author)
            try:
                home = author.xpath(settings.home_path)[0] #获取当前节点对象的子节点对象
                #print(type(home))
                id = home.split('/')[-2]
                name = author.xpath(settings.name_path)[0]
                age = author.xpath(settings.age_path)[0]
                img = 'http:'+author.xpath(settings.src_path)[0]
                print('dsfsd',img)
            except:
                pass
            else:
                item = UserItem(id,name,age,img,home)
                print(item)
                #将数据存入到数据库中
                self.db.save(item)
                self.saveImg(img,id)
        #读取下一页的链接
        try:
            next_url = settings.run_url+et.xpath(settings.next_page_path)[0]
        except:
            pass
        else:
            return next_url

    def saveImg(self,url,id):
        filename = './head/{}.{}'.format(id,url.split('.')[-1].split('?')[0])
        if os.path.exists(filename):
           return
        request.urlretrieve(url,filename=filename)
        print(filename,'图片下载成功')

if __name__ == '__main__':
    QiuBaiSpider().run()