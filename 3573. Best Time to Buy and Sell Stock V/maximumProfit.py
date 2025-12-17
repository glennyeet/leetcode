from typing import List
from functools import cache


class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        # Top-down DP: O(n * k) time, O(n * k) space

        n = len(prices)

        @cache
        def can_buy(day: int, transactions: int) -> float | int:
            if day == n:
                return float("-inf")
            return max(
                can_buy(day + 1, transactions), -prices[day] + dp(day + 1, transactions)
            )

        @cache
        def can_sell(day: int, transactions: int) -> float | int:
            if day == n:
                return float("-inf")
            return max(
                can_sell(day + 1, transactions), prices[day] + dp(day + 1, transactions)
            )

        @cache
        def dp(day: int, transactions: int) -> int:
            if day == n or transactions == k:
                return 0
            max_profit = max(
                dp(day + 1, transactions),
                prices[day] + can_buy(day + 1, transactions + 1),
                -prices[day] + can_sell(day + 1, transactions + 1),
            )
            return max_profit

        max_profit = dp(0, 0)
        can_buy.cache_clear()
        can_sell.cache_clear()
        dp.cache_clear()
        return max_profit
