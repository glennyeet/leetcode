from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        # Sliding Window: O(n) time, O(1) space, where n is the size of
        # nums

        fixed_bound_subarrays = 0

        def count_subarrays(start_index: int, end_index: int) -> int:
            subarrays = 0
            last_min = -1
            last_max = -1
            for i in range(start_index, end_index + 1):
                if nums[i] == minK:
                    last_min = i - start_index
                if nums[i] == maxK:
                    last_max = i - start_index
                subarrays += min(last_min, last_max) + 1
            return subarrays

        i = 0
        for j, num in enumerate(nums):
            if num < minK or num > maxK:
                fixed_bound_subarrays += count_subarrays(i, j - 1)
                i = j + 1
        fixed_bound_subarrays += count_subarrays(i, j)
        return fixed_bound_subarrays
