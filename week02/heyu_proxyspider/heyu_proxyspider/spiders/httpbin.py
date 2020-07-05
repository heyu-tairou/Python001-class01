# -*- coding: utf-8 -*-
import scrapy
import pymysql
import pandas as pd
from scrapy.selector import Selector

class HttpbinSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    # 起始URL列表
    start_urls = ['https://maoyan.com/films?showType=3']

    def start_requests(self):

        user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'

        i=0
        url = f'https://maoyan.com/films?showType=3'
        yield scrapy.Request(url=url, callback=self.parse, dont_filter=False,
        headers = {'user-agent':user_agent,'cookie':'uuid_n_v=v1; uuid=BFB01E40BA0311EA99166F1ED1B5ECBED384B4FD2A7D4889A78EF6C477F42E7E; _csrf=01954256c3708a33d335b7d52f4bd504e1452e6dd9ae33a392eecae586e49e4c; _lxsdk_cuid=173000afddac8-00db7e5cc27f01-6457742b-e1000-173000afddbc8; _lxsdk=BFB01E40BA0311EA99166F1ED1B5ECBED384B4FD2A7D4889A78EF6C477F42E7E; mojo-uuid=5fcc263c5258a82404e85a42333c8fdc; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1593433587; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593444074; __mta=150920713.1593433587484.1593444072545.1593444074663.14; mojo-session-id={"id":"a4070ec7c82b5a19458585f0f695fb8f","time":1593443472566}; mojo-trace-id=40; _lxsdk_s=17300a1d45c-84c-591-fa3%7C%7C61'}
        )

        
    def parse(self, response):       
        # print(response.url)
        movies = Selector(response=response).xpath('//*[@id="app"]/div/div[2]/div[2]/dl/dd[1]')
        print('========')
        title = []
        mtypes = []
        mdates = []
        for movie in movies:
            title = movie.xpath('//dd/div[1]/div[2]/a/div/div[1]/span[1]/text()').extract()
            mtypes = movie.xpath('//dd/div[1]/div[2]/a/div/div[2]/text()').extract()
            mdates = movie.xpath('//dd/div[1]/div[2]/a/div/div[4]/text()').extract()
        
        mtype = []
        m = 0
        for mm in mtypes:
            m += 1
            if(m % 2) == 0:
                mtype.append(str(mm).strip())

        mdate = []
        m = 0
        for mm in mdates:
            m += 1
            if(m % 2) == 0:
                mdate.append(str(mm).strip())
                
        # 数据库连接信息
        conn = pymysql.connect(host = 'localhost',
                       port = 3306,
                       user = 'root',
                       password = '123456',
                       database = 'mysql',
                       charset = 'utf8mb4'
                        )
        cursor = conn.cursor()

        # 如果数据表已经存在使用 execute() 方法删除表。
        cursor.execute("DROP TABLE IF EXISTS movies")

        # 创建数据表SQL语句
        sql = """CREATE TABLE movies (name  CHAR(255) NOT NULL )"""

        cursor.execute(sql)

        mstr = ''
        k = 0
        for x in title:
            mstr = x
            # 拼装爬到的电影信息
            mstr += '、' + str(mtype[k]).strip()
            mstr += '、' + str(mdate[k]).strip() + "\t"
            k += 1
            # SQL 把爬到的电影信息插入到表
            sql1 = 'INSERT INTO movies(name) VALUES ("' + mstr + '")' 
            try:
                # 执行sql语句
                cursor.execute(sql1)
                # 提交到数据库执行
                conn.commit()
            except:
                conn.rollback()

            if(k == 10):
                break
            


