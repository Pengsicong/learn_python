#!/usr/bin/env python3 
# encoding: utf-8  

""" 

File Name: 快速排序.py

Created by 彭思聪 on 2018/4/4 下午12:01.
Copyright © 2018年 彭思聪. All rights reserved.

"""  


def quicksort(array):

    less = []
    greter = []

    if len(array) <= 1:
        return array

    pivot = array.pop()

    for i in array:
        if i < pivot:
            less.append(i)
        else:
            greter.append(i)

    return quicksort(less) + [pivot] + quicksort(greter)


if __name__ == '__main__':
    print(quicksort([3,2,1,5]))