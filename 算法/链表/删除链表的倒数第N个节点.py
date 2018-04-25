#!/usr/bin/env python3 
# encoding: utf-8  

""" 

File Name: 删除链表的倒数第N个节点.py

Created by 彭思聪 on 2018/4/24 下午9:12.
Copyright © 2018年 彭思聪. All rights reserved.

"""  

"""
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

示例：

给定一个链表: 1->2->3->4->5, 和 n = 2.

当删除了倒数第二个节点后，链表变为 1->2->3->5.

说明：

给定的 n 保证是有效的。

进阶：

你能尝试使用一趟扫描实现吗？
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head.next is None:
            return None

        remove_node = head
        last_node = head
        pre_node = None

        for _ in range(n):
            last_node = last_node.next

        while last_node is not None:
            pre_node = remove_node
            remove_node = remove_node.next
            last_node - last_node.next

        pre_node.next = remove_node.next

        return head
