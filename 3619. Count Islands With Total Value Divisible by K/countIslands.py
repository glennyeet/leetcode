from typing import List


class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        # DFS: O(m * n) time, O(m * n) space

        m = len(grid)
        n = len(grid[0])
        visited = [[False] * n for _ in range(m)]
        directions = ((0, 1), (1, 0), (0, -1), (-1, 0))

        def dfs(i: int, j: int) -> int:
            visited[i][j] = True
            total_value = grid[i][j]
            for di, dj in directions:
                ni = i + di
                nj = j + dj
                if (
                    0 <= ni < m
                    and 0 <= nj < n
                    and grid[ni][nj] > 0
                    and not visited[ni][nj]
                ):
                    total_value += dfs(ni, nj)
            return total_value

        divisible_islands = 0
        for i in range(m):
            for j in range(n):
                if not visited[i][j] and grid[i][j] > 0:
                    total_value = dfs(i, j)
                    divisible_islands += total_value % k == 0
        return divisible_islands
