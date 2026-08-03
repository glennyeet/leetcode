from functools import cache
from typing import List


class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        # Top-down DP + Minimax: O(n) time, O(n) space

        n = len(stoneValue)

        @cache
        def play_game(i: int) -> int:
            turn_score = 0
            total_score = 0
            first_stone = i
            if first_stone < n:
                turn_score += stoneValue[first_stone]
                total_score = turn_score - play_game(first_stone + 1)
            second_stone = i + 1
            if second_stone < n:
                turn_score += stoneValue[second_stone]
                total_score = max(total_score, turn_score - play_game(second_stone + 1))
            third_stone = i + 2
            if third_stone < n:
                turn_score += stoneValue[third_stone]
                total_score = max(total_score, turn_score - play_game(third_stone + 1))
            return total_score

        point_diff = play_game(0)
        if point_diff > 0:
            return "Alice"
        elif point_diff < 0:
            return "Bob"
        return "Tie"
