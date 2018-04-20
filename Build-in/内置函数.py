#!/usr/bin/env python  
# encoding: utf-8  

""" 

File Name: 内置函数.py.py

Created by 彭思聪 on 2017/11/24 下午9:31.
Copyright © 2017年 彭思聪. All rights reserved.

"""  

"""
内置函数（Built-in Function）

     1. abs     接受一个int或float，返回一个绝对值
     2. all
     3. any
     4. ascii
     5. bin
     6. bool
     7. bytearray
     8. bytes
     9. callable
    10. chr
    11. classmethod
    12. compile
    13. complex
    
    14. delattr     通过传入一个字符串去一个对象里面输出一个成员（属性/方法
    
    15. dict
    16. dir
    17. divmod
    18. enumerate
    19. eval
    20. exec
    
    21. filter  接受一个函数和序列，返回一个filter类型的迭代器，按照函数的要求过滤序列, 注意和map的区别：filter只能过滤，不能修改
    
    22. float
    23. format
    24. frozenset
    
    25. getattr  通过传入一个字符串去一个对象里面获取一个成员（属性/方法）的数据
    
    26. globals     将一个全局变量在一个局部空间里面定义为globals意味着在一个局部空间里面可以修改全局变量（不加只能访问，不能修改）
    
    27. hasattr  通过传入一个字符串去一个对象里面判断一个成员（属性/方法）是否存在
    
    28. hash
    29. help
    30. hex
    31. id
    32. input
    33. int
    34. isinstance
    35. issubclass
    36. iter
    37. len
    38. list
    39. locals
    
    40. map     接受一个函数和序列，返回一个map类型的迭代器，将函数作用于序列的每一个值
    
    41. max
    42. memoryview
    43. min
    44. next
    45. object
    46. oct
    47. open
    48. ord
    49. pow
    50. print
    51. property
    52. range
    53. repr
    54. reversed
    55. round
    56. set
    
    57. setattr     通过传入两个字符串去一个对象里面设置一个成员（属性/方法）
    
    58. slice
    59. sorted
    60. staticmethod
    61. str
    62. sum
    63. super
    64. tuple
    65. type
    66. vars
    67. zip
    68. _import_
    
"""


# 21. filter
"""
def func(x):
    if x != 'a':
        return True


# ret是一个<filter at 0x110d4da20>类型的迭代器，通过内置方法__next__来获取值   
ret = filter(func, 'abcd')    

ret.__next__()
Out[4]: 'b'

ret.__next__()
Out[5]: 'c'

ret.__next__()
Out[6]: 'd'

ret.__next__()
Traceback (most recent call last):
  File "/usr/local/lib/python3.5/site-packages/IPython/core/interactiveshell.py", line 2881, in run_code
    exec(code_obj, self.user_global_ns, self.user_ns)
  File "<ipython-input-7-d5230dc54264>", line 1, in <module>
    ret.__next__()
StopIteration
"""


# 40. map
"""
def func(x):
    if isinstance(x, int):
        x = x + 1
        return x
    return x
    
# ret是一个<map at 0x110d4da20>类型的迭代器，通过内置方法__next__来获取值 
ret = map(func, ['a', 1, 2])

ret.__next__()
Out[4]: 'a'

ret.__next__()
Out[5]: 2

ret.__next__()
Out[6]: 3

ret.__next__()
Traceback (most recent call last):
  File "/usr/local/lib/python3.5/site-packages/IPython/core/interactiveshell.py", line 2881, in run_code
    exec(code_obj, self.user_global_ns, self.user_ns)
  File "<ipython-input-7-d5230dc54264>", line 1, in <module>
    ret.__next__()
StopIteration
"""
