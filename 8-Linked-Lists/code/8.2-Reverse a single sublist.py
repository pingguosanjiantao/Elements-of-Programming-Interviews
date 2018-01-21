from LinkedListLib import *


# leetcode 206
def reverselist(head):
    dummy = ListNode(-1)
    while head is not None:
        tmp = head.next
        head.next = dummy.next
        dummy.next = head
        head = tmp
    return dummy.next


# leetcode 92
def reverseSublist(head, start, finish):
    dummy = ListNode(-1)
    dummy.next = head
    cur = dummy
    for _ in range(1, start):
        cur = cur.next
    iter = cur.next
    for _ in range(start, finish):
        tmp = iter.next
        iter.next = tmp.next
        tmp.next = cur.next
        cur.next = tmp
    return dummy.next


# printList(reverselist(head))
printList(reverseSublist(head, 3, 5))
