class TreeNode:
    def __init__(self):
        self.left = None
        self.right = None
        self.parent = None
        self.locked = False
        self.numLockedDescendants = 0

    def isLocked(self):
        return self.locked

    def lock(self):
        if self.numLockedDescendants > 0 or self.locked:
            return False
        iter = self.parent
        while iter is not None:
            if iter.locked:
                return False
            iter = iter.parent
        self.locked = True
        iter = self.parent
        while iter is not None:
            self.numLockedDescendants += 1
            iter = iter.parent
        return True

    def unLock(self):
        if self.locked:
            self.locked = False
            iter = self.parent
            while iter is not None:
                self.numLockedDescendants -= 1
                iter = iter.parent
