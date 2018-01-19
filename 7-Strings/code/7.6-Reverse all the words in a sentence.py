def reverseWords(input):
    input = list(input)

    def reverse(s, left, right):
        while left < right:
            s[left], s[right] = s[right], s[left]
            left, right = left + 1, right - 1

    # reverse the whole sentence
    reverse(input, 0, len(input) - 1)
    # process word by word
    start, end = 0, 0
    while end < len(input):
        while end < len(input) and input[end] != ' ':
            end += 1
        if end < len(input):
            reverse(input, start, end - 1)
            end += 1
            start = end
        # last word
        if end == len(input):
            reverse(input, start, len(input) - 1)
    return ''.join(input)


print reverseWords('Bob likes Alices')
