class Solution:
    def countingSort(self, array: List[int], k: int):
        count = [0] * (k + 1)
        output = [0] * len(array)
        for i in range(len(array)):
            key = array[i]
            count[key] += 1
        for i in range(1, k + 1):
            count[i] += count[i - 1]
        for i in range(len(array) - 1, -1, -1):
            key = array[i]
            count[key] -= 1
            output[count[key]] = array[i]
        return output

    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs = self.countingSort(costs, 10**5)
        coinsSpent = 0
        bars = 0
        i = 0
        while i < len(costs) and coinsSpent < coins:
            coinsSpent += costs[i]
            if coinsSpent <= coins:
                bars += 1
            i += 1
        return bars
