class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def printList(head):
    print '------------'
    while head.next is not None:
        print head.val
        head = head.next
    print head.val
    print '------------'


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(6)
head.next.next.next.next.next.next = ListNode(7)
