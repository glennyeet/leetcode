from typing import List


class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        # Array: O(n) time, O(1) space

        n = len(nums)
        if nums[0] >= nums[1]:
            return False
        i = 2
        while i < n and nums[i - 1] < nums[i]:
            i += 1
        if i >= n - 1:
            return False
        while i < n and nums[i - 1] > nums[i]:
            i += 1
        if i == n:
            return False
        while i < n and nums[i - 1] < nums[i]:
            i += 1
        if i != n:
            return False
        else:
            return True
