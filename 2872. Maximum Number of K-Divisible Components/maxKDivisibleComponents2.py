from typing import List
from collections import defaultdict


class Solution:
    def maxKDivisibleComponents(
        self, n: int, edges: List[List[int]], values: List[int], k: int
    ) -> int:
        # DFS: O(n) time, O(n) space

        adj_list = defaultdict(list)
        for a, b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)
        max_components = 0

        def find_max_components(cur_node: int, parent_node: int) -> int:
            total_value = values[cur_node]
            for child_node in adj_list[cur_node]:
                if child_node != parent_node:
                    total_value += find_max_components(child_node, cur_node)
            if total_value % k == 0:
                nonlocal max_components
                max_components += 1
            return total_value

        find_max_components(0, -1)
        return max_components
