#!/usr/bin/env python3 
# encoding: utf-8  

""" 

File Name: 旋转图像.py

Created by 彭思聪 on 2018/4/21 下午12:55.
Copyright © 2018年 彭思聪. All rights reserved.

"""  

"""
给定一个 n × n 的二维矩阵表示一个图像。

将图像顺时针旋转 90 度。

说明：

你必须在原地旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要使用另一个矩阵来旋转图像。

示例 1:

给定 matrix = 
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

原地旋转输入矩阵，使其变为:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
"""


class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        old_matrix = matrix.copy()
        matrix.clear()
        old_matrix.reverse()
        for row in zip(*old_matrix):
            matrix.append(list(row))


if __name__ == '__main__':
    matrix = [
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]
    Solution().rotate(matrix)

    print(matrix)