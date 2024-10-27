class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        cache = {}

        def get_square_submatrices(i: int, j: int) -> int:
            if (i, j) in cache:
                return cache[(i, j)]
            if i == rows or j == cols or not matrix[i][j]:
                cache[(i, j)] = 0
                return 0
            squares = 1 + min(
                get_square_submatrices(i, j + 1),
                get_square_submatrices(i + 1, j + 1),
                get_square_submatrices(i + 1, j),
            )
            cache[(i, j)] = squares
            return squares

        squares = 0
        for i in range(rows):
            for j in range(cols):
                squares += get_square_submatrices(i, j)
        return squares
