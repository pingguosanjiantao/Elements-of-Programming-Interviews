# assume that there exists
# graphs are the same up to translation and shifting
def findAmpleCity(gallens, distances, mpg):
    ret = [0, 0]
    remain = 0
    for i in range(1, len(gallens)):
        remain += gallens[i - 1] - distances[i - 1] / mpg
        if remain < ret[1]:
            ret = [i, remain]
    return ret[0]


print findAmpleCity([50, 20, 5, 30, 25, 10, 10], [45, 30, 10, 20, 30, 10, 5], 1)
