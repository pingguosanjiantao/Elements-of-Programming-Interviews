def unionOfIntervals(intervals):
    if len(intervals) == 0:
        return []
    intervals.sort(cmp=lambda x, y: x[0] - y[0])
    stack = [intervals[0]]
    for i in range(1, len(intervals)):
        peek, cur = stack[-1], intervals[i]
        if cur[0] > peek[1]:
            stack.append(cur)
        else:
            if cur[1] >= peek[1]:
                stack.pop()
                stack.append([peek[0], cur[1]])
    return stack


print unionOfIntervals([[0, 3], [2, 4], [9, 11], [12, 14], [13, 15], [15, 16]])
