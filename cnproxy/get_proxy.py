# -*-coding:utf8-*-
from lxml import etree
import requests

head = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36'
}

data = {
    'country': u'中国',
    'region': u'全部',
    'city': u'全部',
    'number': 20,
    'anonType': -1,
    'proxyType': -1,
    'ispId': -1,
}

html = requests.post('http://www.haodailiip.com/domftiqu', data, headers=head)
selector = etree.HTML(html.text)
content = selector.xpath("//body")

for each in content:
    proxies = each.xpath('p/text()')
    for proxy in proxies:
        print '"' + proxy + '",'
