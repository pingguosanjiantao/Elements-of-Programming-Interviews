def unionOfIntervals(intervals):
    if len(intervals) == 0:
        return []
    intervals.sort(cmp=lambda x, y: x[0] - y[0])
    ret = []
    pre = intervals[0]
    for i in range(1, len(intervals)):
        cur = intervals[i]
        if cur[0] <= pre[1]:
            pre[1] = cur[1] if cur[1] > pre[1] else pre[1]
        else:
            ret += [pre]
            pre = cur
    ret += [pre]
    return ret


print unionOfIntervals([[0, 3], [2, 4], [9, 11], [12, 14], [13, 15], [15, 16]])
