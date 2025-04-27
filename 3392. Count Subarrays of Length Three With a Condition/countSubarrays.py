from typing import List


class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        # Brute Force: O(n) time, O(1) space

        n = len(nums)
        subarrays = 0
        for i in range(2, n):
            subarrays += nums[i - 2] + nums[i] == nums[i - 1] / 2
        return subarrays
