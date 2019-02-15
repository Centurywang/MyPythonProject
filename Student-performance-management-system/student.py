from useMysql import UsePyMysql
from menu import Menu
# 学生类
class Student():
    def __init__(self):
        self.useMysql = UsePyMysql()
        self.menu = Menu()

    #设置姓名
    def setName(self):
        name = input('姓名:')
        self.name = name

    #设置学号
    def setNumber(self):
        while True:
            number = input('学号:')
            if self.useMysql.doSelect(choice=2,newSno=number):
                print('学号已存在，请重新输入！')
            else:
                self.number = number
                break
    #设置性别
    def setSex(self):
        while True:
            sex = input('性别:')
            if sex == '男' or sex == '女':
                self.sex = sex
                break
            else:
                print('请输入男/女')

    def setAge(self):
        while True:
            age = int(input('年龄:'))
            if age >= 16 and age <= 30:
                self.age = age
                break
            else:
                print('请输入16-30的数')

    # 添加学生信息
    def addStuInformation(self):
        print('添加学生信息')
        self.setName()
        self.setNumber()
        self.setSex()
        self.setAge()
        self.useMysql.doInsert(1, self.number, self.name, self.sex, self.age)

    #显示学生信息
    def showStuInformation(self):
        print('显示学生信息')
        while True:
            print('1.查找学号学生信息\n2.显示所有学生信息\n0.退出')
            choice = input('请输入选择：')
            if choice == '1':
                while True:
                    number = input('请输入学号：')
                    resu = self.useMysql.doSelect(2, newSno=number)
                    if resu:
                        self.useMysql.doSelect(3, number)
                        break
                    else:
                        print('为找到该学号，请重新输入')
                    if number == '0':
                        break
            elif choice == '2':
                self.useMysql.doSelect(1)
            elif choice == '0':
                print('退出')
                break
            else:
                print('输入错误，请重新输入！')
    #删除学生信息
    def delStuInformation(self):
        print('删除学生信息')
        while True:
            number = input('请输入学号：')
            resu = self.useMysql.doSelect(2, newSno=number)
            if resu:
                self.useMysql.doDel(1,number)
                break
            else:
                print('为找到该学号，清重新输入')
            if number == '0':
                break

    #修改学生信息
    def changeStuInfomation(self):
        print('修改学生信息')
        while True:
            changeNumber = input('请输入要修改的学号(0推出)：')
            resu = self.useMysql.doSelect(2,newSno=changeNumber)
            if changeNumber == '0':
                break
            self.menu.menu5()
            if resu:
                choice = input('请输入选择：')
                menuResult = self.menu.choiceMenu2(choice)
                if menuResult == 0:
                    break
                #修改学号
                elif menuResult == 1:
                    self.setNumber()
                    self.useMysql.doUpdate(1,changeNumber,self.number)
                #修改姓名
                elif menuResult == 2:
                    self.setName()
                    self.useMysql.doUpdate(2,changeNumber,self.name)
                #性别
                elif menuResult == 3:
                    self.setSex()
                    self.useMysql.doUpdate(3, changeNumber, self.sex)
                #年龄
                elif menuResult == 4:
                    self.setAge()
                    self.useMysql.doUpdate(4, changeNumber, self.age)
            else:
                print('学号不存在，清重新输入！')

