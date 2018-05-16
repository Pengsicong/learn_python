#!/usr/bin/env python3 
# encoding: utf-8  

""" 

File Name: struct模块.py

Created by 彭思聪 on 2018/5/15 上午12:24.
Copyright © 2018年 彭思聪. All rights reserved.

"""  

import struct
"""
当Python需要通过网络与其他的平台进行交互的时候，必须考虑到将这些数据类型与其他平台或语言之间的类型进行互相转换问题。打个比方：C++写的客户端发
送一个int型(4字节)变量的数据到Python写的服务器，Python接收到表示这个整数的4个字节数据，怎么解析成Python认识的整数呢？ Python的标准模块
struct就用来解决这个问题。
"""

"""
struct 类型表

 
Format	C_Type	             Python_Type	Standard_size
x 	    pad                  byte 	        no value 	  	 
c 	    char 	             string         1 	            	 
b 	    signed_char          integer 	    1 	          
B 	    unsigned_char        integer 	    1 
? 	    _Bool 	             bool 	        1 	
h 	    short 	             integer 	    2 	
H 	    unsigned_short 	     integer 	    2 
i 	    int 	             integer 	    4 	
I 	    unsigned_int 	     integer 	    4 	
l 	    long 	             integer 	    4    	
L 	    unsigned_long 	     integer 	    4 	
q 	    long_long_integer    integer 	    8 	
Q 	    unsigned_long_long 	 integer 	    8 
f 	    float 	             float 	        4 	
d 	    double 	             float 	        8 	
s 	    char[] 	             string 	                    1 	 
p 	    char[] 	             string 	  	 
P 	    void *  	         integer 	  	
"""


def learn_pack():
    """struct模块中打包函数pack学习"""

    # !表示为网络传输中的大端模式
    cmd = struct.pack('!H8sb', 1, b"test.jpg", 2)
    print(cmd)

    # b'\x11"3D'  >> 由于287454020在内存中的表示为 \x11\x22\x33\x44, \x**用2个16进制表示一个字符, \***用3个8进制数表示一个字符
    # ord('\x11') == 17, chr(17) == \x11
    # ord('\x22') == 34, chr(34) == "
    # ord('\x33') == 51, chr(51) == 3
    # ord('\x44') == 68, chr(68) == D
    cmd2 = struct.pack('!l', 287454020)
    print(cmd2)


def learn_unpack():
    """struct模块中解包函数unpack学习"""
    fmt = '!H8sb'
    data = b'\x00\x01test.jpg\x02'
    unpack_data = struct.unpack(fmt, data)
    print(unpack_data)


if __name__ == '__main__':
    learn_pack()
    learn_unpack()
