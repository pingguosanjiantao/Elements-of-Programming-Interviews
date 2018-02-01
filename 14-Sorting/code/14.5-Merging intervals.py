def addInterval(intervals, newInter):
    i = 0
    ret = []
    while i < len(intervals) and newInter[0] > intervals[i][1]:
        ret += [intervals[i]]
        i += 1
    while i < len(intervals) and newInter[1] >= intervals[i][0]:
        newInter[0] = min(newInter[0], intervals[i][0])
        newInter[1] = max(newInter[1], intervals[i][1])
        i += 1
    ret += [newInter]
    ret += intervals[i:]
    return ret


print addInterval([[-4, -1], [0, 2], [3, 6], [7, 9], [11, 12], [14, 17]], [1, 8])
