class Solution:
    def judgeCircle(self, moves: str) -> bool:
        # Simulation: O(n) time, O(1) space, where n is the size of moves

        move_counter = [0] * 4  # R, L, U, D
        for move in moves:
            if move == "R":
                move_counter[0] += 1
            elif move == "L":
                move_counter[1] += 1
            elif move == "U":
                move_counter[2] += 1
            else:
                move_counter[3] += 1
        return move_counter[0] == move_counter[1] and move_counter[2] == move_counter[3]
