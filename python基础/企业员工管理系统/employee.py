
class Employee(object):
    """员工类"""
    # is_leave=0 表示在职，1表示离职
    def __init__(self, name, gender, age, mobile_number, is_leave=0):
        self.name = name
        self.gender = gender
        self.age = age
        self.mobile_number = mobile_number
        self.is_leave = False if is_leave==0 else True     # is_leave=True表示离职，否则就是在职。

    def __str__(self):
        msg = '离职' if self.is_leave else '在职'
        return f'{self.name}\t{self.gender}\t{self.age}\t{self.mobile_number}\t{msg}'

if __name__ == '__main__':
    e = Employee('尚书', '男', 45, '465464648', 0)
    print(e.__dict__)    # 第一种：把python对象转换成字典。
    print(vars(e))       # 第二种：把python对象转换成字典。
    # e.is_leave = 1
    print(e)