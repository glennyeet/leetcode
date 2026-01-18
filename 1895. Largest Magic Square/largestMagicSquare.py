from typing import List


class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        # Enumeration: O((m * n)^2 * k) time, O(1) space

        m = len(grid)
        n = len(grid[0])
        max_size = 1

        def is_magic_square(i_start: int, i_end: int, j_start: int, j_end: int) -> bool:
            expected_sum = 0
            for j in range(j_start, j_end + 1):
                expected_sum += grid[i_start][j]
            for i in range(i_start + 1, i_end + 1):
                row_sum = 0
                for j in range(j_start, j_end + 1):
                    row_sum += grid[i][j]
                if row_sum != expected_sum:
                    return False
            for j in range(j_start, j_end + 1):
                column_sum = 0
                for i in range(i_start, i_end + 1):
                    column_sum += grid[i][j]
                if column_sum != expected_sum:
                    return False
            left_diagonal_sum = 0
            j = j_start
            for i in range(i_start, i_end + 1):
                left_diagonal_sum += grid[i][j]
                j += 1
            if left_diagonal_sum != expected_sum:
                return False
            right_diagonal_sum = 0
            j = j_end
            for i in range(i_start, i_end + 1):
                right_diagonal_sum += grid[i][j]
                j -= 1
            if right_diagonal_sum != expected_sum:
                return False
            return True

        for k in range(2, min(m, n) + 1):
            found_magic_square = False
            for i in range(m - k + 1):
                for j in range(n - k + 1):
                    if is_magic_square(i, i + k - 1, j, j + k - 1):
                        max_size = max(max_size, k)
                        found_magic_square = True
                        break
                if found_magic_square:
                    break
        return max_size
