from typing import List


class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        # Sliding Window: O(n) time, O(n) space

        n = len(nums)
        sorted_nums = sorted(nums)
        min_elements_removed = float("inf")
        i = 0
        for j in range(n):
            while i < j and sorted_nums[j] / sorted_nums[i] > k:
                i += 1
            min_elements_removed = min(min_elements_removed, n - (j - i + 1))
        return min_elements_removed
