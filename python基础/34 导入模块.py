import random   #随机生成数字的模块

# 模版 math
# 第一种
import math

# 模块名.函数（对象）
print(math.log2(16))
print(math.log(8,2))

# 第二种：from 模块名字 import *
from math import *

print(log2(8))
print(log10(100))

# 第三种：精确导入
from math import log2, log10

print(log2(8))
print(log10(100))

# 第四种
import multiprocessing as mp    # 把模块重命名为mp，以便于后续代码编写。

#第五种
from math import log2 as lg2
