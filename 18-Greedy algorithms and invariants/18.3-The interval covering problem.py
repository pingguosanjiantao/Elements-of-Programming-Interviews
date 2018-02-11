def findMiniVisits(intervals):
    if len(intervals) == 0:
        return 0
    intervals.sort(cmp=lambda x, y: x[1] - y[1])
    pre = intervals[0][1]
    ret = [pre]
    for inter in intervals:
        if inter[0] > pre:
            pre = inter[1]
            ret += [pre]
    return ret


intervals = [[1, 2], [2, 3], [3, 4], [2, 3], [3, 4], [4, 5]]
print findMiniVisits(intervals)
