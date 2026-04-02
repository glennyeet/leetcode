from typing import List
from functools import cache


class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        # Top-down DP: O(m * n) time, O(m * n) space

        m = len(coins)
        n = len(coins[0])

        @cache
        def dp(i: int, j: int, neutralized: int) -> int:
            if i == m - 1 and j == n - 1:
                if neutralized > 0:
                    return max(coins[i][j], 0)
                return coins[i][j]
            max_profit = float("-inf")
            if i + 1 < m:
                max_profit = max(max_profit, coins[i][j] + dp(i + 1, j, neutralized))
                if neutralized > 0 and coins[i][j] < 0:
                    max_profit = max(max_profit, dp(i + 1, j, neutralized - 1))
            if j + 1 < n:
                max_profit = max(max_profit, coins[i][j] + dp(i, j + 1, neutralized))
                if neutralized > 0 and coins[i][j] < 0:
                    max_profit = max(max_profit, dp(i, j + 1, neutralized - 1))
            return max_profit

        max_profit = dp(0, 0, 2)
        dp.cache_clear()
        return max_profit
