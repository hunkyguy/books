#coding:utf-8
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from books_crawl.items import BooksScrapyItem

__author__ = 'Zep'

class Books(CrawlSpider):
    name = 'books'
    allowed_domains = ['douban.com']
    start_urls = ['http://read.douban.com']
    rules = [Rule(SgmlLinkExtractor(allow=('/ebook/\d+')), callback='parse_book')]
    #rules = [Rule(SgmlLinkExtractor(allow=('/ebook/\d+')), callback='parse_book', follow=True)]

    def parse_book(self, response):
        sel = Selector(response)
        book = BooksScrapyItem()
        book['url'] = response.url
        name = sel.xpath('//h1[@class="article-title"]/text()').extract()
        rate = sel.xpath('//span[@class="rating-average"]/text()').extract()
        cover = sel.xpath('//div[@class="cover"]/img/@src').extract()
        if name:
            book['name'] = name[0]
        if rate:
            book['rate'] = rate[0]
        if cover:
            book['cover'] = cover[0]

        for i in sel.xpath('//div[@class="article-meta"]/p'):
            key = i.xpath('span[@class="label"]/text()').extract()
            value = i.xpath('span[@class="labeled-text"]/text()').extract()
            if key and value:
                if key[0] == u"作者":
                    book['author'] = '%s' %value[0]
                if key[0] == u"译者":
                    book['translator'] = '%s' %value[0]
                if key[0] == u"类别":
                    book['category'] = '%s' %value[0]
                if key[0] == u"出版信息":
                    book['publisher'] = '%s' %value[0]
                if key[0] == u"字数":
                    book['words'] = '%s' %value[0]
        yield book

#from scrapy.spider import BaseSpider
#class DmozSpider(BaseSpider):
#    name = "dmoz"
#    allowed_domains = ["dmoz.org"]
#    start_urls = [
#        #"http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
#        'http://read.douban.com/ebook/1484452/',
#        'http://read.douban.com/ebook/563132/',
#        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
#    ]
#
#    def parse(self, response):
#        filename = response.url.split("/")[-2]
#        open(filename, 'wb').write(response.body)
