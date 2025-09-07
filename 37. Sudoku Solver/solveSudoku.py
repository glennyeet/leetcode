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
                    num_bit = 1 << num
                    rows[i] |= num_bit
                    cols[j] |= num_bit
                    sub_box = (i // 3) * 3 + j // 3
                    sub_boxes[sub_box] |= num_bit
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
                num_bit = 1 << num
                if (
                    not rows[i] & num_bit
                    and not cols[j] & num_bit
                    and not sub_boxes[sub_box] & num_bit
                ):
                    rows[i] |= num_bit
                    cols[j] |= num_bit
                    sub_boxes[sub_box] |= num_bit
                    board[i][j] = str(num + 1)
                    solve_sudoku(blank + 1)
                    rows[i] ^= num_bit
                    cols[j] ^= num_bit
                    sub_boxes[sub_box] ^= num_bit

        solve_sudoku(0)
