#-*-coding:utf8-*-
from lxml import etree
from multiprocessing.dummy import Pool as ThreadPool
import requests
import sys

reload(sys)

sys.setdefaultencoding('utf-8')


def writeHead():
    f.writelines('<!DOCTYPE html> \n')
    f.writelines('<html lang="en"> \n')
    f.writelines('<head> \n')
    f.writelines('    <meta charset="UTF-8"> \n')
    f.writelines('    <title></title> \n')
    f.writelines('</head> \n')
    f.writelines('<body> \n')
    f.writelines('<table> \n')


def wirteEnd():
    f.writelines('</table> \n')
    f.writelines('</body> \n')
    f.writelines('</html> \n')


def spider(url):
    html = requests.post(url)
    selector = etree.HTML(html.text)
    content = selector.xpath('//div[@class="model-box model-user"]')
    item = {}
    f.writelines('<tr> \n')
    for each in content:
        face = each.xpath('a/img/@src')
        for i in range(len(face)):
            f.writelines('<td><img src="' + face[i] + '"/></td> \n')
    f.writelines('</tr> \n')

    f.writelines('<tr> \n')
    for each in content:
        name = each.xpath('h3/text()')
        link = each.xpath('a/@href')
        for i in range(len(name)):
            f.writelines('<td><a href="' + link[i] + '">' + name[i] + '</a></td> \n')
    f.writelines('</tr> \n')


if __name__ == '__main__':
    pool = ThreadPool(1)
    f = open('teacher.html', 'w')
    page = []
    writeHead()
    for i in range(1, 146, 8):
        newpage = 'http://mooc.gzhu.edu.cn/home/getMoreTeacher.mooc?beginIndex=' + str(i)
        print(newpage)
        page.append(newpage)

    results = pool.map(spider, page)
    pool.close()
    pool.join()
    wirteEnd()
    f.close()
