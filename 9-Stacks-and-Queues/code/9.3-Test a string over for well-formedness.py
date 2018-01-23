def isWellFormed(s):
    leftChars = []
    brackets = {'(': ')', '[': ']', '{': '}'}
    for c in s:
        if c in brackets.keys():
            leftChars += [c]
        else:
            if len(leftChars) == 0:
                return False
            if brackets[leftChars[-1]] != c:
                return False
            leftChars.pop()

    return len(leftChars) == 0


print isWellFormed('{}()[(]')
