#!/usr/bin/env python3 
# encoding: utf-8  

""" 

File Name: 生成器.py

Created by 彭思聪 on 2018/5/10 上午11:09.
Copyright © 2018年 彭思聪. All rights reserved.

"""  

"""
生成器:
    当我们需要一个很大的列表或者字典, 但是不想占用过多的内存, 我们就可以使用生成器.
    通过一个固定的算法, 在需要的时候去取数据, 而不是将数据一次性全部载入到内存中.这种一边循环一边计算的机制, 成为生成器

定义生成器的方式:
    1. 列表生成式的[]改为()
    2. 将函数中的return改为yield
        
"""

gen = (x for x in range(5))

print(gen)

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

# StopIteration
# print(next(gen))


def myrange(n):

    i = 0

    while i < n:
        yield i
        i += 1


print(myrange(10))

for val in myrange(5):
    print(val)


# 斐波那契数列普通版
def fib(times):

    i = 0
    a, b = 0, 1
    fib_list = []
    while i < times:
        fib_list.append(b)
        a, b = b, a+b
        i += 1
    return fib_list


print(fib(10))


# 斐波那契数列迭代器版
def fib_gen(times):

    i = 0
    a, b = 0, 1
    while i < times:
        yield b
        a, b = b, a+b
        i += 1


print(fib_gen(10))
print(list(fib_gen(10)))

a = fib_gen(10)
for val in a:
    print(val)
