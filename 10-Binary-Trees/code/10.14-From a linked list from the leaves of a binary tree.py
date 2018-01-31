# optimal solution
def createListOfLeaves(root):
    ret = []

    def doCreateListOfLeaves(root):
        if root is not None:
            if root.left is None and root.right is None:
                ret.append(root.val)
            else:
                doCreateListOfLeaves(root.left)
                doCreateListOfLeaves(root.right)

    doCreateListOfLeaves(root)
    return root
