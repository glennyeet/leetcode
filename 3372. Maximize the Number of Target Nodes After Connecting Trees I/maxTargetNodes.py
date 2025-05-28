from typing import List
from collections import defaultdict, deque


class Solution:
    def maxTargetNodes(
        self, edges1: List[List[int]], edges2: List[List[int]], k: int
    ) -> List[int]:
        # BFS: O(m^2 + n^2) time, O(n + m) space

        n = len(edges1) + 1
        m = len(edges2) + 1

        def build_adj_list(edges: list[list[int]]) -> defaultdict[int, list[int]]:
            adj_list = defaultdict(list)
            for u, v in edges:
                adj_list[u].append(v)
                adj_list[v].append(u)
            return adj_list

        adj_list1 = build_adj_list(edges1)
        adj_list2 = build_adj_list(edges2)

        def find_total_targets(
            adj_list: defaultdict[int, list[int]],
            start_node: int,
            total_nodes: int,
            max_distance: int,
        ) -> int:
            queue = deque([start_node])
            distances = [float("inf")] * total_nodes
            distances[start_node] = 0
            while queue:
                cur_node = queue.popleft()
                if distances[cur_node] == max_distance:
                    break
                for neighbour_node in adj_list[cur_node]:
                    if distances[neighbour_node] == float("inf"):
                        distances[neighbour_node] = distances[cur_node] + 1
                        queue.append(neighbour_node)
            targets = 0
            for distance in distances:
                targets += distance <= max_distance
            return targets

        max_target2 = 0
        for node in range(m):
            max_target2 = max(
                max_target2, find_total_targets(adj_list2, node, m, k - 1)
            )
        answer = []
        for i in range(n):
            answer.append(find_total_targets(adj_list1, i, n, k) + max_target2)
        return answer
