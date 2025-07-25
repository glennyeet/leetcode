class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # profits = [[0] * 2] * len(prices)
        # profits[0][0] = max(0, float("-inf") + prices[0])
        # profits[0][1] = max(float("-inf"), -prices[0])
        # for i in range(1, len(prices)):
        #     for j in range(2):
        #         if j == 0:
        #             profits[i][j] = max(
        #                 profits[i - 1][j], profits[i - 1][1] + prices[i]
        #             )
        #         else:
        #             profits[i][j] = max(
        #                 profits[i - 1][j], profits[i - 1][0] - prices[i]
        #             )
        # answer = profits[len(prices) - 1][0]
        # return answer
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        return profit
