# https://leetcode.com/problems/count-primes/
# Runtime: 2678 ms, faster than 50.37% of Python online submissions for Count Primes.
# Memory Usage: 129.8 MB, less than 85.45% of Python online submissions for Count Primes.
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if n < 2:
            return 0

        is_prime = [False, False] + [True] * (n - 2)
        max_prime = int(n ** 0.5)
        for i in range(2, max_prime + 1):
            if is_prime[i]: 
                for j in range(i*i, n, i):
                    if is_prime[j]:
                        is_prime[j] = False

        return sum(is_prime)
