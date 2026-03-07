#1、计算1~100的所有奇数和

my_sum = 0
n = 1
while 1<= n <= 100:
    if n % 2 != 0:
        my_sum += n
    n += 1
print(f'结果是：{my_sum}')


# 输出 99 乘法表
# 99 乘法表有：9行

i = 1
while i <= 9: #代表行数：9
    j = 1
    while j <= i:
        # 把当前的所有算式输出
        print(f'{j}*{i}={j*i}', end='\t')
        j += 1
    i += 1
    print()
