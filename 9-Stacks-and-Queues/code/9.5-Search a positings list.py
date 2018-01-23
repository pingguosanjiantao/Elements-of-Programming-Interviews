class PostingListNode:
    def __init__(self, val, next, jump):
        self.val = val
        self.order = -1
        self.next = None
        self.jump = None


def setJumpOrder(head):
    stack = [head]
    order = 0
    while len(stack) > 0:
        cur = stack.pop()
        if cur is not None and cur.order != -1:
            cur.order = order
            order += 1
            stack += [cur.next]
            stack += [cur.jump]
