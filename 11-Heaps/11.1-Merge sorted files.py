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


heap = MinHeap()
heap.add(5)
heap.add(3)
heap.add(1)
heap.add(2)
print heap.poll()
print heap.poll()
print heap.poll()
print heap.poll()
print heap.poll()
