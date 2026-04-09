import os

print(os.getcwd())    # 当前工作目录

# os.listdir() 获取目录下所有文件名（路径需要修改为实际存在的目录）
print(os.listdir('.'))   # 列出当前目录下所有文件

print(os.path.abspath('test3.txt'))   # 查询文件绝对路径

# os.path.split() 将路径拆分为目录和文件名两部分
# Windows 示例（在 Windows 上才能正常运行）：
# print(os.path.split(r'D:\sunny_code\sunny_python\text3.txt'))
# Linux / macOS 示例：
print(os.path.split('/home/user/python-/test3.txt'))

# os.path.splitext() 分离文件名和扩展名
print(os.path.splitext('/home/user/python-/test3.txt'))   # ('.../test3', '.txt')

# os.path.getsize() 获取文件大小（字节数）
if os.path.exists('test3.txt'):
    print(os.path.getsize('test3.txt'))
else:
    print('test3.txt 不存在，跳过 getsize')

# 其他常用操作
print(os.path.isfile('test3.txt'))      # 是否是文件
print(os.path.isdir('.'))               # 是否是目录
print(os.path.exists('test3.txt'))      # 文件/目录是否存在
print(os.path.join('/home', 'user', 'python-'))   # 路径拼接（跨平台安全）
