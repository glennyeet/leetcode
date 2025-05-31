from typing import List
from collections import deque


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        # BFS: O(n^2) time, O(n^2) space

        n = len(board)
        boustrophedon_board = []
        for i, row in enumerate(board[::-1]):
            if not i % 2:
                boustrophedon_board.extend(row)
            else:
                boustrophedon_board.extend(row[::-1])
        least_rolls = [None] * (n**2)
        least_rolls[0] = 0
        queue = deque([0])
        while queue:
            cur_square = queue.popleft()
            for roll in range(1, 7):
                next_square = cur_square + roll
                if boustrophedon_board[next_square] != -1:
                    next_square = boustrophedon_board[next_square] - 1
                if least_rolls[next_square] == None:
                    least_rolls[next_square] = least_rolls[cur_square] + 1
                    queue.append(next_square)
                if next_square == n**2 - 1:
                    return least_rolls[next_square]
        return -1
