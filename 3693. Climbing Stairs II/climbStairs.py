from functools import cache
from typing import List


class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        # Top-down DP: O(n) time, O(n) space

        @cache
        def dp(i: int) -> int:
            if i == n:
                return 0
            min_cost = float("inf")
            for j in range(i + 1, i + 4):
                if j > n:
                    break
                jump_cost = costs[j - 1] + (j - i) ** 2
                min_cost = min(min_cost, jump_cost + dp(j))
            return min_cost

        return dp(0)
