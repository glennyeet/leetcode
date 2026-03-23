from typing import List
from functools import cache


class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        # Top-down DP: O(m * n) time, O(m * n) space

        mod_factor = 10**9 + 7
        m = len(grid)
        n = len(grid[0])

        @cache
        def dp(i: int, j: int):
            if i == m or j == n:
                return float("-inf"), float("inf")
            elif i == m - 1 and j == n - 1:
                return grid[i][j], grid[i][j]
            elif grid[i][j] == 0:
                return 0, 0
            max_down, min_down = dp(i + 1, j)
            max_right, min_right = dp(i, j + 1)
            max_product = max(max_down, max_right) * grid[i][j]
            min_product = min(min_down, min_right) * grid[i][j]
            if grid[i][j] > 0:
                return max_product, min_product
            else:
                return min_product, max_product

        max_product, _ = dp(0, 0)
        if max_product < 0:
            return -1
        return max_product % mod_factor
