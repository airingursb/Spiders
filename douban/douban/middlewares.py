import random
import pymongo
from settings import MONGODB_HOST, MONGODB_PORT, MONGODB_DBNAME


class RandomUserAgent(object):
    """Randomly rotate user agents based on a list of predefined ones"""
    def __init__(self, agents):
        self.agents = agents

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings.getlist('USER_AGENTS'))

    def process_request(self, request, spider):
        request.headers.setdefault('User-Agent', random.choice(self.agents))


class ProxyMiddleware(object):
    def process_request(self, request, spider):
        host = MONGODB_HOST
        port = MONGODB_PORT
        dbName = MONGODB_DBNAME
        client = pymongo.MongoClient(host=host, port=port)
        tdb = client[dbName]
        proxys = tdb.proxy.find()
        proxy_list = []

        for ip in proxys:
            proxy = ip['ip'].replace('\r', '').replace('\n', '').replace('\t', '') + ":" \
                    + ip['port'].replace('\r', '').replace('\n', '').replace('\t', '')
            proxy_list.append(proxy)

        proxy = random.choice(proxy_list)
        # proxy = "116.228.143.200:80"
        print(proxy)
        request.meta['proxy'] = "http://%s" % proxy

    def process_exception(self, request, exception, spider):
        try:
            self.process_request(request, spider)
        except ValueError:
            pass