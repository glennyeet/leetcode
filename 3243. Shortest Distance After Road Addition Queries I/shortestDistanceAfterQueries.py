from collections import defaultdict
from math import inf
from heapq import heappop, heappush


class Solution:
    def shortestDistanceAfterQueries(
        self, n: int, queries: List[List[int]]
    ) -> List[int]:
        adj_list = defaultdict(list)
        for i in range(n - 1):
            adj_list[i].append(i + 1)

        def dijkstra() -> int:
            dist = [inf] * n
            dist[0] = 0
            visited = [False] * n
            p_queue = [(0, 0)]
            while p_queue:
                u_dist, u = heappop(p_queue)
                if u == n - 1:
                    return u_dist
                elif visited[u]:
                    continue
                visited[u] = True
                for v in adj_list[u]:
                    new_dist = u_dist + 1
                    if new_dist < dist[v]:
                        dist[v] = new_dist
                        heappush(p_queue, (new_dist, v))
            return inf

        answer = []
        for u, v in queries:
            adj_list[u].append(v)
            answer.append(dijkstra())
        return answer
