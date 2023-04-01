import pymongo
import scrapy
from ..items import *
from ..config import *
from scrapy.shell import inspect_response


class SailboatdataSpider(scrapy.Spider):
    name = "sailboatdata"
    # allowed_domains = ["sailboatdata.com"]
    start_urls = [Config.getSailboatdata(i) for i in range(353, 1 - 1, -1)]
    # start_urls = [Config.getSailboatdata(i) for i in range(1, 5 + 1)]
    custom_settings = {
        'MONGO_COLLECTION': 'sailboatdata3',
    }

    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        kwargs['mongo_uri'] = crawler.settings.get("MONGO_URI")
        kwargs['mongo_database'] = crawler.settings.get('MONGO_DATABASE')
        kwargs['mongo_collection'] = crawler.settings.get('MONGO_COLLECTION')
        return super(SailboatdataSpider, cls).from_crawler(crawler, *args, **kwargs)

    def __init__(self, mongo_uri=None, mongo_database=None, mongo_collection=None, **kwargs):
        super(SailboatdataSpider, self).__init__(**kwargs)
        self.client = pymongo.MongoClient(mongo_uri)
        self.db = self.client[mongo_database]
        self.collection = self.db[mongo_collection]
        # self.scraped_urls = self.collection.find({}, {'url': 1, '_id': 0})
        # self.scraped_urls = [i['url'] for i in list(self.scraped_urls)]
        print()

    def processAllException(self, response):
        if not response.url:  # 接收到url==''时
            self.logger.warning('500')
            return None
        elif 'exception' in response.url:
            self.logger.warning('exception')
            return None
        return True

    def parse(self, response, **kwargs):
        boatDetailUrls = response.xpath(
            '//table//a[starts-with(@href,"https://sailboatdata.com/sailboat")]/@href').getall()
        detailList = list(map(Config.getSailboatdataDetail, boatDetailUrls))
        scraped_urls = self.collection.find({'url': {'$in': detailList}}, {'url': 1, '_id': 0})
        scraped_urls = [i['url'] for i in list(scraped_urls)]
        unscrape_urls = [x for x in detailList if x not in scraped_urls]

        self.logger.info(f'跳过：{scraped_urls}')
        yield from response.follow_all(unscrape_urls, callback=self.parsePage)

    def parsePage(self, response, **kwargs):
        if self.processAllException(response) is None:
            yield None
        else:
            def getItem(name, resp):
                return ''.join(resp.xpath(
                    f'(//*[contains(@class,"sailboatdata-label") and contains(text(),"{name}")]/following-sibling::div)[1]//text()').getall()).strip()

            item = sailboatdata()
            item['url'] = response.url
            item['hullType'] = getItem('Hull Type', response)
            item['riggingType'] = getItem('Rigging Type', response)
            item['LOA'] = getItem('LOA', response)
            item['LWL'] = getItem('LWL', response)
            item['Beam'] = getItem('Beam', response)
            item['SA'] = getItem('S.A.', response)
            item['DraftMax'] = getItem('Draft (max)', response)
            item['DraftMin'] = getItem('Draft (min)', response)
            item['Displacement'] = getItem('Displacement', response)
            item['Ballast'] = getItem('Ballast', response)
            item['SA2Disp'] = getItem('S.A./Disp', response)
            item['Bal2Disp'] = getItem('Bal./Disp', response)
            item['Construction'] = getItem('Construction', response)
            item['firstBuilt'] = getItem('First Built', response)
            item['Builder'] = getItem('Builder', response)
            item['Designer'] = getItem('Designer', response)
            item['Headroom'] = getItem('Headroom', response)
            item['Water'] = getItem('Water', response)
            yield item
