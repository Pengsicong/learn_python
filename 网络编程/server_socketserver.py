#!/usr/bin/env python3 
# encoding: utf-8  

""" 

File Name: server_socketserver.py

Created by 彭思聪 on 2018/2/26 下午3:10.
Copyright © 2018年 彭思聪. All rights reserved.

"""  

import socketserver
import time


def now():
    return time.ctime(time.time())


class MyClientHandler(socketserver.BaseRequestHandler):
    def handle(self):
        print(self.client_address, now())
        time.sleep(5)
        while True:
            data = self.request.recv(1024).decode()
            if not data:
                break
            reply = 'Echo=>%s at %s' % (data, now())
            self.request.send(reply.encode())
        self.request.close()


host = '127.0.0.1'
port = 8080

addr = (host, port)
server = socketserver.ThreadingTCPServer(addr, MyClientHandler)
server.serve_forever()
