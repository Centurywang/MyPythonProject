import pymysql

class MySQLDB():
    def __init__(self):
        self.mydb = pymysql.connect(
            host = '39.106.205.225',
            user = 'movieInfo',
            passwd = 'movieInfo',
            database="movieInfo"
        )
        self.mycursor = self.mydb.cursor()
    # 一般操作
    def execute_sql(self,sql):
        results = None
        try:
            # 执行SQL语句
            self.mycursor.execute(sql)
            # 获取所有记录列表
            results = self.mycursor.fetchall()
        except:
            print("Error: unable to fetch data")
        return results

    # 执行数据库更新的操作
    def execute_update(self,sql):
        try:
            # 执行sql语句
            self.mycursor.execute(sql)
            # 提交到数据库执行
            self.mydb.commit()
            print('信息插入成功')
        except:
            # 如果发生错误则回滚
            self.mydb.rollback()

    def __del__(self):
        # 关闭数据库连接
        self.mydb.close()