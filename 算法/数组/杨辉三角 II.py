#!/usr/bin/env python3 
# encoding: utf-8  

""" 

File Name: 杨辉三角 II.py

Created by 彭思聪 on 2018/5/7 下午5:47.
Copyright © 2018年 彭思聪. All rights reserved.

"""  

"""
给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。

在杨辉三角中，每个数是它左上方和右上方的数的和。

示例:

输入: 3
输出: [1,3,3,1]

进阶：

你可以优化你的算法到 O(k) 空间复杂度吗？
"""


class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        prev = []
        current_row = []

        for i in range(rowIndex+1):
            if i == 0:
                current_row = [1]
            elif i == 1:
                prev = [1, 1]
                current_row = [1, 1]
            else:
                current_row = [1]

                j = 0
                k = 1

                while j < len(prev)-1:
                    current_row.append(prev[j]+prev[k])
                    j += 1
                    k += 1
                current_row.append(1)
                prev = current_row
        return current_row


print(Solution().getRow(0))