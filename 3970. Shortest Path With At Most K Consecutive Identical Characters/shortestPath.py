from collections import defaultdict
from heapq import heappop, heappush
from typing import List


class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        # Dijkstra's Algorithm: O(n * k + e * k * log(e * k)) time, O(n * k + m * k)

        adj_list = defaultdict(list)
        for u, v, w in edges:
            adj_list[u].append((v, w))
        min_total = defaultdict(lambda: float("inf"))
        priority_queue = []
        heappush(priority_queue, (0, 1, 0))
        min_total[(0, 1)] = 0
        while priority_queue:
            dist, consecutive_identical_chars, u = heappop(priority_queue)
            if u == n - 1:
                return dist
            if min_total[(u, consecutive_identical_chars)] < dist:
                continue
            for v, w in adj_list[u]:
                new_dist = dist + w
                new_consecutive_identital_chars = 1
                if labels[v] == labels[u]:
                    new_consecutive_identital_chars += consecutive_identical_chars
                if (
                    new_consecutive_identital_chars <= k
                    and new_dist < min_total[(v, new_consecutive_identital_chars)]
                ):
                    heappush(
                        priority_queue, (new_dist, new_consecutive_identital_chars, v)
                    )
                    min_total[(v, new_consecutive_identital_chars)] = new_dist
        return -1
