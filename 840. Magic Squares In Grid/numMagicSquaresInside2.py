from typing import List


class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        # Hash Table: O(m * n) time, O(1) space

        m = len(grid)
        n = len(grid[0])
        magic_squares = 0
        for i in range(m - 2):
            for j in range(n - 2):
                cell_1 = grid[i][j]
                cell_2 = grid[i][j + 1]
                cell_3 = grid[i][j + 2]
                cell_4 = grid[i + 1][j]
                cell_5 = grid[i + 1][j + 1]
                cell_6 = grid[i + 1][j + 2]
                cell_7 = grid[i + 2][j]
                cell_8 = grid[i + 2][j + 1]
                cell_9 = grid[i + 2][j + 2]
                nums = set(
                    [
                        cell_1,
                        cell_2,
                        cell_3,
                        cell_4,
                        cell_5,
                        cell_6,
                        cell_7,
                        cell_8,
                        cell_9,
                    ]
                )
                if (
                    len(nums) < 9
                    or 0 in nums
                    or 10 in nums
                    or 11 in nums
                    or 12 in nums
                    or 13 in nums
                    or 14 in nums
                    or 15 in nums
                ):
                    continue
                row_1 = cell_1 + cell_2 + cell_3
                row_2 = cell_4 + cell_5 + cell_6
                if row_2 != row_1:
                    continue
                row_3 = cell_7 + cell_8 + cell_9
                if row_3 != row_1:
                    continue
                col_1 = cell_1 + cell_4 + cell_7
                if col_1 != row_1:
                    continue
                col_2 = cell_2 + cell_5 + cell_8
                if col_2 != row_1:
                    continue
                col_3 = cell_3 + cell_6 + cell_9
                if col_3 != row_1:
                    continue
                diag_1 = cell_1 + cell_5 + cell_9
                if diag_1 != row_1:
                    continue
                diag_2 = cell_3 + cell_5 + cell_7
                if diag_2 != row_1:
                    continue
                magic_squares += 1
        return magic_squares
