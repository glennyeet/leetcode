from typing import List
from collections import Counter


class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        # Greedy + Hash Table: O(nlog(n)) time, O(n) space, where n
        # is the size of basket1

        costs_counter = Counter(basket1 + basket2)
        for cost in costs_counter:
            if costs_counter[cost] % 2:
                return -1
        basket1_counter = Counter(basket1)
        basket2_counter = Counter(basket2)
        unique_basket1 = basket1_counter - basket2_counter
        unique_basket2 = basket2_counter - basket1_counter
        swappable_costs = []
        for cost, count in list(unique_basket1.items()) + list(unique_basket2.items()):
            for _ in range(count // 2):
                swappable_costs.append(cost)
        swappable_costs.sort()
        min_cost = min(min(basket1), min(basket2))
        min_total_cost = 0
        for i in range(len(swappable_costs) // 2):
            min_total_cost += min(min_cost * 2, swappable_costs[i])
        return min_total_cost
