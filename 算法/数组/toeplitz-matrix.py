#!/usr/bin/env python3 
# encoding: utf-8  

""" 

File Name: toeplitz-matrix.py

Created by 彭思聪 on 2018/4/20 下午6:56.
Copyright © 2018年 彭思聪. All rights reserved.

"""  

"""
Description

A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same element.

Now given an M x N matrix, return True if and only if the matrix is Toeplitz.
"""

"""
Example

Input: matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
Output: True
Explanation:
1234
5123
9512

In the above grid, the diagonals are "[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]", 
and in each diagonal all elements are the same, so the answer is True.
"""


class Solution:
    """Runtime: 56 ms"""

    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        if len(matrix) == 0:
            return False
        if len(matrix) == 1 or len(matrix[0]) == 1:
            return True

        row = len(matrix)
        col = len(matrix[0])

        # 中线扫描
        result_set = set()
        for mid in range(min(row, col)):
            result_set.add(matrix[mid][mid])
        if len(result_set) > 1:
            return False

        # 左侧扫描
        for i in range(1, row):
            result_set = set()
            scan_col = 0
            result_set.add(matrix[i][scan_col])
            r = i
            while True:
                if r + 1 > row - 1 or scan_col + 1 > col - 1:
                    break
                result_set.add(matrix[r+1][scan_col+1])
                r += 1
                scan_col += 1
            if len(result_set) > 1:
                return False

        # 右侧扫描
        for j in range(1, col):
            result_set = set()
            scan_row = 0
            result_set.add(matrix[scan_row][j])
            c = j
            while True:
                if c + 1 > col - 1 or scan_row + 1 > row - 1:
                    break
                result_set.add(matrix[scan_row+1][c+1])
                c += 1
                scan_row += 1
            if len(result_set) > 1:
                return False

        return True


if __name__ == '__main__':
    nums = [[1,2,3,4],
            [5,1,2,3],
            [9,5,1,2]]

    print(Solution().isToeplitzMatrix(nums))
