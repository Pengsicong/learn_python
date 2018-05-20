#!/usr/bin/env python3 
# encoding: utf-8  

""" 

File Name: 协程.py

Created by 彭思聪 on 2017/12/6 下午5:27.
Copyright © 2017年 彭思聪. All rights reserved.

"""  

"""
协程概念
    协程，又称微线程，纤程。英文名Coroutine。一句话说明什么是线程：协程是一种用户态的轻量级线程。

    协程拥有自己的寄存器上下文和栈。
    协程调度切换时，将寄存器上下文和栈保存到其他地方，在切回来的时候，恢复先前保存的寄存器上下文和栈。因此：

    协程能保留上一次调用时的状态（即所有局部状态的一个特定组合），每次过程重入时，就相当于进入上一次调用的状态，
    换种说法：进入上一次离开时所处逻辑流的位置。
    
协程好处
    1. 无需线程上下文切换的开销
    2. 无需原子操作锁定及同步的开销
　　     "原子操作(atomic operation)是不需要synchronized"，所谓原子操作是指不会被线程调度机制打断的操作；
        这种操作一旦开始，就一直运行到结束，中间不会有任何 context switch （切换到另一个线程）。
        原子操作可以是一个步骤，也可以是多个操作步骤，但是其顺序是不可以被打乱，或者切割掉只执行部分。视作整体是原子性的核心。
    3. 方便切换控制流，简化编程模型
    4. 高并发+高扩展性+低成本：一个CPU支持上万的协程都不是问题。所以很适合用于高并发处理。

协程缺点
    1. 无法利用多核资源：协程的本质是个单线程,它不能同时将 单个CPU 的多个核用上,协程需要和进程配合才能运行在多CPU上.
       当然我们日常所编写的绝大部分应用都没有这个必要，除非是cpu密集型应用。
    2. 进行阻塞（Blocking）操作（如IO时）会阻塞掉整个程序
"""

import time
import queue


def consumer(name):
    print("--->starting eating baozi...")
    while True:
        new_baozi = yield 'done'
        print("[%s] is eating baozi %s" % (name, new_baozi))
        time.sleep(1)


def producer():
    # 激活consumer生成器
    con.__next__()
    n = 0
    while n < 10:
        print("\033[32;1m[producer]\033[0m is making baozi %s" % n)
        stat = con.send(n)
        print(stat)
        n += 1


if __name__ == '__main__':
    con = consumer("c1")
    producer()
