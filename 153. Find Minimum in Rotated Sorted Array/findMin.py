from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Binary Search: O(log(n)) time, O(1) space

        n = len(nums)
        if nums[0] < nums[-1]:
            return nums[0]
        l = 0
        r = n - 1
        while l < r:
            m = (l + r) // 2
            if nums[0] <= nums[m]:
                l = m + 1
            else:
                r = m
        return nums[l]
