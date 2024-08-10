class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxBuy = float("-inf")
        maxSell = 0
        prevMaxSell = maxSell
        prevPrevMaxSell = prevMaxSell
        for price in prices:
            prevMaxSell = maxSell
            maxSell = max(maxSell, maxBuy + price)
            maxBuy = max(maxBuy, prevPrevMaxSell - price)
            prevPrevMaxSell = prevMaxSell
        return maxSell
