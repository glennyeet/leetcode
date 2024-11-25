from collections import deque


class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        valid_moves = {
            0: [1, 3],
            1: [0, 2, 4],
            2: [1, 5],
            3: [0, 4],
            4: [3, 1, 5],
            5: [2, 4],
        }
        initial_board = []
        for row in range(len(board)):
            for col in range(len(board[0])):
                initial_board.append(str(board[row][col]))
        initial_board = "".join(initial_board)
        boards = deque([(initial_board.index("0"), initial_board, 0)])
        visited = set(initial_board)
        while boards:
            i, cur_board, moves = boards.popleft()
            if cur_board == "123450":
                return moves
            cur_board_list = list(cur_board)
            cur_position = cur_board.index("0")
            for j in valid_moves[cur_position]:
                new_board = cur_board_list.copy()
                new_board[i], new_board[j] = new_board[j], new_board[i]
                new_board = "".join(new_board)
                if new_board not in visited:
                    boards.append((j, new_board, moves + 1))
                    visited.add(new_board)
        return -1
