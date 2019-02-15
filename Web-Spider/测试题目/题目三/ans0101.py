from lxml import etree
# 写入csv文件
import csv
# 电影名称、电影类型、电影评分、上映场次

# 获取网页内容
def get_content():
    path = 'www1/北京影讯,北京电影院-在线选座购票-购电影票.html'
    htmlfile = open(path, 'r', encoding='utf-8')
    htmlhandle = htmlfile.read()
    return htmlhandle

# 解析数据并写入文件
def get_information(cont):
    item = {}
    cont = etree.HTML(cont)
    all_movies = cont.xpath('//li[@class="clearfix"]')
    with open('ans0101.csv', 'w', newline='') as f:
        list1 = ['电影名称', '电影类型', '电影评分', '上映场次']
        writer = csv.writer(f)
        writer.writerow(list1)

        # 解析并写入文件
        for movie in all_movies:
            try:
                item['name'] = movie.xpath('.//a[@class="__r_c_"]/text()')[0]
                item['type'] = movie.xpath('.//dd[1]//a/text()')
                item['grade'] = movie.xpath('.//span[@class="score"]/text()')[0]
                item['numbers'] = movie.xpath('.//dd[2]/text()')[0]
            except:
                pass
            print(item.values())
            writer.writerow(item.values())

cont = get_content()
cont = get_information(cont)