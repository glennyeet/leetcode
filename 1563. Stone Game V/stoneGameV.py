from functools import cache
from typing import List


class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        # Prefix Sum + Top-down DP: O(n^3) time, O(n^2) space

        n = len(stoneValue)
        prefix_values = [0]
        total_value = 0
        for value in stoneValue:
            total_value += value
            prefix_values.append(total_value)

        @cache
        def play_game(start: int, end: int) -> int:
            if start == end:
                return 0
            max_score = 0
            for cut in range(start + 1, end):
                left_row_score = prefix_values[cut] - prefix_values[start]
                right_row_score = prefix_values[end] - prefix_values[cut]
                if left_row_score > right_row_score:
                    round_score = right_row_score + play_game(cut, end)
                elif left_row_score < right_row_score:
                    round_score = left_row_score + play_game(start, cut)
                else:
                    round_score = max(
                        left_row_score + play_game(start, cut),
                        right_row_score + play_game(cut, end),
                    )
                max_score = max(max_score, round_score)
            return max_score

        return play_game(0, n)
