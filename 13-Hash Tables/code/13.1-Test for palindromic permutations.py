from collections import defaultdict

def canFormPalindrome(s):
    dict = defaultdict(lambda: 0)
    for i in range(len(s)):
        dict[s[i]] += 1
    hasOdd = False
    for c in dict.keys():
        if dict[c] % 2 != 0:
            if hasOdd:
                return False
            else:
                hasOdd = True
    return True

print canFormPalindrome("abb")