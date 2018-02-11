def miniTotalWaiting(durations):
    durations.sort()
    ret, pre = 0, 0
    for i in range(len(durations) - 1):
        pre = pre + durations[i]
        ret += pre
    return ret


print miniTotalWaiting([2, 5, 1, 3])
