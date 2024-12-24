from collections import defaultdict
from heapq import heappushpop
from math import ceil


class Solution:
    def minimumDiameterAfterMerge(
        self, edges1: List[List[int]], edges2: List[List[int]]
    ) -> int:
        # DFS: O(m + n) time, O(m + n) space

        def create_adj_list(edges: list[list[int]]) -> defaultdict[int, list[int]]:
            adj_list = defaultdict(list)
            for a, b in edges:
                adj_list[a].append(b)
                adj_list[b].append(a)
            return adj_list

        adj_list1 = create_adj_list(edges1)
        adj_list2 = create_adj_list(edges2)

        def find_diameter(
            adj_list: defaultdict[int, list[int]], cur_node: int, parent_node: int
        ) -> tuple[int, int]:
            max_diameter = 0
            max_child_paths = [0, 0]
            for neighbour_node in adj_list[cur_node]:
                if neighbour_node == parent_node:
                    continue
                neighbour_max_diameter, neighbour_max_child_path = find_diameter(
                    adj_list, neighbour_node, cur_node
                )
                max_diameter = max(max_diameter, neighbour_max_diameter)
                heappushpop(max_child_paths, neighbour_max_child_path)
            max_diameter = max(max_diameter, sum(max_child_paths))
            return (max_diameter, max(max_child_paths) + 1)

        diameter1, _ = find_diameter(adj_list1, 0, -1)
        diameter2, _ = find_diameter(adj_list2, 0, -1)
        return max(diameter1, diameter2, ceil(diameter1 / 2) + ceil(diameter2 / 2) + 1)
