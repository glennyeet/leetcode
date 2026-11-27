from functools import cache
from typing import List


class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        # Top-down DP + Greedy: O(n^2) time, O(n) space

        n = len(items)
        free_copies = [0] * n
        for i in range(n):
            for j in range(n):
                if j == i:
                    continue
                free_copies[i] += items[j][0] % items[i][0] == 0
        min_price = float("inf")
        for i in range(n):
            min_price = min(min_price, items[i][1])

        @cache
        def dp(i: int, budget_left: int) -> int:
            if i == n:
                return budget_left // min_price
            max_copies = 0
            cur_copies = 1 + free_copies[i]
            cur_price = items[i][1]
            if budget_left >= cur_price:
                max_copies = max(
                    max_copies, cur_copies + dp(i + 1, budget_left - cur_price)
                )
            max_copies = max(max_copies, dp(i + 1, budget_left))
            return max_copies

        return dp(0, budget)
