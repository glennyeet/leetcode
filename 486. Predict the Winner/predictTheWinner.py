from typing import List


class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        # Minimax: O(2^n) time, O(2^n) space

        n = len(nums)

        def simulate_game(i: int, j: int) -> bool:
            if i == j:
                return nums[i]
            pick_left_score = nums[i] - simulate_game(i + 1, j)
            pick_right_score = nums[j] - simulate_game(i, j - 1)
            return max(pick_left_score, pick_right_score)

        if simulate_game(0, n - 1) >= 0:
            return True
        return False
