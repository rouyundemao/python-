#描述一台汽车

class Car():

    # self： 代表当前对象就是实例本身
    def __init__(self, brand, type_name, category):
        print('开始初始化Car对象')
        # brand, type_name, category都是对象属性（成员属性）
        #汽车的品牌
        self.brand = brand
        #汽车的型号
        self.type_name = type_name
        #汽车的类型
        self.category = category

    def run(self): # run函数是车的行为,对象函数（成员函数）
        print(f'{self.brand}-{self.type_name}-{self.category}')
        print('开起来，飞起来')


    def __new__(cls, *args, **kwargs):
        print('创建Car的对象')
        return super().__new__(cls)


    def __str__(self):
        '''
        str魔法函数： 以后只要有print（对象），则会自动调用str函数，并且打印str函数的返回值
        :return: 自己定义
        '''
        return f'汽车的品牌是：{self.brand}， 型号是：{self.type_name}， 汽车的类别是{self.category}'

    def __del__(self):
        print('开始删除对象')

#创建类的对象
c1 = Car('BYD','汉','中型轿车')
print(c1)
# del c1    # 调用del删除c1
print(c1.brand)  # 访问对象c1的属性
c1.run()  #调用对象的函数
c2 = Car('一汽大众','迈腾','中型轿车')
c2.run()

