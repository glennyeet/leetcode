from collections import deque
from typing import List


class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        # BFS: O(m * n) time, O(m * n) space

        m = len(grid)
        n = len(grid[0])
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
        starting_health = health - grid[0][0]
        queue = deque(((0, 0, starting_health),))
        max_health = [[0] * n for _ in range(m)]
        max_health[0][0] = starting_health
        while queue:
            i, j, cur_health = queue.popleft()
            if cur_health < 1:
                continue
            if i == m - 1 and j == n - 1:
                return True
            for di, dj in directions:
                ni = i + di
                nj = j + dj
                if 0 <= ni < m and 0 <= nj < n:
                    new_health = cur_health - grid[ni][nj]
                    if new_health > max_health[ni][nj]:
                        max_health[ni][nj] = new_health
                        queue.append((ni, nj, new_health))
        return False
