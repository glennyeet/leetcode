from typing import List


class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        # Brute force: O(n) time, O(1) space

        positive_nums = 0
        negative_nums = 0
        for num in nums:
            if num > 0:
                positive_nums += 1
            elif num < 0:
                negative_nums += 1
        return max(positive_nums, negative_nums)
