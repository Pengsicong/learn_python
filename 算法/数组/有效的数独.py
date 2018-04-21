#!/usr/bin/env python3 
# encoding: utf-8  

""" 

File Name: 有效的数独.py

Created by 彭思聪 on 2018/4/21 上午11:59.
Copyright © 2018年 彭思聪. All rights reserved.

"""  

"""
判断一个 9x9 的数独是否有效。只需要根据以下规则，验证已经填入的数字是否有效即可。

    数字 1-9 在每一行只能出现一次。
    数字 1-9 在每一列只能出现一次。
    数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。

说明:

    一个有效的数独（部分已被填充）不一定是可解的。
    只需要根据以上规则，验证已经填入的数字是否有效即可。
    给定数独序列只包含数字 1-9 和字符 '.' 。
    给定数独永远是 9x9 形式的。
"""


class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        for row in range(9):
            # 横向扫描
            transverse_scan = []
            # 纵向扫描
            longitudinal_scan = []

            for col in range(9):
                number1 = board[row][col]
                number2 = board[col][row]
                if number1 != ".":
                    transverse_scan.append(number1)
                if number2 != ".":
                    longitudinal_scan.append(number2)

            if self.containsDuplicate(transverse_scan):
                return False

            if self.containsDuplicate(longitudinal_scan):
                return False

        for row in range(0,9,3):
            for col in range(0,9,3):
                block_scan = []
                for i in range(3):
                    for j in range(3):
                        number = board[row+i][col+j]
                        if number != ".":
                            block_scan.append(board[row+i][col+j])

                if self.containsDuplicate(block_scan):
                    return False

        return True

    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s = set(nums)

        if len(s) != len(nums):
            return True

        return False


if __name__ == '__main__':
    board = [
  ["5","3",".",".","7",".",".",".","."],
  ["6","",".","1","9","5",".",".","."],
  [".","9","3",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
    print(Solution().isValidSudoku(board))