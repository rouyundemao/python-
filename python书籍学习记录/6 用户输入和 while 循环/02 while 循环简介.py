
# for 循环用于针对集合中的每个元素执行一个代码块，而 while 循环则不断地运行，直到指定的条件不再满足为止。

# 使用 while 循环

current_number = 1
while current_number <= 20:
    print(current_number)
    current_number += 1

# 让用户选择何时退出
# 可以使用 while 循环让程序在用户愿意时不断地运行
# 我们在其中定义了一个退出值，只要用户输入的不是这个值，程序就将一直运行
   
# prompt = "\nTell me something, and I will repeat it back to you:"
# prompt += "\nEnter 'quit' to end the program. "

# message = ""
# while message != 'quit':
#     message = input(prompt)
#     print(message)

prompt = '\n输入一条信息，我将继续运行。'
prompt += '\n输入“quit”我将结束运行。'

message = ''
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)

# 使用标志
# 在要求满足很多条件才继续运行的程序中，可定义一个变量，用于判断整个程序是否处于活动状态。这个变量称为标志（flag），充当程序的交通信号灯。

prompt = '\n输入一条信息，我将继续运行。'
prompt += '\n输入“quit”我将结束运行。'

active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)

# 使用 break 退出循环
# 如果不管条件测试的结果如何，想立即退出 while 循环，不再运行循环中余下的代码，可使用 break 语句。

prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\nEnter 'quit' when you are finished. "

while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}")

# 注意：在所有 Python 循环中都可使用 break 语句。例如，可使用 break 语句来退出遍历列表或字典的 for 循环。
glossary = {
    'variable': 'A name that refers to a value stored in memory.',
    'function': 'A block of code that performs a specific task.',
    'loop': 'A way to repeat a block of code multiple times.',
    'list': 'An ordered collection of items.',
    'dictionary': 'A collection of key-value pairs.',
    'tuple': 'An ordered, immutable collection of elements.',
    'set': 'An unordered collection of unique items.',
    'if statement': 'Used to make decisions based on conditions.',
    'class': 'A blueprint for creating objects with specific attributes and methods.',
    'module': 'A file containing Python definitions and statements, used for code reuse.'
    }

for glo,mes in glossary.items():
    if glo == 'loop':
        break
    print(f'{glo} meaning is: {mes}')

# 在循环中使用 continue
# 要返回循环开头，并根据条件测试的结果决定是否继续执行循环，可使用 continue 语句，它不像 break 语句那样不再执行余下的代码并退出整个循环。

current_number = 0

while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)

# 避免无限循环
# 注意：与众多其他的编辑器一样，VS Code 也在内嵌的终端窗口中显示输出。要结束无限循环，可在输出区域中单击鼠标，再按 Ctrl + C。
# 确认程序至少有一个地方导致循环条件为 False 或导致 break 语句得以执行。


# 练习

# 1、比萨配料　编写一个循环，提示用户输入一系列比萨配料，并在用户输入 'quit' 时结束循环。每当用户输入一种配料后，都打印一条消息，指出要在比萨中添加这种配料。
topp = '请输入你喜欢的披萨配料：'

toppings = []
while True:
    topping = input(topp)
    toppings.append(topping)
    if topping == 'quit':
        break
    else:
        print(f'这次添加披萨配料是：{topping}')
print(f'总的披萨配料添加：{toppings}')

# 2、电影票　有家电影院根据观众的年龄收取不同的票价：
    # 不到 3 岁的观众免费；
    # 3（含）～12 岁的观众收费 10 美元；
    # 年满 12 岁的观众收费 15 美元。
    # 请编写一个循环，在其中询问用户的年龄，并指出其票价。

ag = '\n我们将通过你的年龄来判断对你的收费标准。'
ag += '\n输入"0"询问将退出，你的年龄是：'

while True:
    age = int(input(ag))
    if 0 < age < 3:
        print('你可以免费观看。')
    elif 3 <= age < 12:
        print('你的票价是10美元。')
    elif age >= 12:
        print('你的票价是15美元。')
    elif age == 0:
        break

# 3、三种出路　以不同的方式完成练习 1 或练习 2，在程序中采取如下做法。
    # 在 while 循环中使用条件测试来结束循环。
    # 使用变量 active 来控制循环结束的时机。
    # 使用 break 语句在用户输入 '0' 时退出循环。

ag = '\n我们将通过你的年龄来判断对你的收费标准。'
ag += '\n输入"0"询问将退出，你的年龄是：'

active = True
while active:
    age = int(input(ag))
    if age == 0:
        active = False
    elif 0 < age < 3:
        print('你可以免费观看。')
    elif 3 <= age < 12:
        print('你的票价是10美元。')
    elif age >= 12:
        print('你的票价是15美元。')




