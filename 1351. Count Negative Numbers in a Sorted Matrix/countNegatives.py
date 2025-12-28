from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        # Enumeration: O(n * m) time, O(1) space

        n = len(grid)
        m = len(grid[0])
        negative_nums = 0
        for i in range(n):
            for j in range(m):
                negative_nums += grid[i][j] < 0
        return negative_nums
