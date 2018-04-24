# hash match
def rabinKarp(s, t):
    if len(t) > len(s):
        return -1
    sHash, tHash = 0, 0
    BASE, powerT = 26, 1
    for i in range(len(t)):
        if i > 0:
            powerT = powerT * BASE
        sHash = sHash * BASE + ord(s[i])
        tHash = tHash * BASE + ord(t[i])
    for k in range(len(t), len(s) + 1):
        idx = k - len(t)
        if tHash == sHash and s[idx:k] == t:
            return idx
        if k == len(s):
            break
        sHash -= ord(s[idx]) * powerT
        sHash = sHash * BASE + ord(s[k])
    return -1


print rabinKarp('ATCGT', 'CGT')
