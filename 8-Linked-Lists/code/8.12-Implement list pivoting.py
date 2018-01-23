from LinkedListLib import *


def listPivoting(head, key):
    lessDummy, equalDummy, greaterDummy = ListNode(-1), ListNode(-1), ListNode(-1)
    lessHead, equalHead, greaterHead = lessDummy, equalDummy, greaterDummy
    while head is not None:
        if head.val < key:
            lessHead.next = head
            lessHead = lessHead.next
        elif head.val == key:
            equalHead.next = head
            equalHead = equalHead.next
        else:
            greaterHead.next = head
            greaterHead = greaterHead.next
        head = head.next
    lessHead.next = equalDummy.next
    equalHead.next = greaterDummy.next
    greaterHead.next = None

    return lessDummy.next


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(3)
head.next.next.next.next.next = ListNode(2)
head.next.next.next.next.next.next = ListNode(1)

printList(listPivoting(head, 2))
