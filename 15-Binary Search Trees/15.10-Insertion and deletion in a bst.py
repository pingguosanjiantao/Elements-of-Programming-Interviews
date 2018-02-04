class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# basic fundment
class BinarySearchTree:
    def __init__(self, root=None):
        self.root = root

    def insert(self, key):
        if self.root is None:
            self.root = TreeNode(key)
        else:
            pre, cur = None, self.root
            while cur is not None:
                pre = cur
                if key == cur.val:
                    return False
                cur = cur.left if key < cur.val else cur.right
            if key < pre.val:
                pre.left = TreeNode(key)
            else:
                pre.right = TreeNode(key)
        return True

    def delete(self, key):
        pre, cur = None, self.root
        while cur is not None and key != cur.val:
            pre = cur
            cur = cur.left if key < cur.val else cur.right
        if cur is None:
            return False
        if cur.right is not None:
            rPre, rCur = pre, cur
            while rCur.left is not None:  # find the minimun of the right subtree
                rPre = rCur
                rCur = rCur.left
            cur.val = rCur.val
            if rPre.left.val == rCur.val:
                rPre.left = rCur.right
            else:
                rPre.right = rCur.right
        else:
            if self.root.val == cur.val:
                self.root = cur.left
            else:
                if pre.left.val == cur.val:
                    pre.left = cur.left
                else:
                    pre.right = cur.left
        return True
