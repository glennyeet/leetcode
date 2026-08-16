from collections import Counter
from typing import List


class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        # Greedy + Hash Table: O(n) time, O(1) space

        n = len(stones)

        def play_game(starting_remainder: int) -> bool:
            remainder_counter = Counter()
            for value in stones:
                remainder_counter[value % 3] += 1
            if remainder_counter[starting_remainder] == 0:
                return False
            cur_remainder = starting_remainder
            remainder_counter[starting_remainder] -= 1
            for turn in range(n - 1):
                found_valid_stone = False
                for remainder in range(3):
                    if (remainder + cur_remainder) % 3 != 0 and remainder_counter[
                        remainder
                    ] > 0:
                        found_valid_stone = True
                        cur_remainder = (cur_remainder + remainder) % 3
                        remainder_counter[remainder] -= 1
                        break
                if not found_valid_stone:
                    if turn % 2 == 0:
                        return True
                    return False
            return False

        return play_game(1) or play_game(2)
