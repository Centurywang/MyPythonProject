from lxml import etree
# 写入csv文件
import re
import csv
# 电影名称、电影类型、电影评分、上映场次
# 获取网页内容
def get_content():
    path = 'www2/电影票房数据库.html'
    htmlfile = open(path, 'r', encoding='utf-8')
    htmlhandle = htmlfile.read()
    return htmlhandle

# 解析数据并写入文件
def get_information(cont):
    # 电影名称 总场次/占比 网票票房 哈票票房 万达票房 金逸票房 星美票房 实时(不含预售) 预计 累积
    # 获取第一部分
    cont = etree.HTML(cont)
    cont = cont.xpath('//div[@class="table-responsive"]/table[@class="table table table-bordered table-condensed"]//tr//text()')
    print(cont)
    for i in cont:
        if i ==  ' ':
            cont.remove(i)
    print(cont)
    with open('ans0102.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        # 解析并写入文件
        # 存储票房总额
        avgs = 0
        i = 10
        while i <= len(cont):
            list = cont[i-10:i]
            i += 10
            writer.writerow(list)

        for i in range(len(cont)):
            if i != 9 and i % 10 == 9:
                # 匹配数字
                try:
                    if cont[i][-1] == '亿':
                        resu = float(cont[i][:-1])
                    elif cont[i][-1] == '万':
                        resu = float(cont[i][:-1])/10000
                    print(resu)
                    avgs += resu
                except:
                    pass
        with open('ans0102.txt','w') as f:
            f.write(str(avgs)+'亿')

cont = get_content()
cont = get_information(cont)
