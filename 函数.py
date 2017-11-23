#!/usr/bin/env python  
# encoding: utf-8  

""" 

File Name: 函数.py

Created by 彭思聪 on 2017/11/23 下午10:06.
Copyright © 2017年 彭思聪. All rights reserved.

"""

"""
函数的作用：
    1. 代码重用
    2. 降低程序的耦合度
    3. 抽象
    4. 保持一致性
    5. 可拓展
"""

"""
函数的参数：
    1.位置参数（positional arguments）
        调用函数时，传入的两个值按照位置顺序依次赋给参数
        
    2.默认参数
        将函数的参数设置一个默认值，简化函数的调用
        注意：
            1. 默认参数必须在后，否则Python的解释器会报错
            2. 当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。降低调用函数的难度。
            3. 默认参数必须指向不变对象！
    
    3.可变参数
        可变参数就是传入的参数个数是可变的，可以是1个、2个到任意个，还可以是0个。
        注意：
            1. 函数可变参数前必须加*，例如 def func(*args)
            2. 可变参数在函数调用时自动组装为一个tuple
            3. 如果已经有一个list或者tuple, 在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去
        
    4.关键字参数
        关键字参数允许你传入0个或任意个含参数名的参数
        注意：
            1. 函数关键字参数前必须加**， 例如 def func(**kw)
            2. 关键字参数在函数内部自动组装为一个dict
            3. 如果已经有一个dict， 在dict前面加一个**号，把dict的元素变成关键字参数传进去
            
    5.命名关键字参数
        用命名关键字参数可以限制关键字参数的名字
        注意：
            1. 和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。
            2. 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了
            
    6. 参数组合
        在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。
        但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
        例如：def f1(a, b, c=0, *args, e **kw)
        其中：
            a, b  必须参数
            c     默认参数
            args  可变参数
            e     命名关键字参数
            kw    关键字参数
        
"""


# 命名关键字参数，city，job为限制关键字参数的名字
# 注意1
def person1(name, age, *, city, job):
    print(name, age, city, job)


# 注意2
def person2(name, age, *args, city, job):
    print(name, age, args, city, job)


# 错误
# person2('cong', 24, 'Shanghai', 'IT')   # TypeError:missing 2 required keyword-only arguments: 'city' and 'job'

# 正确
# person2('cong', 24, city='Shanghai', job='IT')  # cong 24 () Shanghai IT
