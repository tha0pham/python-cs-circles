# Return a table of all the prime numbers up to some number n
def makePrimeTable(n):

    # isPrime[0] and isPrime[1] should be False
    isPrime = [False, False]

    # Initially treat all numbers as primes.
    # As we loop through the table later, isPrime[i] == True
    # indicates that i is "available" for finding multiples
    for i in range(2, n):
        isPrime.append(True)

    # Start from the smallest available number.
    # Limit the upper bound because divisors of n are at most
    # the square root of n.
    for p in range(2, int(n**1/2) + 1):
        if isPrime[p] == True:
            k = p ** 2  # Optimize running time by starting from squares
            l = 0  # Step
            # Find the first multiple. Example: If p is 2, then nextMultiple starts at 2*2 + 0*1 = 4
            nextMultiple = k + l*p

            # Cross out multiples of k
            while nextMultiple < n:
                isPrime[nextMultiple] = False
                l += 1
                # Example: If p is 2, then nextMultiple is increased to 6, 8, 10, etc.
                nextMultiple = k + l*p
    return isPrime


n = 1000001  # required table length
isPrime = makePrimeTable(n)
