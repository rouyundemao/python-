#创建字典
from types import new_class

dict2 = {}   #空字典
dict1 = {'name':'sunny','age':21}  #冒号前面为键（key），后面为值（value）,key是唯一的
dict3 = dict([('name','hs'),('age',23)])
dict4 = dict(name='sunny',age=21,city='xingyi')

#新增和修改
dict1['address'] = '贵州'
# dict1['age'] = 23
print(dict1)

#删除
# dict1.clear() #清空所有项
# dict1.pop('address') #指定删除
# del dict1['age']

#查询
if 'age' in dict1:
    print(dict1['age'])

#字典中的函数
# new_dict = dict.fromkeys(['name','age','city','address'])
# new_dict['name'] = '克斯'
# print(new_dict)

print(dict1['address'])
print(dict1.get('address'))
print(dict1)

#字典的遍历
#items把所有的项放到一个列表中
for k,v in dict1.items():
    print(f'键={k},值={v}')
    # print(k,v)

for k in dict1.keys():
    print(k)
for v in dict1.values():
    print(v)
