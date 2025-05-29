from typing import List
from collections import defaultdict, deque


class Solution:
    def maxTargetNodes(
        self, edges1: List[List[int]], edges2: List[List[int]]
    ) -> List[int]:
        # BFS: O(n + m) time, O(n + m) space

        n = len(edges1) + 1
        m = len(edges2) + 1

        def create_adj_list(edges: list[list[int]]) -> defaultdict[int, list[int]]:
            adj_list = defaultdict(list)
            for u, v in edges:
                adj_list[u].append(v)
                adj_list[v].append(u)
            return adj_list

        adj_list1 = create_adj_list(edges1)
        adj_list2 = create_adj_list(edges2)

        def count_targets(
            adj_list: defaultdict[int, list[int]], start_node: int, total_nodes: int
        ) -> tuple[int, int, list[int]]:
            queue = deque([start_node])
            parities = [float("inf")] * total_nodes
            parities[start_node] = 0
            while queue:
                cur_node = queue.popleft()
                for neighbour_node in adj_list[cur_node]:
                    if parities[neighbour_node] == float("inf"):
                        parities[neighbour_node] = 1 - parities[cur_node]
                        queue.append(neighbour_node)
            even_nodes = 0
            for parity in parities:
                even_nodes += not parity
            return even_nodes, total_nodes - even_nodes, parities

        even_nodes2, odd_nodes2, _ = count_targets(adj_list2, 0, m)
        max_target2 = max(even_nodes2, odd_nodes2)
        even_nodes1, odd_nodes1, parities1 = count_targets(adj_list1, 0, n)
        answer = []
        for i in range(n):
            if not parities1[i]:
                answer.append(even_nodes1 + max_target2)
            else:
                answer.append(odd_nodes1 + max_target2)
        return answer
