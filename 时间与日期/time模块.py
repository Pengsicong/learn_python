#!/usr/bin/env python3 
# encoding: utf-8  

""" 

File Name: time模块.py

Created by 彭思聪 on 2017/11/29 上午1:58.
Copyright © 2017年 彭思聪. All rights reserved.

"""

import time

"""
time模块介绍
    This module provides various functions to manipulate time values.
    
    该模块提供了多个用来操作时间相关变量的函数

    There are two standard representations of time.  One is the number
    of seconds since the Epoch, in UTC (a.k.a. GMT).  It may be an integer
    or a floating point number (to represent fractions of seconds).
    The Epoch is system-defined; on Unix, it is generally January 1st, 1970.
    The actual value can be retrieved by calling gmtime(0).
    
    它定义了两种标准来表示时间。
    
    第一种是世界时UT即格林尼治平太阳时间从1970年1月1日开始算起所经历的秒数来表示，这里的秒数可能是整形或者浮点型。

    The other representation is a tuple of 9 integers giving local time.
    The tuple items are:
      year (including century, e.g. 1998)
      month (1-12)
      day (1-31)
      hours (0-23)
      minutes (0-59)
      seconds (0-59)
      weekday (0-6, Monday is 0)
      Julian day (day in the year, 1-366)
      DST (Daylight Savings Time) flag (-1, 0 or 1)
    If the DST flag is 0, the time is given in the regular time zone;
    if it is 1, the time is given in the DST time zone;
    if it is -1, mktime() should guess based on the date and time.
    
    第二种是一个利用含有9元素的元组来表示
    
    这9个元素分别是
        year 年
        month 月
        day 日
        hours 小时
        minutes 分钟
        seconds 秒
        weekday 星期 0-6 星期一用0来表示
        Julian day 表示当天是一年中的第几天
        DST 夏令时 默认为0

    Variables:
    
    变量介绍

    timezone -- difference in seconds between UTC and local standard time
    altzone -- difference in  seconds between UTC and local DST time
    daylight -- whether local time should reflect DST
    tzname -- tuple of (standard time zone name, DST time zone name)
    
    timezone 当地时区（未启动夏令时）
    altzone 当地时区（启动夏令时）
    daylight 夏令时标记 默认为0
    tzname 包含一对根据情况的不同而不同的字符串，分别是带夏令时的本地时区名称，和不带的

    Functions:
    
    函数介绍

    time() -- return current time in seconds since the Epoch as a float
    clock() -- return CPU time since process start as a float
    sleep() -- delay for a number of seconds given as a float
    gmtime() -- convert seconds since Epoch to UTC tuple
    localtime() -- convert seconds since Epoch to local time tuple
    asctime() -- convert time tuple to string
    ctime() -- convert time in seconds to string
    mktime() -- convert local time tuple to seconds since Epoch
    strftime() -- convert time tuple to string according to format specification
    strptime() -- parse string to time tuple according to format specification
    tzset() -- change the local timezone
    
    time() 返回当前时间的时间戳（1970纪元后经过的浮点秒数）
    clock() 用以浮点数计算的秒数返回当前的CPU时间。用来衡量不同程序的耗时，比time.time()更有用
    sleep() 推迟调用线程的运行，secs指秒数。
    gmtime() 接收时间辍（1970纪元后经过的浮点秒数）并返回格林威治天文时间下的时间元组t。注：t.tm_isdst始终为0
    localtime() 接收时间辍（1970纪元后经过的浮点秒数）并返回当地时间下的时间元组t（t.tm_isdst可取0或1，取决于当地当时是不是夏令时)
    asctime() 接受时间元组并返回一个可读的形式为"Tue Dec 11 18:07:14 2008"（2008年12月11日 周二18时07分14秒）的24个字符的字符串。
    ctime() 接受时间戳返回当地时间的可读形式，作用相当于asctime(localtime(secs))，未给参数相当于asctime()
    mktime() 接受时间元组并返回当地时间辍（1970纪元后经过的浮点秒数）。
    strftime() 接收以时间元组，并返回以可读字符串表示的当地时间，格式由fmt决定。
    strptime() 根据fmt的格式把一个时间字符串解析为时间元组。
    tzset() 根据环境变量TZ重新初始化时间相关设置
    
    strftime函数详解
        
        strftime(format[, tuple]) -> string
    
        Convert a time tuple to a string according to a format specification.
        See the library reference manual for formatting codes. When the time tuple
        is not present, current time as returned by localtime() is used.
        
        Commonly used format codes:
        
        %Y  Year with century as a decimal number.
        %m  Month as a decimal number [01,12].
        %d  Day of the month as a decimal number [01,31].
        %H  Hour (24-hour clock) as a decimal number [00,23].
        %M  Minute as a decimal number [00,59].
        %S  Second as a decimal number [00,61].
        %z  Time zone offset from UTC.
        %a  Locale's abbreviated weekday name.
        %A  Locale's full weekday name.
        %b  Locale's abbreviated month name.
        %B  Locale's full month name.
        %c  Locale's appropriate date and time representation.
        %I  Hour (12-hour clock) as a decimal number [01,12].
        %p  Locale's equivalent of either AM or PM.
        
        Other codes may be available on your platform.  See documentation for
        the C library strftime function.
"""

# time.struct_time(tm_year=1970, tm_mon=1, tm_mday=1, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=3, tm_yday=1, tm_isdst=0)
gmt_tuple = time.gmtime(0)

# time.struct_time(tm_year=1970, tm_mon=1, tm_mday=1, tm_hour=8, tm_min=0, tm_sec=0, tm_wday=3, tm_yday=1, tm_isdst=0)
local_tuple = time.localtime(0)

t_formate = "%Y-%m-%d %H:%M:%S %z %a %A %b %B %c %I %p"

# 1970-01-01 08:00:00 +0800 Thu Thursday Jan January Thu Jan  1 08:00:00 1970 08 AM
print(time.strftime(t_formate, local_tuple))

# time.struct_time(tm_year=2017, tm_mon=1, tm_mday=1, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=6, tm_yday=1, tm_isdst=-1)
print(time.strptime("2017-01-01", '%Y-%m-%d'))

# -28800.0
print(time.mktime(gmt_tuple))

# 0.0
print(time.mktime(local_tuple))
