class Rectangle:
    def __init__(self, left, right, height):
        self.left = left
        self.right = right
        self.height = height


def drawingSkylines(buildings):
    minLeft, maxRight = float('inf'), float('-inf')
    for cur in buildings:
        minLeft = min(minLeft, cur.left)
        maxRight = max(maxRight, cur.right)
    heights = [0] * (maxRight - minLeft + 1)
    for cur in buildings:
        for i in range(cur.left, cur.right + 1):
            heights[i - minLeft] = max(heights[i - minLeft], cur.height)
    result = []
    left = 0
    for i in range(1, len(heights)):
        if heights[i] != heights[i - 1]:
            result += [Rectangle(left + minLeft, i - 1 + minLeft, heights[i - 1])]
            left = i
    result += [Rectangle(left + minLeft, maxRight, heights[- 1])]
    return result

