
class Animal:
    name = '动物'

    def say(self):
        print('动物的叫声')

class Dog(Animal):   #  子类只继承一个父类： 单继承

    def see_home(self):
        print('狗可以看家')

d = Dog()
d.say()
print(d.name)
d.see_home()

class Cat(Animal):

    def say_cat(self):
        print('猫毛茸茸的很可爱')

f = Cat()
print(f.name)
f.say_cat()

#子类的对象是子类类型，同时也是父类类型
print(type(f))
# isinstance 判断对象是否是某个类型
print(isinstance(f, Cat))
print(isinstance(f, Animal))

# issubclass 判断类，是否是某个父类的子类
print(issubclass(Dog, Animal))
print(issubclass(Cat, Animal))
print(issubclass(Cat, object))  # 所有的类都继承object