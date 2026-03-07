import random #导入random模块
print('-'*50)
print("欢迎来到 sunny 的《猜字游戏》")
print("规则一：系统每次会自动生成一个1~10之间的随机数")
print("规则二：每次游戏最多只能猜3次")
print("规则三：进入游戏或者继续玩，输入：yes或者y")
print("规则四：离开游戏：输入：no或者n")
print('-'*50)

# 定义一个记录游戏次数的变量
n = 0
while True:
    order = input('请输入是否开始游戏：')
    if order == 'yes' or order == 'y':  # 用户想玩游戏
        n += 1
        print(f'正式开始第{n}次游戏')
        number = random.randint(1,10)#生成一个随机数
        for i in range(1,4):  #用户最多可以猜3次
            my_num = int(input('请玩家输入所猜的数字：'))
            if my_num == number:
              print(f'恭喜你！猜中了，答案就是{my_num}。')
              break
            elif my_num > number:
                print(f'你猜的数字太大了，还剩下{3-i}次')
            else:
                print(f'你猜的数字太小了，还剩下{3-i}次')
        else:  #三次都猜错了
            print(f'你三次都猜错了，正确答案是{number}')
    elif order == 'no' or order == 'n': #用户不想玩游戏
        print('谢谢，游戏结束！')
        break
    else:
        print("请输入正确的语句")



