from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        # Sliding Window: O(n) time, O(1) space

        n = len(nums)
        subarrays = 0
        left = 0
        cur_sum = 0
        for right in range(n):
            cur_sum += nums[right]
            while cur_sum * (right - left + 1) >= k:
                cur_sum -= nums[left]
                left += 1
            subarrays += right - left + 1
        return subarrays
