import requests
import re
from time import sleep
# 获取html网页代码
def get_url_html(url):
    html = requests.get(url)
    return html.text

# 根据re规则获取内容
def search_re_content(re_grammer,html):
    result = re.findall(re_grammer,html)
    return result

# 获取套图url
def get_pictures_url(url):
    index_html = get_url_html(url)
    # 构造re语法 获取套图url
    re_grammer1 = '<ul id="pins">.*?</ul>'
    url_content1 = search_re_content(re_grammer1, index_html)[0]
    re_grammer2 = '''<li><a href=".*?" target="_blank"><img class='lazy' src='.*?' data-original='.*?' alt='(.*?)' width='236' height='354' /></a><span><a href="(.*?)" target="_blank">.*?</a></span><span class="time">.*?</span></li>'''
    url_content2 = search_re_content(re_grammer2, url_content1)
    # 套图标题及url
    return url_content2
# 获取下一页url
def get_next_url(url):
    html = get_url_html(url)
    # 构造re语法 获取下一页url
    re_grammer = '<a class="next page-numbers" href="(.*?)">下一页.*?</a></div>'
    next_url = search_re_content(re_grammer,html)
    if next_url:
        return next_url[0]
    else:
        return None
def start_get_all():
    # 首地址
    index_url = 'https://www.mzitu.com/xinggan/'
    # 获取套图url及标题
    picture_url = get_pictures_url(index_url)
    # 存入数据库
    for url in picture_url:
        save_to_mysql(url)
    print('该页保存完成')
    # 判断下一页
    next_url = get_next_url(index_url)
    print('next_url:',next_url)
    while next_url:
        print('下一页')
        sleep(2)
        picture_url = get_pictures_url(next_url)
        # 存入数据库
        for url in picture_url:
            save_to_mysql(url)
        print('该页保存完成')
        # 判断下一页
        next_url = get_next_url(next_url)

# 保存到mysql数据库
from ConnectMySql import MySQLDB
mysql = MySQLDB()
def save_to_mysql(content):
    sql = 'INSERT INTO meizitu(name,url) VALUES("{}","{}")'.format(content[0],content[1])
    mysql.execute_update(sql)


def main():
    start_get_all()

if __name__ == '__main__':
    main()

