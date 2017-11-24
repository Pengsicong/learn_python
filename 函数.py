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


"""
形参和实参

    形参：形式参数，不是实际存在，是虚拟变量。在定义函数和函数体的时候使用形参，目的是在函数调用时接收实参（实参个数，类型应与实参一一对应）

    实参：实际参数，调用函数时传给函数的参数，可以是常量，变量，表达式，函数，传给形参   

    区别：形参是虚拟的，不占用内存空间，.形参变量只有在被调用时才分配内存单元，
         实参是一个变量，占用内存空间，数据传送单向，实参传给形参，不能形参传给实参
"""

"""
作用域

    python中的作用域分4种情况：

    L：local，局部作用域，即函数中定义的变量；
    E：enclosing，嵌套的父级函数的局部作用域，即包含此函数的上级函数的局部作用域，但不是全局的；
    G：global，全局变量，就是模块级别定义的变量；
    B：built-in，系统固定模块里面的变量，比如int, bytearray等。 

    搜索变量的优先级顺序依次是：作用域局部>外层作用域>当前模块中的全局>python内置作用域，也就是LEGB
"""

# 全局变量，在下面函数中不能改变
x = 10


def func():
    # 错误，因为在局部作用域改变了全局变量
    # x = x + 1
    # return x
    # 正确，定义了一个局部变量，可以在局部作用域内改变
    i = x + 1
    return i


print(func())
