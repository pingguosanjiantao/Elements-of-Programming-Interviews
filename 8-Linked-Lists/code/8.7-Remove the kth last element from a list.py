from LinkedListLib import *


def removeKthLast(head, k):
    dummy = ListNode(-1)
    dummy.next = head
    first = dummy
    second = dummy

    for _ in range(k + 1):
        first = first.next

    while first is not None:
        first = first.next
        second = second.next
    second.next = second.next.next
    return dummy.next


printList(removeKthLast(head, 1))
