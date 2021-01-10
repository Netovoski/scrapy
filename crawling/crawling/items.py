# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy_djangoitem import DjangoItem
from core.models import Movie

class MovieItem(scrapy.Item):
    identifier =scrapy.Field()
    title = scrapy.Field()
    url = scrapy.Field()
    