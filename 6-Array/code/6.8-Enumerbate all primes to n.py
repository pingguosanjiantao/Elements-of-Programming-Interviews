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

def cntPrimes(n):
    isPrime = [True] * n
    isPrime[0] = isPrime[1] = False
    for k in range(2, int(n ** 0.5) + 1):
        if isPrime[k]:
            for i in range(k * k, n, k):
                isPrime[i] = False
    return sum(isPrime)

print generatePrimes(5)
