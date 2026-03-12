from typing import List


class Solution:
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:
        # Maximum Spanning Tree + Union Find + Greedy: O(n + e * log(e)) time,
        # O(n + e) space, where e is the size of edges

        parents = []
        for i in range(n):
            parents.append(i)

        def find(u: int) -> int:
            if parents[u] != u:
                parents[u] = find(parents[u])
            return parents[u]

        def union(u: int, v: int) -> None:
            u_parent = find(u)
            v_parent = find(v)
            if u_parent != v_parent:
                parents[u_parent] = v_parent

        sorted_edges = []
        edges_left = n - 1
        max_stability = float("inf")
        for u, v, s, must in edges:
            if must == 1:
                if find(u) == find(v):
                    return -1
                union(u, v)
                max_stability = min(max_stability, s)
                edges_left -= 1
            else:
                sorted_edges.append((s, u, v))
        sorted_edges.sort(reverse=True)
        upgradeable_edges = []
        for s, u, v in sorted_edges:
            if find(u) == find(v):
                continue
            union(u, v)
            edges_left -= 1
            upgradeable_edges.append(s)
        upgradeable_edges.reverse()
        for i in range(min(k, len(upgradeable_edges))):
            upgradeable_edges[i] *= 2
        if edges_left > 0:
            return -1
        return min(max_stability, min(upgradeable_edges, default=max_stability))
