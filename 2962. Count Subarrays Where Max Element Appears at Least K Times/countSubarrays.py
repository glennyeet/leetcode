from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        # Sliding Window: O(n) time, O(1) space

        max_num = max(nums)
        n = len(nums)
        left = 0
        subarrays = 0
        max_num_count = 0
        for right in range(n):
            max_num_count += nums[right] == max_num
            while max_num_count >= k:
                max_num_count -= nums[left] == max_num
                left += 1
            subarrays += left
        return subarrays
