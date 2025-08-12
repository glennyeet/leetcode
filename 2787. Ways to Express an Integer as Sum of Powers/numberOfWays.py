from functools import cache


class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        # Top-down DP: O(n^2) time, O(n^2) space

        mod_factor = 10**9 + 7

        @cache
        def calculate_sum(cur_base: int, cur_sum: int) -> int:
            if cur_sum < 0:
                return 0
            elif cur_sum == 0:
                return 1
            new_num = pow(cur_base, x, mod_factor)
            if new_num > cur_sum:
                return 0
            new_base = cur_base + 1
            total_ways = calculate_sum(new_base, cur_sum)
            total_ways = (
                total_ways + calculate_sum(new_base, cur_sum - new_num)
            ) % mod_factor
            return total_ways

        return calculate_sum(1, n)
