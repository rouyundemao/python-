#函数要先定义后面才能调用，顺序不能乱。

def my_abs(num):
    """
    该函数，可以返回一个数字得到绝对值。
    :param num: 传入的数字，必须是一个数字，而且必传。
    :return: 返回该数字的绝对值。
    """
    if num < 0:
        return -num
    else:
        return num

#py3.5之后可以对函数参数和返回值进行类型的声明
def new_abs(num:int) -> int:
    """
该函数，可以返回一个数字得到绝对值。
:param num: 传入的数字，必须是一个数字，而且必传。
:return: 返回该数字的绝对值。
"""
    if num < 0:
        return -num
    else:
        return num
print(my_abs(-5))
# print(my_abs('shs'))

print(new_abs(-34))
# print(new_abs('sgg'))


def fib(n):  #到n斐波那契数列
    a,b = 0,1
    while a < n:
        print(a,end = " ")
        a, b = b, a+b
    print()

print(fib(15457))


def fib2(n):
    """
    返回斐波那契数列直到n。
    :param n:
    :return:
    """
    # 确保在函数内部正确初始化 result
    fib_result = []  # 这里必须初始化
    a, b = 0, 1
    while a < n:
        fib_result.append(a)
        a, b = b, a + b
    return fib_result

# 调用函数
fib_num = fib2(5456)
print(fib_num)
