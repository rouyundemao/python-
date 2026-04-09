
class PasswordToShortError(Exception):
    '''
    自定义异常：密码太短了
    '''

    def __init__(self, length, min_len):
        self.length = length
        self.min_len = min_len

    # 打印异常对象，就会打印str函数的返回值。
    def __str__(self):
        return f'你输入的密码长度是{self.length},密码不能少于{self.min_len}个字符'

def input_password():
    pwd = input('请输入你的密码：')
    # 规定密码的长度不能少于6个字符
    if len(pwd) < 6:
        raise PasswordToShortError(len(pwd), 6)  # 第一个参数是实际长度，第二个是最小长度

if __name__ == '__main__':
    try:
        input_password()
    except PasswordToShortError as e:
        print(e)