
# 切片(slice)
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[2:3])
print(players[:3])
print(players[2:])
print(players[-2:])
# 注意：可在表示切片的方括号内指定第三个值。这个值告诉 Python 在指定范围内每隔多少元素提取一个。
# 列表名 [起始索引 : 结束索引 : 步长]    步长也可以为负数
print(players[0:3:2])

print('Here are the first three players on my team:')
for player in players[0:3]:            # 列表调用：list[x:y:z]
    print(player)

# 复制列表
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

# friend_foods 与 my_foods 是两个独立的列表，可以分别添加元素。
my_foods.append('cannoli')
friend_foods.append('ice cream')   
# # 这是行不通的： 这里将 my_foods 赋给 friend_foods，而不是将 my_foods 的副本赋给 friend_foods。
# friend_foods = my_foods
# 这种语法实际上是让 Python 将新变量 friend_foods 关联到已与 my_foods 相关联的列表，因此这两个变量指向同一个列表。

print(f'\nMy favorite food are:{my_foods}')
print(f"\nMy friend's favorite food are:{friend_foods}")

# 练习

# 1、切片　选择你在本章编写的一个程序，在末尾添加几行代码，以完成如下任务。
    # 打印消息“The first three items in the list are:”，再使用切片来打印列表的前三个元素。
    # 打印消息“Three items from the middle of the list are:”，再使用切片来打印列表中间的三个元素。
    # 打印消息“The last three items in the list are:”，再使用切片来打印列表末尾的三个元素。
players = ['charles', 'martina', 'michael', 'florence', 'eli']

print('\nThe first three items in the list are:')
print(players[:3])
print('\nThree items from the middle of the list are:')
print(players[1:4])
print('\nThe last three items in the list are:')
print(players[-3:])

# 2、你的比萨，我的比萨　在你为编写的程序中，创建比萨列表的副本，并将其赋给变量 friend_pizzas，再完成如下任务。
    # 在原来的比萨列表中添加一种比萨。
    # 在列表 friend_pizzas 中添加另一种比萨。
    # 核实有两个不同的列表。为此，打印消息“My favorite pizzas are:”，再使用一个 for 循环来打印第一个列表；
    # 打印消息“My friend's favorite pizzas are:”，再使用一个 for 循环来打印第二个列表。核实新增的比萨被添加到了正确的列表中。

my_pizzas = ['pepperoni', 'Margherita', 'Hawaiian']
friend_pizzas = my_pizzas[:]

my_pizzas.append('Chicken')
friend_pizzas.append('Beef')

print(f'My favorite pizzas are:')

for pizza in my_pizzas:
    print(pizza)

print(f"My friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)

# 3、请选择一个版本的 foods 列表，在其中编写两个 for 循环，将各个食品列表都打印出来。
print('\nMy favorite food are:')
for food in my_foods:
    print(food)

print("\nMy friend's favorite food are:")
for food in friend_foods:
    print(food)


