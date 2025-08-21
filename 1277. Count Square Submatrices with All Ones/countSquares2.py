from typing import List


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        # Bottom-up DP: O(mn) time, O(mn) space

        m = len(matrix)
        n = len(matrix[0])
        total = 0
        valid_submatricies = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    valid_submatricies[i][j] = 1
                    if i - 1 >= 0 and j - 1 >= 0:
                        valid_submatricies[i][j] += min(
                            valid_submatricies[i - 1][j],
                            valid_submatricies[i - 1][j - 1],
                            valid_submatricies[i][j - 1],
                        )
                total += valid_submatricies[i][j]
        return total
