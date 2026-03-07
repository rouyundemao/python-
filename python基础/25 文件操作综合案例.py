import os

# 拷贝文件目录下的py文件

def copy_dir(source_dir, destination_dir):
    '''
    拷贝source_dir目录中的所有py文件到另一个目录destination_dir中
    :param source_dir:  原始目录
    :param destination_dir:  目标目录
    :return:  返回总拷贝文件数量
    '''
    count = 0
    sum
    for f in os.listdir(source_dir):  # 其中的f代表目录下的每一个文件（目录）名字
        # 把文件名和目录拼凑成一个绝对路径
        f_path = os.path.join(source_dir, f)
        if os.path.isfile(f_path) and f.endswith('.py'):  #  表示f是一个普通文件,并且也是py文件
            # 要拷贝该文件
            if not os.path.exists(destination_dir):
                os.makedirs(destination_dir)
            #拼凑一个拷贝之后的目标文件绝对路线
            sink_path = os.path.join(destination_dir, f)
            #拷贝文件内容到sink_path中
            num = copy_file(f_path, sink_path)
            count += 1
        elif os.path.isdir(f_path):   # 表示f是一个目录
            # 采用递归函数
            # 为了保持同样的目录结构， 目标目录要跟着变化
            new_destination_dir = os.path.join(destination_dir, f)
            copy_dir(f_path, new_destination_dir)
    return count


def copy_file(source_dir, sink_file):
    '''
    拷贝单个文件，把source_file文件内容，拷贝到sink_file中
    :param source_dir:原始文件的绝对路径
    :param sink_file: 目标文件的绝对路线
    :return: 拷贝成功之后返回1
    '''

    # 第一种： 考虑到文件都是小文件：可一次性提取全部内容， 并一次性写入全部内容
    # with open(source_dir, 'r', encoding='utf-8') as source_f:
    #     content = source_f.read()
    #     with open(sink_file,'w', encoding='utf-8') as sink_f:
    #         sink_f.write(content)

    # 第二种： 文件较大，每次从文件中读取一部分内容，并且写入到新文件（循环多次）

    source_f = open(source_dir, 'r', encoding='utf-8')
    sink_f = open(sink_file, 'w', encoding='utf-8')

    while True:
        count = source_f.read(1024*10)  # 每次读取10kb
        if count == '' or count is None:   #没有读取到数据
            break  #文件读完
        sink_f.write(count)
    source_f.close()
    sink_f.close()
    return 1

copy_dir(r'/sunny_网络爬虫', r'E:\jianpianDownload')

