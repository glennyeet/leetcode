from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        # Prefix Sum: O(m^2 * n) time, O(m * n) space

        m = len(matrix)
        n = len(matrix[0])
        column_prefix_sums = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                column_prefix_sums[i + 1][j] = column_prefix_sums[i][j] + int(
                    matrix[i][j]
                )
        max_area = 0
        for i_start in range(m):
            for i_end in range(i_start, m):
                length = 0
                for j in range(n):
                    if (
                        column_prefix_sums[i_end + 1][j]
                        - column_prefix_sums[i_start][j]
                        == i_end - i_start + 1
                    ):
                        length += 1
                    else:
                        max_area = max(max_area, length * (i_end - i_start + 1))
                        length = 0
                else:
                    max_area = max(max_area, length * (i_end - i_start + 1))
        return max_area
