#!/usr/bin/env python3 
# encoding: utf-8  

""" 

File Name: 面向对象.py

Created by 彭思聪 on 2017/11/27 下午3:27.
Copyright © 2017年 彭思聪. All rights reserved.

"""

"""
面向对象与函数的区别
    定义
        函数
            def + 函数名（参数）
        面向对象：
            class ---> 类
            def   ---> 方法
        
    执行
        函数
            直接访问
            函数名（参数）
        面向对象 
            间接访问
            首先实例化一个类生成一个对象（实例），然后通过对象（实例）来操作类的一些方法与属性
"""


"""
面向对象

    三大特性
        封装：将一变量或者函数统一集成在一个类的属性（字段）或者方法中
        继承：(之类->父类, 派生类->基类)
        多态：python原生多态，变量有多种形态，
             java中可以声明一个函数，接受一个类或它的一个子类作为参数，这种参数可以有多种形态的叫做多态
                 
                 
    python中的类(class)
        类成员
            1. 属性（字段)  ----> 静态
                1. 普通／实例属性(字段)，保存在对象中，每次实例化一个对象都会生成一个属性的值（有可能浪费内存）, 且只能通过对象访问
                
                2. 静态属性(字段)，保存在类中，多次实例化内存中只保存一次值，既可以通过类名也可以通过对象访问
                
                class Bar:
                
                    # 静态属性
                    static_foo = 250
                    
                    def __init__(self, num=250):
                        # 普通／实例属性
                        self.foo = num
                                               
            2. 方法     ------> 动态
                1. 普通／实例方法，保存在类中，由对象调用      self --> 对象
                
                    obj = Bar() 
                    obj.foo()    # 等价于  Bar.foo(obj)
                    
                2. 静态方法，不需要self，需要@staticmethod装饰器， 并通过类或者对象调用
                
                3. 类方法, 保存在类中， 有类调用， cls --> 当前类
                
                ### 应用场景
                    如果对象需要保存一些值，执行某功能时，需要使用对象的值则用普通方法
                    不需要任何对象中的值，则使用静态或者类方法
                
                    class Bar:
                        
                        # 普通／实例方法
                        def foo(self):
                            print('foo')
                         
                        # 静态方法
                        @staticmethod   
                        def static_foo():
                            print('static_foo')
                            
                        # 类方法
                        @classmethod
                        def class_foo(cls):
                            # cls是类名 'Bar'
                            print(cls)
                            print('class_foo')
         
         self：指类的调用者
                                 
        
        super：主动调用父类的一些方法，调用形式为super(子类名, self).some_father_method()
                        
        多重继承
            和c++一样可以继承多个父类
            
            执行顺序
                1. 从左到右顺序查找
                2. 采用深度查找
                3. 多个父类继承同一个类时，该类最后执行
        
        property：使类中的一个属性（静态）成为方法，并通过fget, fset, fdel来调用等价与下面3个属性装饰器的功能
            
            Class Bar:
            
                def f1(self):
                    print('f1')
                    
                def f2(self, val):
                    print('f2', val)
                    
                def f3(self):
                    print('f3')
                    
                foo = property(fget=f1, fset=f2, fdel=f3, doc='some documents')
        
        类装饰器
            @staticmethod：定义静态方法
            
            @classmethod：定义类方法
            
            @property：属性装饰器，通过调用属性的方法调用方法（不用括号来调用），使一个方法成为属性
            
            @propertymethod.setter：使原属性方法可以使属性方法赋值, 并调用相关方法
            
            @propertymethod.deleter：使原属性方法可以调用del，并调用相关方法
            
                class Bar:
                
                    @property
                    def foo(self):
                        print('propertymethod_foo')

                    @foo.setter
                    def foo(self, var):
                        print('foo.setter', var)

                    @foo.deleter
                    def foo(self):
                        print('foo.deleter')

                obj = Bar()        
                obj.foo             # propertymethod_foo
                obj.foo = 3         # foo.setter 3
                del obj.foo         # foo.deleter
        
        私有成员符'__'
            私有属性：属性前加上'__'则使该属性成为私有属性，外部无法访问，只有通过内部访问
            私有方法：方法前加上'__'则使该方法成为私有属性，外部无法访问，只有通过内部访问
            
            注意：父类的私有成员子类无法使用
    
        特殊成员
            __init__（构造方法）
                创建对象时自动执行，用于初始化
                
            __del__（析构方方法）
                对象被析构时自动执行，与构造方法相反，
                
            __call__
                当对象被当成函数一样运行时，调用类的__call__方法
                    
                    class Bar:
                    
                        def __call__(self, *args, **kwargs):
                            print('I am called!')

                    obj = Bar()
                    obj()       # 这里调用__call__方法， 在屏幕打印 'I am called!'
                    
            __dict__
                将对象中的所有内容通过字典的形式返回
                
                    class Bar:
                        def __init__(self, name):
                          self.name = name


                    obj1 = Bar('foo')

                    print(obj1.__dict__)    # {'name': 'foo'}
                    
            __str__
                当str(某个对象）时，自动执行对象的__str__方法， 并返回值赋给int对象（常用）
                可以通过print(某个对象)，调用定义好的__str__方法
                
            __getitem__, __setitem__, __delitem__
                令类可以使用切片（slice）或者索引，分别对应 获取、赋值、删除
                
                    class Bar:
                        def __init__(self, name, age):
                            self.name = name
                            self.age = age

                        def __getitem__(self, item):
                            print('getitem', item)

                        def __setitem__(self, key, value):
                            print('setitem', key, value)

                        def __delitem__(self, key):
                            print('delitem', key)


                    obj = Bar('foo', 19)

                    obj[100]                # getitem 100
                    obj[150] = 'hi'         # setitem 150 hi
                    del obj[300]            # delitem 300
                    
            __iter__
                使对象成为可迭代对象
                
                    class Bar:
                        def __iter__(self):
                            for i in range(3):
                                yield i


                    obj = Bar()
                    for item in obj:        # 执行对象的__iter__方法，获取迭代器
                        print(item)         # 屏幕打印 0 1 2
                
                
            __doc__
                对类的功能进行说明
                    
            __int__
                当int(某个对象）时，自动执行对象的__int__方法， 并返回值赋给int对象(不常用)
            
                    class Bar:

                        def __int__(self):
                            return 100

                    obj = Bar()
                    print(int(obj))     # 屏幕打印100
                
            __add__
                两个对象相加时，调用该方法
                
                    class Bar:
                        def __init__(self, name):
                            self.name = name

                        def __add__(self, other):
                            return self.name + other.name

                    obj1 = Bar('hello ')
                    obj2 = Bar('world!')

                    print(obj1 + obj2)  # 屏幕打印 'hello world!'
                
        metaclass（类的祖宗）
            1. 在python中一切皆是对象
            2. Bar类也是一个对象，由type创建，它是type的对象
                class bar:                                def function(self):
                    def func(self):         等价于             print(123) 
                        print(123)                        Bar = type('Bar', (object,), {'func':function})
                        
            所有元类的metaless默认都是'type'，我们创建一个MyType类继承type类。然后再创建一个Bar类并设置metaless的值为MyType, 则当
            Bar类创建时自动调用MyType的__init__方法。最后利用Bar类实例化一个对象 obj=Bar()， 这时候会调用MyType的__call__方法
            
                class MyType(type):
                    def __init__(self, *args, **kw):
                        print('MyType')
                        
                    def __call__(self, *args, **kwargs):            # 这里的self指的是Bar类
                        print('call')
                        return self.__new__(self, *args, **kwargs)      # 实例化对象必须的一步


                class Bar(object, metaclass=MyType):
                    def foo(self):
                        print('foo')
                    
                    def __new__(cls, *args, **kwargs):          # 真正创建类的步骤
                        return object.__new__(cls, *args, **kwargs)
                        
                obj = Bar()                 #   屏幕打印 'MyType' 'call'
            
    
"""
#
# class MyType(type):
#     def __init__(self, *args, **kw):
#         print('MyType')
#
#     def __call__(self, *args, **kwargs):
#         print('call')
#         return self.__new__(self, *args, **kwargs)
#
#
# class Bar(object, metaclass=MyType):
#     def foo(self):
#         print('foo')
#
# obj = Bar()
# obj.foo()
