from functools import cache
from math import gcd
from typing import List


class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        # Top-down DP: O(n^3) time, O(n^3) space

        n = len(nums)
        mod_factor = 10**9 + 7

        @cache
        def dp(i: int, gcd1: int, gcd2: int) -> int:
            if i == n:
                if gcd1 == gcd2:
                    return 1
                return 0
            total_pairs = 0
            if gcd1 == -1:
                total_pairs = (total_pairs + dp(i + 1, nums[i], gcd2)) % mod_factor
            else:
                total_pairs = (
                    total_pairs + dp(i + 1, gcd(gcd1, nums[i]), gcd2)
                ) % mod_factor
            if gcd2 == -1:
                total_pairs = (total_pairs + dp(i + 1, gcd1, nums[i])) % mod_factor
            else:
                total_pairs = (
                    total_pairs + dp(i + 1, gcd1, gcd(gcd2, nums[i]))
                ) % mod_factor
            total_pairs = (total_pairs + dp(i + 1, gcd1, gcd2)) % mod_factor
            return total_pairs

        return dp(0, -1, -1) - 1
