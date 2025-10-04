from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Bottom-up DP: O(n) time, O(1) space

        n = len(prices)
        min_buy = prices[0]
        max_profit = 0
        for i in range(1, n):
            max_profit = max(max_profit, prices[i] - min_buy)
            min_buy = min(min_buy, prices[i])
        return max_profit
