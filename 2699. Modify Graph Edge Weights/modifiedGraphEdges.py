from collections import defaultdict
import heapq


class Solution:
    def modifiedGraphEdges(
        self, n: int, edges: List[List[int]], source: int, destination: int, target: int
    ) -> List[List[int]]:
        inf = 10**9
        adj_list = defaultdict(lambda: defaultdict(int))
        nedges = []
        for u, v, w in edges:
            if w == -1:
                nedges.append((u, v))
                adj_list[u][v] = inf
                adj_list[v][u] = inf
            else:
                adj_list[u][v] = w
                adj_list[v][u] = w

        def dijkstra(adj_list: defaultdict[int, defaultdict[int, int]]) -> int:
            dist = [inf] * n
            dist[source] = 0
            visited = [False] * n
            p_queue = [(0, source)]
            while len(p_queue) > 0:
                u_w, u = heapq.heappop(p_queue)
                if u == destination:
                    return u_w
                elif visited[u]:
                    continue
                visited[u] = True
                for v, v_w in adj_list[u].items():
                    new_dist = u_w + v_w
                    if new_dist < dist[v]:
                        dist[v] = new_dist
                        heapq.heappush(p_queue, (new_dist, v))
            return inf

        def get_edge_array(
            adj_list: defaultdict[int, defaultdict[int, int]]
        ) -> list[int]:
            edges = []
            for u in adj_list.keys():
                for v in adj_list[u].keys():
                    if u < v:
                        edges.append((u, v, adj_list[u][v]))
            return edges

        min_dist = dijkstra(adj_list)
        if min_dist < target:
            return []
        elif min_dist == target:
            return get_edge_array(adj_list)
        for u, v in nedges:
            adj_list[u][v] = 1
            adj_list[v][u] = 1
            min_dist = dijkstra(adj_list)
            if min_dist == target:
                return get_edge_array(adj_list)
            elif min_dist < target:
                delta = target - min_dist
                adj_list[u][v] += delta
                adj_list[v][u] += delta
                return get_edge_array(adj_list)
        return []
