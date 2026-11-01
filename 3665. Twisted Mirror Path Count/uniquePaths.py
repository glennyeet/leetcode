from typing import List


class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        # Top-down DP: O(m * n) time, O(m * n) space

        m = len(grid)
        n = len(grid[0])
        mod_factor = 10**9 + 7
        cache = [[[None] * 2 for _ in range(n)] for _ in range(m)]

        # direction: 0 = right, 1 = down
        def dp(i: int, j: int, direction: int) -> int:
            if i == m - 1 and j == n - 1:
                return 1
            if cache[i][j][direction] is not None:
                return cache[i][j][direction]
            unique_paths = 0
            ni = i + 1
            nj = j + 1
            if grid[i][j]:
                if direction == 0:
                    if ni < m:
                        unique_paths = (unique_paths + dp(ni, j, 1)) % mod_factor
                else:
                    if nj < n:
                        unique_paths = (unique_paths + dp(i, nj, 0)) % mod_factor
            else:
                if nj < n:
                    unique_paths = (unique_paths + dp(i, nj, 0)) % mod_factor
                if ni < m:
                    unique_paths = (unique_paths + dp(ni, j, 1)) % mod_factor
            cache[i][j][direction] = unique_paths
            return unique_paths

        return dp(0, 0, 0)
