from functools import cache


class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        # Top-down DP + Bit Manipulation: O(m * n * x) time, O(m * n * x)
        # space, where x is the number of possible XOR values

        m = len(grid)
        n = len(grid[0])

        @cache
        def dp(i: int, j: int, xor_val: int) -> float | int:
            if i < 0 or i >= m or j < 0 or j >= n:
                return float("inf")
            new_xor_val = xor_val ^ grid[i][j]
            if i == m - 1 and j == n - 1:
                return new_xor_val
            return min(dp(i, j + 1, new_xor_val), dp(i + 1, j, new_xor_val))

        min_xor_val = dp(0, 0, 0)
        dp.cache_clear()
        return min_xor_val
