from typing import List
from heapq import heappush, heappop


class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        # BFS: O(qlog(q) + m * nlog(m * n)) time, O(m * n) space
        m = len(grid)
        n = len(grid[0])
        q = len(queries)
        grid_priority_queue = [(grid[0][0], 0, 0)]
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        visited_cells = set([(0, 0)])
        sorted_queries = []
        for i, query in enumerate(queries):
            sorted_queries.append((query, i))
        sorted_queries.sort()
        current_points = 0
        answer = [0] * q
        for query, i in sorted_queries:
            while grid_priority_queue and grid_priority_queue[0][0] < query:
                _, x1, y1 = heappop(grid_priority_queue)
                current_points += 1
                for dx, dy in directions:
                    x2 = x1 + dx
                    y2 = y1 + dy
                    if 0 <= x2 < m and 0 <= y2 < n and (x2, y2) not in visited_cells:
                        heappush(grid_priority_queue, (grid[x2][y2], x2, y2))
                        visited_cells.add((x2, y2))
            answer[i] = current_points
        return answer
