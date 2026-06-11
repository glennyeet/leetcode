from collections import defaultdict
from typing import List


class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        # DFS + Math: O(n) time, O(n) space, where n is the
        # size of edges

        mod_factor = 10**9 + 7
        adj_list = defaultdict(list)
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        visited = set()

        def dfs(u: int) -> int:
            visited.add(u)
            max_depth = 0
            for v in adj_list[u]:
                if v not in visited:
                    max_depth = max(max_depth, 1 + dfs(v))
            return max_depth

        max_depth = dfs(1)
        ways = pow(2, max_depth - 1, mod_factor)
        return ways
