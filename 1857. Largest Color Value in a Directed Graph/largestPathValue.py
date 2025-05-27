from typing import List
from collections import defaultdict, deque


class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        # BFS: O(v + e) time, O(e + n) space, where v is the number of
        # vertices and e is the number of edges

        n = len(colors)
        adj_list = defaultdict(list)
        in_degree = [0] * n
        for a, b in edges:
            adj_list[a].append(b)
            in_degree[b] += 1
        colour_values = [[0] * 26 for _ in range(n)]
        queue = deque()
        for node in range(n):
            if in_degree[node] == 0:
                queue.append(node)
                colour = ord(colors[node]) - ord("a")
                colour_values[node][colour] = 1
        while queue:
            cur_node = queue.popleft()
            for neighbour_node in adj_list[cur_node]:
                for colour in range(26):
                    if colour == ord(colors[neighbour_node]) - ord("a"):
                        colour_values[neighbour_node][colour] = max(
                            colour_values[neighbour_node][colour],
                            colour_values[cur_node][colour] + 1,
                        )
                    else:
                        colour_values[neighbour_node][colour] = max(
                            colour_values[neighbour_node][colour],
                            colour_values[cur_node][colour],
                        )
                in_degree[neighbour_node] -= 1
                if in_degree[neighbour_node] == 0:
                    queue.append(neighbour_node)
        for degree in in_degree:
            if degree > 0:
                return -1
        largest_colour_value = 0
        for node in range(n):
            largest_colour_value = max(largest_colour_value, max(colour_values[node]))
        return largest_colour_value
