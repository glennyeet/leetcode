from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # Bit Manipulation: O(n) time, O(1) space, where
        # n is the size of nums

        max_num = max(nums)
        streak = 0
        longest_subarray = 0
        for num in nums:
            if num == max_num:
                streak += 1
                longest_subarray = max(longest_subarray, streak)
            else:
                streak = 0
        return longest_subarray
