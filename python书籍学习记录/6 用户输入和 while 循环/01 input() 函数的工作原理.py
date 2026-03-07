# input() 函数让程序暂停运行，等待用户输入一些文本。获取用户输入后，Python 将其赋给一个变量，以便使用。

# input() 函数接受一个参数，即要向用户显示的提示（prompt），让用户知道该输入什么样的信息。

message = input('请输入你的名字：')
print(message)

# 注意：有些文本编辑器不能运行提示用户输入的程序。你可使用这些文本编辑器编写提示用户输入的程序，但必须从终端运行它们。

# 编写清晰的提示
# 每当使用 input() 函数时，都应指定清晰易懂的提示，准确地指出希望用户提供什么样的信息——能指出用户应该输入什么信息的任何提示都行

message = input('请输入你所在的城市： ')     # 在提示后面加一个空格，以便于用户输入信息。
print(message)

prompt = '如果你输入你的名字，我们将个性化你的名字。'
prompt += '\n你的名字是？'

name = input(prompt)
print(f'你好{name}，欢迎来到新的世界！')

# 使用 int() 来获取数值输入
# 在使用 input() 函数时，Python 会将用户输入解读为字符串。
# 在将数值输入用于计算和比较前，务必将其转换为数值表示。

age = int(input('你今年多少岁了？'))

if age >= 18:
    print('你已经成年了！')
else:
    print('你还没有成年！')

# 示例
height = input("How tall are you? ")
height = int(height)

if height >= 140:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")

# 求模运算符 
# 求模运算符（%）是个很有用的工具，它将两个数相除并返回余数

mes = '请输入一个数，我将告诉你它是奇数还是偶数。'
mes += '\n你输入的数是：'
number = int(input(mes))

if number % 2 == 0:
    print(f'{number}是一个偶数。')
else:
    print(f'{number}是一个奇数。')


# 练习

# 1、汽车租赁　编写一个程序，询问用户要租什么样的汽车，并打印一条消息，如下所示。
    #Let me see if I can find you a Subaru.

car = input('你想要购买的车的名字是： ')
print(f'我看看能不能帮你找到一辆{car}.')

# 2、餐馆订位　编写一个程序，询问用户有多少人用餐。如果超过 8 个人，就打印一条消息，指出没有空桌；否则指出有空桌。

prompt = '请问有几位客人需要用餐？'
prompt += '\n用餐的人有： '
eats = int(input(prompt))
if eats >8:
    print('非常抱歉，没有空桌了。')
else:
    print('还有空桌。')


# 3、10 的整数倍　让用户输入一个数，并指出这个数是否是 10 的整数倍。

number = int(input('请输入一个数： '))

if number % 10 == 0:
    print('这个数是10的整数倍。')
else:
    print('这个数不是10的整数倍。')
    


