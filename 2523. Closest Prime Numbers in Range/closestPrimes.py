from typing import List
from math import sqrt


class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        # Sieve of Eratosthenes: O(nlog(log(n))) time, O(n) space,
        # where n is right

        is_prime = [True] * (right + 1)
        is_prime[0] = False
        is_prime[1] = False
        for i in range(2, int(sqrt(right)) + 1):
            if not is_prime[i]:
                continue
            for j in range(i**2, right + 1, i):
                is_prime[j] = False
        prime1 = None
        prime2 = None
        ans = [-1, -1]
        for i in range(left, right + 1):
            if not is_prime[i]:
                continue
            if not prime1:
                prime1 = i
                continue
            elif not prime2:
                prime2 = i
            else:
                prime1 = prime2
                prime2 = i
            if ans[0] == -1 or prime2 - prime1 < ans[1] - ans[0]:
                print(prime1, prime2)
                ans[0] = prime1
                ans[1] = prime2
        return ans
