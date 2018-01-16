# add one
def addOne(nums):
    carry = 1
    idx = 1
    while carry != 0:
        if idx <= len(nums):
            sums = nums[len(nums) - idx] + carry
            nums[len(nums) - idx] = sums % 10
            carry = sums / 10
            idx += 1
        else:
            return [carry] + nums
    return nums

print addOne([9,9,9])
