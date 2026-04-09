# import my_module   # 导入模块的时候会把整个模块执行一遍。
#
# print(my_module.test(6))

# 名字冲突问题：名字相同时，调用的是后面导入的代码。
from my_module import *
from my_module2 import test as other_test

print(test(2))           # 调用 my_module 中的 test（阶乘）
print(other_test(5))     # 调用 my_module2 中的 test（使用别名避免冲突）

import sys
print(sys.path)   # 打印 python 模块库所在目录和查询顺序

import random
print(random.randint(1, 100))  # 生成 1~100 的随机整数
