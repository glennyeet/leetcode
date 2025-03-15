from typing import List


class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        # Binary search: O(mlog(n)) time, O(1) space, where
        # m is max(nums) - min(nums) + 1 and n is the size
        # of nums

        n = len(nums)
        left = min(nums)
        right = max(nums)
        min_capability = right

        def is_valid_capability(capability: int) -> bool:
            houses = 0
            i = 0
            while i < n:
                if nums[i] <= capability:
                    houses += 1
                    i += 2
                else:
                    i += 1
                if houses == k:
                    return True
            return False

        while left <= right:
            mid = (left + right) // 2
            if is_valid_capability(mid):
                min_capability = mid
                right = mid - 1
            else:
                left = mid + 1
        return min_capability
