lst = [12,'sds',12,12,6.26,[1,5,4]]

lst[1] = 'dfw'#通过索引修改sds为dfw
#查找
print(lst.index(12))#12的第一个位置
print(lst.count(12))#12在列表中出现的次数
print(len(lst)) #列表元素个数

#添加
lst.append('world')  #整体添加到列表结尾
# lst.extend('python')  #将字符串分开，添加到最后
lst.insert(0,123)
lst.insert(5,'kiss')  #指定下标插入数据

print(lst)
#删除
# print(lst.pop(2)) #删除指定下标的值
# del lst[2]
lst.remove('kiss')  #删除指定内容的值，删除从左到右的第一个值

#顺序修改
# print(lst[::-1])#逆序
lst.reverse()#逆序
print(lst)

lst1 = [2,41,5784,45,45,67,11,74]
# lst1.sort()  #升序
lst1.sort(reverse=True)  #逆序
print(lst1)

#遍历每一位值
for i in lst:
    print(i)
