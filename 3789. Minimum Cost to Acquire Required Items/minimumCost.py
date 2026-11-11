class Solution:
    def minimumCost(
        self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int
    ) -> int:
        # Greedy: O(1) time, O(1) space

        no_cost_both = cost1 * need1 + cost2 * need2
        max_need = max(need1, need2)
        all_cost_both = costBoth * max_need
        min_need = min(need1, need2)
        max_need_cost = cost1 if need1 > need2 else cost2
        some_cost_both = costBoth * min_need + max_need_cost * (max_need - min_need)
        return min(no_cost_both, all_cost_both, some_cost_both)
