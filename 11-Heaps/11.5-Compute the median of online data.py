# copied from 11.1
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

    def peek(self):
        return self.data[0] if len(self.data) > 0 else None

    def size(self):
        return len(self.data)


class MaxHeap:
    def __init__(self):
        self.data = []

    def add(self, x):
        k = len(self.data)
        if k == 0:
            self.data += [x]
        else:
            self.data += [float("-inf")]
            while k > 0:
                idx = (k - 1) >> 1
                parent = self.data[idx]
                if parent >= x:
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
            if x >= child:
                break
            self.data[k] = child
            k = idx
        self.data[k] = x

        return ret

    def isEmpty(self):
        return len(self.data) == 0

    def peek(self):
        return self.data[0] if len(self.data) > 0 else None

    def size(self):
        return len(self.data)

# running median
# be cautions, nums is a online sequence
def onlineMedian(nums):
    minHeap, maxHeap = MinHeap(), MaxHeap()
    for i in range(len(nums)):
        cur = nums[i]
        if minHeap.isEmpty():
            minHeap.add(cur)
        else:
            if cur >= minHeap.peek():
                minHeap.add(cur)
            else:
                maxHeap.add(cur)
        if minHeap.size() > maxHeap.size() + 1:
            maxHeap.add(minHeap.poll())
        elif maxHeap.size() > minHeap.size():
            minHeap.add(maxHeap.poll())
        print 0.5 * (minHeap.peek() + maxHeap.peek()) if minHeap.size() == maxHeap.size() else minHeap.peek()


onlineMedian([1, 0, 3, 5, 2, 0, 1])
