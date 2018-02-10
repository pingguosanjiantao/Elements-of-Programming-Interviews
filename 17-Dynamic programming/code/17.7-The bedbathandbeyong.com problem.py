# optimal solution
def decomposeIntoDicWords(str, dictionary):
    length = len(str)
    dp = [-1 for _ in range(length)]
    for i in range(length):
        word = str[:i + 1]
        if word in dictionary:
            dp[i] = i + 1
        if dp[i] == -1:
            for j in range(i):
                if dp[j] != -1 and str[j + 1: i + 1] in dictionary:
                    dp[i] = i - j
                    break
    ret = []
    if dp[-1] != -1:
        idx = length - 1
        while idx >= 0:
            ret = [str[idx + 1 - dp[idx]: idx + 1]] + ret
            idx -= dp[idx]
    return ret


print decomposeIntoDicWords('bedbathbeyond', ['beyond', 'bath', 'bed'])
