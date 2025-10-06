from typing import List
from heapq import heappop, heappush


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # Dijkstra's Algorithm: O(n^2 * log(n)) time, O(n) space

        n = len(grid)
        visited = [[False] * n for _ in range(n)]
        priority_queue = [(grid[0][0], 0, 0)]
        min_time = [[float("inf")] * n for _ in range(n)]
        min_time[0][0] = grid[0][0]
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        while priority_queue:
            _, i, j = heappop(priority_queue)
            visited[i][j] = True
            for di, dj in directions:
                i2 = i + di
                j2 = j + dj
                if (
                    0 <= i2 < n
                    and 0 <= j2 < n
                    and not visited[i2][j2]
                    and max(min_time[i][j], grid[i2][j2]) < min_time[i2][j2]
                ):
                    time = max(min_time[i][j], grid[i2][j2])
                    min_time[i2][j2] = time
                    heappush(priority_queue, (time, i2, j2))
        return min_time[n - 1][n - 1]
