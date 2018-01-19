def isPalindrom(s):
    left, right = 0, len(s) - 1
    while left < right:
        while left < right and not (s[left].isdigit() or s[left].isalpha()):
            left += 1
        while left < right and not (s[right].isdigit() or s[right].isalpha()):
            right -= 1
        if left < right and (s[left].lower() != s[right].lower()):
            return False
        left, right = left + 1, right - 1
    return True


print isPalindrom("A man, a plan, a canal, Panama.")
