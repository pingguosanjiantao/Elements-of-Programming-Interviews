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


def sortKIncreasingDecreasingArray(nums):
    isIncreasing = True
    numLists = []
    startIdx = 0
    for i in range(1, len(nums) + 1):
        if i == len(nums) or (nums[i - 1] < nums[i] and not isIncreasing) or (nums[i - 1] >= nums[i] and isIncreasing):
            cur = nums[startIdx:i]
            if not isIncreasing:
                cur = cur[::-1]
            numLists += [cur]
            startIdx = i
            isIncreasing = not isIncreasing
    minHeap = MinHeap()
    ret = []
    for ele in numLists:
        for num in ele:
            minHeap.add(num)

    while not minHeap.isEmpty():
        ret += [minHeap.poll()]

    return ret


print sortKIncreasingDecreasingArray([57, 131, 493, 294, 221, 339, 418, 452, 442, 190])
