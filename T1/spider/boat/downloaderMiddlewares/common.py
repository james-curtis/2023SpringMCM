from anole import UserAgent
from ..proxy import *

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
