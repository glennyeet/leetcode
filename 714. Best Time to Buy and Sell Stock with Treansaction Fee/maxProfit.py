class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        maxSell = 0
        maxBuy = float("-inf")
        for price in prices:
            maxSell = max(maxSell, maxBuy + price - fee)
            maxBuy = max(maxBuy, maxSell - price)
        return maxSell
