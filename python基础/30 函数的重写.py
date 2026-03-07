
class Parent:

    def __init__(self, name):
        self.name = name
        print('Parent的init函数被执行了')

    def say_hello(self):
        print(f'{self.name}:hello')
        print('Parent的say_hello函数被执行了')

class Son(Parent):
    # pass  # 占位
    def __init__(self, name, age):  # 不是重写init，是一个新的函数。
        super().__init__(name)    # 在子类中调用父类的init函数中的name
        self.age = age
        print('Son的init函数被执行了')

    def say_hello(self):
        print(f'{self.name}:hello world!')
        print('Son的say_hello函数被执行了')

s1 = Son('生动',15)
s1.say_hello()
