# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 03:53:42 2022

@author: Avinash Kumar
"""

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

def pairSum(head: ListNode) :
        lst = []
        curr = head
        while curr != None:
            lst.append(curr.val)
            curr = curr.next
        sum = 0
        sIdx = 0
        lIdx = len(lst) - 1
        while lIdx > sIdx:
            sum = max(sum, lst[sIdx] + lst[lIdx])
            sIdx+=1
            lIdx-=1
        return sum
    
head = ListNode(5, ListNode(4, ListNode(2, ListNode(1))))
res = pairSum(head)
print(res)