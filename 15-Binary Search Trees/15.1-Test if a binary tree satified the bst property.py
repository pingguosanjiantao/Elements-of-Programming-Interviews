# assume root is not None
def isBST(root):
    def doIsBST(root, lower, upper):
        if root is None:
            return True
        elif root.val < lower or root.val > upper:
            return False
        else:
            return doIsBST(root.left, lower, root.val) and doIsBST(root.right, root.val, upper)

    return doIsBST(root, float('-inf'), float('inf'))


# iteration version
def isBSTIteration(root):
    queue = [[root, float('-inf'), float('inf')]]
    while len(queue) > 0:
        [cur, lower, upper] = queue.pop(0)
        if cur.val < lower or cur.val > upper:
            return False
        if cur.left is not None:
            queue += [[cur.left, lower, cur.val]]
        if cur.right is not None:
            queue += [[cur.right, root.val, upper]]
    return Ture
