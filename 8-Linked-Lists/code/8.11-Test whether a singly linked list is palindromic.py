from LinkedListLib import *


# copied from 8.2
def reverselist(head):
    dummy = ListNode(-1)
    while head is not None:
        tmp = head.next
        head.next = dummy.next
        dummy.next = head
        head = tmp
    return dummy.next


def getHalf(head):
    fast, slow = head, head
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
    return slow


def isLinkedListAPalindrom(head):
    if head is None:
        return True
    half = getHalf(head)
    half = reverselist(half)
    while head is not None and half is not None:
        if head.val != half.val:
            return False
        head, half = head.next, half.next
    return True


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(3)
head.next.next.next.next.next = ListNode(2)
head.next.next.next.next.next.next = ListNode(1)
print isLinkedListAPalindrom(head)
