from typing import List
from collections import Counter


class Solution:
    def findLucky(self, arr: List[int]) -> int:
        # Hash Table: O(n) time, O(n) space, where
        # n is the size of arr

        max_lucky_integer = -1
        nums_counter = Counter(arr)
        for num in nums_counter:
            if nums_counter[num] == num:
                max_lucky_integer = max(max_lucky_integer, num)
        return max_lucky_integer
