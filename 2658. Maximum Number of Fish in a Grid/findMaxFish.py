from collections import deque


class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        # BFS: O(m * n) time, O(m * n) space

        m = len(grid)
        n = len(grid[0])
        visited = [[False] * n for _ in range(m)]

        def find_total_fish(start: tuple[int, int]) -> int:
            visited[start[0]][start[1]] = True
            queue = deque([start])
            directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
            total_fish = 0
            while queue:
                x, y = queue.popleft()
                total_fish += grid[x][y]
                for dx, dy in directions:
                    x2 = x + dx
                    y2 = y + dy
                    if (
                        0 <= x2 < m
                        and 0 <= y2 < n
                        and not visited[x2][y2]
                        and grid[x2][y2] > 0
                    ):
                        visited[x2][y2] = True
                        queue.append((x2, y2))
            return total_fish

        max_fish = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0 and not visited[i][j]:
                    max_fish = max(max_fish, find_total_fish((i, j)))
        return max_fish
