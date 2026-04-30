from typing import List
from functools import cache


class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        # Top-down DP: O(m * n * k) time, O(m * n * k) space

        m = len(grid)
        n = len(grid[0])
        directions = ((0, 1), (1, 0))

        @cache
        def dp(i: int, j: int, cost: int) -> int:
            if grid[i][j] == 0:
                new_cost = cost
            else:
                new_cost = cost + 1
            if new_cost > k:
                return -1
            if i == m - 1 and j == n - 1:
                return grid[i][j]
            max_score = -1
            for di, dj in directions:
                new_i = i + di
                new_j = j + dj
                if 0 <= new_i < m and 0 <= new_j < n:
                    future_score = dp(new_i, new_j, new_cost)
                    if future_score > -1:
                        max_score = max(max_score, grid[i][j] + future_score)
            return max_score

        max_score = dp(0, 0, 0)
        dp.cache_clear()
        return max_score
