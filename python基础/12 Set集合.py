set1 = set()
#set只存不可变的值，属于可变类型。
set1 = {'ayw',185,260,54}
print(len(set1))

#添加
set1.add(234)
set1.add(234)
set1.add('world')    #无序添加
print(set1)

#删除
set1.remove('world')
print(set1)

#for循环遍历
for n in set1:
    print(n)



