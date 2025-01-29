from collections import defaultdict


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # DFS: O(n) time, O(n) space

        n = len(edges)
        adj_list = defaultdict(list)
        for a, b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)
        visited = [False] * (n + 1)
        cycle_nodes = set()
        cycle_start_node = -1

        def find_cycle(cur_node: int, parent_node: int) -> bool:
            if visited[cur_node]:
                nonlocal cycle_start_node
                cycle_start_node = cur_node
                return True
            visited[cur_node] = True
            for neighbour_node in adj_list[cur_node]:
                if neighbour_node == parent_node:
                    continue
                if find_cycle(neighbour_node, cur_node):
                    if cycle_start_node != -1:
                        cycle_nodes.add(cur_node)
                    if cur_node == cycle_start_node:
                        cycle_start_node = -1
                    return True
            return False

        find_cycle(1, -1)
        for a, b in reversed(edges):
            if a in cycle_nodes and b in cycle_nodes:
                return [a, b]
        return []
