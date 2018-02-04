class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# optimal solution
def buildMidBST(nums):
    def doBuildMidBST(nums, left, right):
        if left >= right:
            return None
        mid = (left + right) / 2
        root = TreeNode(nums[mid])
        root.left = buildMidBST(nums, left, mid)
        root.right = buildMidBST(nums, mid + 1, right)

    return doBuildMidBST(nums, 0, len(nums))
