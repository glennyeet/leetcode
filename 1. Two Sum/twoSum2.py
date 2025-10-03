from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Hash Table: O(n) time, O(n) space, where n is the size
        # of nums

        seen_nums = {}
        for i, num1 in enumerate(nums):
            num2 = target - num1
            if num2 in seen_nums:
                return [i, seen_nums[num2]]
            seen_nums[num1] = i
        return [-1, -1]
