from typing import List


class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        # Prefix Sum + Hash Table: O(n) time, O(n)
        # space, where n is the size of nums

        max_num = max(nums)
        sequential_prefix = 0
        sequential_num = 0
        for i, num in enumerate(nums):
            if i > 0 and num != sequential_num + 1:
                break
            sequential_num = num
            sequential_prefix += sequential_num
        nums_set = set(nums)
        x = sequential_prefix
        while x <= max_num:
            if x not in nums_set:
                break
            x += 1
        return x
