class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        totalCoins = len(coins)
        defaultValue = amount + 1
        minCoins = [defaultValue for _ in range(defaultValue)]
        minCoins[0] = 0

        for i in range(1, defaultValue):
            for j in range(totalCoins):
                coin = coins[j]
                if i - coin >= 0:
                    minCoins[i] = min(minCoins[i], minCoins[i - coin] + 1)
        
        return minCoins[amount] if minCoins[amount] != defaultValue else -1
