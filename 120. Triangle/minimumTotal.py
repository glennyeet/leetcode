from typing import List
from functools import cache


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # Top-down DP: O(n * m) time, O(n * m) space, where m is the size
        # of the largest row in triangle

        n = len(triangle)

        @cache
        def find_min_path_sum(i: int, j: int) -> int:
            if i == n - 1:
                return triangle[i][j]
            return triangle[i][j] + min(
                find_min_path_sum(i + 1, j), find_min_path_sum(i + 1, j + 1)
            )

        return find_min_path_sum(0, 0)
