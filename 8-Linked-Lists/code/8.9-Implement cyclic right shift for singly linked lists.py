from LinkedListLib import *


def cyclicallyRightShiftList(head, k):
    if head is None:
        return head
    tail = head
    length = 1
    while tail.next != None:
        tail = tail.next
        length += 1
    k %= length
    if k == 0:
        return head
    tail.next = head
    stepsToNewHead = length - k
    newTail = tail
    for _ in range(stepsToNewHead):
        newTail = newTail.next
    newHead = newTail.next
    newTail.next = None
    return newHead


printList(cyclicallyRightShiftList(head, 7))
