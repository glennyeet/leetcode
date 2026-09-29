from functools import cache


class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        # Top-down DP: O(m * n * (m + n)) time and
        # O(m * n * (m + n)) space

        m = len(grid)
        n = len(grid[0])
        if grid[0][0] == ")" or grid[m - 1][n - 1] == "(":
            return False

        @cache
        def dp(i: int, j: int, open_brackets: int) -> bool:
            if i == m - 1 and j == n - 1:
                return open_brackets == 1
            if grid[i][j] == "(":
                if (
                    i + 1 < m
                    and dp(i + 1, j, open_brackets + 1)
                    or j + 1 < n
                    and dp(i, j + 1, open_brackets + 1)
                ):
                    return True
            else:
                if open_brackets == 0:
                    return False
                if (
                    i + 1 < m
                    and dp(i + 1, j, open_brackets - 1)
                    or j + 1 < n
                    and dp(i, j + 1, open_brackets - 1)
                ):
                    return True
            return False

        return dp(0, 0, 0)
