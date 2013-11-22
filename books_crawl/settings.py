# Scrapy settings for books_douban_scrapy project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'books_crawl'

SPIDER_MODULES = ['books_crawl.spiders']
NEWSPIDER_MODULE = 'books_crawl.spiders'

DEFAULT_ITEM_CLASS = 'books_crawl.items.BooksScrapyItem'
ITEM_PIPELINES = ['books_crawl.pipelines.BooksScrapyPipeline']

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'books_crawl (+http://www.yourdomain.com)'
