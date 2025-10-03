from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Hash Table: O(n) time, O(n) space, where n is
        # the size of nums

        unique_nums = set()
        for num in nums:
            if num in unique_nums:
                return True
            unique_nums.add(num)
        return False
