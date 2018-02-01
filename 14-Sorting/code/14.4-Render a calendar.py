class EndPoint:
    def __init__(self, time, isStart):
        self.time = time
        self.isStart = isStart


def findMaxEvents(intervals):
    endPoints = []
    for inter in intervals:
        endPoints += [EndPoint(inter[0], True)]
        endPoints += [EndPoint(inter[1], False)]
    endPoints.sort(cmp=lambda x, y: x.time - y.time)
    maxCnt, numCnt = 0, 0
    for endPoint in endPoints:
        if endPoint.isStart:
            numCnt += 1
            maxCnt = max(maxCnt, numCnt)
        else:
            numCnt -= 1
    return maxCnt


print findMaxEvents([[1, 5], [6, 10], [11, 13], [14, 15], [2, 7], [8, 9], [12, 15], [4, 5], [9, 17]])
