class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def insertionSort(head):
    dummy = ListNode(0, head)
    iter = head
    while iter is not None and iter.next is not None:
        if iter.val > iter.next.val:
            target = iter.next
            pre = dummy
            while pre.next.val < target.val:
                pre = pre.next
            tmp = pre.next
            pre.next = target
            iter.next = target.next
            target.next = tmp
        else:
            iter = iter.next
    return dummy.next


def stableSort(head):
    def mergeList(a, b):
        dummy = ListNode(-1)
        cur = dummy
        while a is not None or b is not None:
            if a is None or (b is not None and b.val < a.val):
                cur.next = b
                b = b.next
            else:
                cur.next = a
                a = a.next
            cur = cur.next

        return dummy.next

    if head is None or head.next is None:
        return head
    preSlow, slow, fast = None, head, head
    while fast is not None and fast.next is not None:
        preSlow = slow
        fast, slow = fast.next.next, slow.next
    preSlow.next = None
    left = stableSort(head)
    right = stableSort(slow)
    return mergeList(left, right)


def toList(head):
    ret = []
    while head is not None:
        ret += [head.val]
        head = head.next
    return ret


head = ListNode(5, ListNode(3, ListNode(7, ListNode(1))))

# print toList(insertionSort(head))
out = stableSort(head)
print toList(out)
