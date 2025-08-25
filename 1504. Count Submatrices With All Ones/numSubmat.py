from typing import List


class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        # Bottom-up DP: O(m^2 * n) time, O(m * n) space

        m = len(mat)
        n = len(mat[0])
        prefix_sums = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0:
                    prefix_sums[i][j] = mat[i][j]
                else:
                    prefix_sums[i][j] = prefix_sums[i - 1][j] + mat[i][j]
        total = 0
        for i1 in range(m):
            for i2 in range(i1, m):
                width = 0
                for j in range(n):
                    if i1 == 0:
                        all_ones = prefix_sums[i2][j] == i2 + 1
                    else:
                        all_ones = prefix_sums[i2][j] - prefix_sums[i1 - 1][j] == (
                            i2 - i1 + 1
                        )
                    if all_ones:
                        width += 1
                    else:
                        width = 0
                    total += width
        return total
