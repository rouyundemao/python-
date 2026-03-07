# Python 将不能修改的值称为不可变的，而不可变的列表称为元组（tuple）。

# 定义元组
# 元组看起来很像列表，但使用圆括号而不是方括号来标识。定义元组后，就可使用索引来访问其元素，就像访问列表元素一样。
# 相比于列表，元组是更简单的数据结构。如果需要存储一组在程序的整个生命周期内都不变的值，就可以使用元组。

dimensions = (500,200)
print(dimensions[1])
# 元组不可以修改
# 注意：严格地说，元组是由逗号标识的，圆括号只是让元组看起来更整洁、更清晰。如果你要定义只包含一个元素的元组，必须在这个元素后面加上逗号：
num =(1,)

# 遍历元组中的所有值
# 像列表一样，也可以使用 for 循环来遍历元组中的所有值
for dimension in dimensions:
    print(dimension)

# 修改元组变量
# 虽然不能修改元组的元素，但可以给表示元组的变量赋值。
print("\nOriginal dimensions:")
for dimension in dimensions:
    print(dimension)
    
dimensions = (400, 100)      # 元组变量可以重新赋值。
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)

# 练习

# 自助餐　有一家自助式餐馆，只提供 5 种简单的食品。请想出 5 种简单的食品，并将其存储在一个元组中。
    # 使用一个 for 循环将该餐馆提供的 5 种食品都打印出来。
    # 尝试修改其中的一个元素，核实 Python 确实会拒绝你这样做。
    # 餐馆调整菜单，替换了两种食品。请编写一行给元组变量赋值的代码，并使用一个 for 循环将新元组的每个元素都打印出来。

print('\n这是初始的菜单：')
foods = ('鸡腿', '豆腐干', '五花肉', '生菜', '折耳根')

for food in foods:
    print(food)

# foods[0] = '火腿肠'

print('\n这是修改后的菜单：')
foods = ('鸡腿', '洋芋片', '五花肉', '火腿肠', '折耳根')

for food in foods:
    print(food)
