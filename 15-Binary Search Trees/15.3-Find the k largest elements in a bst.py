def findKLargest(root, k):
    ret = []

    def doFindKLargest(root, k, ret):
        if root is not None and len(ret) < k:
            doFindKLargest(root.right, k, ret)
            if len(ret) < k:
                ret += [root.val]
                doFindKLargest(root.left, k, ret)

    doFindKLargest(root, k, ret)
    return ret
