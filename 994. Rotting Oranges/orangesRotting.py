from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # BFS: O(m * n) time, O(m * n) space

        m = len(grid)
        n = len(grid[0])
        visited = [[False] * n for _ in range(m)]
        queue = deque()
        fresh_oranges = 0
        rotten_oranges = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh_oranges += 1
                elif grid[i][j] == 2:
                    rotten_oranges += 1
                    visited[i][j] = True
                    queue.append((i, j, 0))
        minutes = 0
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        grid_copy = grid.copy()
        while queue:
            x, y, minute = queue.popleft()
            minutes = max(minutes, minute)
            for dx, dy in directions:
                x2 = x + dx
                y2 = y + dy
                if (
                    0 <= x2 < m
                    and 0 <= y2 < n
                    and not visited[x2][y2]
                    and grid_copy[x2][y2] == 1
                ):
                    fresh_oranges -= 1
                    grid_copy[x2][y2] = 2
                    visited[x2][y2] = True
                    queue.append((x2, y2, minute + 1))
        if fresh_oranges > 0:
            return -1
        return minutes
