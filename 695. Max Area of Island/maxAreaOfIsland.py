from collections import deque


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # BFS: O(m * n) time, O(m * n) space

        m = len(grid)
        n = len(grid[0])
        visited = [[False] * n for _ in range(m)]

        def find_island_area(start: tuple[int, int]) -> int:
            visited[start[0]][start[1]] = True
            queue = deque([start])
            directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
            area = 0
            while queue:
                x, y = queue.popleft()
                area += 1
                for dx, dy in directions:
                    x2 = x + dx
                    y2 = y + dy
                    if (
                        0 <= x2 < m
                        and 0 <= y2 < n
                        and grid[x2][y2]
                        and not visited[x2][y2]
                    ):
                        visited[x2][y2] = True
                        queue.append((x2, y2))
            return area

        max_area = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] and not visited[i][j]:
                    max_area = max(max_area, find_island_area((i, j)))
        return max_area
