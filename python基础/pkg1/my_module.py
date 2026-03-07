
__all__ = ['my_sum','test']  # 声明当前模块只能公开[]中的函数

def my_sum(n):
    '''
    计算从0到n的数字之和
    :param n: 正整数
    :return:
    '''
    s = 0
    for i in range(n):
        s += i
    return s

def test(n: int) -> int:
    '''
    计算一个数字n的阶乘
    :param n:
    :return:
    '''

    if n == 1:
        return 1  #递归函数退出的出口。
    return n * test(n-1)    # n不是1时执行。

# 这样测是有瑕疵的，如果不删，再次调用此模块时会出现打印下面这些代码的错误。
# print(my_sum(45))
# print(test(5))

if __name__ == '__main__':    # 如果当前的py文件就是执行的入口（运行代码的窗口），执行下面的代码。
    print(my_sum(45))
    print(test(5))