from typing import List


class UnionFind:
    def __init__(self, n: int) -> None:
        self.parent = [i for i in range(n)]
        self.size = [1] * n

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> None:
        ux = self.find(x)
        uy = self.find(y)
        if ux == uy:
            return
        if self.size[ux] > self.size[uy]:
            self.parent[uy] = ux
            self.size[ux] += self.size[uy]
        else:
            self.parent[ux] = uy
            self.size[uy] += self.size[ux]

    def size(self, x: int) -> int:
        root = self.find(x)
        return self.size[root]


class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        # Union Find: O(n^2) time, O(n^2) space

        n = len(lcp)
        for i in range(n):
            if lcp[i][i] != n - i:
                return ""
            for j in range(n):
                if lcp[i][j] != lcp[j][i]:
                    return ""
                elif lcp[i][j] > n - i:
                    return ""
                elif lcp[i][j] > n - j:
                    return ""
        uf = UnionFind(n)
        for i in range(n):
            for j in range(i + 1, n):
                if lcp[i][j] > 0:
                    uf.union(i, j)
        cur_group = 0
        groups = {}
        for i in range(n):
            parent_group = uf.find(i)
            if parent_group not in groups:
                groups[parent_group] = cur_group
                cur_group += 1
        if cur_group > 26:
            return ""
        word = []
        for i in range(n):
            group = uf.find(i)
            word.append(chr(groups[group] + ord("a")))
        lcp2 = [[0] * n for _ in range(n)]
        for i in reversed(range(n)):
            for j in reversed(range(n)):
                if word[i] == word[j]:
                    lcp2[i][j] = 1
                    if i + 1 < n and j + 1 < n:
                        lcp2[i][j] = lcp2[i + 1][j + 1] + 1
        if lcp == lcp2:
            return "".join(word)
        return ""
