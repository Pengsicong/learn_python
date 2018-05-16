#!/usr/bin/env python3 
# encoding: utf-8  

""" 

File Name: 简单聊天程序.py

Created by 彭思聪 on 2018/5/14 下午8:25.
Copyright © 2018年 彭思聪. All rights reserved.

"""

import socket
from threading import Thread


class ChatClient(object):
    """聊天客户端"""

    def __init__(self, client_ip='', client_port=1234):
        client_addr = (client_ip, client_port)
        sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sk.connect(client_addr)

        self.client_addr = client_addr
        self.sk = sk

    def recv_msg(self):
        while True:
            recv_data = self.sk.recv(1024)
            print('\n'+recv_data.decode('gb2312'))

    def send_msg(self):
        while True:
            send_msg = input('请输入内容:')
            self.sk.send(bytes(send_msg, 'gb2312') + b'\n')

    def run(self):
        """客户端运行接口"""
        recv_thread = Thread(target=self.recv_msg, daemon=True)
        recv_thread.start()

        send_thread = Thread(target=self.send_msg, daemon=True)
        send_thread.start()

        recv_thread.join()
        send_thread.join()

    def __del__(self):
        print('已关闭socket...')
        try:
            self.sk.close()
        except AttributeError:
            pass


if __name__ == '__main__':
    client = ChatClient('192.168.0.108', 8080)
    client.run()
