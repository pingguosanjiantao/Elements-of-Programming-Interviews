def remainingInt(nums, idx):
    return reduce(lambda x, y: x * 10 + y, nums[idx:], 0)


def evaluate(nums, operators):
    nums = nums[::-1]
    stack = [nums.pop()]
    for oper in operators:
        if oper == '*':
            stack += [stack.pop() * nums.pop()]
        else:
            stack += [nums.pop()]
    return sum(stack)


def doExpressionSynthesis(nums, target, cur, offset, operands, operators):
    cur = cur * 10 + nums[offset]
    if (offset == len(nums) - 1):
        operands += [cur]
        if evaluate(operands, operators) == target:
            return True
        operands.pop()
        return False
    if doExpressionSynthesis(nums, target, cur, offset + 1, operands, operators):
        return True
    # test '*'
    operands += [cur]
    operators += ['*']
    if doExpressionSynthesis(nums, target, 0, offset + 1, operands, operators):
        return True
    operands.pop()
    operators.pop()
    # test '+'
    operands += [cur]
    if target - evaluate(operands, operators) <= remainingInt(nums, offset + 1):
        operators += ['+']
        if doExpressionSynthesis(nums, target, 0, offset + 1, operands, operators):
            return True
        operators.pop()
    operands.pop()
    return False


def expressionSynthesis(nums, target):
    return doExpressionSynthesis(nums, target, 0, 0, [], [])


print expressionSynthesis([1, 2, 3, 4, 5, 6, 7, 8, 9], 995)
