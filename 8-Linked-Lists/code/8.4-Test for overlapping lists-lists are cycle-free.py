# leetcode 160
def getIntersectionNode(a, b):
    def findEnd(head):
        while head is not None and head.next is not None:
            head = head.next
        return head

    def linkCycle(head):
        end = findEnd(head)
        end.next = head

    def deteckCycle(head):
        fast, slow = head, head
        while fast is not None and fast.next is not None:
            fast, slow = fast.next.next, slow
            if fast is slow:
                while head is not slow:
                    head, slow = head.next, slow.next
                return head
        return None

    linkCycle(a)
    return deteckCycle(b)
