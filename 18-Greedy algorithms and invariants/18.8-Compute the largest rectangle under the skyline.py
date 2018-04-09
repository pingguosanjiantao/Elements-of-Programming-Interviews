# amazing problem, optimal solution
# variant of 18.7
def getLargestRectangle(nums):
    ret = 0
    stack = []  # store the idx of stepping up
    for i in range(len(nums) + 1):
        # update the idx of same value
        if len(stack) > 0 and i < len(nums) and nums[i] == nums[stack[-1]]:
            stack[-1] = i
        # maximum the rectangle
        while len(stack) > 0 and (i == len(nums) or nums[i] < nums[stack[-1]]):
            height = nums[stack.pop()]
            head = -1 if len(stack) == 0 else stack[-1]
            width = i - 1 - head
            ret = max(ret, height * width)
        stack += [i]
    return ret


print getLargestRectangle([1, 3, 3, 1, 3])
