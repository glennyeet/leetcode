from typing import List


class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        # Prefix Sum: O(m * n) time, O(n) space

        m = len(grid)
        n = len(grid[0])
        letter_prefix_sums = [(0, 0)] * n
        valid_submatrices = 0
        for i in range(m):
            x_count = 0
            y_count = 0
            for j in range(n):
                x_count += letter_prefix_sums[j][0]
                y_count += letter_prefix_sums[j][1]
                if grid[i][j] == "X":
                    x_count += 1
                    letter_prefix_sums[j] = (
                        letter_prefix_sums[j][0] + 1,
                        letter_prefix_sums[j][1],
                    )
                elif grid[i][j] == "Y":
                    y_count += 1
                    letter_prefix_sums[j] = (
                        letter_prefix_sums[j][0],
                        letter_prefix_sums[j][1] + 1,
                    )
                if x_count >= 1 and x_count == y_count:
                    valid_submatrices += 1
        return valid_submatrices
