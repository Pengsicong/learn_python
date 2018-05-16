#!/usr/bin/env python3 
# encoding: utf-8  

""" 

File Name: MyThread.py

Created by 彭思聪 on 2018/5/13 下午7:09.
Copyright © 2018年 彭思聪. All rights reserved.

"""  

from threading import Thread
import time


class MyThread(Thread):
    def __init__(self, t_name):
        super(MyThread, self).__init__()
        self.t_name = t_name

    def run(self):
        print('hello %s, my name is %s' % (self.t_name, self.name))
        time.sleep(1)


if __name__ == '__main__':
    t1 = MyThread('t1')
    t2 = MyThread('t2')
    t1.start()
    t2.start()
