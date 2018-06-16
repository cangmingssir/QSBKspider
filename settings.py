# coding:utf-8

#配置
#配置请求头
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'
}

#配置代理
proxies={
    'http':['112.115.57.20:3128','121.42.167.160:3128','101.6.97.134:1080'],
    'https':'183.159.228.92:3128',
}

#配置爬虫的起始位置
run_url='https://www.qiushibaike.com'

#配置xpath路径
author_path = '//div[starts-with(@class,"author")]'
home_path = './a[1]/@href'
src_path = './a/img/@src'
name_path = './a/img/@alt'
age_path = './div/text()'

next_page_path = '//ul[@class="pagination"]/li[last()]/a/@href'

#配置数据库
DATABASE = {
    #属性名要参考pymysql.connect（）函数中的参数
    'default':{
        'host':'localhost',
        'port':3306,
        'user':'root',
        'password':'root',
        'db':'qiubai',
        'charset':'utf8'
    }
}