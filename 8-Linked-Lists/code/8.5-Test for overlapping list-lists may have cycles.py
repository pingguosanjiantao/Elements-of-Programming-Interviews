# need to check whether has a cycle
# copied from 8.3
def detectCycle(head):
    if head is not None:
        slow, fast = head, head
        while fast is not None and fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                while head != slow:
                    head = head.next
                    slow = slow.next
                return head
    return None


# copied from 8.4
def overlappingNoCycleLists(a, b):
    def getLength(head):
        cnt = 0
        while head is not None:
            head = head.next
            cnt += 1
        return cnt

    def advanceByK(head, k):
        for _ in range(k):
            head = head.next
        return head

    aLength, bLength = getLength(a), getLength(b)
    if aLength > bLength:
        a = advanceByK(a, aLength - bLength)
    else:
        b = advanceByK(b, bLength - aLength)
    while a is not None and b is not None and a != b:
        a, b = a.next, b.next
    return a


def overlappingLists(a, b):
    aCycleTail, bCycleTail = detectCycle(a), detectCycle(b)
    if aCycleTail is None and bCycleTail is None:
        return overlappingNoCycleLists(a, b)
    elif aCycleTail is not None and bCycleTail is None:
        return None
    elif aCycleTail is None and bCycleTail is not None:
        return None
    cur = aCycleTail
    while cur != aCycleTail and cur != bCycleTail:
        cur = cur.next
    # a and b do not end in the same cycle
    if cur != bCycleTail:
        return None

    # both have cycle
    def distance(head, target):
        cnt = 0
        while head != target:
            head = head.next
            cnt += 1
        return cnt

    def advanceByK(head, k):
        for _ in range(k):
            head = head.next
        return head

    aStemLength, bStemLength = distance(a, aCycleTail), distance(b, bCycleTail)
    if aStemLength > bStemLength:
        a = advanceByK(a, aStemLength - bStemLength)
    else:
        b = advanceByK(b, bStemLength - aStemLength)
    while a != b and a != aCycleTail and b != bCycleTail:
        a, b = a.next, b.next
    return a if a == b else aCycleTail
