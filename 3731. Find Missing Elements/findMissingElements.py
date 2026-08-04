from typing import List


class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        # Hash Table: O(m) time, O(m) space, where m is
        # max(nums)

        missing_nums = []
        unique_nums = set(nums)
        for num in range(min(nums), max(nums) + 1):
            if num not in unique_nums:
                missing_nums.append(num)
        return missing_nums
