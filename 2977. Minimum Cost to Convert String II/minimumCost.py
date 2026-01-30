from typing import List
from collections import defaultdict
from heapq import heappush, heappop
from functools import cache


class Solution:
    def minimumCost(
        self,
        source: str,
        target: str,
        original: List[str],
        changed: List[str],
        cost: List[int],
    ) -> int:
        # Dijkstra's Algorithm + Top-down DP: O(m^2 * log(m) + n * m * (n + o)) time,
        # O(m + n) space, where o is the size of the largest string in original

        m = len(original)
        n = len(source)
        adj_list = defaultdict(list)
        for x, y, z in zip(original, changed, cost):
            adj_list[x].append((y, z))
        min_cost = defaultdict(lambda: defaultdict(lambda: float("inf")))

        def get_min_costs(start: str) -> None:
            priority_queue = [(0, start)]
            min_cost[start][start] = 0
            while priority_queue:
                cur_cost, u = heappop(priority_queue)
                if cur_cost > min_cost[start][u]:
                    continue
                for v, uv_cost in adj_list[u]:
                    new_cost = cur_cost + uv_cost
                    if new_cost < min_cost[start][v]:
                        min_cost[start][v] = new_cost
                        heappush(priority_queue, (new_cost, v))

        for x in original:
            get_min_costs(x)

        @cache
        def get_min_source_to_target_cost(index: int) -> int:
            if index == n:
                return 0
            min_source_to_target_cost = float("inf")
            if source[index] == target[index]:
                min_source_to_target_cost = min(
                    min_source_to_target_cost, get_min_source_to_target_cost(index + 1)
                )
            for i in range(m):
                if source[index:].startswith(original[i]):
                    x_len = len(original[i])
                    if target[index : index + x_len] in min_cost[original[i]]:
                        min_source_to_target_cost = min(
                            min_source_to_target_cost,
                            get_min_source_to_target_cost(index + x_len)
                            + min_cost[original[i]][target[index : index + x_len]],
                        )
            return min_source_to_target_cost

        min_source_to_target_cost = get_min_source_to_target_cost(0)
        if min_source_to_target_cost == float("inf"):
            return -1
        return min_source_to_target_cost
