
# 简单的 if 语句
# if 条件测试：
#     执行操作
#     ......
# if conditional_test:
#     do something

age = 21
if age >= 18:
    print('You are old enough to vote!')
    print("Have you registered to vote yet?")

# if-else 语句
age = 16
if age >= 18:
    print('You are old enough to vote!')
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")

# if-elif-else 语句

# 4 岁以下免费。
# 4（含）～18 岁收费 25 美元。
# 年满 18 岁收费 40 美元。

age = 15
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $25.")
else:
    print("Your admission cost is $40.")

# 简洁写法
age = 18
if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40
print(f'Your admission cost is ${price}.')

# 使用多个 elif 代码块
# 假设年满 65 岁的老人可半价（即 20 美元）购买门票
age = 80
if age <4:
    price = 0
elif age < 18:
    price = 25
elif age >= 65:
    price = 20
else:
    price = 40
print(f'Your admission cost is ${price}.')

# 省略 else 代码块
# else 是一条包罗万象的语句，只要不满足任何 if 或 elif 中的条件测试，其中的代码就会执行。这可能引入无效甚至恶意的数据。

age = 15
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 20
print(f'Your admission cost is ${price}.')

# 测试多个条件
requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

# 总之，如果只想运行一个代码块，就使用 if-elif-else 语句；如果要运行多个代码块，就使用一系列独立的 if 语句。

# 练习

# 1、外星人颜色 1　假设玩家在游戏中消灭了一个外星人，请创建一个名为 alien_color 的变量，并将其赋值为 'green'、'yellow' 或 'red'。
    # 编写一条 if 语句，测试外星人是否是绿色的。如果是，就打印一条消息，指出玩家获得了 5 分。
    # 编写这个程序的两个版本，上述条件测试在其中的一个版本中通过，在另一个版本中未通过（未通过条件测试时没有输出）。

alien_color = 'yellow'
if alien_color == 'green':
    print('获得5分！')

alien_color = 'green'
if alien_color == 'green':
    print('获得5分！')

# 2、外星人颜色 2　像练习 1 那样设置外星人的颜色，并编写一个 if-else 结构。
    # 如果外星人是绿色的，就打印一条消息，指出玩家因消灭该外星人获得了 5 分。
    # 如果外星人不是绿色的，就打印一条消息，指出玩家获得了 10 分。
    # 编写这个程序的两个版本，在一个版本中将执行 if 代码块，在另一个版本中将执行 else 代码块。

alien_color = 'yellow'
if alien_color == 'green':
    print('获得5分！')
else:
    print('获得10分！')

alien_color = 'green'
if alien_color == 'green':
    print('获得5分！')
else:
    print('获得10分！')

# 3、外星人颜色 3　将练习 2 中的 if-else 结构改为 if-elif-else 结构。
    # 如果外星人是绿色的，就打印一条消息，指出玩家获得了 5 分。
    # 如果外星人是黄色的，就打印一条消息，指出玩家获得了 10 分。
    # 如果外星人是红色的，就打印一条消息，指出玩家获得了 15 分。
    # 编写这个程序的三个版本，分别在外星人为绿色、黄色和红色时打印一条消息。

alien_color = ['red', 'green', 'yellow']

for color in alien_color:
    if color == 'green':
        print('获得5分！')
    elif color == 'yellow':
        print('获得10分！')
    else:
        print('获得15分！')
        
# 4、人生的不同阶段　设置变量 age 的值，再编写一个 if-elif-else 结构，根据 age 的值判断这个人处于人生的哪个阶段。
    # 如果年龄小于 2 岁，就打印一条消息，指出这个人是婴儿。
    # 如果年龄为 2（含）～4 岁，就打印一条消息，指出这个人是幼儿。
    # 如果年龄为 4（含）～13 岁，就打印一条消息，指出这个人是儿童。
    # 如果年龄为 13（含）～18 岁，就打印一条消息，指出这个人是少年。
    # 如果年龄为 18（含）～65 岁，就打印一条消息，指出这个人是中青年人。
    # 如果年龄达到 65 岁，就打印一条消息，指出这个人是老年人。

age = 14
if age < 2:
    print('这是一个婴儿。')
elif 2 <= age <4:
    print('这是一个幼儿。')
elif 4 <= age < 13:
    print('这是一个儿童。')
elif 13 <= age < 18:
    print('这是一个少年。')
elif 18 <= age < 65:
    print('这是一个中青年人')
else:
    print('这是一个老年人')

# 5、喜欢的水果　创建一个列表，其中包含你喜欢的水果，再编写一系列独立的 if 语句，检查列表中是否包含特定的水果。   
    # 将该列表命名为 favorite_fruits，并让其包含三种水果。
    # 编写 5 条 if 语句，每条都检查某种水果是否在列表中。如果是，就打印一条像下面这样的消息。
    # You really like bananas!

# 使用 in 作条件测试。
# 创建喜欢的水果列表
favorite_fruits = ['苹果', '香蕉', '葡萄']

# 检查不同水果是否在列表中
if '苹果' in favorite_fruits:
    print("You really like apples!")

if '香蕉' in favorite_fruits:
    print("You really like bananas!")

if '葡萄' in favorite_fruits:
    print("You really like grapes!")

if '草莓' in favorite_fruits:
    print("You really like strawberries!")

if '橙子' in favorite_fruits:
    print("You really like oranges!")


favorite_fruits = ['apple', 'banana', 'grape']

for fruit in favorite_fruits:
    if fruit == 'apple':
        print('I really like apple!')
    if fruit == 'pear':
        print('I really like pear!')
    if fruit == 'banana':
        print('I really like banana!')
    if fruit == 'grape':
        print('I really like grape!')
    if fruit == 'hami melon':
        print('I really like hami melon!')
