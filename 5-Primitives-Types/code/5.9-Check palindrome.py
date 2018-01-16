import math


def isPalindrome(x):
    if x < 0: return False
    numDigits = int(math.log10(x)) + 1
    mask = int(math.pow(10, numDigits - 1))
    for i in range(numDigits / 2):
        if x / mask != x % 10:
            return False
        x %= mask
        x /= 10
        mask /= 100
    return True


print isPalindrome(157751)
