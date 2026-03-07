
class Animal(object):

    __name = '动物'  # 私有属性（类属性）  类外面都不能访问

    def __init__(self,color):
        self.__color = color  # 私有属性


    def __run(self):  # 私有函数
        print(self.__name)   # 类里面访问私有属性
        print('动物跑起来')

    def say(self):  # 私有函数
        print('动物叫起来')
        # self.__color = '粉红色'
        Animal.__name = '水母'   # medusa：水母
        self.__run()
        print(self.__color)

    def set_color(self,new_color):   # 通过 set_ 函数修改私有属性
        self.__color = new_color

    def get_color(self):   # get_函数访问私有函数
        return self.__color

class Dog(Animal):
    pass

d = Dog('red')
d.set_color('青色')
print(d.get_color())
# d.run()  # d无法调用
d.say()
