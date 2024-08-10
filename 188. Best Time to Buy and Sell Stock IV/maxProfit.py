class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        maxBuy = [float("-inf")] * (k + 1)
        maxSell = [0] * (k + 1)
        for price in prices:
            for i in range(1, k + 1):
                maxBuy[i] = max(maxBuy[i], maxSell[i - 1] - price)
                maxSell[i] = max(maxSell[i], maxBuy[i] + price)
        profit = max(maxSell)
        return profit
