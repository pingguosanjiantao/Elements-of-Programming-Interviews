def generatePrimes(n):
    primes = []
    isPrime = [True] * (n + 1)
    isPrime[0], isPrime[1] = False, False
    for i in range(2, n + 1):
        if isPrime[i]:
            primes += [i]
            # step is i, it means i*1, i*2, i*3 ... n
            for j in range(i, n + 1, i):
                isPrime[j] = False
    return primes


print generatePrimes(5)
