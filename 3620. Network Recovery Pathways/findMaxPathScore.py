from collections import defaultdict
from heapq import heappop, heappush
from typing import List


class Solution:
    def findMaxPathScore(
        self, edges: List[List[int]], online: List[bool], k: int
    ) -> int:
        # Dijkstra's Algorithm + Binary Search:
        # O((n + e) * log(n) * log(c)) time, O(n + e) space, e
        # is the number of edges, and c is the max edge cost

        n = len(online)
        adj_list = defaultdict(list)
        right = 0
        for u, v, cost in edges:
            adj_list[u].append((v, cost))
            right = max(right, cost)

        def is_valid_path(score: int) -> bool:
            priority_queue = []
            min_cost = [float("inf")] * n
            min_cost[0] = 0
            heappush(priority_queue, (0, 0))
            while priority_queue:
                cost, u = heappop(priority_queue)
                if min_cost[u] != cost:
                    continue
                if u == n - 1:
                    return True
                for v, cost in adj_list[u]:
                    new_cost = min_cost[u] + cost
                    if (
                        online[v]
                        and cost >= score
                        and min_cost[v] > new_cost
                        and new_cost <= k
                    ):
                        heappush(priority_queue, (new_cost, v))
                        min_cost[v] = new_cost
            return False

        left = -1
        while left < right:
            mid = (left + right + 1) // 2
            if is_valid_path(mid):
                left = mid
            else:
                right = mid - 1
        return left
