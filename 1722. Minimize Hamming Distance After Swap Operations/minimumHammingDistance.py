from typing import List
from collections import defaultdict, Counter


class Solution:
    def minimumHammingDistance(
        self, source: List[int], target: List[int], allowedSwaps: List[List[int]]
    ) -> int:
        # Union Find + Hash Table: O(m * α(n) + n) time, O(n) space, where m is
        # the size of allowedSwaps

        n = len(source)
        parent = [i for i in range(n)]
        rank = [0] * n

        def union(x: int, y: int) -> None:
            root_x = find(x)
            root_y = find(y)
            if root_x == root_y:
                return
            if rank[root_x] < rank[root_y]:
                root_x, root_y = root_y, root_x
            parent[root_y] = root_x
            if rank[root_x] == rank[root_y]:
                rank[root_x] += 1

        def find(x: int) -> int:
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        for a, b in allowedSwaps:
            union(a, b)
        delta = defaultdict(Counter)
        for i in range(n):
            component = find(i)
            delta[component][source[i]] += 1
            delta[component][target[i]] -= 1
        min_hamming_dist = 0
        for i in range(n):
            for j in delta[i].values():
                if j > 0:
                    min_hamming_dist += j
        return min_hamming_dist
