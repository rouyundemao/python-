def test1():
    print('sun is warm')
    return 1

result = test1()
print(result)


def test2(x,y):
    x2 = x**2
    y2 = y**2
    return [x2,y2]

result = test2(5,7)
r1, r2 = test2(5,9)
print(result)
print(r1)
print(r2)
print(r1,r2)
