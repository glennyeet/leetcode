from collections import deque
from math import inf


class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        # BFS: O(m * n) time, O(m * n) space

        m = len(isWater)
        n = len(isWater[0])
        queue = deque()
        max_heights = [[inf] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if isWater[i][j]:
                    queue.append((i, j, 0))
                    max_heights[i][j] = 0
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        while queue:
            x, y, distance = queue.popleft()
            for dx, dy in directions:
                x2 = x + dx
                y2 = y + dy
                if (
                    0 <= x2 < m
                    and 0 <= y2 < n
                    and not isWater[x2][y2]
                    and max_heights[x2][y2] == inf
                ):
                    new_distance = distance + 1
                    queue.append((x2, y2, new_distance))
                    max_heights[x2][y2] = new_distance
        return max_heights
