class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyk1 = buyk2 = float("-inf")
        sellk1 = sellk2 = 0
        for price in prices:
            buyk1 = max(buyk1, -price)
            buyk2 = max(buyk2, sellk1 - price)
            sellk1 = max(sellk1, buyk1 + price)
            sellk2 = max(sellk2, buyk2 + price)
        maxSell = max(sellk1, sellk2)
        return maxSell
