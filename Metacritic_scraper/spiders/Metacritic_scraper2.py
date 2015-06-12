from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.spiders import CrawlSpider
from scrapy.log import *
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
import scrapy
from scrapy.http import Request
import urlparse
from scrapy.item import Item, Field
from scrapy import Spider
from scrapy.selector import Selector
 
class MetacriticItem(scrapy.Item):
    Album_title = scrapy.Field()
    Artist = scrapy.Field()
    Release_date = scrapy.Field()
    Critic_review = scrapy.Field()
    User_review = scrapy.Field()
    Score = scrapy.Field()
 
class MetaSpider(CrawlSpider):
 
    name = 'Metacritic_scraper2'
    start_urls = [
        'http://www.metacritic.com/browse/albums/release-date/available/date'
    ]
    rules = (
    Rule(SgmlLinkExtractor(allow=('http://www.metacritic.com/browse/albums/release-date/available/date')), callback="parse", follow= True),

)
 
    def parse(self, response):
       hxs = HtmlXPathSelector(response)
       urls = hxs.select('//*[@id="main"]/div[1]/div[2]/div[2]/div/ol/li/div/div/a/@href').extract()  ## only grab url with content in url name
       for i in urls:
           yield Request(urlparse.urljoin("http://www.metacritic.com", i[1:]),callback=self.parse_url)

       #ex_blog_urls = hxs.select('//*[@id="main"]/div/div[4]/div/div[1]/div[2]/ol/li[1]/div/div/div/div/div/div[2]/ul/li[2]/a/@href').extract()  ## only grab url with content in url name
       #for j in ex_blog_urls:
           #yield Request(urlparse.urljoin("http://www.metacritic.com/music", j[1:]),callback=self.parse_url)

       next_page = hxs.select('//*[@id="main"]/div[1]/div[3]/div/div/div/div[1]/span[2]/a/@href').extract()  ## only grab url with content in url name
       for i in next_page:
           yield Request(urlparse.urljoin("http://www.metacritic.com", i[1:]),callback=self.parse)



    def parse_url(self, response):
       hxs = HtmlXPathSelector(response)
       item = MetacriticItem()
       item['Album_title'] = hxs.select('//div/div[1]/div[2]/span/a/span/text()').extract()
       item['Artist'] = hxs.select('//*[@id="main"]/div/div[1]/div[3]/a/span/text()').extract()
       item['Release_date'] = hxs.select('//*[@id="main"]/div/div[1]/div[4]/ul/li[2]/span[2]/text()').extract()
       item['Critic_review'] = hxs.select('//div[@class="source"]/a/@href').extract() ## this grabs it
       item['User_review'] = hxs.select('//div[@class="name"]/a/@href').extract() 
       item['Score'] = hxs.select('//*[@id="main"]/div/div[4]/div/div[1]/div[2]/ol/li[1]/div/div/div/div/div/div[1]/div[1]/div[2]/div/text()').extract() 
       with open('log2.txt', 'a') as f:
           f.write('Album_title: {0}, Artist: {1},Release_date: {2},Critic_review: {3},User_review: {4},Score: {5}\n'.format(item['Album_title'], item['Artist'],item['Release_date'], item['Critic_review'],item['User_review'], item['Score']))