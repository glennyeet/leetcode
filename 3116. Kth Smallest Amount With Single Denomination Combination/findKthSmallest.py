from math import lcm
from typing import List


class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        # Inclusion-Exclusion + Binary Search:
        # O(2^n * n * log(min(coins) * k)) time, O(1) space

        n = len(coins)
        left = 0
        right = min(coins) * k

        def at_least_k_multiples(x: int) -> bool:
            total_multiples = 0
            for i in range(1, 1 << n):
                subset_size = 0
                subset_lcm = 1
                for j in range(n):
                    if 1 << j & i > 0:
                        subset_size += 1
                        subset_lcm = lcm(subset_lcm, coins[j])
                multiples = x // subset_lcm
                if subset_size % 2 == 0:
                    multiples *= -1
                total_multiples += multiples
            return total_multiples >= k

        while left < right:
            mid = (left + right) // 2
            if at_least_k_multiples(mid):
                right = mid
            else:
                left = mid + 1
        return left
