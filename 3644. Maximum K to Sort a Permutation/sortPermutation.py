from typing import List


class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        # Bit Manipulation: O(n) time, O(1) space

        n = len(nums)
        max_k = -1
        for i in range(n):
            if nums[i] != i:
                max_k &= nums[i]
        if max_k == -1:
            return 0
        return max_k