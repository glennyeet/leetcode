from collections import deque, defaultdict


class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        # BFS: O(n * (n + m)) time, O(n) space
        adj_list = defaultdict(list)
        for a, b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)
        visited = set()

        def get_connected_component(start_node: int) -> list[int]:
            nodes = set([start_node])
            queue = deque([start_node])
            while queue:
                cur_node = queue.popleft()
                for neighbour_node in adj_list[cur_node]:
                    if neighbour_node in nodes:
                        continue
                    visited.add(neighbour_node)
                    nodes.add(neighbour_node)
                    queue.append(neighbour_node)
            return nodes

        def count_component_groups(start_node: int) -> int:
            group = {start_node: 1}
            queue = deque([(start_node, 1)])
            groups = 1
            while queue:
                cur_node, cur_node_group = queue.popleft()
                for neighbour_node in adj_list[cur_node]:
                    if neighbour_node in group:
                        if group[neighbour_node] == cur_node_group:
                            return -1
                        continue
                    neighbour_node_group = cur_node_group + 1
                    group[neighbour_node] = neighbour_node_group
                    queue.append((neighbour_node, neighbour_node_group))
                    groups = max(groups, neighbour_node_group)
            return groups

        max_groups = 0
        for i in range(1, n + 1):
            if i in visited:
                continue
            visited.add(i)
            component = get_connected_component(i)
            total_groups = 0
            for node in component:
                groups = count_component_groups(node)
                if groups == -1:
                    return -1
                total_groups = max(total_groups, groups)
            max_groups += total_groups
        return max_groups
