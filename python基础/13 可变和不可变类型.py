#字符串为不可变类型
s1 = 'sweet'
print(id(s1))
s1 = 'sga'
print(id(s1))


#列表（list）为可变类型
lst = [100,511,6478,2515]
print(id(lst))

lst.append(154)
lst.pop(0)
print(id(lst))
