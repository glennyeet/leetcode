from typing import List
from math import ceil


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        # Hash table: O(n) time, O(n) space

        unique_nums = set()
        removed_nums = 0
        for i, num in reversed(list(enumerate(nums))):
            if num in unique_nums:
                removed_nums = i + 1
                break
            unique_nums.add(num)
        return ceil(removed_nums / 3)
