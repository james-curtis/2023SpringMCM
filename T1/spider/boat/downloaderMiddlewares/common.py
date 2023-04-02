from anole import UserAgent
from ..proxy import *
import requests


class DownloadLoggerMiddleware:
    def process_request(self, request, spider):
        spider.logger.info('开始请求: {url}'.format(url=request.url))


class CustomUserAgentMiddleware:
    def __init__(self):
        self.user_agent = UserAgent()

    def process_request(self, request, spider):
        request.headers['User-Agent'] = self.user_agent.random


class HttpProxyMiddleware:
    def process_request(self, request, spider):
        proxy = Proxy.get_proxy()
        addr = proxy.get("proxy")
        request.meta['proxy'] = f'http://{addr}'
        spider.logger.info(f'使用代理：[{proxy.get("source")}]{addr}，{proxy.get("region")}')
        Proxy.delete_proxy(addr)


class HttpProxyMiddleware2:
    def process_request(self, request, spider):
        url = 'http://v2.api.juliangip.com/unlimited/getips?num=1&pt=1&result_type=text&split=1&trade_no=5137351507572391&sign=9bcc6332d6bdc8c9ecafcb6dfea8d99f'
        addr = requests.get(url, proxies=None).text.strip()
        request.meta['proxy'] = f'http://{addr}'
        spider.logger.info(f'使用代理：{addr}')
