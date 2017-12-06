#!/usr/bin/env python3 
# encoding: utf-8  

""" 

File Name: python3的编码.py

Created by 彭思聪 on 2017/12/4 下午3:04.
Copyright © 2017年 彭思聪. All rights reserved.

"""  

"""
在python3中，字符串默认为Unicode也就是万国码
它是一个统一的标准也是字符串在内存中的形式每个字符都占两个字节，因此可能会造成一定的资源浪费。
python2中，字符串默认为ASCII码，如果要使用Unicode需要在字符串前面加u 比如 s = u'你好'

我们都知道在网络中传输的数据都是二进制的形式，因此如果按照Unicode的形式来传输数据就会发生资源严重浪费的情况，且提高了数据传输的开销。
因为Unicode会让原本占一个字节的ASCII字符也会统一的占两个字节，而网络上的数据大部分都是ASCII字符。因此为了提高字符串的网络传输效率，出现了
utf8、gbk等等各式的编码方案，其中utf8最为常用，它的最大特点就是字符所占大小可变长，原占一个字节的ASCII字符的大小保持不变，而一些其他的字符
占两到三个字节。

在python3中采用utf8的编码的数据是以Bytes的形式展现的

从 Unicode ----->  UTF8     是一个编码（encode）的过程
从 UTF8    ----->  Unicode  是一个解码（decode）的过程
"""