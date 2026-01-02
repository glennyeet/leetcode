from typing import List


class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        # Hash Table: O(n) time, O(n) space, where n
        # is the size of nums

        unique_nums = set()
        for num in nums:
            if num in unique_nums:
                return num
            unique_nums.add(num)
        return -1
