
class Parent(object):

    def __init__(self, name, *args, **kwargs):
        self.name = name
        print('Parent的init函数执行了')

    def test(self):
        print('Parent的test函数执行了')

class Son1(Parent):

    def __init__(self, name, age, *args, **kwargs):
        self.age = age
        super(Son1, self).__init__(name, *args, **kwargs)
        print('Son1的init的函数执行了')

    def test(self):
        print('Son1的test函数执行了')

class Son2(Parent):

    def __init__(self, name, sex, *args, **kwargs):
        self.sex = sex
        super(Son2, self).__init__(name, *args, **kwargs)
        print('Son2的init的函数执行了')

    def test(self):
        print('Son2的test函数执行了')

class GrandSon(Son1, Son2):  #多继承

    def __init__(self, name, age, sex, *args, **kwargs):
        super(GrandSon, self).__init__(name, age, sex)
        print('GrandSon的init的函数执行了')

print(f'MRO序列是：{GrandSon.__mro__}')    # MRO序列查看,MRO序列是函数的执行顺序。
gs = GrandSon('跟人', 23, '男')
gs.test()