# I really do not know what is this for?
def snakeString(s):
    ret = []
    for i in range(1, len(s), 4):
        ret += [s[i]]
    for i in range(0, len(s), 2):
        ret += [s[i]]
    for i in range(3, len(s), 4):
        ret += [s[i]]
    return ''.join(ret)


print snakeString("Hello world!")
