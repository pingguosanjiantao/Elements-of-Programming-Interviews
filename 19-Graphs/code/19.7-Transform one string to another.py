# amazing problem
def transformString(dictionary, s, t):
    dictionary.remove(s)
    q = [[s, 0]]
    while len(q) > 0:
        [curStr, dis] = q.pop(0)
        if curStr == t:
            return dis
        for i in range(len(curStr)):
            strStart = curStr[:i]
            strEnd = curStr[i + 1:]
            for j in range(26):
                modStr = strStart + chr(ord('a') + j) + strEnd
                if modStr in dictionary:
                    dictionary.remove(modStr)
                    q.append([modStr, dis + 1])
    return -1


dictionary = ['bat', 'cot', 'dog', 'dag', 'dot', 'cat']
print transformString(dictionary, 'cot', 'dot')
