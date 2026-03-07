
cars = ['bmw', 'audi', 'toyota', 'subaru']

# 使用 sort() 方法对列表进行永久排序
cars.sort()
print(cars)

# 还可以按与字母顺序相反的顺序排列列表元素，只需向 sort() 方法传递参数 reverse=True 即可
cars.sort(reverse=True)
print(cars)

# 使用 sorted() 函数对列表进行临时排序
# 如果要按与字母顺序相反的顺序显示列表，也可向 sorted() 函数传递参数 reverse=True。
print('Here is the original list:')
print(cars)

print('\nHere is the sorted list:')
print(sorted(cars))       # sorted() 函数 将要处理的变量填写在括号里面。

print('\nHere is the original list:')
print(cars)

# 注意：在并非所有的值都是全小写的时，按字母顺序排列列表要复杂一些。
# 在确定排列顺序时，有多种解读大写字母的方式，此时要指定准确的排列顺序，可能会比这里所做的更加复杂。
# 然而，大多数排序方式是以本节介绍的知识为基础的。

# 反向打印列表  reverse() 方法  
cars.reverse()
print(cars)
# 注意，reverse() 不是按与字母顺序相反的顺序排列列表元素，只是反转列表元素的排列顺序
# reverse() 方法会永久地修改列表元素的排列顺序，但可随时恢复到原来的排列顺序，只需对列表再次调用 reverse() 即可。

# 确定列表的长度 len() 函数
# len() 函数可快速获悉列表的长度
print(len(cars))
# len() 函数可用于：明确还有多少个外星人未被消灭，确定需要管理多少项可视化数据，计算网站有多少注册用户，等等。
# 注意：Python 在计算列表元素数时从 1 开始，因此你在确定列表长度时应该不会遇到差一错误。

# 练习

# 1、放眼世界　想出至少 5 个你想去旅游的地方。
    # 将这些地方存储在一个列表中，并确保其中的元素不是按字母顺序排列的。
    # 按原始排列顺序打印该列表。不要考虑输出是否整洁，只管打印原始 Python 列表就好。
    # 使用 sorted() 按字母顺序打印这个列表，不要修改它。
    # 再次打印该列表，核实排列顺序未变。
    # 使用 sorted() 按与字母顺序相反的顺序打印这个列表，不要修改它。
    # 再次打印该列表，核实排列顺序未变。
    # 使用 reverse() 修改列表元素的排列顺序。打印该列表，核实排列顺序确实变了。
    # 使用 reverse() 再次修改列表元素的排列顺序。打印该列表，核实已恢复到原来的排列顺序。
    # 使用 sort() 修改该列表，使其元素按字母顺序排列。打印该列表，核实排列顺序确实变了。
    # 使用 sort() 修改该列表，使其元素按与字母顺序相反的顺序排列。打印该列表，核实排列顺序确实变了。

# scenic_spot = ['长城', '金字塔', '故宫', '布达拉宫', '滕王阁']
scenic_spot = ["Great Wall", "Pyramid", "Forbidden City", "Potala Palace", "Tengwang Pavilion"]
print(scenic_spot)
print(sorted(scenic_spot))
print(scenic_spot)
print(sorted(scenic_spot,reverse=True))
print(scenic_spot)
scenic_spot.reverse()
print(scenic_spot)
scenic_spot.reverse()
print(scenic_spot)
scenic_spot.sort()
print(scenic_spot)
scenic_spot.sort(reverse=True)
print(scenic_spot)

# 2、尝试使用各个函数　想想可存储到列表中的东西，如山川、河流、国家、城市、语言或你喜欢的任何东西。
# 编写一个程序，在其中创建一个包含这些元素的列表。然后，至少把本章介绍的每个函数都使用一次来处理这个列表。
my_like = ['星星', '太阳', '月亮', '山林', '花朵', '天空', '白云']
print(my_like[0])
print(f'小时候，在晴朗的夜晚，{my_like[-2]}中总能看到许多{my_like[0]}')
