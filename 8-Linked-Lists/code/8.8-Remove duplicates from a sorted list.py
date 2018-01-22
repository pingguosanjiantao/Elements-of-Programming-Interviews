def removeDuplicates(head):
    cur = head
    while cur is not None:
        nextDistinct = cur.next
        while nextDistinct is not None and nextDistinct.val == cur.next:
            nextDistinct = nextDistinct.next
        cur.next = nextDistinct
        cur.next = cur.next
    return head
