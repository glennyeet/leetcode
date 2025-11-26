from typing import List


class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        # Top-down DP: O(m * n * k) time, O(m * n * k) space

        mod_factor = 10**9 + 7
        m = len(grid)
        n = len(grid[0])
        path_cache = [[[-1] * k for _ in range(n)] for _ in range(m)]

        def count_valid_paths(i: int, j: int, remainder: int) -> int:
            if i == m or j == n:
                return 0
            remainder = (remainder + grid[i][j]) % k
            if path_cache[i][j][remainder] != -1:
                return path_cache[i][j][remainder]
            elif i == m - 1 and j == n - 1:
                if remainder == 0:
                    return 1
                else:
                    return 0
            path_cache[i][j][remainder] = (
                count_valid_paths(i + 1, j, remainder) % mod_factor
                + count_valid_paths(i, j + 1, remainder) % mod_factor
            ) % mod_factor
            return path_cache[i][j][remainder]

        return count_valid_paths(0, 0, 0)
