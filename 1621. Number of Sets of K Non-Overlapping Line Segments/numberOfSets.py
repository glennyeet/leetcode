from functools import cache


class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        # Top-down DP + Prefix Sum: O(n * k) time, O(n * k) space

        mod_factor = 10**9 + 7

        @cache
        def prefix_sum(i: int, k_left: int) -> int:
            if i + 1 <= k_left:
                return 0
            return (dp(i, k_left) + prefix_sum(i - 1, k_left)) % mod_factor

        @cache
        def dp(i: int, k_left: int) -> int:
            if k_left == 0:
                return 1
            elif i < 0:
                return 0
            ways = dp(i - 1, k_left) + prefix_sum(i - 1, k_left - 1)
            return ways % mod_factor

        return dp(n - 1, k)
