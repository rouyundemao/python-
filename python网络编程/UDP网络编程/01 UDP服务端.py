import socket
# 实现客户端和服务端的即时聊天

# 创建一个UDP的socket对象
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# IP:172.16.76.217，其他主机可以和当前的服务端通信
# IP:127.0.0.1 其他主机不可以和当前的服务端通信，除非客户端也在本地。
# server_socket.bind(('172.16.76.217', 2477))
# IP:'', 该服务端绑定到所有的IP地址上。
server_socket.bind(('', 3568))

while True:
    # msg是收到的数据， addr是原地址和端口号（客户端）
    msg, addr = server_socket.recvfrom(1024)    # recvfrom 是阻塞函数，没有数到数据包，那么程序就会在此处暂停
    if msg.decode('utf8') == 'exit':   # 表示终止聊天
        break
    # decode函数可以把字节数据转换成字符串
    print(f'来自客户端IP为：{addr[0]},端口号:{addr[1]}的消息:{msg.decode("utf-8")}')

    # 服务端也可以发送数据到客户端
    send_msg = input('服务端>>')
    # sendto 发送的数据不能是字符串，只能是字节数据，字符串的encode
    server_socket.sendto(send_msg.encode('utf8'), addr)

# 最后关闭socket
server_socket.close()

