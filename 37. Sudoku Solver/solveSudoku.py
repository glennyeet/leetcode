from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # Backtracking: O(1) time, O(1) space

        blanks = []
        rows = [0] * 9
        cols = [0] * 9
        sub_boxes = [0] * 9
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    blanks.append((i, j))
                else:
                    num = int(board[i][j]) - 1
                    bitmask = 1 << num
                    rows[i] |= bitmask
                    cols[j] |= bitmask
                    sub_box = (i // 3) * 3 + j // 3
                    sub_boxes[sub_box] |= bitmask
        solved = False

        def solve_sudoku(blank: int) -> None:
            if blank == len(blanks):
                nonlocal solved
                solved = True
                return
            i, j = blanks[blank]
            sub_box = (i // 3) * 3 + j // 3
            for num in range(9):
                if solved:
                    return
                bitmask = 1 << num
                if (
                    not rows[i] & bitmask
                    and not cols[j] & bitmask
                    and not sub_boxes[sub_box] & bitmask
                ):
                    rows[i] |= bitmask
                    cols[j] |= bitmask
                    sub_boxes[sub_box] |= bitmask
                    board[i][j] = str(num + 1)
                    solve_sudoku(blank + 1)
                    rows[i] ^= bitmask
                    cols[j] ^= bitmask
                    sub_boxes[sub_box] ^= bitmask

        solve_sudoku(0)
