# 函数定义中可能包含多个形参，因此函数调用中也可能包含多个实参。
# 向函数传递实参的方式很多：既可以使用位置实参，这要求实参的顺序与形参的顺序相同；也可以使用关键字实参，其中每个实参都由变量名和值组成；还可以使用列表和字典。

# 位置实参
# 在调用函数时，Python 必须将函数调用中的每个实参关联到函数定义中的一个形参。最简单的方式是基于实参的顺序进行关联。以这种方式关联的实参称为位置实参。

def describe_prt(animal_type, pet_name):
    """ 显示动物信息 """
    print(f'我有一只{animal_type}，我真的很喜欢它！')
    print(f'我的{animal_type}的名字叫{pet_name}。')

# 按照形参顺序提供实参
describe_prt('猫', '小灰') 

    # 调用函数多次
describe_prt('狗', '蛋黄')
# 在函数中，可根据需要使用任意数量的位置实参，Python 将按顺序将函数调用中的实参关联到函数定义中相应的形参。
    # 位置实参的顺序很重要，如果调用时输入实参反了，会造成很大的歧义。
    
# 关键字实参
# 关键字实参是传递给函数的名值对。
# 这样会直接在实参中将名称和值关联起来，因此向函数传递实参时就不会混淆了。
# 关键字实参不仅让你无须考虑函数调用中的实参顺序，而且清楚地指出了函数调用中各个值的用途。

# 关键字实参的顺序无关紧要，因为 Python 知道各个值该被赋给哪个形参。
describe_prt(animal_type= '猫', pet_name= '小节')
describe_prt(pet_name= '小节', animal_type= '猫')
# 注意：在使用关键字实参时，务必准确地指定函数定义中的形参名。

# 默认值
# 在编写函数时，可以给每个形参指定默认值。
# 如果在调用函数中给形参提供了实参，Python 将使用指定的实参值；否则，将使用形参的默认值。
# 因此，给形参指定默认值后，可在函数调用中省略相应的实参。使用默认值不仅能简化函数调用，还能清楚地指出函数的典型用法。

# Python 依然将这个实参视为位置实参，如果函数调用只包含宠物的名字，这个实参将被关联到函数定义中的第一个形参。
# 注意：当使用默认值时，必须在形参列表中先列出没有默认值的形参，再列出有默认值的形参。这让 Python 依然能够正确地解读位置实参。
def describe_prt(pet_name, animal_type = '狗'):
    """ 显示动物信息 """
    print(f'我有一只{animal_type}，我真的很喜欢它！')
    print(f'我的{animal_type}的名字叫{pet_name}。')

describe_prt('阿达')
describe_prt('阿喜', '猫')

# 等效的函数调用
def describe_pet(pet_name, animal_type='狗'):
    """ 显示动物信息 """
    print(f'我有一只{animal_type}，我真的很喜欢它！')
    print(f'我的{animal_type}的名字叫{pet_name}。')

    # 一条名为 Willie 的小狗
describe_pet('willie')
describe_pet(pet_name='willie')

    # 一只名为 Harry 的仓鼠
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')
    # 使用哪种调用方式无关紧要。可以使用对你来说最容易理解的调用方式，只要函数调用能生成你期望的输出就好。  


# 练习

# 1、T 恤　编写一个名为 make_shirt() 的函数，它接受一个尺码以及要印到 T 恤上的字样。这个函数应该打印一个句子，简要地说明 T 恤的尺码和字样。
    # 先使用位置实参调用这个函数来制作一件 T 恤，再使用关键字实参来调用这个函数。
def make_shirt(size, word):
    print(f'\nT恤的尺码是{size}。')
    print(f'要印上去的字样是{word}。')

# 位置实参
make_shirt(45, 'Love')
# 关键字实参
make_shirt(word='Alice, I love you.', size= 44)

# 2、大号 T 恤　修改 make_shirt() 函数，使其在默认情况下制作一件印有
    # “I love world!”字样的大号 T 恤。调用这个函数分别制作一件印有默认字样的大号 T 恤，一件印有默认字样的中号 T 恤，以及一件印有其他字样的 T 恤（尺码无关紧要）。
def make_shirt(size, word = 'I love world!'):
    print(f'\nT恤的尺码是{size}。')
    print(f'要印上去的字样是{word}。')

make_shirt('大号') 
make_shirt('大号', '杰卡斯') 

# 3、城市　编写一个名为 describe_city() 的函数，它接受一座城市的名字以及该城市所属的国家。这个函数应该打印一个像下面这样简单的句子。
    # Reykjavik is in Iceland.    雷克雅未克在冰岛。
    # 给用于存储国家的形参指定默认值。为三座不同的城市调用这个函数，其中至少有一座城市不属于默认的国家。

def describe_city(city_name, city_country = 'china'):
    """ 显示城市信息 """
    print(f'\n{city_name.title()} is in {city_country.title()}.')

describe_city('beijing')
describe_city('shanghai')
describe_city('New York', 'America')


