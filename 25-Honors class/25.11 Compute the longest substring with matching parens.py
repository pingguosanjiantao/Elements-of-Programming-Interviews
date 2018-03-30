# coding=utf-8
def longestValidParenthese(s):
    maxLen, end = 0, -1
    stack = []
    for i in range(len(s)):
        if s[i] == '(':
            stack += [i]
        elif len(stack) == 0:
            end = i
        else:
            stack.pop()
            start = end if len(stack) == 0 else stack[-1]
            maxLen = max(maxLen, i - start)
    return maxLen


print longestValidParenthese('((())()(()(')
