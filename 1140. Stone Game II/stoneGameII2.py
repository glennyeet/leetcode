from functools import cache
from typing import List


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        # Top-down DP + Minimax: O(n^3) time, O(n^2) space

        n = len(piles)

        @cache
        def play_game(i: int, m: int) -> int:
            if i == n:
                return 0
            max_delta = float("-inf")
            stones = 0
            for x in range(1, min(n - i, 2 * m) + 1):
                stones += piles[i + x - 1]
                new_m = min(max(m, x), (n + 1) // 2)
                max_delta = max(max_delta, -play_game(i + x, new_m) + stones)
            return max_delta

        total_stones = sum(piles)
        max_delta = play_game(0, 1)
        alice_max_stones = (total_stones + max_delta) // 2
        return alice_max_stones
