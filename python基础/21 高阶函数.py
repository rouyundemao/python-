
#对任意两个数字整理之后再求和

def sum_num(a,b):
    return abs(a) + abs(b)

#高阶函数的实现

def sum_num2(a,b,f):
    '''
    对任意两个数字整理之后再求和
    :param a:
    :param b:
    :param f: 就是对两个数字进行整理的函数
    :return:
    '''
    return f(a) + f(b)
# abs() 绝对值 之后求和
print(sum_num2(2,6,abs))

# 通过平方整理之后再求和
print(sum_num2(6, 5, lambda n: n ** 2))

#第二种高阶函数
def test3(*args):
    def sum_nums():
        sum = 0
        for n in args:
            sum += n
        return sum
    return sum_nums

#打印函数
print(test3(3, 184, 11,))
#加（）打印返回值，即计算结果
print(test3(3, 184, 11, )())



