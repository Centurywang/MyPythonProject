from ConnectMySql import MySQLDB
from download_picture import download_pictures
mysql = MySQLDB()

sql = 'select * from meizitu'
data = mysql.execute_sql(sql)

for i in data[15:30]:
    print(i)
    download_pictures(i)