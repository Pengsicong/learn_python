#!/usr/bin/env python  
# encoding: utf-8  

"""

File Name: 正则表达式.py

Created by 彭思聪 on 2017/11/26 上午11:46.
Copyright © 2017年 彭思聪. All rights reserved.

"""

import re

"""
正则表达式
    11个元字符
        '.' : 通配符，除了换行符，可以匹配任意一个字符
        '^' : 尖角符，只从字符串的开头开始匹配, 等同于\A
        '$' : 刀了符，只从字符串的结尾开始匹配, 等同与\Z
        '*' : 重复匹配, 匹配0次或多次
        '+' : 重复匹配, 匹配1次或多次
        '?' : 匹配0次或1次,等价与{0, 1}
        '{}': 自定义匹配次数，或者次数的范围
        '[]': 字符集，0-9代表数字，a-z代表小写字母，^0-9代表非数字，其中^是取反的意思
        '|' : 管道符，或者的意思，用于分组
        '()': 分组符号，用于创建分组
        '\' : 反斜杆，主要有两个作用：
                        1. 后跟元字符去除元字符特殊功能  
                        2. 后跟普通字符实现特殊功能
                            \d : 数字     [0-9]
                            \D : 非数字    [^ 0-9]
                            \s : 空白字符 、 \t、\r、\n、空格
                            \S : 非空白字符
                            \w : 单个的 数字和字母，包括汉字
                            \W : 非数字和字母
                            \\b : 特殊边界，可以捕捉特殊字符，(r'\bh\b') 或者 ('\\bh\\b') 可以匹配被特殊边界(\W)孤立的 h 字母
    
    主要方法
        1. compile      # 创建模式对象, pattern = compile(pattern)
        
        2. findall      # 所有的结果都返回到一个列表中
        
        3. search       # search(pattern,string)：在字符串中寻找模式,
                        # 匹配成功，返回MatchObject（True），利用group方法返回值（返回第一个匹配到的结果）
                        # 匹配失败，返回None（False），不能调用group方法
                            
        4. math         # 只在字符串开始匹配，同search
        
        5. split        # 按要求分割字符串, 功能更强大
        
        6. sub          # 字符串替换，比python字符串内置方法replace更强大
"""

s = """18755802570
abc123456789@163.com
cdf@gmail.com
18755802578
12345802578
123456789 h*hello world
https://www.taobao.com/markets/nanzhuang/2017new?spm=a21bo.2017.201867-main.2.65eebe74CDhj8G
https://docs.python.org/3/library/re.html
http://www.baidu.com
！@#%……*@#$%^&
https://www.google.com/webhp?hl=en&sa=X&ved=0ahUKEwj2l7D51dvXAhVkTd8KHRBrChQ4ChA8CAM
https://photo.tuchong.com/48676/f/32611554.jpg
你好h 中国\Wa"""

# pattern = re.compile('(?P<protocol>https|http)://(?P<host>[\w.]+)(?P<path>[\w/]*)')
#
# print(re.findall(pattern, s))
#
# print(pattern.search(s))

print(re.sub('[,]', "聪", '9kill,hikm'))
