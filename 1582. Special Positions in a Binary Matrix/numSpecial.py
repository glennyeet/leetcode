from typing import List


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        # Matrix: O(m * n) time, O(m + n) space

        m = len(mat)
        n = len(mat[0])
        row_ones = [0] * m
        col_ones = [0] * n
        for i in range(m):
            for j in range(n):
                row_ones[i] += mat[i][j]
                col_ones[j] += mat[i][j]
        special_positions = 0
        for i in range(m):
            for j in range(n):
                special_positions += mat[i][j] and row_ones[i] == 1 and col_ones[j] == 1
        return special_positions
