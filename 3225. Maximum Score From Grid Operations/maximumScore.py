from typing import List
from functools import cache


class Solution:
    def maximumScore(self, grid: List[List[int]]) -> int:
        # Top-down DP: O(n^3) time, O(n^2) space

        n = len(grid)
        prefix_sum = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n):
            score = 0
            for j in range(n):
                score += grid[j][i]
                prefix_sum[j + 1][i] = score

        @cache
        def dp(col: int, prev_height: int, was_prev_move_up: bool) -> int:
            if col == n:
                return 0
            max_score = 0
            for i in range(n + 1):
                if prev_height > i:
                    score = prefix_sum[prev_height][col] - prefix_sum[i][col]
                    max_score = max(max_score, score + dp(col + 1, i, True))
                elif i > prev_height and not was_prev_move_up:
                    prev_score = (
                        prefix_sum[i][col - 1] - prefix_sum[prev_height][col - 1]
                    )
                    max_score = max(max_score, prev_score + dp(col + 1, i, False))
                else:
                    max_score = max(max_score, dp(col + 1, i, False))
            return max_score

        return dp(0, 0, True)
