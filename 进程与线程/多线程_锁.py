#!/usr/bin/env python3 
# encoding: utf-8  

""" 

File Name: 多线程_锁.py

Created by 彭思聪 on 2017/12/5 下午2:45.
Copyright © 2017年 彭思聪. All rights reserved.

"""

from functools import wraps
import threading
import time

"""
GIL
    python解释器自带了一把全局解释锁(GIL),它的存在直接导致python中的多线程只能利用cpu的一个核心.
    因为有GIL的存在,python中的多线程其实类似操作系统中的时间片切换,每个线程通过操作系统的时间片调度来分配cpu时间.
    
同步锁
    python中虽然有GIL的限制,但是在多线程中如果涉及到线程的局部变量与全局变量的交互时,可能会产生数据冒险.
    
    比如说下面函数中出现的 num+=1 , num+=1 虽然只是一条语句,但是在内部它会先计算num+1,然后令一个局部变量temp=num+1, 最后才将temp
    赋值给全局变量num.这里如果foo线程在计算完temp=num+1这一步后由于时间片到,系统会将cpu切换到bar线程,等到bar线程的时间片到,如果这时的
    全局变量num出现变动,那么foo线程继续的第二步num=temp就会出现数据不一致的错误.因此需要加上一把同步锁,令temp=num+1, num=temp成为一个
    原子操作.这样就不会出现数据不一致的情况.
    
    这里需要注意的是,由于加锁解锁需要消耗一定的cpu的资源,因此在相同条件下,有锁的情况会比没有锁的情况慢很多!
    
    什么时候需要同步锁? 
    由于GIL的存在,因此当线程函数出现局部变量与全局多次交互的情况,就需要加同步锁.
    单次交互不需要同步锁(因为有GIL),这和其他语言比如c/c++, java不同.
    
    
同步锁与GIL的关系？

    Python的线程在GIL的控制之下，线程之间，对整个python解释器，对python提供的C API的访问都是互斥的，这可以看作是Python内核级的互斥机制。
    但是这种互斥是我们不能控制的，我们还需要另外一种可控的互斥机制———用户级互斥。
    内核级通过互斥保护了内核的共享资源，同样，用户级互斥保护了用户程序中的共享资源。
    
GIL 的作用是：
    对于一个解释器，只能有一个thread在执行bytecode。
    所以每时每刻只有一条bytecode在被执行一个thread。GIL保证了bytecode 这层面上是thread safe的。
    但是如果你有个操作比如 x += 1，这个操作需要多个bytecodes操作，在执行这个操作的多条bytecodes期间的时候可能中途就换thread了，
    这样就出现了data races的情况了。
    
"""

num = 0

lock = threading.RLock()


def show_perf(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        print("%s start at thread %s" % (wrapper.__name__, threading.current_thread()))
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print("%s end after %s sec" % (wrapper.__name__, (end-start)))
    return wrapper


@show_perf
def foo():
    global num
    for i in range(10000000):

        lock.acquire()
        num += 1
        lock.release()


@show_perf
def bar():
    global num
    for i in range(10000000):

        lock.acquire()
        num += 1
        lock.release()


@show_perf
def main():
    t1 = threading.Thread(target=foo)
    t2 = threading.Thread(target=bar)

    t1.start()
    t2.start()

    print('Thread active count: %s (in front of join)' % threading.active_count())

    t1.join()
    t2.join()


if __name__ == '__main__':

    main()
    print('Thread active count: %s (after join)' % threading.active_count())
    print('num = %s' % num)

