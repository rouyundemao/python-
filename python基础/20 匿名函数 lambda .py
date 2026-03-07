
#使用匿名函数计算两个数字的和

# fn = lambda x, y : x + y
# print(fn(20, 4664))

# 给复杂的列表排序
lst = [
    {'name': '版本','age': '154'},
    {'name': '多少度','age': '554'},
    {'name': '阿达','age': '1564'}
]

#根据年龄来排序
# print(lst.sort())  sort 不能对比多元素列表
lst.sort(key=lambda item: int(item['age']), reverse=True)
print(lst)


