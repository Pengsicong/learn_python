#!/usr/bin/env python3 
# encoding: utf-8  

""" 

File Name: socket对象.py

Created by 彭思聪 on 2017/11/30 上午12:41.
Copyright © 2017年 彭思聪. All rights reserved.

"""

"""
SOCK_STREAM     # TCP
SOCK_DGRAM      # UDP

family=AddressFamily.AF_INET    # 服务器之间的通信
family=AddressFamily.AF_INET6   # 服务器之间的通信
family=AddressFamily.AF_UNIX    # UNIX进程之间的通信
"""

"""
socket对象下的成员：
    1 accept    # accept阻塞，直到有连接过来 
                # 接受连接并返回（conn,address）,其中conn是新的套接字对象，可以用来接收和发送数据。address是连接客户端的地址。
        
    2 bind      # 将套接字绑定到地址。address地址的格式取决于地址族。在AF_INET下，以元组（host,port）的形式表示地址。
    
    3 close     # 关闭socket连接  
    
    4 connect   # 连接到address处的套接字。一般，address的格式为元组（hostname,port）,如果连接出错，返回socket.error错误。
    
    5 connect_ex # 同上，只不过会有返回值，连接成功时返回 0 ，连接失败时候返回编码
    
    6 detach
    7 dup
    8 family
    
    9 fileno    # 套接字的文件描述符
    
    10 get_inheritable
    
    11 getpeername  # 返回连接套接字的远程地址。返回值通常是元组（ipaddr,port）。
    
    12 getsockname  # 返回套接字自己的地址。通常是一个元组(ipaddr,port)
    
    13 getsockopt
    14 gettimeout
    
    15 listen   # 开始监听传入连接。backlog指定在拒绝连接之前，可以挂起的最大连接数量。
    
    16 makefile
    17 proto
    
    18 recv       # 接受套接字的数据。数据以字符串形式返回，bufsize指定最多可以接收的数量。flag提供有关消息的其他信息，通常可以忽略。
    
    19 recv_into
    
    20 recvfrom   # 与recv()类似，但返回值是（data,address）。其中data是包含接收数据的字符串，address是发送数据的套接字地址。
    
    21 recvfrom_into
    22 recvmsg
    23 recvmsg_into
    
    24 send        # 将string中的数据发送到连接的套接字。返回值是要发送的字节数量，该数量可能小于string的字节大小。即：可能未将指定内容全部发送。
    
    25 sendall     # 将string中的数据发送到连接的套接字，但在返回之前会尝试发送所有数据。成功返回None，失败则抛出异常。
                   # 内部通过递归调用send，将所有内容发送出去。

    26 sendfile
    27 sendmsg
    
    28 sendto      # 将数据发送到套接字，address是形式为（ipaddr，port）的元组，指定远程地址。返回值是发送的字节数。该函数主要用于UDP协议。
        
    29 set_inheritable
    
    30 setblocking  # 是否阻塞（默认True），如果设置False，那么accept和recv时一旦无数据，则报错。
    
    31 setsockopt
    32 settimeout
    33 shutdown
    
    34 timeout      # 设置套接字操作的超时期，timeout是一个浮点数，单位是秒。值为None表示没有超时期。
                    # 一般，超时期应该在刚创建套接字时设置，因为它们可能用于连接的操作（如 client 连接最多等待5s ）
    35 type
"""

from socket import socket

for i, k in enumerate(dir(socket)[35:]):
    print(i, k)