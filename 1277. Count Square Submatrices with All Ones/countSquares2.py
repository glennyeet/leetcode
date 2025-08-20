from typing import List


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        # Bottom-up DP: O(mn) time, O(mn) space

        m = len(matrix)
        n = len(matrix[0])
        valid_submatricies = 0
        max_sides = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    max_sides[i][j] = 1
                    if i - 1 >= 0 and j - 1 >= 0:
                        max_sides[i][j] += min(
                            max_sides[i - 1][j],
                            max_sides[i - 1][j - 1],
                            max_sides[i][j - 1],
                        )
                valid_submatricies += max_sides[i][j]
        return valid_submatricies
