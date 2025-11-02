from typing import List


class Solution:
    def countUnguarded(
        self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]
    ) -> int:
        # Simulation: O(m * n) time, O(m * n) space

        grid = [[0] * n for _ in range(m)]
        for i, j in walls:
            grid[i][j] = 1
        for i, j in guards:
            grid[i][j] = 2
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        for i1, j1 in guards:
            for di, dj in directions:
                i2 = i1 + di
                j2 = j1 + dj
                while (
                    0 <= i2 < m
                    and 0 <= j2 < n
                    and (grid[i2][j2] == 0 or grid[i2][j2] == 3)
                ):
                    if grid[i2][j2] == 0:
                        grid[i2][j2] = 3
                    i2 += di
                    j2 += dj
        unguarded_cells = 0
        for i in range(m):
            for j in range(n):
                unguarded_cells += grid[i][j] == 0
        return unguarded_cells
