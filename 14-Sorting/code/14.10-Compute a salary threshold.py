# amazing
def findSalaryCap(salaries, target):
    salaries.sort()
    unadjust, length = 0, len(salaries)
    for i in range(length):
        adjust = salaries[i] * (length - i)
        if unadjust + adjust >= target:
            return (target - unadjust) / (length - i)
        unadjust += salaries[i]
    return -1


print findSalaryCap([20, 30, 40, 90, 100], 210)
