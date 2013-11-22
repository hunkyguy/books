#coding:utf-8
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import sys

class BooksScrapyPipeline(object):
    #def process_item(self, item, spider):
    #    return item
    #
    def __init__(self):
        self.file = open('books.json', 'wb')
        reload(sys)
        sys.setdefaultencoding('utf-8')
    def process_item(self, item, spider):
        #line = json.dumps(dict(item)) + "\r\n"
        line = json.dumps(dict(item), ensure_ascii=False) + "\r\n"
        self.file.write(line)
        return item
