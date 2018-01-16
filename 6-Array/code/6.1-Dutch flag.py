# the same name with sort color
def dutchFlagPartition(nums):
    red, white, blue = -1, -1, -1
    for i in range(len(nums)):
        if nums[i] == 0:
            blue += 1
            nums[blue] = 2
            white += 1
            nums[white] = 1
            red += 1
            nums[red] = 0
        elif nums[i] == 1:
            blue += 1
            nums[blue] = 2
            white += 1
            nums[white] = 1
        else:
            blue += 1
            nums[blue] = 2
    return nums


print dutchFlagPartition([0, 2, 0, 2, 1, 2, 0])
