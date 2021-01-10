# import scrapy
# from crawling.items import MovieItem

# class RottenTomatoesSpider(scrapy.Spider):

#     name = 'rottentomatoes'
#     allowed_domains = ['rottentomatoes.com']
#     start_urls = ['https://www.rottentomatoes.com/top/bestofrt/?year=2018',]

#     def parse(self, response):
#         rows = response.xpath('//*[@class="table"]/tr/td[3]/a/@href').get()
#         for row in rows:
#             link = 'https://www.rottentomatoes.com' + row
#             yield scrapy.Request(url=link, callback=self.parse_item)

#     def parse_item(self, response):
#         item = MovieItem()
#         import ipdb; ipdb.set_trace()
#         #item["title"] = response.xpath('//*[@class="table"]/tr/td[3]/a/@href').extract()
#         item['title'] = response.css('h1.mop-ratings-wrap__title ::text').extract_first()
#         item["url"] = response.url
#         item["identifier"] = response.url.split("/")[4]
        
#         return item

#         #
import scrapy
from crawling.items import MovieItem

class TecnoblogSpider(scrapy.Spider):
    name = 'rottentomatoes'
    allowed_domains = ['tecnoblog.net']
    start_urls = ['http://tecnoblog.net/']

    def parse(self, response):
      for item in response.css("item"):
        item["link"]    = response.css("div.texts h2 a::attr(href)").extract_first()
        item["title"]   = response.css("div.texts h2 a::text").extract_first()
        
        item["identifier"] = response.url.split("/")[4]
        item["url"] = response.url
        return item
