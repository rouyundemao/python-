
# for 循环语句
# 对于（for）列表 magicians 中的每位魔术师（magician），都打印（print）该魔术师（magician）的名字。
magicians = ['alice', 'david', 'carolina']

for magician in magicians:
    print(magician)
    
# 深入研究循环
# 循环很重要，因为它是让计算机自动完成重复工作的常见方式之一。

# 在编写 for 循环时，可以给将依次与列表中的每个值相关联的临时变量指定任意名称。
# 然而，选择描述单个列表元素的有意义的名称大有裨益。例如，对于小猫列表、小狗列表和一般性列表，像下面这样编写 for 循环的第一行代码是不错的选择：
# for cat in cats:
# for dog in dogs:
# for item in list_of_items:

# 在 for 循环中执行更多的操作
for magician in magicians:
        print(f'{magician},tath was a greet trick!')

# 避免缩进错误
# 常见错误

# 忘记缩进
# 忘记缩进额外的代码行  有时候，虽然循环能够运行且不会出现错误，但结果出人意料。当试图在循环中执行多项任务，却忘记缩进其中的一些代码行时，就会出现这种情况。
# 不必要的缩进 
# 循环后不必要的缩进
# 遗漏冒号

# 练习

# 1、比萨　想出至少三种你喜欢的比萨，将其名称存储在一个列表中，再使用 for 循环将每种比萨的名称打印出来。
    # 修改这个 for 循环，使其打印包含比萨名称的句子，而不仅仅是比萨的名称。对于每种比萨都显示一行输出，如下所示。
    # I like pepperoni pizza.
    # 在程序末尾添加一行代码（不包含在 for 循环中），指出你有多喜欢比萨。输出应包含针对每种比萨的消息，还有一个总结性的句子，如下所示。
    # I really love pizza!

pizzas = ['pepperoni', 'Margherita', 'Hawaiian']

for pizza in pizzas:
    print(f'I like {pizza} pizza.')
print('I really love pizza!')

# 2、动物　想出至少三种有共同特征的动物，将其名称存储在一个列表中，再使用 for 循环将每种动物的名称打印出来
    # 修改这个程序，使其针对每种动物都打印一个句子，如下所示。
    # A dog would make a great pet.
    # 在程序末尾添加一行代码，指出这些动物的共同之处，如打印下面这样的句子。
    # Any of these animals would make a great pet!
animals = ['cat', 'dog', 'bird']
for animal in animals:
    print(f'A {animal} would make a great pet.')
print('Any of these animals would make a great pet!')

