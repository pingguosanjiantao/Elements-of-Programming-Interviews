# nodes have an parent field
class TreeNode:
    def __init__(self, val, parent):
        self.val = val
        self.parent = parent
        self.left = None
        self.right = None


# optimal solution
def inorderTraversal(root):
    pre, cur = None, root
    result = []
    while cur:
        if cur.parent is pre:  # from father
            if cur.left:
                next = cur.left
            else:
                result += [cur.val]
                next = cur.right if cur.right else cur.parent
        elif cur.left is pre:  # from left children
            result += [cur.val]
            next = cur.right if cur.right else cur.parent
        else:  # from right
            next = cur.parent

        pre = cur
        cur = next
    return result


root = TreeNode(5, None)

left = TreeNode(4, root)
right = TreeNode(7, root)

root.left = left
root.right = right

rightLeft = TreeNode(6, root.right)
rightRight = TreeNode(8, root.right)

right.left = rightLeft
right.right = rightRight

print inorderTraversal(root)
