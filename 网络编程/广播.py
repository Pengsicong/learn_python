#!/usr/bin/env python3 
# encoding: utf-8  

""" 

File Name: 广播.py

Created by 彭思聪 on 2018/5/15 上午10:05.
Copyright © 2018年 彭思聪. All rights reserved.

"""  

import socket


dest = ('<broadcast>', 1234)

# 创建udp套接字
sk = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 对这个需要发送广播的套接字修改设置, 否则不能发送广播
sk.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

# 已广播的形式发送数据到本网络的所有地址
sk.sendto('Hi', dest)

# 等待对方回复
while True:
    (buf, addr) = sk.recvfrom(1024)
    print('(%s): %s' % (addr, buf))
