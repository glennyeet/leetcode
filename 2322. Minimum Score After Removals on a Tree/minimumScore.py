from typing import List
from collections import defaultdict


class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        # DFS: O(n^2) time, O(n^2) space

        n = len(nums)
        adj_list = defaultdict(list)
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        subtree_sums = [0] * n

        def get_subtree_sums(cur_node: int, par_node: int) -> int:
            subtree_sum = nums[cur_node]
            for nei_node in adj_list[cur_node]:
                if nei_node != par_node:
                    subtree_sum ^= get_subtree_sums(nei_node, cur_node)
            subtree_sums[cur_node] = subtree_sum
            return subtree_sum

        get_subtree_sums(0, -1)
        descendants = [set() for _ in range(n)]

        def get_descendants(cur_node: int, par_node: int) -> int:
            descendants[cur_node] = set([cur_node])
            for nei_node in adj_list[cur_node]:
                if nei_node != par_node:
                    descendants[cur_node] |= get_descendants(nei_node, cur_node)
            return descendants[cur_node]

        get_descendants(0, -1)
        min_removals = float("inf")
        for i in range(1, n):
            for j in range(i + 1, n):
                if j in descendants[i]:
                    c1 = subtree_sums[0] ^ subtree_sums[i]
                    c2 = subtree_sums[i] ^ subtree_sums[j]
                    c3 = subtree_sums[j]
                elif i in descendants[j]:
                    c1 = subtree_sums[0] ^ subtree_sums[j]
                    c2 = subtree_sums[j] ^ subtree_sums[i]
                    c3 = subtree_sums[i]
                else:
                    c1 = subtree_sums[0] ^ subtree_sums[i] ^ subtree_sums[j]
                    c2 = subtree_sums[i]
                    c3 = subtree_sums[j]
                min_removals = min(min_removals, max(c1, c2, c3) - min(c1, c2, c3))
        return min_removals
