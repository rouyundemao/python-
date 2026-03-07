#1、数学运算符

s1 = 'scg'+'sah'
print(s1)
lst = [233]
# lst1 = lst + [1,14,24,555]
lst += lst + [1,14,24,555]

print(lst)

print('-'*65)
print([2,3]*19)

# lst *= 35

lst1 = [5,6,8]
lst2 = [3,5,9]
print(lst1 >lst2)


#成员判断
t1 = (100,200)
print(10 in t1)
print(10 not in t1)
print(100 in t1)

print(len(t1)) #值数量
print(len(lst))

#内置函数
print(max(t1))
print(min(t1))
print(sum(t1))

print(max('hello')) #o的顺序靠后值大
print(min('hello')) #e的顺序靠前值小
