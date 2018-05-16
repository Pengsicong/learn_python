#!/usr/bin/env python3 
# encoding: utf-8  

""" 

File Name: 多进程.py

Created by 彭思聪 on 2017/12/6 下午2:50.
Copyright © 2017年 彭思聪. All rights reserved.

"""  

from multiprocessing import Process
from functools import wraps
import multiprocessing
import time
import os

"""
multiprocessing is a package that supports spawning processes using an API similar to the threading module. 
The multiprocessing package offers both local and remote concurrency,effectively side-stepping the 
Global Interpreter Lock by using subprocesses instead of threads. Due to this, the multiprocessing module allows the 
programmer to fully leverage multiple processors on a given machine. It runs on both Unix and Windows.

由于GIL的存在，python中的多线程其实并不是真正的多线程，如果想要充分地使用多核CPU的资源，在python中大部分情况需要使用多进程。
Python提供了非常好用的多进程包multiprocessing，只需要定义一个函数，Python会完成其他所有事情。
借助这个包，可以轻松完成从单进程到并发执行的转换。
multiprocessing支持子进程、通信和共享数据、执行不同形式的同步，提供了Process、Queue、Pipe、Lock等组件。
multiprocessing包是Python中的多进程管理包。
与threading.Thread类似，它可以利用multiprocessing.Process对象来创建一个进程。
该进程可以运行在Python程序内部编写的函数。
该Process对象与Thread对象的用法相同，也有start(), run(), join()的方法。
此外multiprocessing包中也有Lock/Event/Semaphore/Condition类 (这些对象可以像多线程那样，通过参数传递给各个进程)，用以同步进程，
其用法与threading包中的同名类一致。所以，multiprocessing的很大一部份与threading使用同一套API，只不过换到了多进程的情境。

但在使用这些共享API的时候，我们要注意以下几点:

在UNIX平台上，当某个进程终结之后，该进程需要被其父进程调用wait，否则进程成为僵尸进程(Zombie)。
所以，有必要对每个Process对象调用join()方法 (实际上等同于wait)。对于多线程来说，由于只有一个进程，所以不存在此必要性。
multiprocessing提供了threading包中没有的IPC(比如Pipe和Queue)，效率上更高。
应优先考虑Pipe和Queue，避免使用Lock/Event/Semaphore/Condition等同步方式 (因为它们占据的不是用户进程的资源)。
多进程应该避免共享资源。在多线程中，我们可以比较容易地共享资源，比如使用全局变量或者传递参数。在多进程情况下，
由于每个进程有自己独立的内存空间，以上方法并不合适。此时我们可以通过共享内存和Manager的方法来共享资源。
但这样做提高了程序的复杂度，并因为同步的需要而降低了程序的效率。
Process.PID中保存有PID，如果进程还没有start()，则PID为None。

window系统下，需要注意的是要想启动一个子进程，必须加上那句if __name__ == "main"，进程相关的要写在这句下面。
"""


def show_perf(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        print("%s start at %s %s" % (wrapper.__name__, time.ctime(), multiprocessing.current_process()))
        print('%s process parrent: \033[32;1m%s\033[0m, process id: \033[33;1m%s\033[0m'
              % (wrapper.__name__, os.getppid(), os.getpid()))
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("%s end after %s sec" % (wrapper.__name__, (end-start)))
        return result
    return wrapper


@show_perf
def foo(x):
    global num
    # IO bounch
    for i in range(10000000):
        num += 1

    # CPU bounch
    time.sleep(x)


@show_perf
def bar(x):
    global num
    # IO bounch
    for i in range(10000000):
        num += 1

    # CPU bounch
    time.sleep(x)


def main():
    p1 = Process(target=foo, args=(1,))
    p2 = Process(target=bar, args=(2,))
    print('\033[32;1mmain process: id %s\033[0m' % os.getpid())

    p1.start()
    p2.start()

    print('active_children(before join): %s' % multiprocessing.active_children())

    # join 方法表示父进程等待子进程执行完毕,才继续执行下一步
    p1.join()
    p2.join()

    print('active_children(after join): %s' % multiprocessing.active_children())


if __name__ == '__main__':
    num = 0

    main()

    # 在多进程中, 系统重新开辟一段内存空间给子进程,因此父进程的数据和子进程的数据相互独立, 无法共享.
    print('num = %s' % num)
