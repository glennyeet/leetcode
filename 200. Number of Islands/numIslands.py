from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # BFS: O(m * n) time, O(m * n) space

        m = len(grid)
        n = len(grid[0])
        visited = [[False] * n for _ in range(m)]

        def mark_island(start: tuple[int, int]) -> None:
            queue = deque([start])
            directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
            while queue:
                x, y = queue.popleft()
                for dx, dy in directions:
                    x2 = x + dx
                    y2 = y + dy
                    if (
                        0 <= x2 < m
                        and 0 <= y2 < n
                        and grid[x2][y2] == "1"
                        and not visited[x2][y2]
                    ):
                        visited[x2][y2] = True
                        queue.append((x2, y2))
            return

        islands = 0
        for x in range(m):
            for y in range(n):
                if grid[x][y] == "1" and not visited[x][y]:
                    islands += 1
                    visited[x][y] = True
                    mark_island((x, y))
        return islands
