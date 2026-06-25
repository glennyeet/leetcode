from typing import List


class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        # Enumeration: O(n^2) time, O(1) space

        n = len(nums)
        majority_subarrays = 0
        for i in range(n):
            target_count = 0
            for j in range(i, n):
                if nums[j] == target:
                    target_count += 1
                if target_count > (j - i + 1) // 2:
                    majority_subarrays += 1
        return majority_subarrays
