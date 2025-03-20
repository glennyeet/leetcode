from typing import List


class UnionFind:
    def __init__(self, n: int) -> None:
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x: int) -> int:
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> None:
        x = self.find(x)
        y = self.find(y)
        if x != y:
            if self.size[x] < self.size[y]:
                self.parent[x] = y
                self.size[y] += self.size[x]
            else:
                self.parent[y] = x
                self.size[x] += self.size[y]


class Solution:
    def minimumCost(
        self, n: int, edges: List[List[int]], query: List[List[int]]
    ) -> List[int]:
        # Union Find: O(e + q) time, O(n) space, where e is the size
        # of edges, q is the size of query, and n is the number of
        # nodes

        uf = UnionFind(n)
        for u, v, _ in edges:
            uf.union(u, v)
        component_cost = {}
        for u, v, w in edges:
            root = uf.find(u)
            if root not in component_cost:
                component_cost[root] = w
            else:
                component_cost[root] &= w
        answer = []
        for src, dest in query:
            root1 = uf.find(src)
            root2 = uf.find(dest)
            if root1 != root2:
                answer.append(-1)
            else:
                answer.append(component_cost[root1])
        return answer
