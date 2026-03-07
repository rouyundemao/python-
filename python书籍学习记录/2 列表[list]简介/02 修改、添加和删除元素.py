
names = ['明月', '山间', '星辰', '银河', '清风', '落叶']
print(names)

# 利用索引直接修改列表中的某个元素。
names[0] = '暗月'
print(names)

# 在列表中添加元素 追加（append）
names.append('山花')
print(names)

world = []
world.append('你')
print(world)
world.append('我')
world.append('ta')
print(world)

# 在列表中插入元素 插入：insert()方法

# 需要指定新元素的索引和值
print(repr(world))
world.insert(1, '山川')
print(world)

# 从列表中删除元素 del()方法

del world[1]
print(world)
# 使用 del 语句将值从列表中删除后，就无法再访问它了

# 使用 pop() 方法删除元素

# pop() 方法删除列表末尾的元素，并让你能够接着使用它。术语弹出（pop）源自这样的类比：列表就像一个栈，而删除列表末尾的元素相当于弹出栈顶元素。
popped_world = world.pop()
print(world)
print(popped_world)
# pop() 方法用来取出最后一次的元素记录。

# 删除列表中任意位置的元素  pop(位置索引)

# 也可以使用 pop() 删除列表中任意位置的元素，只需要在括号中指定要删除的元素的索引即可。
motorcycles = ['honda', 'yamaha', 'suzuki']

first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")

# 该使用 del 语句还是 pop() 方法，下面是一个简单的判断标准：
# 如果要从列表中删除一个元素，且不再以任何方式使用它，就使用 del 语句；如果要在删除元素后继续使用它，就使用 pop() 方法。

# 根据值删除元素 remove()
# 如果只知道要删除的元素的值，可使用 remove() 方法。
motorcycles.append('ducati')
print(motorcycles)
motorcycles.remove('ducati')    #使用 remove() 从列表中删除元素后，也可继续使用它的值。
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")
# 注意：remove() 方法只删除第一个指定的值。如果要删除的值可能在列表中出现多次，就需要使用循环，确保将每个值都删除。

# 练习

# 1、嘉宾名单　如果你可以邀请任何人一起共进晚餐（无论是在世的还是故去的），你会邀请哪些人？请创建一个列表，其中包含至少三个你想邀请的人，然后使用这个列表打印消息，邀请这些人都来与你共进晚餐。
my_friends = ['天空', '大海', '森林', '雪山']
for i in my_friends:
    message = f'\n{i}，不知是否有幸与你共进晚餐？'
    print(message)

# 2、修改嘉宾名单　你刚得知有位嘉宾无法赴约，因此需要另外邀请一位嘉宾。
    # 以完成练习 1 时编写的程序为基础，在程序末尾添加函数调用 print()，指出哪位嘉宾无法赴约。
    # 修改嘉宾名单，将无法赴约的嘉宾的姓名替换为新邀请的嘉宾的姓名。
    # 再次打印一系列消息，向名单中的每位嘉宾发出邀请。

print(f'\n{my_friends[-1]}无法赴约。')

my_friends[-1] = '江流'

for x in my_friends:
    message = f'\n{x}:不知是否有幸与你共进晚餐。'
    print(message)
    
# 3、添加嘉宾　你刚找到了一张更大的餐桌，可容纳更多的嘉宾就座。请想想你还想邀请哪三位嘉宾。
    # 以完成练习 1 或练习 2 时编写的程序为基础，在程序末尾添加函数调用 print()，指出你找到了一张更大的餐桌。
    # 使用 insert() 将一位新嘉宾添加到名单开头。
    # 使用 insert() 将另一位新嘉宾添加到名单中间。
    # 使用 append() 将最后一位新嘉宾添加到名单末尾。 

print('\n我刚找到了一张更大的餐桌，可以邀请更多的嘉宾啦！')
new_friends = ['天空', '大海', '森林', '雪山']

new_friends.insert(0, '星星')
new_friends.insert(2, '玫瑰')
new_friends.append('小鸟')

# len() 方法可以获取列表、字符串或其他容器的长度。
print(len(new_friends))

print(f'\n新的嘉宾名单是：{new_friends}')

for x in new_friends:
    message = f'\n{x}:不知是否有幸与你共进晚餐。'
    print(message)

# 4、缩短名单　你刚得知新购买的餐桌无法及时送达，因此只能邀请两位嘉宾。
# 以完成练习 3 时编写的程序为基础，在程序末尾添加一行代码，打印一条你只能邀请两位嘉宾共进晚餐的消息。
    # 使用 pop() 不断地删除名单中的嘉宾，直到只有两位嘉宾为止。每次从名单中弹出一位嘉宾时，都打印一条消息，让该嘉宾知道你很抱歉，无法邀请他来共进晚餐。
    # 对于余下两位嘉宾中的每一位，都打印一条消息，指出他依然在受邀之列。
    # 使用 del 将最后两位嘉宾从名单中删除，让名单变成空的。打印该名单，核实名单在程序结束时确实是空的。

print('\n很遗憾，新购买的餐桌无法及时送达，因此只能邀请两位嘉宾共进晚餐。')

# 不断删除嘉宾直到只剩两位
while len(new_friends) > 2:                 # 利用 while 循环语句将列表元素删至两个。   当条件为真（True）时，不断重复执行下面的代码块。      
    remove_guest = new_friends.pop()        
    print(f'很抱歉，{remove_guest}，餐位有限，无法邀请你来共进晚餐。')

for guest in new_friends:
    print(f'{guest}，你依然在受邀名单中，期待与你共进晚餐！')

del new_friends[:]

print(new_friends)

# 晚餐嘉宾　选择你为完成练习 1～练习 4 而编写的一个程序，在其中使用 len() 打印一条消息，指出你邀请了多少位嘉宾来共进晚餐。
n = len(my_friends)
print(f'我邀请了{n}位嘉宾来共进晚餐。')

