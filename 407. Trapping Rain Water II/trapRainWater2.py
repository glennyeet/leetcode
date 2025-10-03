from typing import List
from heapq import heappush, heappop


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        # Priority Queue + BFS:  O((r * c)log(r * c)) time, O(r * c) space

        r = len(heightMap)
        c = len(heightMap[0])
        min_priority_queue = []
        visited = [[False] * c for _ in range(r)]
        for row in range(r):
            for col in range(c):
                if row in [0, r - 1] or col in [0, c - 1]:
                    heappush(min_priority_queue, (heightMap[row][col], row, col))
                    visited[row][col] = True
        water_volume = 0
        max_height = -1
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        while min_priority_queue:
            height, row, col = heappop(min_priority_queue)
            max_height = max(max_height, height)
            water_volume += max_height - height
            for dr, dc in directions:
                new_row = row + dr
                new_col = col + dc
                if (
                    0 <= new_row < r
                    and 0 <= new_col < c
                    and not visited[new_row][new_col]
                ):
                    heappush(
                        min_priority_queue,
                        (heightMap[new_row][new_col], new_row, new_col),
                    )
                    visited[new_row][new_col] = True
        return water_volume
