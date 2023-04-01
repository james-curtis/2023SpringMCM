import pymongo
from .items import *
import json
from scrapy.exporters import *


def filterBoatItem(item):
    if not isinstance(item, BoatItem):
        return item
    it = ItemAdapter(item)
    del it['basicText']
    del it['descriptionText']
    del it['otherDetailsText']
    del it['propulsionText']
    del it['specificationsText']
    return it.item


class CsvPipeline(object):

    def __init__(self):
        self.file = open('demo.csv', 'wb')
        self.exporter = CsvItemExporter(self.file)
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        if item is not None:
            self.exporter.export_item(item)
        return item


class JsonLinePipeline(object):

    def __init__(self):
        self.file = open('demo.jl', 'wb')
        self.exporter = JsonLinesItemExporter(self.file)
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        if item is not None:
            self.exporter.export_item(item)
        return item


class MongoPipeline:

    def __init__(self, mongo_uri, mongo_db, mongo_collection):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db
        self.mongo_collection = mongo_collection

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE'),
            mongo_collection=crawler.settings.get('MONGO_COLLECTION'),
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        if item is not None:
            self.db[self.mongo_collection].insert_one(ItemAdapter(item).asdict())
        return item
