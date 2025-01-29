from collections import defaultdict


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # DFS: O(n) time, O(n) space

        # n = len(edges)
        # adj_list = defaultdict(list)
        # for a, b in edges:
        #     adj_list[a].append(b)
        #     adj_list[b].append(a)
        # visited = [False] * (n + 1)
        # cycle_nodes = set()
        # cycle_start_node = -1

        # def find_cycle(cur_node: int, parent_node: int) -> bool:
        #     if visited[cur_node]:
        #         nonlocal cycle_start_node
        #         cycle_start_node = cur_node
        #         return True
        #     visited[cur_node] = True
        #     for neighbour_node in adj_list[cur_node]:
        #         if neighbour_node == parent_node:
        #             continue
        #         if find_cycle(neighbour_node, cur_node):
        #             if cycle_start_node != -1:
        #                 cycle_nodes.add(cur_node)
        #             if cur_node == cycle_start_node:
        #                 cycle_start_node = -1
        #             return True
        #     return False

        # find_cycle(1, -1)
        # for a, b in reversed(edges):
        #     if a in cycle_nodes and b in cycle_nodes:
        #         return [a, b]
        # return []

        # Union Find: O(n * α(n)) time, O(n) space

        n = len(edges)
        parent = [i for i in range(n + 1)]
        rank = [1] * (n + 1)

        def find(node: int) -> int:
            if node != parent[node]:
                parent[node] = find(parent[node])
            return parent[node]

        def union(node1: int, node2: int) -> bool:
            parent1 = find(node1)
            parent2 = find(node2)
            if parent1 == parent2:
                return False
            if rank[parent1] > rank[parent2]:
                parent[parent2] = parent1
                rank[parent1] += rank[parent2]
            else:
                parent[parent1] = parent2
                rank[parent2] += rank[parent1]
            return True

        for a, b in edges:
            if not union(a, b):
                return [a, b]
        return []
