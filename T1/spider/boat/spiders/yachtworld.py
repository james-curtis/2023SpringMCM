import scrapy
from scrapy.shell import inspect_response
from ..items import *
from ..config import *


def getTableParams(selector, itemDict, item):
    for k, v in itemDict.items():
        item[v] = selector.xpath(
            f'//tr[@class="datatable-item" and .//*[text()="{k}"]]/td[@class="datatable-value"]/text()').get()


class YachtworldSpider(scrapy.Spider):
    name = 'yachtworld'
    # allowed_domains = ['www.yachtworld.com']
    start_urls = [
        # 'https://www.yachtworld.co.uk/yacht/1939-abo-a-b-batvarv-vintage-sail-boat-havskryssare,-byggd-8722010/',
        Config.getStartUrl(i) for i in range(1, 666 + 1)
    ]

    def processAllException(self, response):
        if not response.url:  # 接收到url==''时
            self.logger.warning('500')
        elif 'exception' in response.url:
            self.logger.warning('exception')
        return None

    def parse(self, response, **kwargs):
        # yield self.processAllException(response, BoatItem)
        boatDetailUrls = response.xpath('//*[@class="listings-container"]/a/@href').getall()
        yield from response.follow_all(boatDetailUrls, callback=self.parsePage)
        #
        # '''拿到下一页'''
        # nextUrl = response.xpath('//a[@class="icon-chevron-right "]/@href').get()
        # if nextUrl is not None:
        #     yield response.follow(nextUrl, callback=self.parse)

    def parsePage(self, response):
        if self.processAllException(response) is None:
            yield None
        else:
            content = response.xpath('//*[@id="BoatDetails"]//div[@class="boat-details-content"]')
            item = BoatItem()
            item['url'] = response.url

            self.parseGeneral(response, item, content)

            basicsCtx = response.xpath('//div[contains(@class,"collapse-content-details") and .//a[text()="Basics"]]')
            self.parseBasic(response, item, basicsCtx)

            descCtx = response.xpath('//div[contains(@class,"collapse-content-details") and .//a[text()="Description"]]')
            self.parseDesc(response, item, descCtx)

            otherDetailsCtx = response.xpath(
                '//div[contains(@class,"collapse-content-details") and .//a[text()="Other Details"]]')
            self.parseOtherDetails(response, item, otherDetailsCtx)

            propulsionCtx = response.xpath(
                '//div[contains(@class,"collapse-content-details") and .//a[text()="Propulsion"]]//*[contains(@class,"detail-data-table")]/*[1]//tbody')
            self.parsePropulsion(response, item, propulsionCtx)

            # Specifications
            DimensionsCtx = response.xpath('//*[./h3[text()="Dimensions"]]/table')
            self.parseDimensions(response, item, DimensionsCtx)
            TanksCtx = response.xpath('//*[./h3[text()="Tanks"]]/table')
            self.parseTanks(response, item, TanksCtx)
            AccommodationsCtx = response.xpath('//*[./h3[text()="Accommodations"]]/table')
            self.parseAccommodations(response, item, AccommodationsCtx)

            yield item

    def parseGeneral(self, response, item, ctx):
        '''商品名'''
        item['name'] = ctx.xpath('//header[@class="boatNameHeading"]/h1/text()').get()

        '''现价'''
        item['currentPrice'] = ctx.xpath('//span[@class="payment-total"]/text()').get()

        '''商品所在位置'''
        item['location'] = ctx.xpath('//h2[@class="location"]/text()').get()

    def parseBasic(self, response, item, ctx):
        itemKeys = {
            'Year': 'year',
            'Make': 'make',
            'Model': 'model',
            'Class': 'classes',
            'Length': 'length',
            'Fuel Type': 'fuelTpe',
            'Hull Material': 'hullMaterial',
            'Hull Shape': 'hullShape',
        }
        getTableParams(ctx, itemKeys, item)

    def parseDesc(self, response, item, ctx):
        item['descriptionText'] = ''.join(
            ctx.xpath('(//*[contains(@class,"detail-description")])[1]/*[1]//text()').getall())

    def parseOtherDetails(self, response, item, ctx):
        item['otherDetailsText'] = ''.join(
            ctx.xpath('(//*[contains(@class,"detail-description")])[1]/*[1]//text()').getall())

    def parsePropulsion(self, response, item, ctx):
        itemKeys = {
            'Engine Make': 'engineMake',
            'Engine Model': 'engineModel',
            'Engine Year': 'engineYear',
            'Total Power': 'totalPower',
            'Engine Hours': 'engineHours',
            'Engine Type': 'engineType',
            'Fuel Type': 'engineFuelType',
        }
        getTableParams(ctx, itemKeys, item)

    def parseDimensions(self, response, item, ctx):
        itemKeys = {
            'Length Overall': 'lengthOverall',
            'Max Bridge Clearance': 'maxBridgeClearance',
            'Beam': 'beam',
        }
        getTableParams(ctx, itemKeys, item)

    def parseTanks(self, response, item, ctx):
        itemKeys = {
            'Fresh Water Tank': 'freshWaterTank',
            'Fuel Tank': 'fuelTank',
            'Holding Tank': 'holdingTank',
        }
        getTableParams(ctx, itemKeys, item)

    def parseAccommodations(self, response, item, ctx):
        itemKeys = {
            'Single Berths': 'singleBerths',
            'Cabins': 'cabins',
            'Heads': 'heads',
        }
        getTableParams(ctx, itemKeys, item)
