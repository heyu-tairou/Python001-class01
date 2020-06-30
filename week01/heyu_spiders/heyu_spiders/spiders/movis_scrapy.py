import scrapy
import pandas as pd
from scrapy.selector import Selector

class DoubanSpider(scrapy.Spider):

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
        # 打印网页的url
        
        print(response.url)
        # movies = Selector(response=response).xpath('//*[@id="app"]/div/div[2]/div[2]/dl/dd[1]/div[1]/div[2]/a/div')
        movies = Selector(response=response).xpath('//*[@id="app"]/div/div[2]/div[2]/dl/dd[1]')
        # movies = Selector(response=response).xpath('//dd')
        print('========')
        # print(movies.extract())
        j = 0
        title = []
        mtypes = []
        mdates = []
        for movie in movies:
            if(j > 1):
                break
            # title = movie.xpath('//*[@id="app"]/div/div[2]/div[2]/dl/dd[1]/div[1]/div[2]/a/div/div[1]/span[1]/text()').extract()
            title = movie.xpath('//dd/div[1]/div[2]/a/div/div[1]/span[1]/text()').extract()
            # //*[@id="app"]/div/div[2]/div[2]/dl/dd[2]/div[1]/div[2]/a/div/div[1]/span[1]
            # print(movie.extract())
            # print(title)
            # link = movie.xpath('./a/@href')
            # mtype = movie.xpath('//*[@id="app"]/div/div[2]/div[2]/dl/dd[1]/div[1]/div[2]/a/div/div[2]/text()').extract()
            mtypes = movie.xpath('//dd/div[1]/div[2]/a/div/div[2]/text()').extract()
            # print(str(mtype).strip())
            # mdate = movie.xpath('//*[@id="app"]/div/div[2]/div[2]/dl/dd[1]/div[1]/div[2]/a/div/div[4]/text()').extract()
            mdates = movie.xpath('//dd/div[1]/div[2]/a/div/div[4]/text()').extract()
            # print(str(mdate).strip())
            # print(title.extract())
            # print(link.extract())
            # print(title.extract_first())
            # print(link.extract_first())
            # print(title.extract_first().strip())
            # print(link.extract_first().strip())
        
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

        mstr = ''
        move_list = []
        k = 0
        for x in title:
            mstr = x
            mstr += '、' + str(mtype[k]).strip()
            mstr += '、' + str(mdate[k]).strip() + "\t"
            move_list.append(mstr)
            k += 1
            if(k == 10):
                break
        # print('00000000000000000000')
        print(mstr)

        movie1 = pd.DataFrame(data = move_list)

        # windows需要使用gbk字符集
        movie1.to_csv('./movie1.csv', encoding='utf_8_sig', index=False, header=False)



   