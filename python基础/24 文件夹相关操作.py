import os

print(os.getcwd())    # 当前工作目录

print(os.listdir(r'D:\sunny_code'))   # 获取目录下所有文件名

print(os.path.abspath('text3.txt'))   # 查询文件绝对路径

print(os.path.split(r'D:\sunny_code\sunny_python\text3.txt'))

print(os.path.splitext(r'D:\sunny_code\sunny_python\text3.txt'))   #分离文件扩展名

print(os.path.getsize('test3.txt'))
