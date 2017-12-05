#!/usr/bin/env python3 
# encoding: utf-8  

""" 

File Name: server_threading.py

Created by 彭思聪 on 2017/12/4 下午4:24.
Copyright © 2017年 彭思聪. All rights reserved.

"""  

import socketserver

"""
server端多线程版本
"""


class MyServer(socketserver.BaseRequestHandler):

    def handle(self):
        print('server start...')

        # 获取客户端连接过来的套接字
        conn = self.request
        print(self.client_address)
        while True:
            try:
                client_data = conn.recv(1024)
                print(client_data.decode('utf8'))
                print('waiting...')
                server_data = input('>>>')
                conn.sendall(server_data.encode('utf8'))
            except:
                conn.close()
                break


if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer(('127.0.0.1', 8088), MyServer)
    server.serve_forever()