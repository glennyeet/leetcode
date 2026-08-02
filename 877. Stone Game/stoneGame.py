from functools import cache
from typing import List


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # Top-down DP + Minimax: O(n^2) time, O(n^2) space

        n = len(piles)

        @cache
        def play_game(left: int, right: int) -> int:
            if left == right:
                return piles[left]
            pick_left_score = piles[left] - play_game(left + 1, right)
            pick_right_score = piles[right] - play_game(left, right - 1)
            return max(pick_left_score, pick_right_score)

        if play_game(0, n - 1) > 0:
            return True
        return False
