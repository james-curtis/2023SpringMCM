# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo
from .items import *
import json

class BoatPipeline:
    def process_item(self, item, spider):
        return item


class JsonWriterPipeline:

    def process_item(self, item, spider):
        line = json.dumps(ItemAdapter(item).asdict()) + "\n"
        if isinstance(item, BoatItem):
            self.file = open('BoatItem.jl', 'a')
        self.file.write(line)
        self.file.close()
        return item
