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

DOWNLOAD_TIMEOUT = 15
#COOKIES_ENABLED = True
#COOKIES_DEBUG = True
# DOWNLOAD_DELAY = 2
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'books_crawl (+http://www.yourdomain.com)'
USER_AGENT = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.22 (KHTML, like Gecko) Chrome/25.0.1364.97 Safari/537.22 AlexaToolbar/alxg-3.1"
 
#DEFAULT_REQUEST_HEADERS={
#    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#    'Accept-Language': 'en',
#    'X-JAVASCRIPT-ENABLED': 'true',
#}

DOWNLOADER_MIDDLEWARES = {
    'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware': 400,
    'scrapy.contrib.downloadermiddleware.cookies.CookiesMiddleware':700,
}
