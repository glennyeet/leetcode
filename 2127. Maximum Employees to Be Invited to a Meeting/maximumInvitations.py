from collections import defaultdict, deque


class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        # Graph: O(n) time, O(n) space

        n = len(favorite)
        max_closed_circle_cycle = 0
        global_visited = [False] * n
        non_closed_circle_cycles = []
        for i in range(n):
            if global_visited[i]:
                continue
            start_node = i
            cur_node = i
            local_visited = set()
            while not global_visited[cur_node]:
                global_visited[cur_node] = True
                local_visited.add(cur_node)
                cur_node = favorite[cur_node]
            if cur_node in local_visited:
                cycle_length = len(local_visited)
                while start_node != cur_node:
                    cycle_length -= 1
                    start_node = favorite[start_node]
                max_closed_circle_cycle = max(max_closed_circle_cycle, cycle_length)
                if cycle_length == 2:
                    non_closed_circle_cycles.append((cur_node, favorite[cur_node]))
        inverted_graph = defaultdict(list)
        for dest_node, src_node in enumerate(favorite):
            inverted_graph[src_node].append(dest_node)

        def bfs(src_node: int, parent_node: int) -> int:
            queue = deque([(src_node, 0)])
            max_non_closed_circle = 0
            while queue:
                cur_node, non_closed_circle = queue.popleft()
                if cur_node == parent_node:
                    continue
                max_non_closed_circle = max(max_non_closed_circle, non_closed_circle)
                for neighbour_node in inverted_graph[cur_node]:
                    queue.append((neighbour_node, non_closed_circle + 1))
            return max_non_closed_circle

        non_closed_circle_sum = 0
        for node1, node2 in non_closed_circle_cycles:
            non_closed_circle_sum += bfs(node1, node2) + bfs(node2, node1) + 2
        return max(max_closed_circle_cycle, non_closed_circle_sum)
