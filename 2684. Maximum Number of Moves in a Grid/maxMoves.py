class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        # Iterative DP with O(m * n) space
        # rows = len(grid)
        # cols = len(grid[0])
        # moves = [[0] * cols for _ in range(rows)]
        # for j in range(1, cols):
        #     for i in range(rows):
        #         cur_value = grid[i][j]
        #         cur_moves = 0
        #         if (
        #             i - 1 >= 0
        #             and moves[i - 1][j - 1] == j - 1
        #             and grid[i - 1][j - 1] < cur_value
        #         ):
        #             cur_moves = max(cur_moves, moves[i - 1][j - 1] + 1)
        #         if moves[i][j - 1] == j - 1 and grid[i][j - 1] < cur_value:
        #             cur_moves = max(cur_moves, moves[i][j - 1] + 1)
        #         if (
        #             i + 1 < rows
        #             and moves[i + 1][j - 1] == j - 1
        #             and grid[i + 1][j - 1] < cur_value
        #         ):
        #             cur_moves = max(cur_moves, moves[i + 1][j - 1] + 1)
        #         moves[i][j] = cur_moves
        # max_moves = 0
        # for row in moves:
        #     max_moves = max(max_moves, max(row))
        # return max_moves

        # Iterative DP with O(m) space
        rows = len(grid)
        cols = len(grid[0])
        moves = None
        prev_moves = [0] * rows
        for j in range(1, cols):
            moves = [0] * rows
            for i in range(rows):
                cur_value = grid[i][j]
                moves[i] = prev_moves[i]
                if prev_moves[i] == j - 1 and grid[i][j - 1] < cur_value:
                    moves[i] = prev_moves[i] + 1
                if i - 1 >= 0:
                    moves[i] = max(moves[i], prev_moves[i - 1])
                    if prev_moves[i - 1] == j - 1 and grid[i - 1][j - 1] < cur_value:
                        moves[i] = max(moves[i], prev_moves[i - 1] + 1)
                if i + 1 < rows:
                    moves[i] = max(moves[i], prev_moves[i + 1])
                    if prev_moves[i + 1] == j - 1 and grid[i + 1][j - 1] < cur_value:
                        moves[i] = max(moves[i], prev_moves[i + 1] + 1)
            prev_moves = moves
        return max(moves)
