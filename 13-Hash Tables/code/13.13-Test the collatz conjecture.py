def testCollatzConjecture(n):
    verifiedNumber = []
    for i in range(3, n + 1, 2):
        sequence = []
        testI = i
        while testI >= i:
            if testI in sequence:
                return False
            sequence += [testI]
            if testI % 2 != 0:
                if testI in verifiedNumber:
                    break
                verifiedNumber += [testI]
                nextTestI = 3 * testI + 1
                if nextTestI <= testI:
                    return None
                testI = nextTestI
            else:
                testI /= 2
    return True


print testCollatzConjecture(11)
