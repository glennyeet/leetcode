from typing import List


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        # Simulation: O(k * m * n) time, O(m * n) space

        m = len(grid)
        n = len(grid[0])
        prev_grid = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                prev_grid[i][j] = grid[i][j]
        shifted_grid = grid
        for _ in range(k):
            shifted_grid = [[0] * n for _ in range(m)]
            for i in range(m):
                for j in range(n):
                    if i == m - 1 and j == n - 1:
                        shifted_grid[0][0] = prev_grid[i][j]
                    elif j == n - 1:
                        shifted_grid[i + 1][0] = prev_grid[i][j]
                    else:
                        shifted_grid[i][j + 1] = prev_grid[i][j]
            prev_grid = shifted_grid
        return shifted_grid
