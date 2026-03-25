from typing import List


class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        # Prefix Sum: O(m * n) time, O(m + n) space

        m = len(grid)
        n = len(grid[0])
        row_prefix_sums = [0] * m
        col_prefix_sums = [0] * n
        cur_sum = 0
        for i in range(m):
            for j in range(n):
                cur_sum += grid[i][j]
            row_prefix_sums[i] = cur_sum
        for i in range(1, m):
            if row_prefix_sums[i - 1] == cur_sum - row_prefix_sums[i - 1]:
                return True
        cur_sum = 0
        for j in range(n):
            for i in range(m):
                cur_sum += grid[i][j]
            col_prefix_sums[j] = cur_sum
        for i in range(1, n):
            if col_prefix_sums[i - 1] == cur_sum - col_prefix_sums[i - 1]:
                return True
        return False
