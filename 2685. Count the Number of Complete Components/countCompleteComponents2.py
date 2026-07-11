from typing import List


class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        # Union-Find: O(α(n) * m + n) time, O(n) space, where e is the size
        # of edges

        parent = [x for x in range(n)]

        def find(x: int) -> int:
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x: int, y: int) -> None:
            px = find(x)
            py = find(y)
            parent[px] = py

        for a, b in edges:
            union(a, b)
        edge_count = [0] * n
        for a, b in edges:
            edge_count[find(a)] += 1
        vertex_count = [0] * n
        for a in range(n):
            vertex_count[find(a)] += 1
        complete_connected_components = 0
        for a in range(n):
            vertices = vertex_count[a]
            if vertices > 0:
                if edge_count[a] == vertices * (vertices - 1) // 2:
                    complete_connected_components += 1
        return complete_connected_components
