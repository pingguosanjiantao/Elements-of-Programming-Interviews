def genBalancedParentheses(n):
    def doGenBalancedParentheses(left, right, cur, ret):
        print cur
        if left == 0 and right == 0:
            ret += [cur[:]]
            return
        if left > 0:
            doGenBalancedParentheses(left - 1, right, cur + '(', ret)
        if left < right:
            doGenBalancedParentheses(left, right - 1, cur + ')', ret)

    ret = []
    doGenBalancedParentheses(n, n, '', ret)
    return ret

print genBalancedParentheses(3)