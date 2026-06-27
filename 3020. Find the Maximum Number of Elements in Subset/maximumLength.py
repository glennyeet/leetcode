from collections import Counter
from typing import List


class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        # Hash Table + Enumeration: O(n * log(log(m))) time, O(n) space, where
        # n is the size of nums and m is max(nums)

        nums_counter = Counter(nums)
        max_subset_elements = 1
        for x in nums_counter:
            if x == 1:
                if nums_counter[x] % 2 == 0:
                    nums_counter[x] -= 1
                max_subset_elements = max(max_subset_elements, nums_counter[x])
            elif nums_counter[x] >= 2:
                cur_x = x
                i = 1
                while nums_counter[cur_x**2] >= 2:
                    cur_x *= cur_x
                    i += 1
                if nums_counter[cur_x**2] >= 1:
                    i += 1
                max_subset_elements = max(max_subset_elements, (i - 1) * 2 + 1)
        return max_subset_elements
