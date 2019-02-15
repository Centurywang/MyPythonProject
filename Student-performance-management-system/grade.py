from useMysql import UsePyMysql
# 成绩类
class Grade():
    def __init__(self):
        self.useMysql = UsePyMysql()

    def setSno(self):
        while True:
            number = input('学号:')
            if self.useMysql.doSelect(choice=2,newSno=number):
                self.sno = number
                break
            else:
                print('学号不存在，请重新输入！')

    def setCno(self):
        while True:
            number = input('课程号:')
            if self.useMysql.doSelect(choice=5,newSno=number):
                self.cno = number
                break
            else:
                print('课程号不存在，请重新输入！')


    def setGrade(self):
        while True:
            grade = float(input('成绩:'))
            if grade <= 100 and grade >= 0:
                self.grade = grade
                break
            else:
                print('请输入0-100')

    def addGradeInformation(self):
        print('添加成绩信息')
        self.setSno()
        self.setCno()
        #查询课程是否存在
        resu =self.useMysql.doSelect(7,self.sno,self.cno)
        if resu:
            choice = input('课程已存在，是否覆盖(y/n)？')
            if choice == 'y':
                self.setGrade()
                self.useMysql.doInsert(3, self.sno, self.cno, self.grade)
            elif choice == 'n':
                pass
        else:
            self.setGrade()
            self.useMysql.doInsert(3, self.sno, self.cno, self.grade)


    def changeGradeInformation(self):
        print('修改成绩信息')
        self.setSno()
        self.setCno()
        # 查询课程是否存在
        resu = self.useMysql.doSelect(7, self.sno, self.cno)
        if resu:
            self.setGrade()
            self.useMysql.doUpdate(9, number=self.sno,value=self.cno, grade=self.grade)
        else:
            print('该学号课程号成绩不存在')

    def delGradeInformation(self):
        print('删除成绩信息')
        self.setSno()
        self.setCno()
        # 查询课程是否存在
        resu = self.useMysql.doSelect(7, self.sno, self.cno)
        if resu:
            self.useMysql.doDel(3,number=self.sno,cno=self.cno)
        else:
            print('该学号课程号成绩不存在')

    def showGradeInformation(self):
        print('显示成绩信息')
        while True:
            print('1.查找学号学生信息\n2.查找课程号成绩信息\n0.退出')
            choice = input('请输入选择：')
            if choice == '1':
                while True:
                    number = input('请输入学号：')
                    resu = self.useMysql.doSelect(2, newSno=number)
                    if resu:
                        self.useMysql.doSelect(8, number)
                        break
                    else:
                        print('为找到该学号，请重新输入')
                    if number == '0':
                        break
            elif choice == '2':
                while True:
                    number = input('请输入课程号：')
                    resu = self.useMysql.doSelect(5, newSno=number)
                    if resu:
                        self.useMysql.doSelect(9, number)
                        break
                    else:
                        print('为找到该课程号，请重新输入')
                    if number == '0':
                        break
            elif choice == '0':
                print('退出')
                break
            else:
                print('输入错误，请重新输入！')