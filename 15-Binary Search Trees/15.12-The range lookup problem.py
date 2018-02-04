class Interval:
    def __init__(self, left, right):
        self.left = left
        self.right = right


def rangeLookupInBST(root, inter):
    def doRangeLookupInBST(root, inter, ret):
        if root is None:
            return
        if inter.left <= root.val and root.val <= inter.right:
            doRangeLookupInBST(root.left, inter, ret)
            ret += [root.val]
        elif inter.left > root.val:
            doRangeLookupInBST(root.right, inter, ret)
        else:
            doRangeLookupInBST(root.left, inter, ret)

    ret = []
    doRangeLookupInBST(root, inter, ret)
    return ret
