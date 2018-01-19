def phoneMnemonic(phoneNumber):
    MAPPING = ['0', '1', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

    ret = []
    cur = [None] * len(phoneNumber)

    # the same infrustructure with Combination
    def helper(digit):
        if digit == len(phoneNumber):
            ret.append(cur[:])
        else:
            key = MAPPING[ord(phoneNumber[digit]) - ord('0')]
            for i in range(len(key)):
                cur[digit] = key[i]
                helper(digit + 1)

    helper(0)
    return ret


print phoneMnemonic('28')
