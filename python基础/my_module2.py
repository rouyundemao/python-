
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
    print('my_module2中的test函数')