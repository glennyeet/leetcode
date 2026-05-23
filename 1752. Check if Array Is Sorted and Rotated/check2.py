from typing import List


class Solution:
    def check(self, nums: List[int]) -> bool:
        # Array: O(n) time, O(1) space

        n = len(nums)
        original_start = 0
        for i in range(1, n):
            if nums[i] < nums[i - 1]:
                original_start = i
                break
        if original_start:
            for i in range(original_start, n):
                if nums[i] > nums[0]:
                    return False
                if i > original_start and nums[i] < nums[i - 1]:
                    return False
        return True
