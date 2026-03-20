from typing import List


class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        # Enumeration: O(m * n * k^2 * log(k)) time, O(k^2) space

        m = len(grid)
        n = len(grid[0])
        ans = []
        for i in range(m - k + 1):
            ans_row = []
            for j in range(n - k + 1):
                submatrix_values = set()
                for x in range(i, i + k):
                    for y in range(j, j + k):
                        submatrix_values.add(grid[x][y])
                submatrix_values = sorted(submatrix_values)
                if (len(submatrix_values)) == 1:
                    min_abs_diff = 0
                else:
                    min_abs_diff = float("inf")
                for l in range(len(submatrix_values) - 1):
                    min_abs_diff = min(
                        min_abs_diff, abs(submatrix_values[l] - submatrix_values[l + 1])
                    )
                ans_row.append(min_abs_diff)
            ans.append(ans_row)
        return ans
