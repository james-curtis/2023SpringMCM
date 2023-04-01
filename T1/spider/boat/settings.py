BOT_NAME = 'boat'

SPIDER_MODULES = ['boat.spiders']
NEWSPIDER_MODULE = 'boat.spiders'

ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 999

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
CONCURRENT_REQUESTS_PER_DOMAIN = 999
# CONCURRENT_REQUESTS_PER_IP = 0

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
TELNETCONSOLE_ENABLED = True
TELNETCONSOLE_USERNAME = 'scrapy'
TELNETCONSOLE_PASSWORD = 'scrapy'

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
SPIDER_MIDDLEWARES = {
    # 'boat.middlewares.BoatSpiderMiddleware': 543,
    # 'scrapy.spidermiddlewares.httperror.HttpErrorMiddleware': None,
    # 'boat.middlewares.HttpErrorMiddleware': 50
}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    # 'boat.middlewares.BoatDownloaderMiddleware': 543,

    # 跳过异常页面
    'boat.downloaderMiddlewares.processAllException.ProcessAllExceptionMiddleware': 120,
    'scrapy.downloadermiddlewares.retry.RetryMiddleware': None,
    'boat.downloaderMiddlewares.retry.RetryMiddleware': 550,

    'boat.downloaderMiddlewares.common.CustomUserAgentMiddleware': 545,
    'boat.downloaderMiddlewares.common.DownloadLoggerMiddleware': 555,
    'boat.downloaderMiddlewares.common.HttpProxyMiddleware': 100,
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    # 'boat.pipelines.JsonWriterPipeline': 300,
    'boat.pipelines.MongoPipeline': 300,
    # 'boat.pipelines.JsonLinePipeline': 310,
    # 'boat.pipelines.CsvPipeline': 320,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
AUTOTHROTTLE_ENABLED = True
# The initial download delay
AUTOTHROTTLE_START_DELAY = 3
# The maximum download delay to be set in case of high latencies
AUTOTHROTTLE_MAX_DELAY = 30
# The average number of requests Scrapy should be sending in parallel to
# each remote server
AUTOTHROTTLE_TARGET_CONCURRENCY = 50
# Enable showing throttling stats for every response received:
AUTOTHROTTLE_DEBUG = True

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
HTTPCACHE_ENABLED = True
HTTPCACHE_EXPIRATION_SECS = 0
HTTPCACHE_DIR = 'httpcache'
HTTPCACHE_IGNORE_HTTP_CODES = []
HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

DOWNLOAD_TIMEOUT = 10
RETRY_TIMES = 10
# HTTPERROR_ALLOWED_CODES = [504]


MONGO_URI = 'mongodb://127.0.0.1:27017/'
MONGO_DATABASE = '2023math'

from scrapy.dupefilters import RFPDupeFilter
