import requests
import pandas as pd
from bs4 import BeautifulSoup as bs

def get_url_name(myurl):
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'

    header = {'user-agent':user_agent,'cookie':'uuid_n_v=v1; uuid=BFB01E40BA0311EA99166F1ED1B5ECBED384B4FD2A7D4889A78EF6C477F42E7E; _csrf=01954256c3708a33d335b7d52f4bd504e1452e6dd9ae33a392eecae586e49e4c; _lxsdk_cuid=173000afddac8-00db7e5cc27f01-6457742b-e1000-173000afddbc8; _lxsdk=BFB01E40BA0311EA99166F1ED1B5ECBED384B4FD2A7D4889A78EF6C477F42E7E; mojo-uuid=5fcc263c5258a82404e85a42333c8fdc; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1593433587; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593444074; __mta=150920713.1593433587484.1593444072545.1593444074663.14; mojo-session-id={"id":"a4070ec7c82b5a19458585f0f695fb8f","time":1593443472566}; mojo-trace-id=40; _lxsdk_s=17300a1d45c-84c-591-fa3%7C%7C61'}
    response = requests.get(myurl,headers=header)
    bs_info = bs(response.text, 'html.parser')
    
    # print(response.status_code)
    i = 0
    move_list = []
    for tags in bs_info.find_all('div', attrs={'class':'movie-hover-info'}):
        i = i + 1
        if(i > 10):
            break
        # 获取电影名字
        # print(tags.find('span',).text)
        mstr = tags.find('span',).text
        # print('aa-df')
        # 获取电影类型
        # print(tags.find_all('div',attrs={'class':'movie-hover-title'})[1].text[4:].strip())
        mstr += '、' + tags.find_all('div',attrs={'class':'movie-hover-title'})[1].text[4:].strip()
        # 获取电影上映时间
        # print(tags.find_all('div',attrs={'class':'movie-hover-title'})[3].text[6:].strip())
        mstr += '、' + tags.find_all('div',attrs={'class':'movie-hover-title'})[3].text[6:].strip() +"\t"

        move_list.append(mstr)
        # print(f.select(".movie-hover-title")[0].select(".name noscore")[0].text)
        # print(f.select(".movie-hover-title")[1].contents[1].strip())
        # print(f.select(".movie-hover-title")[0].text)
    
    print(" ".join(x for x in move_list))

    movie1 = pd.DataFrame(data = move_list)

    # windows需要使用gbk字符集
    movie1.to_csv('./movie1.csv', encoding='utf_8_sig', index=False, header=False)


# 生成包含所有页面的元组
urls = tuple(f'https://maoyan.com/films?showType=3&start=1&filter=' for page in range(1))

print(urls)

# 控制请求的频率，引入了time模块
from time import sleep

sleep(1)

for page in urls:
    get_url_name(page)
    sleep(1)



