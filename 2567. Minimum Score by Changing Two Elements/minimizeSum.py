from typing import List


class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        # Greedy: O(n * log(n)) time, O(n) space

        sorted_nums = sorted(nums)
        min_score = min(
            sorted_nums[-1] - sorted_nums[2],
            sorted_nums[-2] - sorted_nums[1],
            sorted_nums[-3] - sorted_nums[0],
        )
        return min_score
