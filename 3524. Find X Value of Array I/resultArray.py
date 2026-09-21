from functools import cache
from typing import List


class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        # Top-down DP: O(n * k) time, O(n + k) space

        n = len(nums)
        remainders = []
        for i in range(n):
            remainders.append(nums[i] % k)

        @cache
        def dp(i: int, remainder: int) -> list[int]:
            if i == n:
                counts = [0] * k
                counts[remainder] += 1
                return counts
            counts_to_i = dp(i + 1, (remainder * remainders[i]) % k)
            counts = counts_to_i[:]
            counts[remainder] += 1
            return counts

        result = [0] * k
        for i in range(n):
            counts_from_i = dp(i + 1, remainders[i])
            for j in range(k):
                result[j] += counts_from_i[j]
        return result
