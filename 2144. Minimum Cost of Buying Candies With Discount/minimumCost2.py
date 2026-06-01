from typing import List


class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        # Greedy: O(n * log(n)) time, O(n) space,
        # where n is the size of cost

        sorted_cost = sorted(cost, reverse=True)
        min_cost = 0
        for i, candy_cost in enumerate(sorted_cost):
            if i % 3 != 2:
                min_cost += candy_cost
        return min_cost
