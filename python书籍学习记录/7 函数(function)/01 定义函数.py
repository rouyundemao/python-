# 函数是带名字的代码块，用于完成具体的工作。要执行函数定义的特定任务，可调用（call）该函数。
# 当需要在程序中多次执行同一项任务时，无须反复编写完成该任务的代码，只需要调用执行该任务的函数，让 Python 运行其中的代码即可。

# 打印问候语的简单函数
# 使用关键字 def 来告诉 Python，我要定义一个函数
def greet_user():         # 函数名为 greet_user()，它不需要任何信息就能完成工作，因此括号内是空的（即便如此，括号也必不可少）。
    """ 显示简答的问候语 """     # 文档字符串（docstring）: 描述了函数是做什么的。 快捷键：Alt + Shift + A
    print('你好！')        # 函数的代码行
# 调用函数
greet_user()


# 向函数传递信息
# 在函数定义 def greet_user() 的括号内添加 username。
def greet_user(username):      # username 是一个形参。
    """ 显示简答的问候语 """
    print(f"你好！{username.title()}")

greet_user('sunny')    # 'sunny' 是一个实参。

# 实参和形参
# 在 greet_user() 函数的定义中，变量 username 是一个形参（parameter），即函数完成工作所需的信息。
# greet_user('sunny') 中，值 'sunny' 是一个实参（argument），即在调用函数时传递给函数的信息。
# 实参 'sunny' 传递给函数 greet_user()，这个值被赋给了形参 username。


# 练习

# 1、消息　编写一个名为 display_message() 的函数，让它打印一个句子，指出本章的主题是什么。调用这个函数，确认显示的消息正确无误。

def display_message(message):
    """ 显示信息 """
    print(f"本章的主题是{message}")

display_message('函数(function)')

# 喜欢的书　编写一个名为 favorite_book() 的函数，其中包含一个名为 title 的形参。让这个函数打印一条像下面这样的消息。
    # One of my favorite books is Alice in Wonderland.  我最喜欢的书之一是《爱丽丝梦游仙境》。
    # 调用这个函数，并将一本书的书名作为实参传递给它。

def favorite_book(title):
    """ 最喜欢的书 """
    print(f'One of my favorite books is {title}.')

favorite_book('Alice in Wonderland')

