s1 = 'hello'
s2 = "hello"
s3 = """hello
world"""
s4 = '''hello'''

s5 = 'hello\nworld'# “\n” 换行符

s6 = 'I\'m Tom'

s7 = '我是\"贵州\"人' #\转义符

# 索引：正索引：0开始，从左向右；负索引：-1开始，从右到左。定位为：变量[序号]
print(s1[1])
print(s1[-4])
print(s5[8])
print(s7[3])
print(s7[2])

#切片

s = 'abcdefghijklmn'
print(s[2:6]) #[]不含最后的一个索引。
print(s[2:6:1])
print(s[-12:-8])
print(s[:6])
print(s[-6:])
print(s[6:])

# 字符串的倒序
print(s[::-1])

#字符串的函数
xx = 'hellopythonword'
print(xx.find('python'))

#查找字符串位置；判断是否有所查找目标
print(xx.find('thon'))
print(xx.index('thon'))

# 字符串切割
ss = 'I am a student'
print(ss.split(' ')) #split以空格来切割“ss”,分隔符不会出现在结果中
print(ss.partition(' '))  #分区，分隔符单独一个区

# 字符串替换
print(ss.replace('student', 'worker'))






