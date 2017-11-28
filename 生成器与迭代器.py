#!/usr/bin/env python  
# encoding: utf-8  

""" 

File Name: 生成器与迭代器.py

Created by 彭思聪 on 2017/11/25 下午1:11.
Copyright © 2017年 彭思聪. All rights reserved.

"""

# from collections import Generator, Iterator, Iterable

"""
生成器(Generator)
    生成器是一个可迭代对象（Iterable）
    
    创建方式:
        1. (f(x) for x in range(10))
        2. yield 封装了iter和next
"""


"""
迭代器(Iterator)
    满足两个条件
        1. 有iter方法
        2. 有next方法

可迭代对象(Iterable)
    满足条件：
        有iter方法
"""


"""
对于for循环，如果循环对象是一个：
    1. 迭代器
        直接执行迭代器的next方法
    2. 可迭代对象
        调用对象的iter方法，并获取返回值，然后循环上一步的返回对象，直到iter方法结束
        
    
"""


"""
list_ = [1, 2, 3]        # 可迭代对象，有__iter__方法，可以被for迭代，但是没有__next__方法
list_iter = iter(list_)  # 内置函数将list_转换为一个迭代器，拥有了__next__方法

iter(L)
Out[4]: <list_iterator at 0x10a658828>

list_iter = iter(L)

list_iter.__next__()
Out[6]: 1

list_iter.__next__()
Out[7]: 2

list_iter.__next__()
Out[8]: 3

list_iter.__next__()
Traceback (most recent call last):
  File "/usr/local/lib/python3.5/site-packages/IPython/core/interactiveshell.py", line 2881, in run_code
    exec(code_obj, self.user_global_ns, self.user_ns)
  File "<ipython-input-9-4a6c6e6ddc82>", line 1, in <module>
    list_iter.__next__()
StopIteration
"""

"""
for 循环内部的三件事
    1. 调用可迭代对象的iter方法返回一个迭代器对象
    2. 不断调用迭代器对象的next方法
    3. 处理StopIteration异常
"""


"""
def f(x):
    return 3 * x


# map 类型的生成器，利用__next__调用，相当于获取菜单的厨师并通过__next__一盘一盘按顺序上菜，占用内存少
print(map(f, range(10)))    # <map object at 0x106c50ba8>

# 生成器
print((f(x) for x in range(10)))   # <generator object <genexpr> at 0x1087b0af0>

# 列表生成器， 直接将所有内容列出， 相对一桌子菜，占用内存多, 但是比生成器灵活
print([f(x) for x in range(10)])    # [0, 3, 6, 9, 12, 15, 18, 21, 24, 27]
"""


"""
def func(x):
    for i in range(x):
        yield i * i
    print('end')
    return


gen = func(10)

print(gen)  # <generator object func at 0x10107caf0>
print('first:', next(gen))
print('second:', next(gen))
print('third:', next(gen))


# for循环迭代可迭代对象, 都有可迭代方法__iter__
for item in gen:
    print('others:', item)
"""


"""
def foo():
    count1 = yield 1
    print(count1)

    count2 = yield 2
    print(count2)

    yield 3


g = foo()
print(g)
print(g.send(None))  # g.send(None) 等价与 next(g)

print(g.send('hello'))  # 将'hello'传到count1，然后调用__next__来执行yield 2
print(g.send('world'))  # 将'world'传到count2，然后调用__next__来执行yield 3
"""
