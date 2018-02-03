class ArrayData:
    def __init__(self, idx, val):
        self.idx = idx
        self.val = val


# very useful problem
def findMinDisSortedArrays(sortedArrays):
    ret = float('inf')
    heads, currentHeads = [], []
    for _ in sortedArrays:
        heads += [0]
    for i in range(len(sortedArrays)):
        currentHeads += [ArrayData(i, sortedArrays[i][heads[i]])]
    while True:
        currentHeads.sort(cmp=lambda x, y: x.val - y.val if x.val - y.val != 0 else x.idx - y.idx)
        ret = min(ret, currentHeads[-1].val - currentHeads[0].val)
        idxNextMin = currentHeads[0].idx
        heads[idxNextMin] = heads[idxNextMin] + 1
        if heads[idxNextMin] >= len(sortedArrays[idxNextMin]):
            for cur in currentHeads:
                print cur.val
            return ret
        currentHeads.pop(0)
        currentHeads += [ArrayData(idxNextMin, sortedArrays[idxNextMin][heads[idxNextMin]])]
    return ret


print findMinDisSortedArrays([[5, 10, 15], [3, 6, 9, 12, 15], [8, 16, 24]])
