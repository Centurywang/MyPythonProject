from ConnectMySql import MySQLDB
from download_picture import download_pictures
mysql = MySQLDB()

sql = 'select * from meizitu'
data = mysql.execute_sql(sql)

# 在此设置要爬取的套图范围
for i in data[15:30]:
    print(i)
    download_pictures(i)