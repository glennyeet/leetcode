from typing import List
from collections import defaultdict
from heapq import heappop, heappush


class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        # Dijkstra's algorithm: O((n + e) * log(n)) time,
        # O(n + e) space, where e is the size of edges

        adj_list = defaultdict(list)
        for u, v, w in edges:
            adj_list[u].append((v, w))
            adj_list[v].append((u, 2 * w))
        priority_queue = [(0, 0)]
        min_cost = [float("inf")] * n
        min_cost[0] = 0
        while priority_queue:
            cur_cost, u = heappop(priority_queue)
            if cur_cost > min_cost[u]:
                continue
            for v, w in adj_list[u]:
                new_cost = cur_cost + w
                if new_cost < min_cost[v]:
                    min_cost[v] = new_cost
                    heappush(priority_queue, (min_cost[v], v))
        if min_cost[n - 1] == float("inf"):
            return -1
        else:
            return min_cost[n - 1]
