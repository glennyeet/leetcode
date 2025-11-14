from typing import List


class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        # Prefix Sum: O(q * n + n^2) time, O(n^2) space, where q is the size of
        # queries

        prefix_sums = [[0] * (n + 1) for _ in range(n + 1)]
        for row_1, col_1, row_2, col_2 in queries:
            for i in range(row_1, row_2 + 1):
                prefix_sums[i][col_1] += 1
                prefix_sums[i][col_2 + 1] -= 1
        mat = [[0] * n for _ in range(n)]
        for i in range(n):
            value = 0
            for j in range(n):
                value += prefix_sums[i][j]
                mat[i][j] = value
        return mat
