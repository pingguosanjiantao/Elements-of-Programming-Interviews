NUM_BUCKET = 1 << 16


# step1, find the available high 16 bit
# step2, get the unused low 16 bit
# step3, merge and return
def findMissingElement(nums):
    counter = [0] * NUM_BUCKET
    for ele in nums:
        idx = ele >> 16
        counter[idx] += 1
    for i in range(NUM_BUCKET):
        if counter[i] < NUM_BUCKET:  # availabe
            used = [False] * NUM_BUCKET
            for ele in nums:
                if i == (ele >> 16):
                    used[ele % NUM_BUCKET] = True
            for j in range(NUM_BUCKET):
                if not used[j]:
                    return (i << 16) | j


print findMissingElement([])
