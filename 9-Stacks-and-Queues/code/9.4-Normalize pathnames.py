def shortestEquivalentPath(path):
    if path == '':
        return None
    isRoot = True if path[0] == '/' else False
    pathFinal = []
    pathStr = path.split('/')
    for token in pathStr:
        if token == '..':
            if len(pathFinal) == 0 or pathFinal[-1] == '..':
                pathFinal += [token]
            else:
                if pathFinal[-1] == '/':
                    return None
                pathFinal.pop()
        elif not token == '.' and not token == '':
            pathFinal += [token]
    ret = '/'.join(pathFinal)
    return '/' + ret if isRoot else ret


print shortestEquivalentPath("/sc//./../tc/wak")
