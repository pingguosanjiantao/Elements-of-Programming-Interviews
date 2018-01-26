class MinHeap:
    def __init__(self):
        self.data = []

    def add(self, x):
        k = len(self.data)
        if k == 0:
            self.data += [x]
        else:
            self.data += [float("inf")]
            while k > 0:
                idx = (k - 1) >> 1
                parent = self.data[idx]
                if parent <= x:
                    break
                self.data[k] = parent  # parent down
                k = idx
            self.data[k] = x

    def poll(self):
        if len(self.data) == 0:
            return None
        if len(self.data) == 1:
            return self.data.pop()
        ret = self.data[0]
        x = self.data.pop()
        size = len(self.data)
        k, half = 0, size >> 1
        while k < half:
            leftId = (k << 1) + 1
            rightId = leftId + 1
            idx = rightId if rightId < size and self.data[rightId] < self.data[leftId] else leftId
            child = self.data[idx]
            if x <= child:
                break
            self.data[k] = child
            k = idx
        self.data[k] = x

        return ret

    def isEmpty(self):
        return len(self.data) == 0

    def size(self):
        return len(self.data)


def findMaxNums(k, stars):
    minHeap = MinHeap()
    for ele in stars:
        minHeap.add(ele)
        if minHeap.size() == (k + 1):
            minHeap.poll()
    ret = []
    while not minHeap.isEmpty():
        ret += [minHeap.poll()]
    return ret

print findMaxNums(3, [5,2,8,6,1,4,9,6])
