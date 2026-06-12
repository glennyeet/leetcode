from collections import defaultdict
from typing import List


class Solution:
    def assignEdgeWeights(
        self, edges: List[List[int]], queries: List[List[int]]
    ) -> List[int]:
        # DFS + Math: O(n * log(n) + q * log(n)) timee,
        # O(n * log(n)) space, where q is the size of queries

        mod_factor = 10**9 + 7
        n = len(edges) + 1
        max_ancestor_power = 18
        adj_list = defaultdict(list)
        for u, v in edges:
            u -= 1
            v -= 1
            adj_list[u].append(v)
            adj_list[v].append(u)
        timer = 0
        time_in = [None] * n
        time_out = [None] * n
        distances = [None] * n
        parents = [[None] * n for _ in range(max_ancestor_power)]

        def dfs(cur_node: int, parent_node: int, d: int) -> None:
            nonlocal timer
            timer += 1
            time_in[cur_node] = timer
            distances[cur_node] = d
            parents[0][cur_node] = parent_node
            for i in range(1, max_ancestor_power):
                parents[i][cur_node] = parents[i - 1][parents[i - 1][cur_node]]
            for neighbour_node in adj_list[cur_node]:
                if neighbour_node != parent_node:
                    dfs(neighbour_node, cur_node, d + 1)
            timer += 1
            time_out[cur_node] = timer

        dfs(0, 0, 0)

        def is_ancestor(ancestor: int, node: int) -> bool:
            return (
                time_in[ancestor] <= time_in[node]
                and time_out[node] <= time_out[ancestor]
            )

        def lowest_common_ancestor(u: int, v: int) -> int:
            if is_ancestor(u, v):
                return u
            elif is_ancestor(v, u):
                return v
            for i in reversed(range(max_ancestor_power)):
                if not is_ancestor(parents[i][u], v):
                    u = parents[i][u]
            return parents[0][u]

        def distance(u: int, v: int) -> int:
            lca = lowest_common_ancestor(u, v)
            return distances[u] + distances[v] - 2 * distances[lca]

        answer = []
        for u, v in queries:
            u -= 1
            v -= 1
            if u == v:
                ways = 0
            else:
                dist = distance(u, v)
                ways = pow(2, dist - 1, mod_factor)
            answer.append(ways)
        return answer
