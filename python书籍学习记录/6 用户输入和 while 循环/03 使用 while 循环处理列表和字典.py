# 要在遍历列表的同时修改它，可使用 while 循环。
# 通过将 while 循环与列表和字典结合起来使用，可收集、存储并组织大量的输入，供以后查看和使用。

# 在列表之间移动元素

# 首先，创建一个待验证用户列表
# 和一个用于存储已验证用户的空列表
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# 验证每个用户，直到没有未验证用户为止
# 将每个经过验证的用户都移到已验证用户列表中
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

# 显示所有的已验证用户
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

# 删除为特定值的所有列表元素 remove() 方法

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)

# 使用用户输入填充字典
# 可以使用 while 循环提示用户输入任意多的信息。

responses = {}
# 设置一个标志，指出调查是否继续
polling_active = True

while polling_active:
    # 提示输入被调查者的名字和回答
    name = input('你的名字是？')
    response = input('你喜欢的东西有哪些？')
    # 将回答存储在字典中
    responses[name] = response
    # 看看是否还有人要参与调查
    repeat = input('还有其他人回答吗？(yes/no)')
    if repeat == 'no':
        polling_active = False

# 调查结束，显示结果
print("\n--- 调查结果 ---")
for name, response in responses.items():
    print(f"{name}喜欢的东西是{response}.")


# 练习

# 1、熟食店　创建一个名为 sandwich_orders 的列表，其中包含各种三明治的名字，再创建一个名为 finished_sandwiches 的空列表。
# 遍历列表 sandwich_orders，对于其中的每种三明治，都打印一条消息，如“我给你做了金枪鱼三明治。”，并将其移到列表 finished_sandwiches 中。
# 当所有三明治都制作好后，打印一条消息，将这些三明治列出来。

sandwich_orders = ['牛奶三明治', '火腿三明治', '牛肉三明治', '鸡肉三明治', '巧克力三明治']
finished_sandwiches = []

# for sandwich_order in sandwich_orders:
#     print(f'我给你做了{sandwich_order}')

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f'我给你做了{sandwich}。')
    finished_sandwiches.append(sandwich)

print('这些三明治做好了：')
for sandwich in finished_sandwiches:
    print(sandwich)
    
# 2、五香烟熏牛肉卖完了　使用为练习 1 创建的列表 sandwich_orders，并确保 '巧克力三明治' 在其中至少出现了三次。
    # 在程序开头附近添加这样的代码：先打印一条消息，指出熟食店的巧克力卖完了；
    # 再使用一个 while 循环将列表 sandwich_orders 中的 '巧克力三明治' 都删除。确认最终的列表 finished_sandwiches 中未包含 '巧克力三明治'。

sandwich_orders = ['牛奶三明治', '巧克力三明治', '火腿三明治', '巧克力三明治','牛肉三明治', '巧克力三明治', '鸡肉三明治', '巧克力三明治']
print(f'\n{sandwich_orders}')
print('熟食店的巧克力卖完了')

while '巧克力三明治' in sandwich_orders:
    sandwich_orders.remove('巧克力三明治')
print(f'现在的三明治还有：{sandwich_orders}')

# 3、梦想中的度假胜地　编写一个程序，调查用户梦想中的度假胜地。使用类似于“如果你可以去世界上的一个地方，你会去哪里？”的提示，并编写一个打印调查结果的代码块。

prompt = '如果你可以去世界上的一个地方，你会去哪里？'

mess = {}
active = True

while active:
    name = input('\n你的名字是？')
    response = input(prompt)
    mess[name] = response
    while True:
        # strip() 方法可以删除用户输入的空白，lower() 方法可以让用户输入的英文全部变为小写，用户可以不用考虑大小写。
        oth = input('还有人要回答吗？(yes/no)').strip().lower()
        if oth == 'yes':
            break
        elif oth == 'no':
            active = False
            break
        else:
            print('请输入(yes/no)')

print(f"{'----'*15}调查结果{'-----'*15}")
for name, response in mess.items():
    print(f'{name}想去的地方是{response}。')

while True:
    s = input("输入 quit 退出：")
    if s == 'quit':
        break
    print("你输入了：", s)

i = 0
while i < 3:
    print(i)
    i += 1
else:
    print("循环自然结束（条件为 False）")
