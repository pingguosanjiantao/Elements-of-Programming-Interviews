from collections import Counter


def groupBy(people):
    ageToCount = Counter()
    for persion in people:
        ageToCount[persion[1]] = ageToCount[persion[1]] + 1
    ageToOffset = Counter()
    offset = 0
    for age in ageToCount.keys():
        ageToOffset[age] = offset
        offset += ageToCount[age]
    while len(ageToOffset) > 0:
        curAge = ageToOffset.keys()[0]
        curOffset = ageToOffset[curAge]
        person = people[curOffset]
        tarAge = person[1]
        tarOffset = ageToOffset[tarAge]
        people[curOffset], people[tarOffset] = people[tarOffset], people[curOffset]
        ageToCount[tarAge] -= 1
        tarCnt = ageToCount[tarAge]
        if tarCnt > 0:
            ageToOffset[tarAge] += 1
        else:
            del ageToOffset[tarAge]

    return people


print groupBy([['c', 1], ['d', 2], ['e', 2], ['f', 3], ['a', 1], ['b', 1]])
