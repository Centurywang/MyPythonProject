import requests
import re
from time import sleep
from GitMeizitu import search_re_content,get_url_html
from ConnectMySql import MySQLDB
from lxml import etree
import os
title = None
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    'referer' : 'https://www.mzitu.com/'

}
def download(url):
    content = requests.get(url,headers=headers).content
    try:
        with open(title+'/'+ title + url[-7:]) as f:
            pass
    except:
        with open(title+'/'+ title + url[-7:],'wb+') as f:
            print(title+'/'+ title + url[-7:])
            sleep(1)
            f.write(content)
        print('保存完成')

# 获取图片地址
def get_picture_url(html):
    re_grammer = '<div class="main-image"><p><a href=".*?" ><img src="(.*?)" alt=".*?" width=".*?" height=".*?" /></a></p>'
    result = search_re_content(re_grammer, html)
    try:
        download(result[0])
    except:
        print('下载'+title+'失败')
    #return result[0]

# 获取套图下一页
def get_next_url(html):
    #html = etree.HTML(html)
    #re_grammer = '''.*?</span><a href='.*?/span></a><a href='.*?</span></a><a href='.*?/span></a><span class='dots'>…</span><a href='.*?</span></a><a href='(.*?)'><span>下一页'''
    re_grammer = '''</span></a><a href='(.*?)'><span>下一页&raquo;</span></a>'''
    result = search_re_content(re_grammer,html)
    #result = html.xpath('//div[@class="pagenavi"]//a/@href/text()')
    re_grammer = '[a-zA-z]+://[^\s]*'
    try:
        result = search_re_content(re_grammer,result[0])[-1]
    except:
        print('套图查询完毕')
    print(result)
    if result:
        return result
    else:
        return None

# 下载套图内图片
def download_pictures(content):
    html = get_url_html(content[1])
    # 保存图片地址
    # pictures_url = []
    global title
    title = content[0]
    try:
        os.mkdir(title)
    except:
        print('目录已创建')
    # index_url = content[1]
    get_picture_url(html)
    next_url = get_next_url(html)
    while next_url:
        html = get_url_html(next_url)
        get_picture_url(html)
        next_url = get_next_url(html)
