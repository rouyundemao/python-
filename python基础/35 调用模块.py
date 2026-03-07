# import my_module   # 导入模块的时候会把整个模块执行一遍。
#
# print(my_module.test(6))

# 名字冲突问题,名字相同时，调用的是后面导入的代码。
from my_module import *
from my_module2 import test as other_test

print(test(2))

import sys
print(sys.path)   # 打印 python模块库所在目录和查询顺序

import random
