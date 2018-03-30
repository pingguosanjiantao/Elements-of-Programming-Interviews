# coding=utf-8
def searchInUnbound(nums, key):
    p = 0
    while True:
        try:
            idx = (1 << p) - 1
            if nums[idx] == key:
                return idx
            elif nums[idx] > key:
                break
        except IndexError:
            break
        p += 1
    left, right = max(0, 1 << (p - 1)), (1 << p) - 1
    while left < right:
        mid = left + (right - left) / 2
        try:
            if nums[mid] == key:
                return mid
            elif key > nums[mid]:
                left = mid + 1
            else:
                right = mid
        except IndexError:
            right = mid
    return -1


a = [0, 1, 2, 3, 5, 6]
print searchInUnbound(a, 4)
