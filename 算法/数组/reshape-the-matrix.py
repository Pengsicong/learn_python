#!/usr/bin/env python3 
# encoding: utf-8  

""" 

File Name: reshape-the-matrix.py

Created by 彭思聪 on 2018/4/20 下午5:32.
Copyright © 2018年 彭思聪. All rights reserved.

"""
from collections import Iterable
from array import array

"""
Description:

In MATLAB, there is a very useful function called 'reshape', which can reshape a matrix into a new one with different 
size but keep its original data.

You're given a matrix represented by a two-dimensional array, and two positive integers r and c representing the row 
number and column number of the wanted reshaped matrix, respectively.

The reshaped matrix need to be filled with all the elements of the original matrix in the same row-traversing order as 
they were.

If the 'reshape' operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, 
output the original matrix. 
"""

"""
Example
Input: 
nums = 
[[1,2],
 [3,4]]
r = 1, c = 4
Output: 
[[1,2,3,4]]
Explanation:
The row-traversing of nums is [1,2,3,4]. The new reshaped matrix is a 1 * 4 matrix, fill it row by row by using 
the previous list.
"""


class SolutionByQueue:

    """
    Algorithm

    The simplest method is to extract all the elements of the given matrix by reading the elements in a row-wise
    fashion. In this implementation, we use a queue to put the extracted elements. Then, we can take out the
    elements of the queue formed in a serial order and arrange the elements in the resultant required matrix in a
    row-by-row order again.

    The formation of the resultant matrix won't be possible if the number of elements in the original matrix isn't
    equal to the number of elements in the resultant matrix.

    Runtime: 216 ms
    """

    @staticmethod
    def matrix_reshape(nums, r, c):
        """

        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if len(nums) == 0 or len(nums) * len(nums[0]) != r * c:
            return nums

        new_matrix = list()

        from queue import Queue
        q = Queue()

        for i in range(len(nums)):
            for j in range(len(nums[i])):
                q.put(nums[i][j])

        for i in range(r):
            new_col = list()
            for j in range(c):
                new_col.append(q.get())
            new_matrix.append(new_col)

        return new_matrix


class SolutionByFlatten:
    """Runtime: 138 ms"""

    def matrix_reshape(self, nums, r, c):
        flatten_nums = self.flatten(nums)
        m_size = len(flatten_nums)
        if m_size == 0 or m_size != r * c:
            return nums
        new_matrix = list()
        for row in range(r):
            new_col = flatten_nums[row*c: (row+1)*c]
            new_matrix.append(new_col)
        return new_matrix

    def flatten(self, nums):
        """将多层嵌套数组抹平"""
        result = []
        for el in nums:
            if isinstance(el, Iterable) and not isinstance(el, str):
                result.extend(self.flatten(el))
            else:
                result.append(el)
        return result

    def flatten_gen(self, nums):
        """将多层嵌套数组抹平生成器版本"""
        for el in nums:
            if isinstance(el, Iterable) and not isinstance(el, str):
                yield from self.flatten_gen(el)
            else:
                yield el


class SolutionByArray:
    """Runtime: 96 ms"""

    def matrix_reshape(self, nums, r, c):

        if len(nums) == 0 or len(nums) * len(nums[0]) != r * c:
            return nums
        new_array = array('i')

        for row in range(len(nums)):
            new_array.fromlist(nums[row])

        matrix = [[new_array[i * c + j]for j in range(c)] for i in range(r)]
        return matrix


if __name__ == '__main__':
    nums = [[1, 2], [3, 4], [5, 6]]
    print(SolutionByQueue().matrix_reshape(nums, 2, 3))
    print(SolutionByFlatten().matrix_reshape(nums, 2, 3))
    print(SolutionByArray().matrix_reshape(nums, 2, 3))




