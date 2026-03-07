# 键值对包含两个相互关联的值。当你指定键时，Python 将返回与之关联的值。键和值之间用冒号分隔，而键值对之间用逗号分隔。

# 访问字典中的值
alien_0 = {'color': 'green'}
print(alien_0['color'])

alien_0 = {'color': 'green', 'points': 5}

new_points = alien_0['points']
print(f'You just earned {new_points} points')

# 添加键值对     变量[] = '任意类型对象'
# 字典是一种动态结构，可随时在其中添加键值对。

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# 从创建一个空字典开始
# 有时候，在空字典中添加键值对很方便，甚至是必需的。为此，可先使用一对空花括号定义一个空字典，再分行添加各个键值对。
alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)

# 修改字典中的值   重新给想修改的键赋值。
print(f'The alien is {alien_0["color"]}')

alien_0['color'] = 'yellow'
print(f'The alien is now {alien_0["color"]}')

# 对一个能够以不同速度移动的外星人进行位置跟踪。为此，存储该外星人的当前速度，并据此确定该外星人应该向右移动多远.
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}")

# 向右移动外星人
# 根据当前速度确定将外星人向右移动多远
if alien_0['speed'] == 'slow':
    x_crement = 1
elif alien_0['speed'] == 'medium':
    x_crement = 2
else:
    x_crement = 3

alien_0['x_position'] = alien_0['x_position'] + x_crement
print(f'New position: {alien_0['x_position']}')
# 通过修改外星人字典中的值，可改变外星人的行为。

# 删除键值对
alien_0 = {'color': 'green', 'points': 5}
# 注意：删除的键值对永远消失了。
del alien_0['color']
print(alien_0)

# 由类似的对象组成的字典
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python'
    }         # 最后的花括号要缩进。
# 注意：对于较长的列表和字典，大多数编辑器提供了以类似方式设置格式的功能。
# 对于较长的字典，还有其他一些可行的格式设置方式，因此在你的编辑器或其他源代码中，你可能会看到稍微不同的格式设置方式。

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")

# 使用 get() 来访问值
# 可使用 get() 方法在指定的键不存在时返回一个默认值。
# get() 方法
# 第一个参数用于指定键，是必不可少的；
# 第二个参数为当指定的键不存在时要返回的值，是可选的

alien_0 = {'color': 'green', 'speed': 'slow'}
# 如果字典中有键 'points'，将获得与之关联的值；如果没有，将获得指定的默认值。
points_value = alien_0.get('points', 'No point value assigned.')
print(points_value)

# 如果指定的键有可能不存在，应考虑使用 get() 方法，而不要使用方括号表示法。
# 注意：在调用 get() 时，如果没有指定第二个参数且指定的键不存在，Python 将返回值 None，这个特殊的值表示没有相应的值。这并非错误，None 只是一个表示所需值不存在的特殊值

# 练习

# 1、人　使用一个字典来存储一个人的信息，包括名、姓、年龄和居住的城市。该字典应包含键 first_name、last_name、age 和 city。将存储在该字典中的每项信息都打印出来。

people = {'first_name': 'cloud', 'last_name': 'windy', 'age': 22, 'city': 'zunyi'}
print(people['first_name'])
print(people['last_name'])
print(people['age'])
print(people['city'])

# 2、喜欢的数 1　使用一个字典来存储一些人喜欢的数。
# 请想出 5 个人的名字，并将这些名字用作字典中的键。
# 再想出每个人喜欢的一个数，并将这些数作为值存储在字典中。打印每个人的名字和喜欢的数。为了让这个程序更有趣，通过询问朋友确保数据是真实的。

like_numbers ={
    'admin': 5, 
    'kaer': 9,
    'alice': 56, 
    'cloud': 23, 
    'windy':27
    }
# 遍历并打印每个人的名字和喜欢的数字
# items() 方法，同时获得字典的键（key）和值（value）。
for name, number in like_numbers.items():
    print(f'{name.title()}喜欢的数字是{number}。')

# 3、词汇表 1　Python 字典可用于模拟现实生活中的字典。为避免混淆，我们将后者称为词汇表。
    # 想出你在前面学过的 5 个编程术语，将它们用作词汇表中的键，并将它们的含义作为值存储在词汇表中。
    # 以整洁的方式打印每个术语及其含义。为此，既可以先打印术语，在它后面加上一个冒号，再打印其含义；也可以先在一行里打印术语，再使用换行符（\n）插入一个空行，然后在下一行里以缩进的方式打印其含义。

glossary = {
    'variable': 'A name that refers to a value stored in memory.',
    'function': 'A block of code that performs a specific task.',
    'loop': 'A way to repeat a block of code multiple times.',
    'list': 'An ordered collection of items.',
    'dictionary': 'A collection of key-value pairs.'
    }

for word, meaning in glossary.items():
    print(f"{word}: {meaning}")


