def countInversion(nums):
    def doCountInversion(nums, sta, end):
        if end - sta <= 1:
            return 0
        mid = sta + (end - sta) / 2
        return doCountInversion(nums, sta, mid) + doCountInversion(nums, mid, end) + mergeCountInversion(nums, sta, mid,
                                                                                                         end)

    def mergeCountInversion(nums, sta, mid, end):
        soredA = []
        leftSta, rightSta = sta, mid
        cnt = 0
        while leftSta < mid and rightSta < end:
            if nums[leftSta] <= nums[rightSta]:
                soredA += [nums[leftSta]]
                leftSta += 1
            else:
                # nums[left] > nums[right] => nums[left->mid] > nums[right]
                cnt += mid - leftSta
                soredA += [nums[rightSta]]
                rightSta += 1
        soredA += nums[leftSta:mid]
        soredA += nums[rightSta:end]
        nums[sta:sta + len(soredA)] = soredA[:]
        return cnt

    return doCountInversion(nums, 0, len(nums))


print countInversion([4, 1, 2, 3])
