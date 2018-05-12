#!/usr/bin/env python3 
# encoding: utf-8  

""" 

File Name: 杨辉三角.py

Created by 彭思聪 on 2018/5/7 下午5:33.
Copyright © 2018年 彭思聪. All rights reserved.

"""  

"""
给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。

在杨辉三角中，每个数是它左上方和右上方的数的和。

示例:

输入: 5
输出:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""


class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        pascal = []
        for i in range(numRows):
            if i == 0:
                pascal.append([1])
            elif i == 1:
                pascal.append([1,1])
            else:
                j = 0
                k = 1
                prev = pascal[i-1]
                temp = [1]
                while j < len(prev)-1:
                    temp.append(prev[j]+prev[k])
                    j += 1
                    k += 1
                temp.append(1)
                pascal.append(temp)

        return pascal


if __name__ == '__main__':
    print(Solution().generate(20))
