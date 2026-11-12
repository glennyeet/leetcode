from typing import List


class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        # Array: O(n) time, O(1) space

        n = len(nums)
        if n == 1:
            return 1
        longest_subarray = 1
        streak = 1
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                streak += 1
            else:
                longest_subarray = max(longest_subarray, streak)
                streak = 1
        else:
            longest_subarray = max(longest_subarray, streak)
        streak = 1
        for i in range(1, n):
            if nums[i] < nums[i - 1]:
                streak += 1
            else:
                longest_subarray = max(longest_subarray, streak)
                streak = 1
        else:
            longest_subarray = max(longest_subarray, streak)
        return longest_subarray
