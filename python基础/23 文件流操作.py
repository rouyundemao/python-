
#1. 创建（打开）文件流
#文件对象 = open（目标文件，访问模式：r,rb,r+,rb+,wb,w+,wb+,a,ab）
f = open('test.txt', mode = 'r', encoding='utf-8')

#2.读操作
# print(f.read())
print(f.readline())  # 读一行 加s全读
#3.关闭文件流
f.close()

#3.写操作（创建文件：test2.txt）

wf = open('test2.txt', 'w', encoding='utf-8')

#往文件中写入3个hello
for i in range(12):
    print(f'当前指针的位置{wf.tell()}')
    wf.write('sunny\n')

wf.close()

#4. 指针的移动操作
#在第一个词后面加一个：world
wf = open('test2.txt', 'r+', encoding='utf-8')   #  在指定位置写入数据会造成覆盖。
# 把指针移动第一个词后面
wf.seek(5,0)
# 把第一个词（sunny）后面的内容先读出来。
after = wf.read()   #读完后，指针到了文件末尾
# 把指针移动第一个词后面
wf.seek(5,0)
wf.write(' world'+after)
wf.close()


# with语句操作文件流
with open ('test3.txt', 'w+', encoding='utf-8') as f:
    for i in range(10):
        f.write('cloud\n')




