from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Hash Table: O(1) time, O(1) space

        for i in range(9):
            row_nums = set()
            for j in range(9):
                if board[i][j] == ".":
                    continue
                elif board[i][j] in row_nums:
                    return False
                row_nums.add(board[i][j])
        for j in range(9):
            col_nums = set()
            for i in range(9):
                if board[i][j] == ".":
                    continue
                elif board[i][j] in col_nums:
                    return False
                col_nums.add(board[i][j])
        for i0 in range(0, 9, 3):
            for j0 in range(0, 9, 3):
                sub_box_nums = set()
                for i in range(i0, i0 + 3):
                    for j in range(j0, j0 + 3):
                        if board[i][j] == ".":
                            continue
                        elif board[i][j] in sub_box_nums:
                            return False
                        sub_box_nums.add(board[i][j])
        return True
