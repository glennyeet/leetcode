from typing import List


class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        # Hash Table: O(n) time, O(n) space, where n is the size of
        # nums

        nums_set = set(nums)
        new_original = original
        while new_original in nums_set:
            new_original *= 2
        return new_original
