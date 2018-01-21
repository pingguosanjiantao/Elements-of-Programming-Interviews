# leetcode 142
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
