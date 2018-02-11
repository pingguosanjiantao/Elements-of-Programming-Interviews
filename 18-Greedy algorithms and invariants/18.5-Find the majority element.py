def findMajor(nums):
    ret, cnt = None, 0
    for k in nums:
        if cnt == 0:
            ret, cnt = k, 1
        elif ret == k:
            cnt += 1
        else:
            cnt -= 1
    return ret


print findMajor([2, 3, 4, 5, 2, 3, 4, 3, 4, 2, 2, 3])
