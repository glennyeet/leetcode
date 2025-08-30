from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Simulation + Hash Table: O(1) time, O(1) space

        for i in range(9):
            digits = set()
            for j in range(9):
                if board[i][j] == ".":
                    continue
                elif board[i][j] in digits:
                    return False
                digits.add(board[i][j])
        for j in range(9):
            digits = set()
            for i in range(9):
                if board[i][j] == ".":
                    continue
                elif board[i][j] in digits:
                    return False
                digits.add(board[i][j])
        for i0 in range(0, 9, 3):
            for j0 in range(0, 9, 3):
                digits = set()
                for i in range(i0, i0 + 3):
                    for j in range(j0, j0 + 3):
                        if board[i][j] == ".":
                            continue
                        elif board[i][j] in digits:
                            return False
                        digits.add(board[i][j])
        return True
