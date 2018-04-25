#!/usr/bin/env python3 
# encoding: utf-8  

""" 

File Name: 合并两个有序链表.py

Created by 彭思聪 on 2018/4/24 下午10:24.
Copyright © 2018年 彭思聪. All rights reserved.

"""  
"""
将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

示例：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        current = head
        c1 = l1
        c2 = l2
        while c1 and c2:
            if c1.val < c2.val:
                current.next = c1
                c1 = c1.next
            else:
                current.next = c2
                c2 = c2.next
            current = current.next

        while c2:
            current.next = c2
            c2 = c2.next
            current = current.next

        while c1:
            current.next = c1
            c1 = c1.next
            current = current.next

        return head.next





