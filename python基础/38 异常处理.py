import traceback

# svd = 30 / 0

# '23' + 46

# 捕获异常

f = None   # 提前声明，避免 finally 中出现 NameError
try:
    f = open('afc.txt')
    s = f.readline()
    num = int(s.strip())
    print(num)
except FileNotFoundError:
    print(traceback.format_exc())
    print('文件不存在')
except ValueError:
    print(traceback.format_exc())
    print('值不对，不能转换')
except Exception as e:     # Exception所有异常的父类
    print(traceback.format_exc())
else:
    print('没有异常')
finally:
    if f:
        print('不管有没有异常都会执行')
        f.close()

print('程序完成')
