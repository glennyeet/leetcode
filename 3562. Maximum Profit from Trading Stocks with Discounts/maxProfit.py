from typing import List
from collections import defaultdict
from functools import cache


class Solution:
    def maxProfit(
        self,
        n: int,
        present: List[int],
        future: List[int],
        hierarchy: List[List[int]],
        budget: int,
    ) -> int:
        # DFS + Bottom-up DP: O(n * b^2) time, O(n * b) space, where b is the
        # budget

        adj_list = defaultdict(list)
        for u, v in hierarchy:
            adj_list[u - 1].append(v - 1)

        # @cache
        # def find_max_profit(cur_node: int, discount: bool, budget: int) -> int:
        #     max_profit = 0
        #     if discount:
        #         cost = present[cur_node] // 2
        #     else:
        #         cost = present[cur_node]
        #     if budget >= cost:
        #         max_profit = max(
        #             max_profit,
        #             allocate_budget(cur_node, 0, True, budget - cost)
        #             + future[cur_node]
        #             - cost,
        #         )
        #     max_profit = max(max_profit, allocate_budget(cur_node, 0, False, budget))
        #     return max_profit

        # @cache
        # def allocate_budget(
        #     cur_node: int, child_node_index: int, discount: bool, budget: int
        # ) -> int:
        #     if child_node_index == len(adj_list[cur_node]):
        #         return 0
        #     max_profit = 0
        #     for amount in range(budget + 1):
        #         max_profit = max(
        #             max_profit,
        #             allocate_budget(
        #                 cur_node, child_node_index + 1, discount, budget - amount
        #             )
        #             + find_max_profit(
        #                 adj_list[cur_node][child_node_index], discount, amount
        #             ),
        #         )
        #     return max_profit

        # return find_max_profit(0, False, budget)

        @cache
        def dfs(cur_node: int, discount: bool) -> dict:
            if discount:
                cost = present[cur_node] // 2
            else:
                cost = present[cur_node]
            profit = future[cur_node] - cost
            buy = defaultdict(int)
            if cost <= budget:
                buy[cost] = profit
            no_buy = defaultdict(int)
            no_buy[0] = 0
            for child_node in adj_list[cur_node]:
                discount_used = dfs(child_node, True)
                discount_not_used = dfs(child_node, False)
                new_buy = defaultdict(int)
                for cur_cost, cur_profit in buy.items():
                    for child_cost, child_profit in discount_used.items():
                        total_cost = cur_cost + child_cost
                        if total_cost <= budget:
                            total_profit = cur_profit + child_profit
                            if (
                                total_cost not in new_buy
                                or new_buy[total_cost] < total_profit
                            ):
                                new_buy[total_cost] = total_profit
                buy = new_buy
                new_no_buy = defaultdict(int)
                for cur_cost, cur_profit in no_buy.items():
                    for child_cost, child_profit in discount_not_used.items():
                        total_cost = cur_cost + child_cost
                        if total_cost <= budget:
                            total_profit = cur_profit + child_profit
                            if (
                                total_cost not in new_no_buy
                                or new_no_buy[total_cost] < total_profit
                            ):
                                new_no_buy[total_cost] = total_profit
                no_buy = new_no_buy
            max_profits = {}
            for cost, profit in buy.items():
                if cost not in max_profits or max_profits[cost] < profit:
                    max_profits[cost] = profit
            for cost, profit in no_buy.items():
                if cost not in max_profits or max_profits[cost] < profit:
                    max_profits[cost] = profit
            return max_profits

        max_profits = dfs(0, False)
        if not max_profits:
            return 0
        else:
            return max(max_profits.values())
