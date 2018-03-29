class Node:
    def __init__(self, value, jump, next):
        self.value = value
        self.jump = jump
        self.next = next

def copyPostingList(head):
    if head is None:
        return None
    iter = head
    while iter is not None:
        cur = Node(iter.value, None, iter.next)
        iter.next = cur
        iter = cur.next
    iter = head
    while iter is not None:
        if iter.jump is not None:
            iter.next.jump = iter.jump.next
        iter = iter.next.next
    ret = head.next
    iter = head
    while iter.next is not None:
        tmp = iter.next
        iter.next = tmp.next
        iter = tmp
    return ret

a = Node('a', None, None)
b = Node('b', None, None)
c = Node('c', None, None)
d = Node('d', None, None)
a.next = b
b.next = c
c.next = d
a.jump = c
b.jump = d
c.jump = b
d.jump = d

def printList(head):
    ret = ''
    while head.next is not None:
        ret += head.value + '-' + head.jump.value + '-' + head.next.value + ','
        head = head.next
    ret += head.value + '-' + head.jump.value + '-' + 'X.'
    print ret
printList(a)
print '**************************'
another = copyPostingList(a)
printList(another)