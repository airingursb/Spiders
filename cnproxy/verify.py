#-*-coding:utf8-*-
import requests
import sys
import pymongo

reload(sys)
sys.setdefaultencoding('utf-8')

client = pymongo.MongoClient(host='127.0.0.1', port=27017)
tdb = client.bilibili
mongos = tdb.proxy.find()

item = {}

for mongo in mongos:
    item['http'] = 'http://' + str(mongo['proxy'])
    proxy = dict(item)
    print proxy
    try:
        html = requests.get("http://baidu.com", proxies=proxy)
        print 'success:' + str(mongo['proxy'])
        f = open('proxy.txt', 'a')
        f.writelines('  ' + mongo['proxy'] + ', \n')
        f.close()

    except:
        print 'error:' + str(mongo['proxy'])
        continue





