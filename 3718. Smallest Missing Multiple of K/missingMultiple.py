from typing import List


class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        # Hash Table: O(n) time, O(1) space

        nums_set = set(nums)
        min_k_multiple = k
        while min_k_multiple in nums_set:
            min_k_multiple += k
        return min_k_multiple
