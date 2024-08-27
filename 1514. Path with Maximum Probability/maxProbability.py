import collections
import heapq


class Solution:
    def maxProbability(
        self,
        n: int,
        edges: List[List[int]],
        succProb: List[float],
        start_node: int,
        end_node: int,
    ) -> float:
        adj_list = collections.defaultdict(list)
        for (u, v), p in zip(edges, succProb):
            adj_list[u].append((v, p))
            adj_list[v].append((u, p))
        priority_queue = []
        visited = [False for _ in range(n)]
        dist = [0.0 for _ in range(n)]
        dist[start_node] = 1.0
        heapq.heappush(priority_queue, (-1.0, start_node))
        while len(priority_queue) != 0:
            p, u = heapq.heappop(priority_queue)  # p = dist[u]
            p *= -1
            if visited[u]:
                continue
            visited[u] = True
            for v, new_p in adj_list[u]:
                new_dist = p * new_p
                if new_dist > dist[v]:
                    dist[v] = new_dist
                    heapq.heappush(priority_queue, (-new_dist, v))
        return dist[end_node]
