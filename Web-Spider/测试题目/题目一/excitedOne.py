import requests
import re
from lxml import etree

url = "http://www.sdcet.cn/xfw/channels/ch00385/"
# 获取网页内容
def get_content(url):
    cont = requests.get(url)
    cont.encoding = 'utf-8'
    cont = cont.text
    return cont

# 查找标题及url并写入
def search_title(cont):
    result = re.findall(r'''<td width="637" ><a href="(.*?)".*?title="(.*?)".*?target='_blank' class="zi2">''',cont)
    # 标题写入文件
    with open('title.txt','a') as f:
        for r in result:
            f.write(r[1]+'\n')
    # 文章写入文件
    for r in result:
        cont = search_chapter(r[0])
        print(r[1],cont)
        with open(r[1]+'.txt','a',encoding='utf-8')as f:
            for c in cont:
                f.write(c)

# 获取文章内容并写入文件
def search_chapter(url):
    # 获取网页内容
    cont = get_content(url)
    # 查找所需内容
    cont = etree.HTML(cont)
    cont = cont.xpath('//*[@id="content"]//text()')
    print(cont)
    return cont
#cont = get_content(url)
#search_title(cont)
# 查找以条例为结尾的标题
import os
titles = os.listdir()
for i in titles:
    if re.findall('(.*?条例).txt',i):
        title = i
        print(title)

