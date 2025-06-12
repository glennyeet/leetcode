from typing import List


class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        n = len(nums)
        max_difference = abs(nums[0] - nums[-1])
        for i in range(n - 1):
            max_difference = max(max_difference, abs(nums[i] - nums[i + 1]))
        return max_difference
