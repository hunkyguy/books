#coding:utf-8
# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class BooksDoubanScrapyItem(Item):
    # define the fields for your item here like:
    url = Field()
    name = Field()
    cover = Field()
    author = Field()
    translator = Field()
    category = Field()
    publisher = Field()
    words = Field()
    rate = Field()
