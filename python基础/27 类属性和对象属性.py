
class Person():
    species = '人类'

    def __init__(self,name):
        self.name = name   # 对象属性，成员属性，实例属性

    def setName(self,name):
        self.name = name


p1 = Person('张三')
p2 = Person('李四')

print(p1.species)
print(p1.name)
print(p2.species)
print(p2.name)

# 访问属性（类属性，对象属性）
print(p1.species)
print(Person.species)

# 修改属性
p1.name = '莎木'
print(p1.name)

# 修改类属性只有一种方法
Person.species = '人'
print(p1.species)
p1.species = '智慧人'   # 并不是修改类属性，而是增加了一个对象属性
print(p2.species)     # 验证直接使用p1.species
print(p1.species)





