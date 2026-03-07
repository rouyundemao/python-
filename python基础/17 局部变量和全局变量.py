a = 347  # 全局变量
def tset1():
    b = 100  #局部变量
    print(a)
    return b ** 3,a ** 5

print(tset1())
# print(b)  #局部变量b在函数外不能使用


def test2():
    global a   #  函数内部，使用global声明a 为全局变量。
    a = 3244   #  对全局变量a 进行修改。
    print(a,end =" ")
    return "值"  # 函数运行结束。

print(test2())
print(a)