from typing import List
from collections import Counter


class UnionFind:
    def __init__(self, n: int) -> None:
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, x: int) -> int:
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> None:
        x_parent = self.find(x)
        y_parent = self.find(y)
        if self.rank[x_parent] > self.rank[y_parent]:
            self.parent[y_parent] = x_parent
            self.rank[x_parent] += self.rank[y_parent]
        else:
            self.parent[x_parent] = y_parent
            self.rank[y_parent] += self.rank[x_parent]


class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        # Union Find: O(n + e * α(n)) time, O(n) space, where e is the size of edges

        uf = UnionFind(n)
        for a, b in edges:
            uf.union(a, b)
        node_counter = Counter()
        connected_components = set()
        for node in range(n):
            parent_node = uf.find(node)
            node_counter[parent_node] += 1
            connected_components.add(parent_node)
        edge_counter = Counter()
        for a, b in edges:
            parent_node = uf.find(a)
            edge_counter[parent_node] += 1
        complete_connected_components = 0
        for parent_node in connected_components:
            nodes = node_counter[parent_node]
            edges = edge_counter[parent_node]
            if edges == nodes * (nodes - 1) // 2:
                complete_connected_components += 1
        return complete_connected_components
