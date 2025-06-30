from typing import List
from collections import Counter


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        # Hash Table: O(n) time, O(n) space,
        # where n is the size of nums

        nums_counter = Counter(nums)
        max_len = 0
        for num in nums_counter:
            if nums_counter[num + 1]:
                max_len = max(max_len, nums_counter[num] + nums_counter[num + 1])
        return max_len
