def checkFeasible(jugs, L, H):
    cache = []
    return checkFeasibleHelper(jugs, L, H, cache)


def checkFeasibleHelper(jugs, L, H, cache):
    if L > H or [L, H] in cache or (L < 0 and H < 0):
        return False
    for cur in jugs:
        if (cur[0] >= L and cur[1] <= H) or checkFeasibleHelper(jugs, L - cur[0], H - cur[1], cache):
            return True
    cache += [[L, H]]
    return False


print checkFeasible([[230, 240]], 250, 2000)
