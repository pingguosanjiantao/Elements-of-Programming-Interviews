def testIsOrderedNodes(a, b, mid):
    def searchTarget(root, tar):
        while root is not None and root != tar:
            root = root.left if root.val > tar.val else root.right
        return root == tar

    sta, end = a, b
    while sta is not b \
            and sta is not mid \
            and end is not a \
            and end is not mid \
            and (sta is not None or end is not None):
        if sta is not None:
            sta = sta.left if sta.val > mid.val else sta.right
        if end is not None:
            end = end.left if end.val > mid.val else end.right
    if sta == b or end == a or (sta != mid and end != mid):
        return False
    # the result is sta or end equals mid
    return searchTarget(mid, a) if sta == mid else searchTarget(mid, b)
