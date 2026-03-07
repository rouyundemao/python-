# '这是字符串'
# "这也是字符串"
# 单引号与双引号在需要一次引用多个引号时互相嵌套就能避免语法错误。

name = 'ada lovelace'
print(name.title())   # 方法（method）是可以对变量数据进行操作的，此处的title()方法的作用是：让变量以首字母大写显示每个单词。
print(name.upper())   # 让变量单词以大写的形式显示。
print(name.lower())   # 让变量单词以小写的形式显示。

first_name = 'ada'
last_name = 'lovelace'
full_name = f'{first_name} {last_name}'   # f字符串：f为format（设置格式）的简写
print(full_name)
print(f'Hello, {full_name.title()}!')

# 将 f 创建的信息赋予 message 方便后续使用！
message = f'Hello, {full_name.title()}!' 
print(message)

# 使用制表符或换行符来添加空白

# 制表符 \t
print('时间')
print('\t时间')
print('\t时间')
print('时间\t')

# 换行符  \n
print('时\n间')

# 同时包含制表符和换行符 \n\t
words = '\n\t时间流逝，\n\t一去不回，\n\t岁月如歌，\n\t且听且珍。'
print(words)

# 删除空白 - rstrip() 方法
favorite_language = 'python good '
print(favorite_language)
favorite_language.rstrip()    # rstrip() 方法修改只是暂时的，再次访问favorite_language空白还是存在。
print(favorite_language)

favorite_language = favorite_language.rstrip()    # 想要删除变量的空白，要将rstrip()方法处理后的变量关联到原来的变量。
print(favorite_language)

favorite_language = ' 你好！ '
# rstrip()删除字符串右侧的空白
favorite_language.rstrip()
# lstrip()删除字符串左侧的空白
favorite_language.lstrip()
# strip()删除字符串两端的空白
favorite_language.strip()

# 删除前缀 removeprefix('添加要删除的内容')
bilibili_url = 'https://www.bilibili.com'     # removeprefix() 方法删除的内容也是暂时的
bilibili_url.removeprefix('https://')
# 保存删除后的值，重新赋予一个变量或原来的变量
simple_url = bilibili_url.removeprefix('https://')
print(simple_url)
# 删除后缀 removesuffix()
file_name = 'python_notes.txt'
print(file_name.removesuffix('.txt'))

# 避免语法错误
message = "One of Python's strengths is its diverse community."         # 在用单引号引起的字符串中包含撇号，就将导致错误。里面有撇号，外面就使用双引号避免发生语法错误。
print(message)

# 练习
# 1、个性化消息　用变量表示一个人的名字，并向其显示一条消息。显示的消息应非常简单，如下所示。
# Hello Eric, would you like to learn some Python today?
name = 'Eric'
print(f'Hello {name}, would you like to learn some Python today?')

# 2、调整名字的大小写　用变量表示一个人的名字，再分别以全小写、全大写和首字母大写的方式显示这个人名。
print(name.lower())
print(name.upper())
print(name.title())

# 3、名言 1　找到你钦佩的名人说的一句名言，将这个名人的姓名和名言打印出来。输出应类似于下面这样（包括引号）。
# Albert Einstein once said, “A person who never made a mistake never tried anything new.”    翻译：阿尔伯特·爱因斯坦曾经说过：“从不犯错的人从不尝试新事物。”
message = 'Albert Einstein once said, “A person who never made a mistake never tried anything new.”'
print(message)

# 4、名言 2  重复练习，但用变量 famous_person 表示名人的姓名，再创建要显示的消息并将其赋给变量 message，然后打印这条消息。
famous_name = 'Albert Einstein'
famous_say = 'A person who never made a mistake never tried anything new.'
message = f'{famous_name} once said, “{famous_say}”'
print(message)

# 5、删除人名中的空白　用变量表示一个人的名字，并在其开头和末尾都包含一些空白字符。务必至少使用字符组合 "\t" 和 "\n" 各一次。
new_name = '\n\t 蔚蓝色的湖泊 \n\t'
clear_name = new_name.strip()
print(repr(new_name))
print(repr(clear_name))    # repr()方法：显示终端返回一个对象的官方字符串表示，访问变量的终端显示内容。  repr(object) 参数object：任何 Python 对象（字符串、数字、列表、字典、类实例等）都可以。
clear_name = new_name.lstrip()
print(repr(clear_name))
clear_name = new_name.rstrip()
print(repr(clear_name))

# 6、文件扩展名　Python 提供了 removesuffix() 方法，其工作原理与 removeprefix() 很像。
# 请将值 'python_notes.txt' 赋给变量 filename，再使用 removesuffix() 方法来显示不包含扩展名的文件名，就像文件浏览器所做的那样。
file_name = 'python_notes.txt'
print(file_name.removesuffix('.txt'))
