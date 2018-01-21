# leetcode 160
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
