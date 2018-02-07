class TreeNode:
    def __init__(self):
        self.edges = []


class Edge:
    def __init__(self, root, length):
        self.root = root
        self.length = length


class HeightAndDiameter:
    def __init__(self, height, diameter):
        self.height = height
        self.diameter = diameter


def computeHeightAndDiameter(root):
    diameter = float('-inf')
    heights = [0.0, 0.0]
    for e in root.edges:
        heightDiameter = computeHeightAndDiameter(e.root)
        if heightDiameter.height + e.height > heights[0]:
            heights[1] = heights[0]
            heights[0] = heightDiameter.height + e.height
        elif heightDiameter.height + e.length > heights[1]:
            heights[1] = heightDiameter.height + e.length
        diameter = max(diameter, heightDiameter.diameter)
    return HeightAndDiameter(heights[0], max(diameter, heights[0] + heights[1]))


def computeDiameter(root):
    return computeHeightAndDiameter(root).diameter if root is not None else 0.0
