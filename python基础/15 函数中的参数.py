
#形参
def test1(a,x,y):  #x，y为位置参数
     return x + y + a

result = test1(40,54,47) #固定传参
print(result)

print(test1(y=125, x=48746,a=134)) #关键字传参

print(test1(2, y=10,x=224))

#默认值参数

def test2(x,y,init_sum=10): #init_sum设置了一个用于运算的默认值
    init_sum += x + y
    return init_sum


print(test2(10, 20,2000))


#不定长传参
#1.普通参数
def test3(*args,init_sum=10):
    print(type(args))
    if args:
        return init_sum + sum(args)
        # for i in args:
        #     init_sum += i
    return init_sum

print(test3())
print(test3(1,22,44))
print(test3(1,22,44,init_sum=15555))

#2.关键字参数
def test4(init_sum=10, **kwargs,):
    print(type(kwargs))
    for k,v in kwargs.items():
        print(f'参数的名字{k},参数的值{v}')

    return init_sum + sum(kwargs.values())

print(test4(x=10, y=3355, z=1111))

#注意：位置参数在前---》默认传参---》不定长普通参数---》不定长关键字参数

# def test5(a,b,c,**args,):