from typing import List


class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        # Prefix Sum: O(n) time, O(n) space

        n = len(prices)
        strategy_prefix_sum = [0]
        modification_prefix_sum = [0]
        for price, action in zip(prices, strategy):
            strategy_prefix_sum.append(strategy_prefix_sum[-1] + price * action)
            modification_prefix_sum.append(modification_prefix_sum[-1] + price)
        original_profit = strategy_prefix_sum[-1]
        max_profit = original_profit
        for i in range(n):
            if i + k <= n:
                max_profit = max(
                    max_profit,
                    original_profit
                    - (strategy_prefix_sum[i + k] - strategy_prefix_sum[i])
                    + (
                        modification_prefix_sum[i + k]
                        - modification_prefix_sum[i + k // 2]
                    ),
                )
        return max_profit
