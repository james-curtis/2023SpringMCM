from scrapy.cmdline import execute
import sys
sys.stderr = sys.stdout

execute('scrapy crawl sailboatdata'.split())

