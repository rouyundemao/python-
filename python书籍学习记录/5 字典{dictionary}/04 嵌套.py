# 字典列表

# 如何管理成群结队的外星人呢？一种办法是创建一个外星人列表，其中每个外星人都是一个字典，包含有关该外星人的各种信息。
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 20}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

# 更符合现实的情形是，外星人不止三个，而且每个外星人都是用代码自动生成的。

# 创建一个用于存储外星人的空列表
aliens = []

# 创建 30 个绿色的外星人
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# 修改指定的外星人
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['points'] = 20
        alien['speed'] = 'fast'
            
# 显示前 5 个外星人
for alien in aliens[:5]:
    print(alien)
print('-'*50)

# 显示创建了多少个外星人
print(f"Total number of aliens: {len(aliens)}.")

# 在字典中存储列表
# 在下面的示例中，存储了比萨两个方面的信息：外皮类型和配料列表。

# 存储顾客所点比萨的信息
pizza = {
    'crust': 'thick',
      'toppings': ['mushrooms', 'extra cheese'],
    }
# 概述顾客点的比萨
print(f"You ordered a {pizza['crust']}-crust "
      "with the following toppings:")

for topping in pizza['toppings']:
    print(f'\t{topping}')

# 每当需要在字典中将一个键关联到多个值时，都可以在字典中嵌套一个列表。

favorite_languages = {
    'jen': ['python', 'rust'],
    'sarah': ['c'],
    'edward': ['rust', 'go'],
    'phil': ['python', 'haskell'],
    }

# 在遍历字典时，使用变量 languages 来依次存储字典中的每个值，因为我们知道这些值都是列表。
for name, languages in favorite_languages.items():
    # 为了进一步改进这个程序，可在遍历字典的 for 循环开头添加一条 if 语句，通过查看 len(languages) 的值来确定当前的被调查者喜欢的语言是否有多种。
    if len(languages) > 1:
        print(f"{name.title()}'s favorite language are:")
    else:
        print(f"{name.title()}'s favorite language is:")
    # 使用另一个 for 循环来遍历每个人喜欢的语言列表
    for language in languages:
        print(language.title())

# 注意：列表和字典的嵌套层级不应太多。如果嵌套层级比前面的示例多得多，很可能有更简单的解决方案。

# 在字典中存储字典

users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        },

    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        },

    }

for user_name, user_info in users.items():
    print(f'\nUsername: {user_name}')
    
    full_name = f'{user_info['first']} {user_info['last']}'
    location = user_info['location']
    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")

# 注意:表示每个用户的字典都有相同的结构，虽然 Python 并没有这样的要求，但这使得嵌套的字典处理起来更容易。倘若表示每个用户的字典都包含不同的键，for 循环内部的代码将更复杂。


# 练习
# 1、人们　在为练习 人 编写的程序中，再创建两个表示人的字典，然后将这三个字典都存储在一个名为 people 的列表中。遍历这个列表，将其中每个人的所有信息都打印出来。

people_0 = {'first_name': 'cloud', 'last_name': 'windy', 'age': 22, 'city': 'zunyi'}
people_1 = {'first_name': 'ali', 'last_name': 'cjis', 'age': 55, 'city': 'bijie'}
people_2 = {'first_name': 'rose', 'last_name': 'yilis', 'age': 16, 'city': 'xingyi'}

people = [people_0, people_1, people_2]

for peo in people:
    print(peo)

# 2、宠物　创建多个表示宠物的字典，每个字典都包含宠物的类型及其主人的名字。将这些字典存储在一个名为 pets 的列表中，再遍历该列表，并将有关每个宠物的所有信息打印出来。

pet1 = {'type': 'cat', 'ower': 'Alice'}
pet2 = {'type': 'dog', 'ower': 'Bob'}
pet3 = {'type': 'parrot', 'ower': 'Charlie'}
pet4 = {'type': 'hamster', 'ower': 'David'}
pet5 = {'type': 'turtle', 'ower': 'Emma'}

pets = [pet1, pet2, pet3, pet4, pet5]

for pet in pets:
    print(f"\n宠物类型是:{pet['type']}")
    print(f"宠物的主人是:{pet['ower']}")
    

# 3、喜欢的地方　创建一个名为 favorite_places 的字典。
    # 在这个字典中，将三个人的名字用作键，并存储每个人喜欢的 1～3 个地方。为让这个练习更有趣些，让一些朋友说出他们喜欢的几个地方。
    # 遍历这个字典，并将其中每个人的名字及其喜欢的地方打印出来。

favorite_palces = {
    'Alice': ['金字塔', '长城', '马岭河峡谷'],
    'Bob': ['长江', '纽约', '莫斯科'],
    'Emma':['复活岛', '泰姬陵']
    }

for name, place in favorite_palces.items():
    print(f'\n{name}喜欢的地方有：')
    for pla in place:
        print(f'-{pla}-')

# 4、喜欢的数 2　修改为练习 喜欢的数 1 编写的程序，让每个人都可以有多个喜欢的数字，然后将每个人的名字及其喜欢的数打印出来。

like_numbers ={
    'admin': [5,12,44,556], 
    'kaer': [9,45,21,345],
    'alice': [56,546,57], 
    'cloud': [23,4564,2334], 
    'windy':[27,545,356,51]
    }

for name, numbers in like_numbers.items():
    print(f"\n{name}喜欢的数字有：")
    for number in numbers:
        print(f"-{number}")
        
# 5、城市　创建一个名为 cities 的字典，将三个城市名用作键。
    # 对于每座城市，都创建一个字典，并在其中包含该城市所属的国家、人口约数以及一个有关该城市的事实。
    # 表示每座城市的字典都应包含 country、population 和 fact 等键。将每座城市的名字以及相关信息都打印出来。

cities ={
    '遵义':{
        '国家': '中国',
        '人口约数': '660.67万',
        '事实':'经济总量实现新突破——全市地区生产总值连续突破4000亿元、5000亿元大关，经济总量在全国百强城市排第62位，在西部非省会城市排第3位。'
    },
    
    '兴义':{
        '国家': '中国',
        '人口约数': '376.6万',
        '事实':'全国首批新能源示范城市、国家首批全域旅游示范区、国家新型城镇化综合试点地区，是贵州省重点建设的产业发展示范区。'
    },
    
    '毕节':{
        '国家': '中国',
        '人口约数': '689.96万',
        '事实': '毕节是全国唯一一个以“开发扶贫、生态建设”为主题的试验区,具有丰富的自然资源和独特的地理位置,是川、滇、黔三省的交通要冲。'
    }
}

for city_name, city_info in cities.items():
    print(f'\n城市名称：{city_name}')
    
    country = city_info['国家']
    people = city_info['人口约数']
    fact = city_info['事实']
    print(f'\t国家：{country}')
    print(f'\t人口约数：{people}')
    print(f'\t事实：{fact}')
    
    


