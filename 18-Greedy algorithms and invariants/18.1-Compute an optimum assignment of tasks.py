def optimumTaskAssign(tasks):
    tasks.sort()
    i, j = 0, len(tasks) - 1
    ret = []
    while i < j:
        ret += [[tasks[i], tasks[j]]]
        i, j = i + 1, j - 1
    return ret


tasks = [5, 2, 1, 6, 4, 4]
print optimumTaskAssign(tasks)
