#!/usr/bin/env python3 
# encoding: utf-8  

""" 

File Name: 回文链表.py

Created by 彭思聪 on 2018/4/25 上午11:05.
Copyright © 2018年 彭思聪. All rights reserved.

"""  

"""请检查一个链表是否为回文链表。

进阶：
你能在 O(n) 的时间和 O(1) 的额外空间中做到吗？
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        l = []
        current = head
        while current:
            l.append(current.val)
            current = current.next

        return l[:] == l[::-1]



class Solution2:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast=slow=head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        node=None
        while slow:
            nxt=slow.next
            slow.next=node
            node=slow
            slow=nxt
        while node:
            if node.val!=head.val:
                return False
            node=node.next
            head=head.next
        return True