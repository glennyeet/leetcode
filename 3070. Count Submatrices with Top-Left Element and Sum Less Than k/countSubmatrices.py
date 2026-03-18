from typing import List


class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        # Prefix Sum: O(m * n) time, O(n) space

        m = len(grid)
        n = len(grid[0])
        prefix_sums = [0] * n
        valid_submatrices = 0
        for i in range(m):
            submatrix_sum = 0
            for j in range(n):
                submatrix_sum += prefix_sums[j] + grid[i][j]
                prefix_sums[j] += grid[i][j]
                if submatrix_sum <= k:
                    valid_submatrices += 1
                else:
                    break
        return valid_submatrices
