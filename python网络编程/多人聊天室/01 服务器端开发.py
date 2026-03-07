from socket import *
from threading import Thread
import time
import wx


class MyServer(wx.Frame):
    """只要继承了Frame,那么当前类就是一个窗口类"""

    def __init__(self):
        super().__init__(None, 101, 'sunny的服务器', wx.DefaultPosition, size=wx.Size(520,580))
        self.Center()
        # 创建一个面板,把面板放到窗口里面。
        pl = wx.Panel(parent=self)

        # 创建一个可伸缩的网格布局
        fg = wx.FlexGridSizer(wx.HORIZONTAL)
        # 创建三个按钮,并且把三个按钮按照水平的网格布局看成一个整体。
        start_server_button = wx.Button(pl, size=wx.Size(170,45), label='启动服务')
        save_log_button = wx.Button(pl, size=wx.Size(170,45), label='保存聊天记录')
        stop_server_button = wx.Button(pl, size=wx.Size(170,45), label='停止服务')
        fg.Add(start_server_button, 0, wx.ALL)
        fg.Add(save_log_button, 0, wx.ALL)
        fg.Add(stop_server_button, 0, wx.ALL)

        # 创建一个只读的文本框，显示聊天记录
        self.read_text = wx.TextCtrl(pl, size=wx.Size(515,535), style=wx.TE_MULTILINE | wx.TE_READONLY)
        # 创建一个box界面
        box = wx.BoxSizer(wx.VERTICAL)
        box.Add(fg, 1, wx.ALIGN_CENTRE)   # 三个按钮居中对齐
        box.Add(self.read_text, 1, wx.ALIGN_CENTRE)

        pl.SetSizer(box)

        # 给按钮加上鼠标点击事件
        self.Bind(wx.EVT_BUTTON, source=start_server_button, handler=self.start_server)
        self.Bind(wx.EVT_BUTTON, source=save_log_button, handler=self.save_log_to_file)

        # 定义对象的属性
        # 每一个客户端都有一个与之对应的一个线程
        client_dict = {}   # 聊天室中所有的客户端用户，key为客户端的用户名，把一个线程对象作为value。
        
    def start_server(self,event):
        """ 点击启动按钮,开始启动Socket服务 """
        self.server_socket = socket(AF_INET, SOCK_STREAM)    # 采用TCP协议
        self.server_socket.bind(('', 8080))
        self.server_socket.listen(5)

        # 创建子线程，让子线程调用accept, 子线程在阻塞等待客户端连接
        self.server_thread = Thread(target=self.server_work)
        self.server_thread.daemon = True
        self.server_thread.start()

    def server_work(self):
        """服务器已经启动，开始等待客户端（无限个）连接：多人聊天室"""
        print('服务器开始启动，准备接受客户端的连接')
        while True:
            # 当有一个客户端连接之后，返回session_socket
            # session_socket 负责和当前的客户端进行聊天通信。 每一个客户端都有一个对应的session_socket
            session_socket, client_addr = self.server_socket.accept()
            user_name = session_socket.recv(1024).decode('utf8')   # 接收客户端的用户名
            #创建一个和客户端对应的线程
            t1 = SessionThread(user_name,session_socket,self)
            self.client_dict[user_name] = t1     # 保存客户端的用户名和线程对象成为字典的键值对
            # 启动线程
            t1.start()
            # 给客户端发送欢迎消息
            welcome_message = f'服务器通知:欢迎{user_name}进入聊天室！'
            self.show_message_and__send_message(welcome_message)
            
            
    def show_message_and__send_message(self, message):
        """
        显示聊天记录，并把聊天记录发送给所有客户端
        第一步：把聊天记录显示在文本框中
        第二步：把聊天记录发送给所有客户端
        :param message: 聊天记录
        :return: None
        """
        # 得到当前系统时间
        current_datetime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        full_message = f'{message} \n 时间：{current_datetime} \n'
        self.read_text.AppendText(full_message)
        self.read_text.AppendText('-'*50 + '\n')
        # 发送聊天记录给所有客户端
        for client_thread in self.client_dict.values():
            if client_thread.isOn:       # 客户端在线
                # 发送聊天记录给客户端
                client_thread.session_socket.send(full_message.encode('utf8'))
    
    def remove_client(self, user_name):
        """有一个客户端用户离开聊天室，所以需要把他对应的线程从字典中删除"""
        if user_name in self.client.dict:
            self.client_dict.pop(user_name)  
            
    def save_log_to_file(self, envent):
        """
        保存所有的聊天记录到文件中，
        规则：每次保存的文件名是： log-当前时间.txt
        """       
        file_name = f'log-{time.strftime("%y-%m-%d-%H-%M-%S")}.txt'
        log_data = self.read_text.GetValue()
        with open(file_name, 'w', encoding='utf8') as f:
            f.writelines(log_data)        
           
class SessionThread(Thread):        
    """每一个客户端都有一个与之对应的一个线程"""
    def __init__(self, user_name, session_socket:socket, server_frame):
        super().__init__()
        self.session_socket = session_socket
        self.user_name = user_name
        self.server_frame = server_frame
        self.isOn = True # 客户端是否在线,可以控制线程的结束
        
    def run(self) -> None:
        while self.isOn:
            # 接受客户端的聊天信息
            recv_message = self.session_socket.recv(1024).decode('utf8')
            if recv_message == 'sunny^leave^sunny':
                # 表示客户端用户要离开聊天室了
                self.isOn = False
                # 服务器发送给客户端一条离开的确认消息
                self.session_socket('sunny^leave^sunny'.encode('utf8'))
                leave_message = f'服务器通知：{self.user_name}离开聊天室！'
                self.server_frame.show_message_and__send_message(f'{self.user_name}:{leave_message}')
                # 还要把字典中存放当前客户端的数据删除
                self.server_frame.remove_client(self.user_name)
            else:
                self.server_frame.show_message_and__send_message(f'{self.user_name}:{recv_message}')
        self.session_socket.close()
        self.session_socket = None
        
        
if __name__ == '__main__':
    # sys.exit(0)
    app = wx.App()
    frame = MyServer()
    frame.Show()
    app.MainLoop()
