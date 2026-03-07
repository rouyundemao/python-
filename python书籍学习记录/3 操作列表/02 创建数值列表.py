
# 使用 range() 函数

for value in range(1,6):        # 不会打印6， 这是编程语言中常见的差一行为的结果。
    print(value)

# 在调用 range() 函数时，也可只指定一个参数，这样它将从 0 开始，例如，range(6) 返回数 0～5（含）。   range 函数是从 0 开始计数的，所以才会在使用 range(1,6) 只打印1-5.
for i in range(6):
    print(i)

# 使用 range() 创建数值列表   list(range()) 表达式
# 要创建数值列表，可使用 list() 函数将 range() 的结果直接转换为列表。如果将 range() 作为 list() 的参数，输出将是一个数值列表。
numbers = list(range(1,6))
print(numbers)

# 在使用 range() 函数时，还可指定步长。为此，可以给这个函数指定第三个参数，Python 将根据这个步长来生成数。
even_numbers = list(range(3,19,3))
print(even_numbers)

# 如何创建一个列表，其中包含前 10 个整数（1～10）的平方呢？在 Python 中，用两个星号（**）表示乘方运算。
squares = []        # 创建一个空列表
for value in range(1,11):
    square = value ** 2
    squares.append(square)   # 使用append()方法将square添加到squares列表末尾。
print(squares)

# 更简洁，不使用square变量
squares = []
for value in range(1,11):
    squares.append(value**2)
print(squares)

# 对数值列表执行简单的统计计算
# 找出数值列表中的最大值、最小值和总和
print(min(squares))   # 最小值
print(max(squares))   # 最大值
print(sum(squares))   # 总和   
# 注意：这里介绍的知识也适用于包含数百万个数的列表。

# 列表推导式 （list comprehension）
# 列表推导式将 for 循环和创建新元素的代码合并成一行，并自动追加新元素。

squares = [value**2 for value in range(1,11)]
print(squares)
# 表达式为 value**2，它计算平方值。接下来，编写一个 for 循环，用于给表达式提供值，再加上右方括号。在这个示例中，for 循环为 for value in range(1,11)，它将值 1～10 提供给表达式 value**2。

# 练习

# 1、数到 20　使用一个 for 循环打印数 1～20（含）。
for number in range(1,21):
    print(number)

# 2、100 万　创建一个包含数 1～1 000 000 的列表，再使用一个 for 循环将这些数打印出来。（如果输出的时间太长，按 Ctrl + C 停止输出，或关闭输出窗口。）

# num_list = []
# for num in range(1,1000001):
#     num_list.append(num)
# print(num_list)

num_list = list(range(1,1000001))       # list(range())  创建数字列表更简洁。
# print(num_list)    打印全部会增加负荷。
print(f'前五个数是：{num_list[:5]}')
print(f'后五个数是：{num_list[-5:]}')

# 3、100 万求和　创建一个包含数 1～1 000 000 的列表，再使用 min() 和 max() 核实该列表确实是从 1 开始、到 1 000 000 结束的。另外，对这个列表调用函数 sum()，看看 Python 将 100 万个数相加需要多长时间。

print(min(num_list))
print(max(num_list))
print(sum(num_list))

# 4、奇数　通过给 range() 函数指定第三个参数来创建一个列表，其中包含 1～20 的奇数(odd number)；再使用一个 for 循环将这些数打印出来。

for odd_number in range(1,21,2):
    print(odd_number)

# 5、3 的倍数　创建一个列表，其中包含 3～30 内能被 3 整除的数，再使用一个 for 循环将这个列表中的数打印出来。

# 法一
threes = [num for num in range(3,31) if num % 3 == 0]
print(threes)
for num in threes:
    print(num)

# 法二
threes = []
for num in range(3,31):
    if num % 3 == 0:
        threes.append(num)
for num in threes:
    print(num)

# 6、立方　将同一个数乘三次称为立方。例如，在 Python 中，2 的立方用 2**3 表示。创建一个列表，其中包含前 10 个整数（1～10）的立方，再使用一个 for 循环将这些立方数打印出来。

num_li = [value**3 for value in range(1,11)]
for num in num_li:
    print(num)

# 7、立方推导式　使用列表推导式生成一个列表，其中包含前 10 个整数的立方。
num_li = [value**3 for value in range(1,11)]
print(num_li)


