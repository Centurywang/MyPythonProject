from useMysql import UsePyMysql
from menu import Menu
# 课程类
class Course():
    def __init__(self):
        self.useMysql = UsePyMysql()
        self.menu = Menu()
    def setNumber(self):
        while True:
            number = input('课程号:')
            if self.useMysql.doSelect(choice=5,newSno=number):
                print('课程号已存在，请重新输入！')
            else:
                self.number = number
                break

    def setName(self):
        name = input('课程名:')
        self.name = name

    def setPeriod(self):
        period = input('学时:')
        self.period = period

    def setCredit(self):
        while True:
            credit = int(input('学分:'))
            if credit <=10 and credit >=1:
                self.credit = credit
                break
            else:
                print('请输入1-10')

    #添加课程信息
    def addCourseInformation(self):
        print('添加课程信息')
        self.setNumber()
        self.setName()
        self.setPeriod()
        self.setCredit()
        self.useMysql.doInsert(2,self.number, self.name, self.period, self.credit)

    #修改课程信息
    def changeCourseInformation(self):
        print('修改课程信息')
        while True:
            changeNumber = input('请输入要修改的课程号(0推出)：')
            resu = self.useMysql.doSelect(5,newSno=changeNumber)
            if changeNumber == '0':
                break
            self.menu.menu6()
            if resu:
                choice = int(input('请输入选择：'))
                if choice == 0:
                    break
                #修改课程号
                elif choice == 1:
                    self.setNumber()
                    self.useMysql.doUpdate(5,changeNumber,self.number)
                #修改课程名
                elif choice == 2:
                    self.setName()
                    self.useMysql.doUpdate(6,changeNumber,self.name)
                #学时
                elif choice == 3:
                    self.setPeriod()
                    self.useMysql.doUpdate(7, changeNumber, self.period)
                #学分
                elif choice == 4:
                    self.setCredit()
                    self.useMysql.doUpdate(8, changeNumber, self.credit)
            else:
                print('课程号不存在，清重新输入！')
    #删除课程信息
    def delCourseInformation(self):
        print('删除课程信息')
        while True:
            number = input('请输入课程号：')
            resu = self.useMysql.doSelect(5, newSno=number)
            if resu:
                self.useMysql.doDel(2,number)
                break
            else:
                print('未找到该学号，清重新输入')
            if number == '0':
                break
    #显示课程信息
    def showCourseInformation(self):
        print('显示课程信息')
        while True:
            print('1.查找课程号课程信息\n2.显示所有课程信息\n0.退出')
            choice = input('请输入选择：')
            if choice == '1':
                while True:
                    number = input('请输入课程号：')
                    resu = self.useMysql.doSelect(5, newSno=number)
                    if resu:
                        self.useMysql.doSelect(6, number)
                        break
                    else:
                        print('未找到该课程号，请重新输入')
                    if number == '0':
                        break
            elif choice == '2':
                self.useMysql.doSelect(4)
            elif choice == '0':
                print('退出')
                break
            else:
                print('输入错误，请重新输入！')
