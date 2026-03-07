
#一、map函数
print(list(map(lambda n: n ** 2, [1, 2, 3, 4, 5, 6, 7])))

#二、reduce函数
from functools import *

print(reduce(lambda x, y: x + y, [2, 4, 6, 8, 10, 12, 14],50))

#案例： 统计长字符串中每个单词出现的次数

str1 = 'hello world good student child java python good hello good student good world'

#1.切开单词
# lst = str1.split(' ')
# print(lst)

#2.单词只要出现，记为一次。
#['hello':, 'world':, 'good':...]
# new_lst = list(map(lambda item: {item:1},lst))
# print(new_lst)

#3.调用reduce实现同词叠加

def func(dict1,dict2):
 #dict1: 作为叠加的返回字典
    key = list(*dict2.items())[0][0] #得到dict2中的key（单词：world）
    value = list(dict2.items())[0][1]  #得到dict2中的value （数字：1）
    dict1[key] = dict1.get(key,0) + value
    return dict1

print(reduce(func, list(map(lambda item: {item:1},str1.split(' ')))))

#三、filter函数

lst1 = [1,2,3,4,5,6,7,8,9,10,1234,45,34,45]
#偶数留下
print(list(filter(lambda n: n % 2 == 0, lst1)))

#四、sorted函数
lst = [
    {'name': '版本','age': '154'},
    {'name': '多少度','age': '554'},
    {'name': '阿达','age': '1564'}
]

#根据年龄来排序
#lst.sort
print(sorted(lst, key=lambda item:int(item['age']), reverse=True))

str_lst =['花洒','收到回复','sdh','sdg','天下']
print(sorted(str_lst))   #英文大小写变换  str.upper->大写 str.lower->小写

