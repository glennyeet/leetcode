from typing import List


class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        # Math: O(n) time, O(1) space

        n = len(prices)
        smooth_descent_periods = 0
        current_smooth_descent_period = 1
        for i in range(1, n):
            if prices[i - 1] - prices[i] == 1:
                current_smooth_descent_period += 1
            else:
                smooth_descent_periods += (
                    current_smooth_descent_period
                    * (current_smooth_descent_period + 1)
                    // 2
                )
                current_smooth_descent_period = 1
        else:
            smooth_descent_periods += (
                current_smooth_descent_period * (current_smooth_descent_period + 1) // 2
            )
        return smooth_descent_periods
