# copied from 11.5
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


def findHighestThreeScores(data):
    scoresMap = {}
    for ele in data:
        name, score = ele[0], ele[1]
        if scoresMap.has_key(name):
            scoreHeap = scoresMap[name]
            scoreHeap.add(score)
            if scoreHeap.size() > 3:
                scoreHeap.poll()
        else:
            scoreHeap = MinHeap()
            scoreHeap.add(score)
            scoresMap[name] = scoreHeap
    ret = None
    hightScores = float('-inf')
    for name in scoresMap.keys():
        scoreHeap = scoresMap[name]
        if scoreHeap.size() == 3:
            curScore = 0
            while scoreHeap.size() > 0:
                curScore += scoreHeap.poll()
            if curScore > hightScores:
                ret = name
                hightScores = curScore

    return ret


data = [['a', 99], ['a', 95], ['a', 93], ['b', 91], ['b', 90], ['b', 99], ['a', 99], ['b', 92], ['c', 90]]
print findHighestThreeScores(data)
