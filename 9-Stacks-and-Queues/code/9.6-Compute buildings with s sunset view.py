def examineBuildingsWithSunset(nums):
    stack = []
    for i in range(len(nums)):
        cur = nums[i]
        while len(stack) > 0 and cur >= stack[-1]:
            stack.pop()
        stack += [cur]
    return stack


print examineBuildingsWithSunset([5, 4, 3, 2, 1])
print examineBuildingsWithSunset([1, 2, 6, 4, 5])
