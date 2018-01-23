from LinkedListLib import *


def addTwoNumber(a, b):
    dummy = ListNode(-1)
    iter = dummy
    carry = 0
    while a is not None or b is not None:
        sums = carry
        if a is not None:
            sums += a.val
            a = a.next
        if b is not None:
            sums += b.val
            b = b.next
        iter.next = ListNode(sums % 10)
        carry = sums / 10
        iter = iter.next
    if carry != 0:
        iter.next = ListNode(carry)
    return dummy.next


a = ListNode(1)
a.next = ListNode(2)
a.next.next = ListNode(3)
b = ListNode(1)
b.next = ListNode(2)
b.next.next = ListNode(3)

printList(addTwoNumber(a, b))
