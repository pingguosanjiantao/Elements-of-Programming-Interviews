# coding=utf-8
# assumed s is not None, and regex is not None
def isMatchHere(s, regex):
    if regex == '':
        return True
    if regex == '$':
        return len(s) == 0
    if len(regex) >= 2 and regex[1] == '*':
        for i in range(len(s)):
            if regex[0] == '.' or regex[0] == s[i]:
                if isMatch(s[i + 1:], regex[2:]):
                    return True
            else:
                break
        return isMatchHere(s, regex[2:])
    return len(s) > 0 and (regex[0] == '.' or regex[0] == s[0]) and isMatchHere(s[1:], regex[1:])


def isMatch(s, regex):
    if regex[0] == '^':
        return isMatchHere(s, regex[1:])
    for i in range(len(s) + 1):
        if isMatchHere(s[i:], regex):
            return True
    return False


print isMatch('aaa', 'a*a')

# leetcode 10
class Solution(object):
    def isMatch(self, s, regex):
        def isMatchHere(s, regex):
            if regex == '':
                return len(s) == 0
            if len(regex) >= 2 and regex[1] == '*':
                for i in range(len(s)):
                    if regex[0] == '.' or regex[0] == s[i]:
                        if isMatchHere(s[i + 1:], regex[2:]):
                            return True
                    else:
                        break
                return isMatchHere(s, regex[2:])
            return len(s) > 0 and (regex[0] == '.' or regex[0] == s[0]) and isMatchHere(s[1:], regex[1:])
        return isMatchHere(s, regex)
print Solution().isMatch('a', '')