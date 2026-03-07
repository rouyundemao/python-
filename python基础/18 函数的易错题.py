
def test(a, lst1 = [1, 2, 5]):   #定义一个函数
    #把a添加到列表中
    if a not in lst1:
        lst1.append(a)
    return lst1


print(test(12))    # 在lst1中添加了12
print(test(30))    # 再次添加30
print(test(464,lst1 = [654,1115,1111]))    # 改变lst1列表引用，即里面的值,这里的lst1为临时的值

lst = [1,2]
print(lst)
print(id(lst))
lst = [5,9,4]
print(lst)
print(id(lst))
