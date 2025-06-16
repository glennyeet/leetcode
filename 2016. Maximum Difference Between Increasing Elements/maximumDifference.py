from typing import List


class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        # Prefix: O(n) time, O(1) space

        n = len(nums)
        min_value = nums[0]
        max_difference = -1
        for i in range(1, n):
            if nums[i] > min_value:
                max_difference = max(max_difference, nums[i] - min_value)
            min_value = min(min_value, nums[i])
        return max_difference
