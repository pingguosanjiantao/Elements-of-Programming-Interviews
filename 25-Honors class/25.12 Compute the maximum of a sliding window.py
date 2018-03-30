# coding=utf-8
# maxqueue from 9.10
# Deque is needed
class MaxQueue:
    def __init__(self):
        self.data = []
        self.maxs = []

    def enqueue(self, x):
        while len(self.maxs) > 0:
            if self.maxs[-1] < x:
                self.maxs.pop()
            else:
                break
        self.maxs += [x]
        self.data += [x]

    def dequeue(self):
        if len(self.data) <= 0:
            return None
        if self.data[0] == self.maxs[0]:
            self.maxs.pop(0)
        return self.data.pop(0)

    def max(self):
        return self.maxs[0] if len(self.maxs) > 0 else None

    def size(self):
        return len(self.data)


def computeMaximumOfSlidingWindow(nums, k):
    k += 1
    maxQueue = MaxQueue()
    for i in range(len(nums)):
        if maxQueue.size() < k:
            maxQueue.enqueue(nums[i])
        else:
            maxQueue.dequeue()
            maxQueue.enqueue(nums[i])
            if nums[i] != 0:
                nums[i] = maxQueue.max()
    return nums


print computeMaximumOfSlidingWindow([1.3, 0, 2.5, 3.7, 0, 1.4, 2.6, 0, 2.2, 1.7, 0, 0, 0, 0, 1.7], 3)
