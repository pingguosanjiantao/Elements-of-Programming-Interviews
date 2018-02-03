class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# optimal solution
def rebuildBST(nums):
    def doBuildBST(nums, start, end):
        if start >= end:
            return None
        idx = start + 1
        while idx < end and nums[idx] < nums[start]:
            idx += 1
        return TreeNode(nums[start], doBuildBST(nums, start + 1, idx), doBuildBST(nums, idx, end))

    return doBuildBST(nums, 0, len(nums))
