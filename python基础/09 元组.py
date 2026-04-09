#元组：小括号括起来，不可修改的内容
t1 = ()
t2 = ('cwa',)          # 只有一个元素时，末尾必须加逗号，否则括号只是普通括号
t3 = 100,200,300       # 省略括号也能创建元组
t = (1,9,45,62,32,15,54,154,20,30)

# 访问元素（索引和切片与列表一致）
print(t[0])        # 第一个元素
print(t[-1])       # 最后一个元素
print(t[2:5])      # 切片

# 元组的常用操作
print(len(t))      # 元素个数
print(max(t))      # 最大值
print(min(t))      # 最小值
print(sum(t))      # 求和

# 元组不可修改（下面的操作会报错）
# t[0] = 999    # TypeError: 'tuple' object does not support item assignment

# 遍历元组
for item in t:
    print(item, end=' ')
print()

# 元组转列表（转换后可修改）
lst = list(t)
lst[0] = 999
print(lst)

# 列表转元组
new_t = tuple(lst)
print(new_t)
