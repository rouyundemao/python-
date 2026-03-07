
class Animal(object):

    def say(self):
        pass

class Dog(Animal):

    def say(self):
        print('汪汪')

class Cat(Animal):

    def say(self):
        print('喵喵')

def main(obj:Animal):
    obj.say()

d = Dog()
c = Cat()

main(d)
main(c)