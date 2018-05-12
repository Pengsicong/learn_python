#!/usr/bin/env python3 
# encoding: utf-8  

""" 

File Name: python的动态性质.py

Created by 彭思聪 on 2018/5/10 上午10:21.
Copyright © 2018年 彭思聪. All rights reserved.

"""  
import types
"""
动态语言:
    可以在运行的过程中, 修改代码
    比如定义一个没有任何属性的类, 然后为这个类实例化一个对象, 我们可以在执行的过程中动态给这个对象添加一个属性
静态语言:
    编译时已经确定好代码, 运行过程中不能修改
"""


class Person(object):
    pass


tom = Person()

# 给实例对象动态的添加属性
tom.name = 'tom'
tom.age = 18

print(tom.name, tom.age)

# 给类动态的添加属性
Person.gender = 'male'

tony = Person()
print(tony.gender)


def walk(self):
    print('------I am walking-----')


# 给实例对象动态添加普通方法
tom.walk = types.MethodType(walk, tom)  #等价于 Person.walk = walk(tom)
tom.walk()

# 给类动态添加普通方法
Person.walk = walk

jack = Person()
jack.walk()


@staticmethod
def statictest():
    print('------statictest--------')


# 给类动态添加静态方法
Person.statictest = statictest

Person.statictest()


@classmethod
def classmethodtest(cls):
    print('------classmethodtest----')


# 给类动态添加类方法
Person.classmethodtest = classmethodtest

Person.classmethodtest()

