from typing import List


class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        # Two Pointers: O(n) time, O(1) space

        n = len(nums)
        zero_subarrays = 0
        i = 0
        j = 0
        while i < n:
            if nums[i] == 0:
                while j < n and nums[j] == 0:
                    zero_subarrays += j - i + 1
                    j += 1
                i = j
            else:
                i += 1
                j += 1
        return zero_subarrays
