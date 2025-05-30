from typing import List


class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        # BFS: O(n) time, O(n) space

        n = len(edges)

        def find_distances(start_node: int) -> list[int]:
            distances = [float("inf")] * n
            distances[start_node] = 0
            cur_node = start_node
            while edges[cur_node] != -1:
                next_node = edges[cur_node]
                if distances[next_node] != float("inf"):
                    break
                distances[next_node] = distances[cur_node] + 1
                cur_node = next_node
            return distances

        node1_distances = find_distances(node1)
        node2_distances = find_distances(node2)
        min_index = -1
        min_distance = float("inf")
        for i in range(n):
            distance = max(node1_distances[i], node2_distances[i])
            if distance < min_distance:
                min_index = i
                min_distance = distance
        return min_index
