from LinkedListLib import *


def evenOddMerge(head):
    evenDummy, oddDummy = ListNode(-1), ListNode(-1)
    even, odd = evenDummy, oddDummy

    turn = True
    while head is not None:
        if turn:
            even.next = head
            even = even.next
        else:
            odd.next = head
            odd = odd.next
        head = head.next
        turn = not turn
    odd.next = None
    even.next = oddDummy.next

    return evenDummy.next


printList(evenOddMerge(head))
