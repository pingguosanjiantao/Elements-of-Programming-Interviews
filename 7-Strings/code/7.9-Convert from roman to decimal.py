# very very very simply answer
def romanToInteger(s):
    MAP = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    ret = MAP[s[-1]]
    for i in range(len(s) - 2, -1, -1):
        if MAP[s[i]] < MAP[s[i + 1]]:
            ret -= MAP[s[i]]
        else:
            ret += MAP[s[i]]
    return ret


print  romanToInteger('IV')
