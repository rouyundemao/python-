
# 遍历所有的键值对

user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
    }

# for 语句的第二部分包含字典名和方法 items()，这个方法返回一个键值对列表。
# 接下来，for 循环依次将每个键值对赋给指定的两个变量。
for key, value in user_0.items():
    print(f'\nKey:{key}')
    print(f'Value:{value}')

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python'
    }  

for name, language in favorite_languages.items():
    print(f'\n{name.title()} favorite language is {language.title()}.')

# 遍历字典中的所有键   keys() 方法
# 在不需要使用字典中的值时，keys() 方法很有用。下面来遍历字典 favorite_languages，并将每个被调查者的名字都打印出来

for name in favorite_languages.keys():
    print(name.title())

# keys() 方法也可以省略。
# for name in favorite_languages:
#     print(name.title())

friends = ['jen', 'sarah']
for name in favorite_languages.keys():
    print(f'Hello,{name.title()}!')
    if name in friends:
        language = favorite_languages[name].title()
        print(f'{name.title()},I see you love {language}.')

# 还可以使用 keys() 确定某个人是否接受了调查。
if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")
# keys() 方法并非只能用于遍历：
# 实际上，它会返回一个列表，其中包含字典中的所有键。因此 if 语句只核实 'erin' 是否在这个列表中。因为她并不在这个列表中，所以打印一条消息，邀请她参加调查.

# 按特定的顺序遍历字典中的所有键
# 要以特定的顺序返回元素，一种办法是在 for 循环中对返回的键进行排序。为此，可使用 sorted() 函数来获得按特定顺序排列的键列表的副本
# sorted() 函数让列表临时按照字母大小排序。 可以传入 reverse = True 改变排序方向。

for name in sorted(favorite_languages.keys()):
    print(f'{name.title()},thank you for taking the poll.')

# 遍历字典中的所有值   values() 方法
# values() 方法会返回一个值列表，不包含任何键。
print("The following languages have been mentioned:")

for language in favorite_languages.values():
    print(language.title())
# 这种做法提取字典中所有的值，而没有考虑值是否有重复。
# 当涉及的值很少时，这也许不是问题，但如果被调查者很多，最终的列表可能包含大量的重复项。

# 为剔除重复项，可使用集合（set）。集合中的每个元素都必须是独一无二的。
# set() 集合，避免重复值。
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())

# 注意：可以使用一对花括号直接创建集合，并在其中用逗号分隔元素：
languages = {'python', 'rust', 'python', 'c'}
print(languages)
# 集合和字典很容易混淆，因为它们都是用一对花括号定义的。当花括号内没有键值对时，定义的很可能是集合。不同于列表和字典，集合不会以特定的顺序存储元素。

# 练习

# 1、词汇表 2　现在你知道了如何遍历字典，请整理你为词汇表 1编写的代码，将其中的一系列函数调用 print() 替换为一个遍历字典中键和值的循环。
# 确保该循环正确无误后，再在词汇表中添加 5 个 Python 术语。当你再次运行这个程序时，这些新术语及其含义将自动包含在输出中。
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

for word, meaning in glossary.items():
    print(f"{word}: {meaning}")

# 2、河流　创建一个字典，在其中存储三条河流及其流经的国家。例如，一个键值对可能是 'nile': 'egypt'。
    # 使用循环为每条河流打印一条消息，如下所示。
    # The Nile runs through Egypt.
    # 使用循环将该字典中每条河流的名字打印出来。
    # 使用循环将该字典包含的每个国家的名字打印出来。

rivers = {
    'Yangtze River': 'China',
    'nile': 'egypt',
    'Mississippi River': 'America'
    }

for river, country in rivers.items():
    print(f'The {river} runs through {country}.')

for river in rivers.keys():
    print(river)

for country in rivers.values():
    print(country)

# 3、调查　在编写的程序 favorite_languages中执行以下操作。
    # 创建一个应该会接受调查的人的名单，其中有些人已在字典中，而其他人不在字典中。
    # 遍历这个名单。对于已参与调查的人，打印一条消息表示感谢；对于还未参与调查的人，打印一条邀请参加调查的消息。

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python'
    }  

survey_list = ['jen', 'cloud', 'jane']

for sur in survey_list:
    if sur in favorite_languages.keys():
        print(f'{sur.title()},感谢你参与调查！')
    else:
        print(f'你好，{sur.title()},希望你能够参与调查。')


