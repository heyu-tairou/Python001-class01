# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class HeyuSpidersPipeline:
    def process_item(self, item, spider):
		mname = item['name']
        mtype = item['hover-tag']
        mdate = item['movie-hover-title movie-hover-brief']
        output = f'|{mname}|\t|{mtype}|\t|{mdate}|\n\n'
        with open('./doubanmovie.txt', 'a+', encoding='utf-8') as article:
            article.write(output)
        return item
