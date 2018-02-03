class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# optimal solution
def rebuildBST(nums):
    rootIdx = 0

    def doBuildBST(nums, lower, upper):
        global rootIdx
        if rootIdx == len(nums):
            return None
        rootVal = nums[rootIdx]
        if rootVal < lower or rootVal > upper:
            return None
        rootIdx += 1
        return TreeNode(rootVal, doBuildBST(nums, lower, rootVal), doBuildBST(nums, rootVal, upper))

    return doBuildBST(nums, float('-inf'), float('inf'))
