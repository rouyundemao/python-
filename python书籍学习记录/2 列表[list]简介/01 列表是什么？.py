# 列表（list）由一系列按特定顺序排列的元素组成。你不仅可以创建包含字母表中所有字母、数字 0～9 或所有家庭成员姓名的列表，
# 还可以将任何东西加入列表，其中的元素之间可以没有任何关系。列表通常包含多个元素，因此给列表指定一个表示复数的名称（如 letters、digits 或 names）是个不错的主意。
# 列表非常适合用于存储在程序运行期间可能变化的数据集。列表是可以修改的，这对于处理网站的用户列表或游戏中的角色列表至关重要。

# 建立一个列表nice
nice = ['sky', 'sea', 'sun', 'moon']
print(nice)

# 访问列表元素  nice[]
print(nice[0])   # [] 中是列表中的数据的索引，从左往右从 0 开始 从右往左从 -1 开始。

# 访问列表后得到的数据也可以使用title()方法进程处理。
print(nice[0].title())   # 首字母大写

print(nice[3])
print(nice[1].upper())
print(nice[1].upper().lower())

print(nice[-1].upper().lower())
print(nice[-2].upper().lower())

# 使用列表中的值
message = f'I think the most beautiful thing is the {nice[-1].title()}.'
print(message)

# 练习
# 1、姓名　将一些朋友的姓名存储在一个列表中，并将其命名为 names。依次访问该列表的每个元素，从而将每个朋友的姓名都打印出来。
names = ['明月', '山间', '星辰', '银河', '清风', '落叶']
# print(names[0])
# print(names[1])
# print(names[2])
# print(names[3])
# print(names[4])
# print(names[5])
for name in names:
    print(name)

# 2、问候语(greeting)　继续使用练习 1 中的列表，但不打印每个朋友的姓名，而是为每人打印一条消息。每条消息都包含相同的问候语，但抬头为相应朋友的姓名。
# greeting = f'{names[0]},在否？安否？乐否？晴否？'
# print(greeting)
# greeting = f'{names[1]},在否？安否？乐否？晴否？'
# print(greeting)
# greeting = f'{names[2]},在否？安否？乐否？晴否？'
# print(greeting)
# greeting = f'{names[3]},在否？安否？乐否？晴否？'
# print(greeting)
# greeting = f'{names[4]},在否？安否？乐否？晴否？'
# print(greeting)
# greeting = f'{names[5]},在否？安否？乐否？晴否？'
# print(greeting)
for name in names:
    greeting = f'——致{name}:在否？安否？乐否？天晴否？'
    print(greeting)

# 自己的列表　想想你喜欢的通勤方式，如骑摩托车或开汽车，并创建一个包含多种通勤方式的列表。根据该列表打印一系列有关这些通勤方式的陈述，如下所示。
# I would like to own a Honda motorcycle.
commutes = ['公交', '出租车', '自行车', '地铁', '摩托车']
for way in commutes:
    print(f'我喜欢的通勤方式是：{way}。')

