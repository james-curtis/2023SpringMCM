from anole import UserAgent


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
        request.meta['proxy'] = 'http://127.0.0.1:7890'
