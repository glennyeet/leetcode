from functools import cache
from math import comb


class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        # Top-down DP: O(m * n * log(m)) time, O(n^2) space,
        # where m is maxValue

        mod_factor = 10**9 + 7

        @cache
        def combination(n: int, k: int) -> int:
            return comb(n, k) % mod_factor

        ideal_arrays = 0
        buckets = []

        def dp() -> int:
            prime_factor = buckets[-1]
            nonlocal ideal_arrays
            ideal_arrays += combination(n - 1, len(buckets) - 1)
            current_value = prime_factor * 2
            while current_value <= maxValue:
                buckets.append(current_value)
                dp()
                buckets.pop()
                current_value += prime_factor

        for i in range(1, maxValue + 1):
            buckets.append(i)
            dp()
            buckets.pop()

        return ideal_arrays % mod_factor
