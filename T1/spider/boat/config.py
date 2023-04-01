class Config:
    @staticmethod
    def getStartUrl(page):
        return f'https://www.yachtworld.com/boats-for-sale/type-sail/sort-make:asc/?page={page}'

    @staticmethod
    def getSailboatdata(page):
        return f'https://sailboatdata.com/?paginate=25&page={page}'

    @staticmethod
    def getSailboatdataDetail(url):
        return f'{url}?units=imperial'
