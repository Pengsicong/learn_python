#!/usr/bin/env python3 
# encoding: utf-8  

""" 

File Name: 闭包-保存变量python版本.py

Created by 彭思聪 on 2018/5/27 上午11:03.
Copyright © 2018年 彭思聪. All rights reserved.

"""  


class TagLi(object):
    def onclick(self):
        pass


def alert(msg):
    print(msg)


li_tags = [TagLi() for _ in range(5)]

for i in range(len(li_tags)):

    def f(temp):
        def fuc():
            alert(temp)
        li_tags[temp].onclick = fuc

    f(i)


for li in li_tags:
    li.onclick()
