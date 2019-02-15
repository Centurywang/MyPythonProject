import requests
import re
import time
#导入操作mysql类
from ConnectMySql import MySQLDB

# 获取url response
def get_url_response(url):
    headers = {
        'Host': 'book.douban.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    }
    r = requests.get(url,headers=headers)
    return r

# 获取下一页url
def get_next_url(response):
    response = response.text
    result = None
    try:
        result = re.findall('<link rel="next" href="(.*?)"/>',response,re.S)[0]
    except:
        print('没有下一页')
    return result

# 过滤内容
def filter_content(response):
    # 实例化数据库类
    mydb = MySQLDB()
    response = response.text
    result = re.findall('''<a href=".*?title="(.*?)".*?<p class="pl">(.*?)</p>.*?<span class="rating_nums">(.*?)</span>.*?<span class="pl">(.*?)</span>.*?</div>'''
,response,re.S)
    for i,j,k,l in result:
        book = {}
        book['title'] = i
        others = j.split('/')
        book['grade'] = k
        book['number'] = re.findall(r'\d+',l,re.S)[0]
        book['price'] = re.findall(r'\d+',others[-1],re.S)[0]
        book['data'] = others[-2]
        book['press'] = others[-3]
        book['author'] = [r for r in others[:-3]]
        print(book)
        # 写入文件
        #with open('data.data','a+',encoding='utf-8') as f:
        #    f.write(str(book)+'\n')
        # 写入数据库
        sql = """INSERT INTO movieInfo(title,grade,number,price,data,press,author)
                 VALUES ({},{},{},{},{},{},{})""".format('\''+str(book['title'])+'\'',float(book['grade']),int(book['number']),float(book['price']),'\''+str(book['data'])+'\'','\''+str(book['press'])+'\'','\"'+str(book['author'])+'\"')
        print(sql)
        mydb.execute_update(sql)

def get_result():
    # 首地址
    url = 'https://book.douban.com/top250?icn=index-book250-all'
    # 获取response
    response = get_url_response(url)
    # 过滤内容
    filter_content(response)
    # 获取下一页地址
    next_url = get_next_url(response)
    # 循环 条件：当下一页存在
    while next_url:
        time.sleep(10)
        response = get_url_response(next_url)
        filter_content(response)
        next_url = get_next_url(response)
# 获取平均分
def average_score():
    # 读取文件
    with open('data.data', encoding='utf-8') as f:
        result = f.readlines()
    all_grade = []
    for i in result:
        try:
            grade = float(re.findall(r"'grade': '(.*?)'", i)[0])
            all_grade.append(grade)
        except:
            pass
    print('平均分：%.2f' % (sum(all_grade) / len(all_grade)))
    '''
    #第二种方法，数据库方式
    # 实例化数据库类
    mydb = MySQLDB()
    sql = 'select avg(grade) from movieInfo'
    results = mydb.execute_sql(sql)
    print("平均分 = %.2f" %results[0])
    '''
if __name__ == '__main__':
    while True:
        choice = int(input('1.爬取数据并保存为文件并写入数据库\n2.获取平均分\n其他.退出\n请选择：'))
        if choice == 1:
            get_result()
        elif choice == 2:
            # 获取平均分
            average_score()
        else:
            print('结束')
            break


