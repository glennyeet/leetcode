from typing import List


class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        # One-pass: O(mn) time, O(1) space

        m = len(grid)
        n = len(grid[0])
        min_x = m - 1
        max_x = 0
        min_y = n - 1
        max_y = 0
        for x in range(m):
            for y in range(n):
                if grid[x][y]:
                    min_x = min(min_x, x)
                    max_x = max(max_x, x)
                    min_y = min(min_y, y)
                    max_y = max(max_y, y)
        return (max_x - min_x + 1) * (max_y - min_y + 1)
