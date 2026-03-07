
class Person():
    def __init__(self, name, age, gender):         #成员函数，对象函数，实例函数
        self.name = name
        self.age = age
        self.gender = gender

    def eat(self):
        print(f'{self.name}正在吃饭')

    @classmethod
    def work(cls, other, num=100):      #类函数
        print(cls.__name__)
        print(other)
        print('每个人都要工作')

    @staticmethod
    def run():                # 静态函数
        print('每个人都可以跑起来')


p1 = Person('萨利尔', 19,'女')
p1.eat()
# 类函数调用： 两种方法
p1.work('批阅')
Person.work('道人')

# 静态函数调用：两种方法
p1.run()
Person.run()

