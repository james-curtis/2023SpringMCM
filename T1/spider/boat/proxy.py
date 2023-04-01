import requests

class Proxy:
    @staticmethod
    def get_proxy():
        return requests.get("http://127.0.0.1:5010/get/").json()

    @staticmethod
    def delete_proxy(proxy):
        requests.get("http://127.0.0.1:5010/delete/?proxy={}".format(proxy))
