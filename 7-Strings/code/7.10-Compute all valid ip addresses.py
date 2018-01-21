def getValidIpAddress(s):
    def isValidPart(s):
        if len(s) == 0 or len(s) > 3:
            return False
        if s[0] == '0' and len(s) > 1:
            return False
        return int(s) in range(0, 256)

    if len(s) < 4:
        return False
    ret = []
    # max length of segment in ipv4 is 4
    i = 1
    while i < len(s) and i < 4:
        first = s[:i]
        if isValidPart(first):
            j = 1
            while i + j < len(s) and j < 4:
                second = s[i:i + j]
                if isValidPart(second):
                    k = 1
                    while i + j + k < len(s) and k < 4:
                        third = s[i + j:i + j + k]
                        forth = s[i + j + k:]
                        if isValidPart(third) and isValidPart(forth):
                            ret += [first + '.' + second + '.' + third + '.' + forth]
                        k += 1
                j += 1
        i += 1
    return ret


print getValidIpAddress('19216811')
