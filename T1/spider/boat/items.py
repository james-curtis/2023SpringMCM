# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemadapter import ItemAdapter


class BoatItem(scrapy.Item):
    '''
    常规
    '''
    reason = scrapy.Field()

    url = scrapy.Field()

    # 商品标题
    name = scrapy.Field()

    # 现价
    currentPrice = scrapy.Field()

    # 商品所在位置
    location = scrapy.Field()

    '''
    basic
    '''
    # basicText = scrapy.Field()

    # Year
    year = scrapy.Field()

    # Make
    make = scrapy.Field()

    # Model
    model = scrapy.Field()

    # Class
    classes = scrapy.Field()

    # Length
    length = scrapy.Field()

    # Fuel Type     燃料类型
    fuelTpe = scrapy.Field()

    # Hull Material     船体材料
    hullMaterial = scrapy.Field()

    # Hull Shape     船体形状
    hullShape = scrapy.Field()

    '''
    description
    '''
    # descriptionText = scrapy.Field()

    '''
    OTHER DETAILS
    '''
    # otherDetailsText = scrapy.Field()

    '''
    PROPULSION
    动力装置
    '''
    # propulsionText = scrapy.Field()

    engineMake = scrapy.Field()

    engineModel = scrapy.Field()

    engineYear = scrapy.Field()

    totalPower = scrapy.Field()

    engineHours = scrapy.Field()

    engineType = scrapy.Field()

    engineFuelType = scrapy.Field()

    '''
    SPECIFICATIONS
    规格
    '''
    # specificationsText = scrapy.Field()

    ## Dimensions       尺寸

    # 总长度
    lengthOverall = scrapy.Field()

    # 最大桥梁净空
    maxBridgeClearance = scrapy.Field()

    # 横梁
    beam = scrapy.Field()

    ## Tanks     水仓

    # 淡水储罐
    freshWaterTank = scrapy.Field()

    fuelTank = scrapy.Field()

    holdingTank = scrapy.Field()

    ## Accommodations    住宿

    # Single Berths
    singleBerths = scrapy.Field()

    # 隔间
    cabins = scrapy.Field()

    # Heads
    heads = scrapy.Field()

    @staticmethod
    def init(item):
        for k in list(ItemAdapter(item).field_names()):
            item[k] = ''

    @staticmethod
    def none2str(item):
        for k in list(ItemAdapter(item).field_names()):
            if item[k] is None:
                item[k] = ''


class sailboatdata(scrapy.Item):
    # https://sailboatdata.com/sailboat/jeanneau-yachts-55
    url = scrapy.Field()
    hullType = scrapy.Field()
    riggingType = scrapy.Field()
    LOA = scrapy.Field()
    LWL = scrapy.Field()
    Beam = scrapy.Field()
    SA = scrapy.Field()
    DraftMax = scrapy.Field()
    DraftMin = scrapy.Field()
    Displacement = scrapy.Field()
    Ballast = scrapy.Field()
    SA2Disp = scrapy.Field()
    Bal2Disp = scrapy.Field()
    Construction = scrapy.Field()
    firstBuilt = scrapy.Field()
    Builder = scrapy.Field()
    Designer = scrapy.Field()
    Headroom = scrapy.Field()
    Water = scrapy.Field()
