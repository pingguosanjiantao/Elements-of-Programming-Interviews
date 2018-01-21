# coding:utf-8
from LinkedListLib import *


# leetcode 23
def mergeTwoLists(a, b):
    dummy = ListNode(-1)
    cur = dummy
    while a is not None and b is not None:
        if a.val <= b.val:
            cur.next = a
            a = a.next
        else:
            cur.next = b
            b = b.next
        cur = cur.next
    cur.next = a if b is None else b
    return dummy.next
