def validPlacementExists(a, b):
    a.sort()
    b.sort()
    for i in range(min(len(a), len(b))):
        if a[i] >= b[j]:
            return False
    return True
