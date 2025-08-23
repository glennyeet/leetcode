from typing import List
from functools import cache


class Solution:
    def minimumSum(self, grid: List[List[int]]) -> int:
        # Top-down DP: O(m * n * (m + n)) time, O(m * n) space

        m = len(grid)
        n = len(grid[0])

        @cache
        def find_min_sum(x1: int, y1: int, x2: int, y2: int, rectangles: int) -> int:
            if rectangles == 0:
                return 0
            elif rectangles == 1:
                min_x = float("inf")
                min_y = float("inf")
                max_x = 0
                max_y = 0
                for i in range(x1, x2 + 1):
                    for j in range(y1, y2 + 1):
                        if grid[i][j]:
                            min_x = min(min_x, i)
                            min_y = min(min_y, j)
                            max_x = max(max_x, i)
                            max_y = max(max_y, j)
                if min_x == float("inf"):
                    return 0
                return (max_x - min_x + 1) * (max_y - min_y + 1)

            min_sum = float("inf")
            for i in range(1, rectangles):
                for j in range(x1, x2 + 1):
                    min_sum = min(
                        min_sum,
                        find_min_sum(x1, y1, j, y2, i)
                        + find_min_sum(j + 1, y1, x2, y2, rectangles - i),
                    )
            for i in range(1, rectangles):
                for j in range(y1, y2 + 1):
                    min_sum = min(
                        min_sum,
                        find_min_sum(x1, y1, x2, j, i)
                        + find_min_sum(x1, j + 1, x2, y2, rectangles - i),
                    )
            return min_sum

        return find_min_sum(0, 0, m - 1, n - 1, 3)
