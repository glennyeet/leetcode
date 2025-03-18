from typing import List


class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        # Sliding window: O(n) time, O(1) space, where
        # n is the size of nums

        left = 0
        bitmask = 0
        max_length = 0
        for right, num in enumerate(nums):
            while bitmask & num:
                bitmask ^= nums[left]
                left += 1
            max_length = max(max_length, right - left + 1)
            bitmask ^= num
        return max_length
