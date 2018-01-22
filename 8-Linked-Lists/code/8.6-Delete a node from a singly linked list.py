def deleteNode(head):
    head.val = head.next.val
    head.next = head.next.next
