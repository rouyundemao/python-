import socket

# 创建一个UDP的socket对象
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 客户端socket是不需要bind的，由操作系统分配一个随机的端口号

while True:

    # 发送消息给服务器
    send_msg = input('客户端>>')
    if send_msg == 'exit':    # 如果客户端输入exit表示退出聊天
        # 把exit发送给服务器，然后客户端退出循环
        client_socket.sendto(send_msg.encode('utf8'), ('172.16.76.217', 3568))
        break
    client_socket.sendto(send_msg.encode('utf8'), ('172.16.76.217', 3568))

    # 接收服务器发过来的数据
    msg, addr = client_socket.recvfrom(1024)
    print(f'来自服务端IP为：{addr[0]},端口号:{addr[1]}的消息:{msg.decode("utf-8")}')

# 关闭
client_socket.close()