def miniMessiness(words, width):
    length = len(words)
    if length <= 0:
        return None
    dp = [float('inf')] * length
    remain = width - len(words[0])
    dp[0] = remain ** 2
    for i in range(1, length):
        remain = width - len(words[i])
        dp[i] = dp[i - 1] + remain ** 2
        for j in range(i - 1, -1, -1):
            remain -= len(words[j]) + 1
            if remain < 0:
                break
            preMessiness = 0 if j < 1 else dp[j - 1]
            curMessiness = remain ** 2
            dp[i] = min(dp[i], preMessiness + curMessiness)
    return dp[-1]


print miniMessiness('aaa bbb c d ee ff ggggggg'.split(' '), 11)
