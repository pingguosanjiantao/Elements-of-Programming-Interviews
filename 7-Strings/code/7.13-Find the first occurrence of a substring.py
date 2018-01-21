# hash match
def rabinKarp(s, t):
    if len(t) > len(s):
        return -1
    sHash, tHash = 0, 0
    BASE, powerT = 26, 1
    for i in range(len(t)):
        powerT = powerT * BASE if i > 0 else 1
        sHash, tHash = sHash * BASE + ord(s[i]), tHash * BASE + ord(t[i])
    k = len(t)
    while k <= len(s):
        idx = k - len(t)
        if tHash == sHash and s[idx:k] == t:
            return idx
        # break condition
        if k == len(s):
            break
        sHash -= ord(s[idx]) * powerT
        sHash = sHash * BASE + ord(s[k])
        k += 1
    return -1


print rabinKarp('ATCGT', 'CGT')
