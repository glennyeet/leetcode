from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Binary Search: O(log(n)) time, O(1) space

        n = len(nums)
        l = 0
        r = n - 1

        def is_target_between(num: int) -> bool:
            if nums[0] <= target <= num:
                return True
            if num < nums[0]:
                return target >= nums[0] or target <= num
            return False

        while l < r:
            m = l + (r - l) // 2
            if is_target_between(nums[m]):
                r = m
            else:
                l = m + 1
        if nums[l] != target:
            return -1
        return l
