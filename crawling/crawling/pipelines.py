# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from core.models import Movie


def clean_title(param):
    return param

class ScrapyProjectPipeline(object):
    def process_item(self, item, spider):
        try:
            question = Movie.objects.get(identifier=item["title"])
            return item
        except Movie.DoesNotExist:
            pass

        question = Movie()
        question.identifier = item["identifier"]
        question.title = item["title"]
        
        question.save()
        return item
