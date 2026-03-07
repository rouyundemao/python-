# 每条 if 语句的核心都是一个值为 True 或 False 的表达式，这种表达式称为条件测试。
# Python 根据条件测试的值是 True 还是 False 来决定是否执行 if 语句中的代码。
# 如果条件测试的值为 True，Python 就执行紧跟在 if 语句后面的代码；如果为 False，Python 就忽略这些代码。

# 检查是否相等   终端运行: shfit+enter  选中代码片段后运行。
car ='bmw'
car == 'bmw'
car =='asd'
# 一个等号是陈述，于是第6行代码可解读为：将变量 car 的值设置为 'bmw'。两个等号则是发问，于是第7行代码可解读为：变量 car 的值是 'bmw' 吗？大多数编程语言使用等号的方式与这里的示例相同。

# 如何在检查是否相等时忽略大小写
# 在 Python 中检查是否相等时是区分大小写的。
car = 'Audi'
car == 'audi'
# 如果大小写很重要，这种行为有其优点。但如果大小写无关紧要，你只想检查变量的值，可先将变量的值转换为全小写的，再进行比较
car.lower() == 'audi'
# lower() 方法不会修改存储在变量 car 中的值，因此进行这样的比较不会影响原来的变量
car

# 检查是否不等    要判断两个值是否不等，可使用不等运算符（!=）。
requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print("Hold the anchovies!")

# 数值比较
answer = 18
if answer != 42:
    print('That is not the correct answer. Please try again!')

age = int(input('请输入你的年龄：'))

if age >= 18:
    print('你已经成年了，欢迎进入!')
else:
    print('你还未成年，禁止进入！')

# 检查多个条件
# 使用 and 检查多个条件
age_0 = int(input('请输入年龄：'))
age_1 = int(input('请输入年龄：'))

if age_0 >=21 and age_1 >= 21:
    print('两人都达到要求，可以通过！')
else:
    print('不符合要求，不可以通过！')

# 使用 or 检查多个条件
if age_0 >=21 or age_1 >= 21:
    print('有人达到要求，可以通过！')
else:
    print('不符合要求，不可以通过！')

# 检查特定的值是否在列表中    要判断特定的值是否在列表中，可使用关键字 in。
# 有时候，执行操作前必须检查列表是否包含特定的值。
# 例如，在结束用户的注册过程之前，需要检查他提供的用户名是否已在用户名列表中；在地图程序中，需要检查用户提交的位置是否在已知位置的列表中。

requested_toppings = ['mushrooms', 'onions', 'pineapple']

'pepperoni' in requested_toppings
'onions' in requested_toppings

# 检查特定的值是否不在列表中
# 还有些时候，确定特定的值不在列表中很重要。在这种情况下，可使用关键字 not in。
# 例如，有一个列表包含被禁止在论坛上发表评论的用户，这样就可以在允许用户提交评论前检查他是否被禁言了

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")


# 练习

# 1、条件测试　编写一系列条件测试，将每个条件测试以及你对其结果的预测和实际结果都打印出来。你编写的代码应类似于下面这样：
car = 'subaru'
print("\nIs car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')
# 详细研究实际结果，直到你明白它为何为 True 或 False。
# 创建至少 10 个条件测试，而且结果为 True 和 False 的条件测试分别至少有 5 个。
if car == 'subaru':
    print(f'My car is {car}.')
else:
    print('It is not my car!')

# 2、更多条件测试　你并非只能创建 10 个条件测试。如果想尝试做更多的比较，可再编写一些条件测试，并将它们加入 conditional_tests.py。对于下面列出的各种情况，至少编写两个条件测试，结果分别为 True 和 False。
# 检查两个字符串是否相等和不等。
# 使用 lower() 方法的条件测试。
# 涉及相等、不等、大于、小于、大于等于和小于等于的数值比较。
# 使用关键字 and 和 or 的条件测试。
# 测试特定的值是否在列表中。
# 测试特定的值是否不在列表中。

# 布尔表达式
# 随着对编程的了解越来越深入，你将遇到术语布尔表达式，它不过是条件测试的别名罢了。与条件表达式一样，布尔表达式的结果要么为 True，要么为 False。

# 布尔值通常用于记录条件，如游戏是否正在运行或用户是否可以编辑网站的特定内容：
game_active = True
can_edit = False
# 在跟踪程序状态或程序中重要的条件方面，布尔值提供了一种高效的方式。

