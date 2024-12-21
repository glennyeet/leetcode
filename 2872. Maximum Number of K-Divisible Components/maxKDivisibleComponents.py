from collections import defaultdict


class Solution:
    def maxKDivisibleComponents(
        self, n: int, edges: List[List[int]], values: List[int], k: int
    ) -> int:
        adj_list = defaultdict(list)
        for a, b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)
        max_components = 0

        def dfs(cur: int, parent: int):
            total = values[cur]
            for child in adj_list[cur]:
                if child != parent:
                    total += dfs(child, cur)
            if total % k == 0:
                nonlocal max_components
                max_components += 1
            return total

        dfs(0, None)
        return max_components
