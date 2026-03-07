
# 检查特殊元素

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    print(f'Adding {requested_topping}')
print('\nFinished making your pizza!')

# 如果比萨店的青椒（green peppers）用完了，该如何处理呢？为了妥善地处理这种情况，可在 for 循环中包含一条 if 语句

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print('Sorry, we are out of green peppers right now.')
    else:
        print(f'Adding {requested_topping}')
print('\nFinished making your pizza!')

# 确定列表非空
requested_toppings = []

if requested_toppings:     # 判断 requested_topping 是否为空  对于数值 0、空值 None、单引号空字符串 ''、双引号空字符串 ""、空列表 []、空元组 ()、空字典 {}，Python 都会返回 False。
    for requested_topping in requested_toppings:
        print(f'Adding {requested_topping}')
    print('\nFinished making your pizza!')
else:
    print('\nAre you sure you want a plain pizza?')

# 使用多个列表
available_toppings = ['mushrooms', 'olives', 'green peppers','pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f'\nAdding {requested_topping}.')
    else:
        print(f"\nSorry, We don't have {requested_topping}.")


# 练习

# 1、以特殊方式跟管理员打招呼　创建一个至少包含 5 个用户名的列表，并且其中一个用户名为 'admin'。
# 想象你要编写代码，在每个用户登录网站后都打印一条问候消息。遍历用户名列表，向每个用户打印一条问候消息。
    # 如果用户名为 'admin'，就打印一条特殊的问候消息，如下所示。
    # Hello admin, would you like to see a status report?
    # 否则，打印一条普通的问候消息，如下所示。
    # Hello Jaden, thank you for logging in again.

users = ['admin', 'kaer', 'alice', 'cloud', 'windy']

for user in users:
    if user == 'admin':
        print(f'Hello {user}, would you like to see a status report?')
    else:
        print(f'Hello {user}, thank you for logging in again.')

# 2、处理没有用户的情形　在为练习 1 编写的程序中，添加一条 if 语句，检查用户名列表是否为空。
    # 如果为空，就打印如下消息。
    # We need to find some users!
    # 删除列表中的所有用户名，确认将打印正确的消息。

users = []
if users:
    for user in users:
        if user == 'admin':
            print(f'Hello {user}, would you like to see a status report?')
        else:
            print(f'Hello {user}, thank you for logging in again.')
else:
    print('We need to find some users!')

# 3、检查用户名　按照下面的说明编写一个程序，模拟网站如何确保每个用户的用户名都独一无二。
    # 创建一个至少包含 5 个用户名的列表，并将其命名为 current_users。
    # 再创建一个包含 5 个用户名的列表，将其命名为 new_users，并确保其中有一两个用户名也在列表 current_users 中。
    # 遍历列表 new_users，检查其中的每个用户名是否已被使用。如果是，就打印一条消息，指出需要输入别的用户名；否则，打印一条消息，指出这个用户名未被使用。
    # 确保比较时不区分大小写。换句话说，如果用户名 'John' 已被使用，应拒绝用户名 'JOHN'。（为此，需要创建列表 current_users 的副本，其中包含当前所有用户名的全小写版本。）

current_users = ['admin', 'kaer', 'alice', 'cloud', 'windy']
new_users = ['kaer', 'alice', 'snow', 'spring', 'sun']

# 创建一个小写版本的 current_users 列表      lower() 方法只能对字符串使用，不能直接将列表小写化。
current_users_lower = [user.lower() for user in current_users]

# 检查每个新用户名  
for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f'用户名{new_user}请输入别的用户名！')
    else:
        print(f'{new_user}可以使用。')

# 4、序数　序数表示顺序位置，如 1st 和 2nd。序数大多以 th 结尾，只有 1st、2nd、3rd 例外。
    # 在一个列表中存储数字 1～9。
    # 遍历这个列表。
    # 在循环中使用一个 if-elif-else 结构，打印每个数字对应的序数。输出内容应为 "1st 2nd 3rd 4th 5th 6th 7th 8th 9th"，每个序数都独占一行。
numbers = list(range(1,10)) 
for number in numbers:
    if number == 1:
        print(f'{number}st')
    elif number == 2:
        print(f'{number}nd')
    elif number == 3:
        print(f'{number}rd')
    else:
        print(f'{number}th')




