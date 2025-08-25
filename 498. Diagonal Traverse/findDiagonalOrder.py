from typing import List


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        # Simulation: O(m * n) time, O(m * n) space

        m = len(mat)
        n = len(mat[0])
        diagonal_order = []
        cur_i = 0
        cur_j = 0
        move_up = True
        while cur_i != m - 1 or cur_j != n - 1:
            diagonal_order.append(mat[cur_i][cur_j])
            if move_up:
                new_i = cur_i - 1
                new_j = cur_j + 1
                if new_j > n - 1:
                    move_up = False
                    new_i = cur_i + 1
                    new_j = cur_j
                elif new_i < 0:
                    move_up = False
                    new_i = cur_i
                    new_j = cur_j + 1
            else:
                new_i = cur_i + 1
                new_j = cur_j - 1
                if new_i > m - 1:
                    move_up = True
                    new_i = cur_i
                    new_j = cur_j + 1
                elif new_j < 0:
                    move_up = True
                    new_i = cur_i + 1
                    new_j = cur_j
            cur_i = new_i
            cur_j = new_j
        else:
            diagonal_order.append(mat[cur_i][cur_j])
        return diagonal_order
