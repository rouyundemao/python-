#1、计算1~100的所有奇数和
my_sum = 0

# for n in range(1,100,2): #range函数不取最后的数，100
#     my_sum += n

# 第二种写法
# for n in range(1,100):
#     if n % 2 != 0:
#         my_sum += n

# 第三种写法
# n = 0
# while True:
#     n += 1
#     if n > 100:#超出循环范围，则退出。
#         break
#     if n % 2 != 0:
#         my_sum += n

# 第四种：
# for n in range(1,100):
#     if n % 2 ==0:  #此时n为偶数，不做计算，退出此次循环，继续下一个数字。
#         continue
#     my_sum += n
#
#
# print(f'结果是{my_sum}')


# 99 乘法表
#第一种
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(f'{j}*{i}={j*i}', end='\t')
#     print()
# 第二种
i = 1
while i <= 9: #代表行数：9
    j = 1
    while True:
        if j > i : #内层循环结束
            break
        # 把当前的所有算式输出
        print(f'{j}*{i}={j*i}', end='\t')
        j += 1
    i += 1
    print()
