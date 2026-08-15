from typing import List


class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        # Bit Manipulation: O(n) time, O(1) space

        n = len(nums)
        xor_sum = 0
        has_non_zero_num = False
        for num in nums:
            xor_sum ^= num
            if not has_non_zero_num and num != 0:
                has_non_zero_num = True
        if not has_non_zero_num:
            return 0
        elif xor_sum == 0:
            return n - 1
        else:
            return n
