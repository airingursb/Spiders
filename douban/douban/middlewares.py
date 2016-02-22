import random
import pymongo
import base64
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

        # proxy = random.choice(proxy_list)
        proxy = "117.71.120.68:3050"
        print(proxy)
        request.meta['proxy'] = "http://%s" % proxy
        encoded_user_pass = base64.encodestring('kagami')
        request.headers['Proxy-Authorization'] = 'Basic ' + encoded_user_pass

    def process_exception(self, request, exception, spider):
        try:
            self.process_request(request, spider)
        except ValueError:
            pass