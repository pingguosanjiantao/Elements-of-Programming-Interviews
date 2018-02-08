def isPattern(matrix, pattern):
    rows, cols = len(matrix), len(matrix[0])

    def isPatternAt(i, j, offset, failed):
        if offset == len(pattern):
            return True
        if i < 0 or i >= rows or j < 0 or j >= cols or [i, j, offset] in failed:
            return False
        if matrix[i][j] == pattern[offset]:
            if isPatternAt(i - 1, j, offset + 1, failed):
                return True
            if isPatternAt(i + 1, j, offset + 1, failed):
                return True
            if isPatternAt(i, j - 1, offset + 1, failed):
                return True
            if isPatternAt(i, j + 1, offset + 1, failed):
                return True
        failed += [[i, j, offset]]
        return False

    failed = []
    for i in range(rows):
        for j in range(cols):
            if isPatternAt(i, j, 0, failed):
                return True
    return False


matrix = [[1, 2, 3],
          [3, 4, 5],
          [5, 6, 7]]
pattern = [1, 2, 3, 4]
print isPattern(matrix, pattern)
