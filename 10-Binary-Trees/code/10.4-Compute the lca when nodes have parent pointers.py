def findLCAWithParentPoint(root, a, b):
    def getHeight(root):
        ret = 0
        while root.parent is not None:
            ret += 1
            root = root.parent
        return ret

    heightA, heightB = getHeight(a), getHeight(b)
    if heightA < heightB:
        a, b = b, a
    heightDiff = abs(heightA - heightB)
    for _ in range(heightDiff):
        a = a.parent
    while a != b:
        a = a.parent
        b = b.parent
    return a
