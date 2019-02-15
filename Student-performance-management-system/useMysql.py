import pymysql
# 操作数据库类
class UsePyMysql():
    def __init__(self):
        # 连接
        self.db = pymysql.connect(host='', port=3306, db='', user='', passwd='',
                             charset='utf8')
        # 使用cursor()方法获取操作游标
        self.cursor = self.db.cursor()
        self.cursor.execute('use wsj')

    # 查询功能
    def doSelect(self,choice,newSno='0',cno='0'):
        #查询所有学生信息
        if choice == 1:
            sql = "select * from Student"
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
            for row in results:
                if row != results[-1]:
                    print('学号:{} 姓名:{} 性别:{} 年龄:{}'.format(row[0],row[1],row[2],row[3]))
        #查询学号是否存在
        elif choice ==2:
            sql = "select Sno from Student where Sno = '%s'" % newSno
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
            if results:
                return True
            else:
                return False
        #查询学号信息
        elif choice == 3:
            sql = "select * from Student where Sno = '%s'"% newSno
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
            for row in results:
                if row == None:
                    pass
                else:
                    print('学号:{} 姓名:{} 性别:{} 年龄:{}'.format(row[0], row[1], row[2], row[3]))
        #查询所有课程信息
        elif choice == 4:
            sql = "select * from Course"
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
            for row in results:
                print('课程号:{} 课程名:{} 学时:{} 学分:{}'.format(row[0], row[1], row[2], row[3]))
        #查询课程是否存在
        elif choice == 5:
            sql = "select Cno from Course where Cno = '%s'" % newSno
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
            if results:
                return True
            else:
                return False
        #查询课程号课程
        elif choice == 6:
            sql = "select * from Course where Cno = '%s'" % newSno
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
            for row in results:
                if row == None:
                    pass
                else:
                    print('课程号:{} 课程名:{} 学时:{} 学分:{}'.format(row[0], row[1], row[2], row[3]))

        #查询成绩是否存在
        elif choice == 7:
            sql = "select Grade from SC where Sno = '%s' and Cno='%s'" % (newSno,cno)
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
            if results:
                return True
            else:
                return False
        #查询学号学生成绩
        elif choice == 8:
            sql = "select * from SC where Sno = '%s'" % newSno
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
            for row in results:
                if row == None:
                    pass
                else:
                    print('学号:{} 课程名:{} 成绩:{}'.format(row[0], row[1], row[2]))

        #查询课程号学生成绩
        elif choice == 9:
            sql = "select * from SC where Cno = '%s'" % newSno
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
            for row in results:
                if row == None:
                    pass
                else:
                    print('学号:{} 课程名:{} 成绩:{}'.format(row[0], row[1], row[2]))


        else:
            pass

    # 插入功能
    def doInsert(self,choice,sno,sname,ssex,sage='0'):
        #添加学生
        if choice == 1:
            sql = "insert into Student values ('%s','%s','%s',%d)" % (sno, sname, ssex, sage)
        #添加课程
        elif choice == 2:
            sql = "insert into Course values ('%s','%s','%s',%d)" % (sno, sname, ssex, sage)
        #添加成绩
        elif choice == 3:
            sql = "insert into SC values ('%s','%s',%d)" % (sno, sname, ssex)
        try:
            # 执行sql语句
            self.cursor.execute(sql)
            # 提交到数据库执行
            self.db.commit()
            print('添加成功！')
        except:
            print('error!')
            self.db.rollback()

    # 删除功能
    def doDel(self,choice,number,cno=''):
        #删除学生信息
        if choice == 1:
            sql1 = "delete from Student where Sno = '%s'" % number
            sql2 = "delete from SC where Sno = '%s'" % number
            try:
                # 执行sql语句
                self.cursor.execute(sql1)
                self.cursor.execute(sql2)
                # 提交到数据库执行
                self.db.commit()
                print('删除成功！')
            except:
                print('error!')
                self.db.rollback()

        #删除课程信息
        elif choice == 2:
            sql = "delete from Course where Cno = '%s'" % number

        #删除成绩信息
        elif choice == 3:
            sql = "delete from SC where Sno = '%s' and Cno='%s'" % (number,cno)
        try:
            # 执行sql语句
            self.cursor.execute(sql)
            # 提交到数据库执行
            self.db.commit()
            print('删除成功！')
        except:
            print('error!')
            self.db.rollback()

    # 修改（更新）功能
    def doUpdate(self,choice,number,value,grade):
        #修改学号
        if choice == 1:
            sql = "update Student set Sno = '%s' where Sno = '%s'" % (value, number)
            sql2 = "update SC set Sno = '%s' where Sno = '%s'" % (value, number)
            self.cursor.execute(sql2)
        #修改姓名
        elif choice == 2:
            sql = "update Student set Sname = '%s' where Sno = '%s'" % (value, number)
        #修改性别
        elif choice == 3:
            sql = "update Student set Ssex = '%s' where Sno = '%s'" % (value, number)
        #修改年龄
        elif choice == 4:
            sql = "update Student set Sage = %d where Sno = '%s'" % (value, number)
        #修改课程号
        elif choice == 5:
            sql = "update Course set Cno = '%s' where Cno = '%s'" % (value, number)
            sql2 = "update Course set Cno = '%s' where Cno = '%s'" % (value, number)
            self.cursor.execute(sql2)
        #修改课程名
        elif choice == 6:
            sql = "update Course set Cname = '%s' where Cno = '%s'" % (value, number)
        #修改课程学时
        elif choice == 7:
            sql = "update Course set Cpno = '%s' where Cno = '%s'" % (value, number)
        #修改课程学分
        elif choice == 8:
            sql = "update Course set Ccredit = '%s' where Cno = '%s'" % (value, number)
        #修改学号课程号成绩
        elif choice == 9:
            sql = "update SC set Grade = %d where Sno = '%s' and Cno ='%s'" % (grade,number,value)

        try:
            # 执行sql语句
            self.cursor.execute(sql)
            # 提交到数据库执行
            self.db.commit()
            print('修改成功！')
            return 1
        except:
            print('error!')
            self.db.rollback()
            return 0

