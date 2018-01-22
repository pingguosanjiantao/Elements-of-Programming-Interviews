def computeRPN(s):
    str = s.split(',')
    cur = []
    oprators = ['+', '-', '*', '/']
    for c in str:
        if len(c) == 1 and c in oprators:
            x, y = int(cur.pop(0)), int(cur.pop(0))
            if c == '+':
                cur += [x + y]
            elif c == '-':
                cur += [x - y]
            elif c == '*':
                cur += [x * y]
            else:
                cur += [x / y]
        else:
            cur += [int(c)]
    return cur[0]


print computeRPN("3,4,+,2,*,1,+")
