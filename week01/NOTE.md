学习笔记
//windows清理控制台
import os				# 导入os模块
os.system('cls')		# 执行cls命令清空Python控制台
==============================================================
//查看导入包的所有方法
import math
dir(math)

//查看每个方法怎么使用
help(math)

==============================================================
创建scrapy爬虫项目
scrapy startproject spiders

//爬取域名，命名为movies
scrapy genspider movies douban.com

//查看目录下的文件
ls spider/

//清除屏幕
clear

//打开文件
cat **

//下载课程代码后，运行爬虫名称douban
scrapy crawl douban