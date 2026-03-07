from socket import *
from threading import Thread
import wx

class MyClient(wx.Frame):
    """只要继承了Frame,那么当前类就是一个窗口类"""

    def __init__(self, user_name):
        super().__init__(None, 101, f'{user_name}的服务器', wx.DefaultPosition, size=wx.Size(400,520))
        self.Center()
        # 创建一个面板,把面板放到窗口里面。
        pl = wx.Panel(parent=self)

        # 创建一个可伸缩的网格布局
        fg = wx.FlexGridSizer(wx.HORIZONTAL)
        # 创建两个按钮,并且把两个个按钮按照水平的网格布局看成一个整体。
        connet_button = wx.Button(pl, size=wx.Size(200,40), label='进入聊天室')
        leave_button = wx.Button(pl, size=wx.Size(200,40), label='离开聊天室')
        fg.Add(connet_button, 0, wx.ALL)
        fg.Add(leave_button, 0, wx.ALL)

        # 创建一个只读的文本框，显示聊天记录
        self.log_text = wx.TextCtrl(pl, size=wx.Size(400, 260), style=wx.TE_MULTILINE | wx.TE_READONLY)
        # 创建一个可输入的文本框，显示聊天记录
        self.input_text = wx.TextCtrl(pl, size=wx.Size(400, 140), style=wx.TE_MULTILINE)

        # 创建一个可伸缩的网格布局
        fg2 = wx.FlexGridSizer(wx.HORIZONTAL)
        # 创建两个按钮,并且把两个个按钮按照水平的网格布局看成一个整体。
        clear_button = wx.Button(pl, size=wx.Size(200, 40), label='重置')
        send_button = wx.Button(pl, size=wx.Size(200, 40), label='发送')
        fg2.Add(clear_button, 0, wx.ALL)
        fg2.Add(send_button, 0, wx.ALL)

        # 创建一个box界面
        box = wx.BoxSizer(wx.VERTICAL)
        box.Add(fg, 1, wx.ALIGN_CENTRE)   # 两个按钮居中对齐
        box.Add(self.log_text, 1, wx.ALIGN_CENTRE)
        box.Add(self.input_text, 1, wx.ALIGN_CENTRE)
        box.Add(fg2, 1, wx.ALIGN_CENTRE)   # 两个按钮居中对齐

        pl.SetSizer(box)
        
        # 绑定鼠标点击的事件
        self.Bind(wx.EVT_BUTTON, source=connet_button, handler=self.connect_server)
        self.Bind(wx.EVT_BUTTON, source=send_button, handler=self.send_message)
        self.Bind(wx.EVT_BUTTON, source=leave_button, handler=self.leave)
        
        # 给当前对象的属性赋值
        self.user_name = user_name
        
    def connect_server(self, event):
        """ 点击连接按钮，连接到服务器,并把自己的用户名发送给服务器 """
        # 连接到服务器
        self.client_socket = socket(AF_INET, SOCK_STREAM)
        self.client_socket.connect(('127.0.0.1', 8080))
        self.is_on = True   # 客户端在线
        # 连接成功之后发送自己的用户名发送给服务器
        self.client_socket.send(self.user_name.encode('utf8'))
        # 接收服务器的信息
        t = Thread(target=self.recv_data)
        t.daemon = True
        t.start()
    
    def recv_data(self):
        """专门负责：在客户端接受消息的
        第一步：接受服务器发来的消息
        第二部：把接受到的消息显示在文本框中
        """
        while self.is_on:
            message = self.client_socket.recv(1024).decode('utf8')
            if message == 'sunny^leave^sunny':
                self.is_on = False
            else:
                self.log_text.AppendText(message)
                self.log_text.AppendText('-'*50 + '\n')
        
        self.client_socket.close()    
        self.client_socket = None

    def send_message(self, event):
        """负责发送信息到服务端"""
        if self.is_on:
            message = self.input_text.GetValue().strip # 获取输入文本框中的内容并去掉首尾空格。
            if message:
                self.client_socket.send(message.encode('utf8'))
                self.input_text.SetValue('')

    def leave(self, envent):               
        """
        客户端离开聊天室
        规定:1、当客户端发送：sunny^leave^sunny，就代表客户端马上要离开了 2、服务器也要发送同样的消息，客户端收到之后确实离开。
        1、客户端的窗口不关闭
        2、客户端的线程要结束,socket要关闭
        """
        self.ison = False
        self.client_socket.send('sunny^leave^sunny'.encode('utf8'))
        
        
if __name__ == '__main__':
    user_name = input('请输入一个用户名：')
    app = wx.App()
    frame = MyClient(user_name)
    frame.Show()
    app.MainLoop()

