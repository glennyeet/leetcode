from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # Sliding Window: O(n) time, O(1) space

        n = len(nums)
        left = 0
        subarrays = 0
        product = 1
        for right in range(n):
            product *= nums[right]
            while right - left + 1 and product >= k:
                product //= nums[left]
                left += 1
            subarrays += right - left + 1
        return subarrays
