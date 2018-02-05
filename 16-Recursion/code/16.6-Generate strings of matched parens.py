def genBalancedParentheses(n):
    def doGenBalancedParentheses(left, right, cur, ret):
        if left == 0 and right == 0:
            ret += [cur[:]]
        else:
            if left > 0:
                doGenBalancedParentheses(left - 1, right, cur + '(', ret)
            if left < right:
                doGenBalancedParentheses(left, right - 1, cur + ')', ret)

    ret = []
    doGenBalancedParentheses(n, n, '', ret)
    return ret

print genBalancedParentheses(2)