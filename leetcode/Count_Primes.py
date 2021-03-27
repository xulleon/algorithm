class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0

        is_prime = [True for _ in range(n)]
        is_prime[0] = is_prime[1] = False
        is_prime[2] = True

        for i in range(2, int(n ** 0.5) + 1):
            if is_prime[i]:
                for j in range(i*i, n, i):
                    # Start from 2 to int(n**0.5),
                    # find all the non-primes based
                    # on i. those are not primes
                    # because they are times of i.
                    # All the left are primes
                    is_prime[j] = False

        return sum(is_prime)
