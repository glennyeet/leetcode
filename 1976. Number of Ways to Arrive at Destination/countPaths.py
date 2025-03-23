from typing import List
from collections import defaultdict
from heapq import heappop, heappush


class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        # Dijkstra's algorithm: O((n + e)log(n)) time, O(n + e)
        # space, where e is the number of edges

        adj_list = defaultdict(list)
        for u, v, time in roads:
            adj_list[u].append((v, time))
            adj_list[v].append((u, time))
        p_queue = [(0, 0)]
        min_time = [float("inf")] * n
        path_count = [0] * n
        path_count[0] = 1

        while p_queue:
            time, node = heappop(p_queue)
            for neighbour, neighbour_time in adj_list[node]:
                if time + neighbour_time < min_time[neighbour]:
                    min_time[neighbour] = time + neighbour_time
                    path_count[neighbour] = path_count[node]
                    heappush(p_queue, (time + neighbour_time, neighbour))
                elif time + neighbour_time == min_time[neighbour]:
                    path_count[neighbour] = (
                        path_count[neighbour] + path_count[node]
                    ) % (10**9 + 7)
        return path_count[n - 1]
